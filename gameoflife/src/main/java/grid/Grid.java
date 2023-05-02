package grid;

import cell.Cell;

public class Grid {
    private int rows;
    private int cols;
    private Cell[][] cellGrid;

    public Grid(int rows, int cols) {
        this.rows = rows;
        this.cols = cols;
        cellGrid = new Cell[rows][cols];
    }

    public int getRows() {
        return rows;
    }

    public int getCols() {
        return cols;
    }

    public Cell[][] getCellGrid() {
        return cellGrid;
    }
}
