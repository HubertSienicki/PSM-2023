package view;

import model.grid.Grid;
import org.jetbrains.annotations.NotNull;

import javax.swing.*;
import java.awt.*;

public class GridPanel extends JPanel {
    int rows;
    private Grid grid;

    public GridPanel(@NotNull Grid grid) {
        this.grid = grid;
        this.rows = grid.getRows();
    }

    @Override
    public Dimension getPreferredSize() {
        return new Dimension(1000, 1000);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        int panelWidth = getWidth();
        int panelHeight = getHeight();
        int panelSize = Math.min(panelWidth, panelHeight);

        float cellSize = (float) panelSize / rows;

        int xOffset = (panelWidth - panelSize) / 2;
        int yOffset = (panelHeight - panelSize) / 2;

        g.setColor(Color.gray);

        for (int i = 0; i <= rows; i++) {
            int x = Math.round(cellSize * i);
            int y = Math.round(cellSize * i);
            if (i > 0 && i < rows) {
                g.drawLine(xOffset + x, yOffset, xOffset + x, yOffset + panelSize);
                g.drawLine(xOffset, yOffset + y, xOffset + panelSize, yOffset + y);
            } else {
                g.drawLine(xOffset + x, yOffset, xOffset + x, yOffset + panelSize + 1);
                g.drawLine(xOffset, yOffset + y, xOffset + panelSize + 1, yOffset + y);
            }
        }

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < rows; j++) {
                if (grid.getCellGrid()[i][j] != null) {
                    g.setColor(Color.magenta);
                    g.fillRect(Math.round(xOffset + i * cellSize) + 1, Math.round(yOffset + j * cellSize) + 1, Math.round(cellSize) - 1, Math.round(cellSize) - 1);
                }
            }
        }
    }
}
