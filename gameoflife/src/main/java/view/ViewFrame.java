package view;

import javax.swing.*;

public class ViewFrame extends JFrame {
    private final JFrame frame;
    private GridPanel gridPanel;

    public ViewFrame() {
        frame = new JFrame();

        frame.setSize(1920, 1080);

        frame.setLocationRelativeTo(null);
        frame.setTitle("Game of life");
        frame.setDefaultCloseOperation(EXIT_ON_CLOSE);

        frame.setVisible(true);
    }

    public JFrame getFrame() {
        return frame;
    }

    public GridPanel getGridPane() {
        return gridPanel;
    }

    public void setGridPane(GridPanel gridPanel) {
        this.gridPanel = gridPanel;
        frame.add(gridPanel);
        frame.pack();
    }
}
