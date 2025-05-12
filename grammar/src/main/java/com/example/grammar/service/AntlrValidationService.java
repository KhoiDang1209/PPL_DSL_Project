package com.example.grammar.service;

import com.example.grammar.listener.MathListener;
import com.example.grammar.model.GrammarRequestDto;
import com.example.grammar.model.GrammarResponseDto;
import com.example.grammar.listener.CustomErrorListener;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.ParseCancellationException;
import org.antlr.v4.runtime.tree.ParseTreeWalker;
import org.springframework.stereotype.Service;

import com.example.grammar.MathLexer;
import com.example.grammar.MathParser;

@Service
public class AntlrValidationService {
    private static final String FUNCTION_NAMES = "(exp|sin|cos|tan|sqrt)";

    public GrammarResponseDto validate(GrammarRequestDto request){
        // Preprocess the input, need trimming for explicit multiplication convert
        String convertedText = getConvertedInput(request.getFunction());

        CustomErrorListener customErrorListener = new CustomErrorListener(convertedText);

        // ANTLR input stream
        CharStream charStream = CharStreams.fromString(convertedText);

        // Create the lexer
        MathLexer lexer = new MathLexer(charStream);
        lexer.removeErrorListeners();
        lexer.addErrorListener(customErrorListener);

        // Create the token stream
        CommonTokenStream commonTokenStream = new CommonTokenStream(lexer);

        // Create the parser
        MathParser parser = new MathParser(commonTokenStream);
        parser.removeErrorListeners(); // Remove default console error listener
        parser.addErrorListener(customErrorListener); // Add custom error listener
        MathParser.ProgramContext tree;

        try{
            tree = parser.program();
        } catch (ParseCancellationException e) {
            return new GrammarResponseDto(false, null, customErrorListener.getErrors());
        }

        // Add semantic checker using listener
        MathListener listener = new MathListener();
        ParseTreeWalker parseTreeWalker = new ParseTreeWalker();

        // Check for semantic errors
        parseTreeWalker.walk(listener, tree);

        if (!listener.getErrors().isEmpty()) {
            return new GrammarResponseDto(false, null, listener.getErrors());
        }

        return new GrammarResponseDto(true, convertedText, null);
    }

    private static String getConvertedInput(String input) {
        // Replace any '^' into '**' is not actually needed since Sympy can understand
        String convertedString = input.replace("^", "**");

        /*
            Remove any whitespace to perform the next convert even though grammar file skip white space
            Since the grammar not covers the implied multiplication
        */
        convertedString = convertedString.replaceAll("\\s", "");

        // Change implied multiplication to be explicit
        // ?( -> ?*( if not a function name
        convertedString = convertedString.replaceAll("(?<!\\b" + FUNCTION_NAMES + ")(\\b[a-zA-Z\\d])(\\()", "$1*$2");

        // 69x -> 69*x
        convertedString = convertedString.replaceAll("(\\d)([a-zA-Z])", "$1*$2");

        // )? -> )*?
        convertedString = convertedString.replaceAll("(\\))([a-zA-Z\\d])", "$1*$2");

        // )( -> )*(
        convertedString = convertedString.replaceAll("(\\))(\\()", "$1*$2");

        return convertedString;
    }
}
