package com.example.grammar.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class GrammarRequestDto {
    private String function; //e.g: x**2+3, x^2+3
}
