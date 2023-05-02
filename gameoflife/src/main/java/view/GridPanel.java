package view;

import model.cell.Cell;
import model.grid.Grid;
import org.jetbrains.annotations.NotNull;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class GridPanel extends JPanel {
    int rows;
    private Grid grid;

    public GridPanel(@NotNull Grid grid) {
        this.grid = grid;
        this.rows = grid.getRows();

        addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                int panelWidth = getWidth();
                int panelHeight = getHeight();
                int panelSize = Math.min(panelWidth, panelHeight);

                int xOffset = (panelWidth - panelSize) / 2;
                int yOffset = (panelHeight - panelSize) / 2;

                if(e.getX() >= xOffset && e.getX() <= xOffset + panelSize
                && e.getY() >= yOffset && e.getY() <= yOffset + panelSize){
                    float cellSize = (float) panelSize / rows;
                    int i = (int) ((e.getX() - xOffset) / cellSize);
                    int j = (int) ((e.getY() - yOffset) / cellSize);

                    if(grid.getCellGrid()[i][j] == null){
                        grid.getCellGrid()[i][j] = new Cell(i, j);
                        repaint();
                    }
                }
            }
        });
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
