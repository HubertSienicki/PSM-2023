package model.grid;

import model.cell.Cell;

public class Grid {

    private Cell[][] grid;
    public Grid(int rows, int cols) {
        grid = new Cell[rows][cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                grid[i][j] = new Cell(i,j);
            }
        }
    }

    public void setAlive(int x, int y, boolean isAlive){
        grid[x][y].setAlive(isAlive);
    }

    public boolean isAlive(int x, int y){
        return grid[x][y].isAlive();
    }

    public Cell getCell(int x, int y){
        return grid[x][y];
    }

    public int getRows(){
        return grid.length;
    }

    public int getCols(){
        return grid[0].length;
    }
}
