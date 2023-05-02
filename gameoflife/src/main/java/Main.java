import controllers.GameController;
import grid.Grid;
import view.ViewFrame;

public class Main {
    public static void main(String[] args) {
        Grid grid = new Grid();
        ViewFrame viewFrame = new ViewFrame();

        GameController controller = new GameController(grid, viewFrame);
    }
}
