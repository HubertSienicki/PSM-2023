package controllers;

import model.grid.Grid;
import view.GridPanel;

public class GridController {
    public GridPanel createGridPanel(Grid grid) {
        return new GridPanel(grid);
    }
}
