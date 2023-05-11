import controllers.GameController;
import model.grid.Grid;
import view.GridView;

import javax.swing.*;

public class Main {

    public static void main(String[] args) {
        int rows = 100;
        int cols = 100;

        Grid grid = new Grid(rows, cols);
        GridView gridView = new GridView(grid, 10);
        GameController gameController = new GameController(grid, gridView);

        JFrame frame = new JFrame("Game of Life");
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.getContentPane().add(gridView);
        frame.pack();
        frame.setVisible(true);

        gameController.startGame();

    }
}