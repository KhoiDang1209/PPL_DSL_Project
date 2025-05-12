package com.example.grammar.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class GrammarResponseDto {
    private boolean isValid;
    private String function; // formatted function
    private List<SyntaxErrorDto> errors;
}
