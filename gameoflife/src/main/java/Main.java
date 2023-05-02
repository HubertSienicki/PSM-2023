import controllers.GameController;
import model.grid.Grid;
import view.ViewFrame;

public class Main {
    public static void main(String[] args) {
        Grid grid = new Grid(200,200);
        ViewFrame viewFrame = new ViewFrame();

        GameController controller = new GameController(grid, viewFrame);

        grid.addCell(100,100);

        controller.startGame();
    }
}
