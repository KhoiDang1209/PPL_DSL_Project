package com.example.grammar.listener;

import com.example.grammar.model.SyntaxErrorDto;
import lombok.Getter;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.ATNConfigSet;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.ParseCancellationException;

import java.util.ArrayList;
import java.util.BitSet;
import java.util.List;

@Getter
public class CustomErrorListener implements ANTLRErrorListener {
    @Getter
    private final List<SyntaxErrorDto> errors = new ArrayList<>();
    private final String inputString;

    public CustomErrorListener(String inputString){this.inputString = inputString;}

    @Override
    public void syntaxError(Recognizer<?, ?> recognizer, Object o, int i, int i1, String s, RecognitionException e) {
        String token = (o instanceof Token) ? ((Token)o).getText() : "<unknown>";
        String error = String.format("Syntax error at %d in input: %s - %s", i1, inputString, s);

        errors.add(new SyntaxErrorDto(error, token));

        throw new ParseCancellationException(error, e);
    }

    @Override
    public void reportAmbiguity(Parser parser, DFA dfa, int i, int i1, boolean b, BitSet bitSet, ATNConfigSet atnConfigSet) {

    }

    @Override
    public void reportAttemptingFullContext(Parser parser, DFA dfa, int i, int i1, BitSet bitSet, ATNConfigSet atnConfigSet) {

    }

    @Override
    public void reportContextSensitivity(Parser parser, DFA dfa, int i, int i1, int i2, ATNConfigSet atnConfigSet) {

    }
}
