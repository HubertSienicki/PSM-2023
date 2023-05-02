package view;

import javax.swing.*;

public class ViewFrame extends JFrame {
    private JFrame frame;

    public ViewFrame() {
        frame = new JFrame();

        frame.setSize(1920, 1080);

        frame.setLocationRelativeTo(null);
        frame.setTitle("Game of life");
        frame.setDefaultCloseOperation(EXIT_ON_CLOSE);

        frame.setVisible(true);
    }

    public void drawGrid(int rows, int cols){
        frame.add(new GridPane(rows, cols));
    }
}
