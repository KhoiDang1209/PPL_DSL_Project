package com.example.grammar.listener;

import com.example.grammar.MathBaseListener;
import com.example.grammar.MathParser;
import com.example.grammar.model.SyntaxErrorDto;
import lombok.Getter;

import java.util.*;

public class MathListener extends MathBaseListener {
    private final Stack<MatrixShape> shapes = new Stack<>();
    private boolean semanticError = false;
    @Getter
    private List<SyntaxErrorDto> errors = new ArrayList<>();

    static class MatrixShape {
        int rows;
        int cols;

        MatrixShape(int rows, int cols) {
            this.rows = rows;
            this.cols = cols;
        }

        boolean equals(MatrixShape other) {
            return this.rows == other.rows && this.cols == other.cols;
        }

        @Override
        public String toString() {
            return rows + "x" + cols;
        }
    }

    @Override
    public void exitProgram(MathParser.ProgramContext ctx) {
        if(!semanticError){
            System.out.println("Correct semantic");
            System.out.println("Finished parsing: " + ctx.getText());
        }
    }

    @Override
    public void exitFunction(MathParser.FunctionContext ctx) {
        System.out.println("Function: " + ctx.getText());
    }


    @Override
    public void exitMatrix(MathParser.MatrixContext ctx) {
        if(!semanticError && !shapes.isEmpty()){
            MatrixShape shape = shapes.pop();
            int row = ctx.row().element().size();
            System.out.println("Matrix: " + ctx.getText() + ". Matrix dimension: " + shape + " with " + row + " rows.");
        }
    }

    @Override
    public void exitElement(MathParser.ElementContext ctx) {
        if (ctx.NUMBER() != null) {
            // A scalar element is a 1x1 matrix
            shapes.push(new MatrixShape(1, 1));
        }
    }

    @Override
    public void exitRow(MathParser.RowContext ctx){
        int numElements = ctx.element().size();
        List<MatrixShape> subShapes = new ArrayList<>();

        for(int i = 0; i < numElements; i++){
            subShapes.addFirst(shapes.pop());
        }

        if(subShapes.isEmpty()){
            shapes.push(new MatrixShape(1,0));
            return;
        }

        MatrixShape expectedShape = subShapes.getFirst();

        for(MatrixShape ms : subShapes){
            if (!ms.equals(expectedShape)){
               String error = "Semantic error: inconsistent dimension in matrix";
               String offendingMessage = ctx.getText();
               errors.add(new SyntaxErrorDto(error, offendingMessage));
               System.err.println(error);
               semanticError = true;
               return;
            }
        }
        shapes.push(new MatrixShape(1, numElements));
    }
}
