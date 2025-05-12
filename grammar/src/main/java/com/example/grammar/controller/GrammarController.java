package com.example.grammar.controller;

import com.example.grammar.model.GrammarRequestDto;
import com.example.grammar.model.GrammarResponseDto;
import com.example.grammar.model.SyntaxErrorDto;
import com.example.grammar.service.AntlrValidationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Collections;

@RestController
@RequestMapping("/api/grammar")
public class GrammarController {
    private final AntlrValidationService validationService;

    @Autowired
    public GrammarController(AntlrValidationService validationService) {
        this.validationService = validationService;
    }

    @PostMapping("/check")
    public ResponseEntity<GrammarResponseDto> checkGrammar(@RequestBody GrammarRequestDto request) {
        // Basic input validation: check if the request or the text is null.
        if (request == null || request.getFunction() == null || request.getFunction().trim().isEmpty()) {

            // If the input is invalid, return a 400 Bad Request response.
            // Create a simple error message.
            SyntaxErrorDto error = new SyntaxErrorDto("Input function cannot be null or empty.", "");
            GrammarResponseDto errorResponse = new GrammarResponseDto(false, null, Collections.singletonList(error));
            return ResponseEntity.badRequest().body(errorResponse);
        }

        // Delegate the validation logic to the AntlrValidationService.
        GrammarResponseDto response = validationService.validate(request);

        // Return the response from the service with a 200 OK status.
        return ResponseEntity.ok(response);
    }
}
