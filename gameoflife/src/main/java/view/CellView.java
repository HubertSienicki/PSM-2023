package view;

import model.cell.Cell;

import javax.swing.*;
import java.awt.*;

public class CellView extends JPanel {
    private Cell cell;

    public CellView(Cell cell) {
        this.cell = cell;
        updateColor();
    }

    public void updateColor() {
        if (cell.isAlive()) {
            this.setBackground(Color.BLACK);
        } else {
            this.setBackground(Color.WHITE);
        }
    }
}
