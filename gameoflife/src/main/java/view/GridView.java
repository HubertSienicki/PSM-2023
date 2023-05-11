package view;

import model.cell.Cell;
import model.grid.Grid;

import javax.swing.*;
import java.awt.*;

public class GridView extends JPanel {
    private Grid grid;
    private CellView[][] cellViews;
    private int cellSize;

    public GridView(Grid grid, int cellSize) {
        this.grid = grid;
        this.cellSize = cellSize;

        int rows = grid.getRows();
        int cols = grid.getCols();
        cellViews = new CellView[rows][cols];

        setLayout(new GridLayout(rows, cols));
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                Cell cell = grid.getCell(i, j);
                cellViews[i][j] = new CellView(cell);
                add(cellViews[i][j]);
            }
        }
    }

    public void updateGridView() {
        int rows = grid.getRows();
        int cols = grid.getCols();

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                cellViews[i][j].updateColor();
            }
        }
        revalidate();
        repaint();
    }

    public CellView getCellView(int i, int j) {
        return cellViews[i][j];
    }

    public int getCellSize() {
        return cellSize;
    }
}
