from copy import deepcopy
import pygame
import logging
from loaders.csv_loader import CsvLoader
from solvers.naive_solver import NaiveSolver
from solvers.wise_solver import WiseSolver
from gui.visualize import draw_board, draw_buttons, handle_button_click, handle_grid_click, solve_visual

# Configure logger
logging.basicConfig(
    filename="solver_stats.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger()

# Constants
GRID_SIZE = 9
DEFAULT_SCREEN_SIZE = 600
MENU_HEIGHT = 100
BUTTON_FONT = None

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((DEFAULT_SCREEN_SIZE, DEFAULT_SCREEN_SIZE + MENU_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Sudoku Solver")
    BUTTON_FONT = pygame.font.SysFont(None, 36)

    # Load Sudoku puzzle
    sudoku, solved_sudoku = CsvLoader().load()
    saved_sudoku = deepcopy(sudoku)

    # State variables
    running = True
    selected_mode = None
    selected_cell = None

    while running:
        window_width, window_height = screen.get_size()
        cell_size = min(window_width, window_height - MENU_HEIGHT) // GRID_SIZE
        grid_offset = ((window_width - cell_size * GRID_SIZE) // 2, (window_height - MENU_HEIGHT - cell_size * GRID_SIZE) // 2)

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw Sudoku board and buttons
        draw_board(
            screen,
            sudoku.get_board(),
            selected_cell,
            cell_size=cell_size,
            grid_offset=grid_offset,
        )
        draw_buttons(screen, BUTTON_FONT, window_width, window_height, grid_offset[1] + cell_size * GRID_SIZE)

        # Update display
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)  # Adjust to new window size
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle button clicks
                clicked_button = handle_button_click(event.pos, window_width, window_height, grid_offset[1] + cell_size * GRID_SIZE)
                if clicked_button:
                    selected_mode = clicked_button
                    print(f"Button clicked: {selected_mode}")

                # Handle grid cell selection in manual play
                if selected_mode == "manual_play":
                    selected_cell = handle_grid_click(event.pos, cell_size, grid_offset)
                    if selected_cell:
                        print(f"Selected cell: {selected_cell}")

                # Handle solver selection
                if selected_mode == "naive_solver":
                    print("Starting Naive Solver...")
                    solver = NaiveSolver(sudoku=sudoku)
                    solve_visual(
                        screen,
                        solver,
                        cell_size,
                        grid_offset,
                        algorithm_name="Naive",
                    )
                elif selected_mode == "csp_solver":
                    print("Starting CSP Solver...")
                    sudoku = deepcopy(saved_sudoku)  # Reset the board
                    solver = WiseSolver(sudoku=sudoku)
                    solve_visual(
                        screen,
                        solver,
                        cell_size,
                        grid_offset,
                        algorithm_name="CSP",
                    )
                elif selected_mode == "clean_board":
                    print("Cleaning the Sudoku board...")
                    sudoku = deepcopy(saved_sudoku)  # Reset the board
                    selected_cell = None
                elif selected_mode == "load_new_puzzle":
                    print("Loading new Sudoku puzzle...")
                    sudoku, solved_sudoku = CsvLoader().load()  # Load a new puzzle
                    saved_sudoku = deepcopy(sudoku)  # Update saved puzzle
                    selected_cell = None  # Reset selected cell
                    print("New Sudoku puzzle loaded!")
