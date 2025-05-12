package com.example.grammar.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class SyntaxErrorDto {
    private String message;
    private String offendingSymbol;
}
