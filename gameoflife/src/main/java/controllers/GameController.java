package controllers;

import model.grid.Grid;
import view.GridPanel;
import view.ViewFrame;

public class GameController {
    Grid grid;
    ViewFrame frame;

    public GameController(Grid grid, ViewFrame frame) {
        this.grid = grid;
        this.frame = frame;
    }

    public void startGame(){
        drawGrid(grid.getRows(), grid.getCols());
    }
    private void drawGrid(int rows, int cols){
        frame.setGridPane(new GridPanel(rows, cols));
    }
}
