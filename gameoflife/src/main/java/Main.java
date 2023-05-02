import controllers.GameController;
import model.grid.Grid;
import view.ViewFrame;

public class Main {
    public static void main(String[] args) {
        Grid grid = new Grid(200, 200);
        ViewFrame viewFrame = new ViewFrame();

        GameController controller = new GameController(grid, viewFrame);

        // test for cell drawing
//        grid.addCell(100,100);
//        grid.addCell(101,101);
//        grid.addCell(102,102);
//        grid.addCell(103,103);
//        grid.addCell(104,104);
//        grid.addCell(105,105);
//        grid.addCell(106,106);
//        grid.addCell(107,107);


        controller.startGame();
    }
}
