package controllers;

import grid.Grid;
import view.ViewFrame;

public class GameController {
    Grid grid;
    ViewFrame frame;

    public GameController(Grid grid, ViewFrame frame) {
        this.grid = grid;
        this.frame = frame;
    }

    public void startGame(){
        frame.drawGrid(grid.getRows(), grid.getCols());
    }


}
