package controllers;

import model.cell.Cell;
import model.grid.Grid;
import view.CellView;
import view.GridView;

import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Scanner;

public class GameController {
    private final Grid grid;
    private final GridView gridView;
    private final int underpopulationThreshold;
    private final int overpopulationThreshold;
    private final int reproductionThreshold;
    private final int delay;
    private boolean isRunning;
    private boolean isPaused;

    public GameController(Grid grid, GridView gridView) {
        Scanner sc = new Scanner(System.in);

        this.grid = grid;
        this.gridView = gridView;
        this.isRunning = false;

        System.out.println("Input underpopulation threshold (int): ");
        this.underpopulationThreshold = sc.nextInt();
        System.out.println("Input overpopulation threshold (int): ");
        this.overpopulationThreshold = sc.nextInt();
        System.out.println("Input reproduction threshold (int): ");
        this.reproductionThreshold = sc.nextInt();
        this.isPaused = false;
        this.delay = 500; //ms
        initializeListeners();
    }

    public void startGame() {
        if (!isRunning) {
            isRunning = true;
            Thread gameLoopThread = new Thread(new GameLoop());
            gameLoopThread.start();
        }
    }

    public void pauseGame() {
        isPaused = true;
    }

    public void resumeGame() {
        isPaused = false;
    }

    private void initializeListeners() {
        for (int i = 0; i < grid.getRows(); i++) {
            for (int j = 0; j < grid.getCols(); j++) {
                Cell cell = grid.getCell(i, j);
                CellView cellView = gridView.getCellView(i, j);
                cellView.addMouseListener(new CellClickListener(cell));
            }
        }

        gridView.addMouseListener(new GridClickListener());
        gridView.addKeyListener(new PauseKeyListener());
        gridView.setFocusable(true);
    }


    private boolean isValidCell(int neighborX, int neighborY) {
        return neighborX >= 0 && neighborX < grid.getRows() && neighborY >= 0 && neighborY < grid.getCols();
    }

    private class CellClickListener extends MouseAdapter {
        private final Cell cell;

        public CellClickListener(Cell cell) {
            this.cell = cell;
        }

        @Override
        public void mousePressed(MouseEvent e) {
            toggleCellState();
        }

        private void toggleCellState() {
            cell.setAlive(!cell.isAlive());
            gridView.updateGridView();
        }
    }

    private class GridClickListener extends MouseAdapter {
        @Override
        public void mousePressed(MouseEvent e) {
            int cellSize = gridView.getCellSize();
            int row = e.getY() / cellSize;
            int col = e.getX() / cellSize;

            if (isValidCell(row, col)) {
                Cell cell = grid.getCell(row, col);
                cell.setAlive(!cell.isAlive());
                gridView.getCellView(row, col).updateColor();
                gridView.repaint();
            }

            gridView.addMouseMotionListener(new MouseAdapter() {
                @Override
                public void mouseDragged(MouseEvent e) {
                    int row = e.getY() / cellSize;
                    int col = e.getX() / cellSize;

                    if (isValidCell(row, col)) {
                        Cell cell = grid.getCell(row, col);
                        cell.setAlive(true);
                        gridView.getCellView(row, col).updateColor();
                        gridView.repaint();
                    }
                }
            });
        }

        @Override
        public void mouseReleased(MouseEvent e) {
            gridView.removeMouseMotionListener(gridView.getMouseMotionListeners()[0]);
        }
    }

    private class GameLoop implements Runnable {
        @Override
        public void run() {
            while (isRunning) {
                if (!isPaused) {
                    updateGrid();
                }
                try {
                    Thread.sleep(delay);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }

        private void updateGrid() {
            Grid newGrid = new Grid(grid.getRows(), grid.getCols());

            for (int i = 0; i < grid.getRows(); i++) {
                for (int j = 0; j < grid.getCols(); j++) {
                    Cell cell = grid.getCell(i, j);
                    int liveNeighbors = countLiveNeighbors(cell);

                    if (cell.isAlive()) {
                        // Rule 1: Any live cell with fewer than two live neighbors dies (underpopulation)
                        if (liveNeighbors < underpopulationThreshold) {
                            newGrid.setAlive(i, j, false);
                        }
                        // Rule 2: Any live cell with two or three live neighbors survives
                        else if (liveNeighbors == 2 || liveNeighbors == 3) {
                            newGrid.setAlive(i, j, true);
                        }
                        // Rule 3: Any live cell with more than three live neighbors dies (overpopulation)
                        else if (liveNeighbors > overpopulationThreshold) {
                            newGrid.setAlive(i, j, false);
                        }
                    } else {
                        // Rule 4: Any dead cell with exactly three live neighbors becomes a live cell (reproduction)
                        if (liveNeighbors == reproductionThreshold) {
                            newGrid.setAlive(i, j, true);
                        }
                    }
                }
            }

            // Update the original grid with the new grid state
            for (int i = 0; i < grid.getRows(); i++) {
                for (int j = 0; j < grid.getCols(); j++) {
                    grid.setAlive(i, j, newGrid.isAlive(i, j));
                }
            }

            gridView.updateGridView();
        }

        private int countLiveNeighbors(Cell cell) {
            int count = 0;

            int x = cell.getPosX();
            int y = cell.getPosY();

            for (int i = -1; i <= 1; i++) {
                for (int j = -1; j <= 1; j++) {
                    //skip current cell
                    if (i == 0 && j == 0) {
                        continue;
                    }

                    int neighborX = x + i;
                    int neighborY = y + j;

                    if (isValidCell(neighborX, neighborY)) {
                        Cell neighborCell = grid.getCell(neighborX, neighborY);

                        if (neighborCell.isAlive()) {
                            count++;
                        }
                    }
                }
            }
            return count;
        }
    }

    private class PauseKeyListener extends KeyAdapter {
        @Override
        public void keyPressed(KeyEvent e) {
            if (e.getKeyCode() == KeyEvent.VK_SPACE) {
                if (isPaused) {
                    resumeGame();
                } else {
                    pauseGame();
                }
            }
        }
    }
}

