package view;

import javax.swing.*;
import java.awt.*;

public class GridPane extends JPanel {
    int rows;
    int cols;

    public GridPane(int rows, int cols) {
        this.rows = rows;
        this.cols = cols;
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

        g.setColor(Color.BLACK);

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
    }
}
