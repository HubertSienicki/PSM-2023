package model.cell;

public class Cell{
    private int posX;
    private int posY;
    private boolean isAlive;

    public Cell(int posX, int posY) {
        this.posX = posX;
        this.posY = posY;
        this.isAlive = false;
    }

    public boolean isAlive(){
        return isAlive;
    }

    public void setAlive(boolean isAlive){
        this.isAlive = isAlive;
    }

    public int getPosX() {
        return posX;
    }

    public int getPosY() {
        return posY;
    }
}
