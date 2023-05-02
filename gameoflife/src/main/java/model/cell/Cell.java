package model.cell;

import model.cell.cellposition.CellPosition;

public class Cell extends CellPosition{
    private boolean isAlive;

    public Cell(int posX, int posY) {
        super(posX, posY);
        this.isAlive = true;
    }

    public void die(){
        this.isAlive = false;
    }
}
