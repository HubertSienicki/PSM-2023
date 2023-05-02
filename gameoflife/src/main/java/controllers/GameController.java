package controllers;

import model.grid.Grid;
import view.ViewFrame;

public class GameController {
    Grid grid;
    ViewFrame frame;
    GridController gridController = new GridController();

    public GameController(Grid grid, ViewFrame frame) {
        this.grid = grid;
        this.frame = frame;
    }

    public void startGame() {
        drawGrid();
    }

    private void drawGrid() {
        frame.setGridPane(gridController.createGridPanel(grid));
    }
}
