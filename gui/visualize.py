import pygame
import time
import logging

# Configure logger
logger = logging.getLogger()

# Constants
GRID_SIZE = 9
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BUTTON_COLOR = (200, 200, 200)
HOVER_COLOR = (170, 170, 170)
TEXT_COLOR = (50, 50, 50)
HIGHLIGHT_COLOR = (240, 128, 128)
SOLVING_COLOR = (100, 149, 237)

BUTTONS = ["Naive Solver", "CSP Solver", "Manual Play", "Clean Board", "Load New Puzzle"]

def draw_grid(screen, cell_size, grid_offset):
    """Draws the Sudoku grid with adaptive scaling and centering."""
    grid_size = cell_size * GRID_SIZE
    x_offset, y_offset = grid_offset

    for i in range(GRID_SIZE + 1):
        line_width = 3 if i % 3 == 0 else 1  # Thicker lines for sub-grids
        pygame.draw.line(screen, BLACK, (x_offset, y_offset + i * cell_size), (x_offset + grid_size, y_offset + i * cell_size), line_width)
        pygame.draw.line(screen, BLACK, (x_offset + i * cell_size, y_offset), (x_offset + i * cell_size, y_offset + grid_size), line_width)


def draw_board(screen, board, selected_cell=None, solving_cell=None, cell_size=50, grid_offset=(0, 0)):
    """Draws the Sudoku board with adaptive scaling and centering."""
    draw_grid(screen, cell_size, grid_offset)
    font = pygame.font.SysFont(None, cell_size // 2)

    x_offset, y_offset = grid_offset
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            value = board[row][col]
            cell_x = x_offset + col * cell_size
            cell_y = y_offset + row * cell_size

            # Highlight selected cell
            if selected_cell == (col, row):
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, (cell_x, cell_y, cell_size, cell_size))

            # Highlight the current solving cell
            if solving_cell == (col, row):
                pygame.draw.rect(screen, SOLVING_COLOR, (cell_x, cell_y, cell_size, cell_size))

            # Draw the number in the cell
            if value != 0:
                text = font.render(str(value), True, BLACK)
                text_rect = text.get_rect(center=(cell_x + cell_size // 2, cell_y + cell_size // 2))
                screen.blit(text, text_rect)


def draw_buttons(screen, font, window_width, window_height, grid_height):
    """Draws the control buttons with adaptive scaling and positioning."""
    button_width = 150
    button_height = 50
    spacing = 20
    total_button_width = len(BUTTONS) * button_width + (len(BUTTONS) - 1) * spacing
    start_x = (window_width - total_button_width) // 2
    button_y = grid_height + 20

    for index, label in enumerate(BUTTONS):
        rect = pygame.Rect(start_x + index * (button_width + spacing), button_y, button_width, button_height)
        mouse_pos = pygame.mouse.get_pos()
        if rect.collidepoint(mouse_pos):  # Highlight button on hover
            pygame.draw.rect(screen, HOVER_COLOR, rect)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, rect)

        text = font.render(label, True, TEXT_COLOR)
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)


def handle_button_click(mouse_pos, window_width, window_height, grid_height):
    """Checks if a button was clicked and returns the selected mode."""
    button_width = 150
    button_height = 50
    spacing = 20
    total_button_width = len(BUTTONS) * button_width + (len(BUTTONS) - 1) * spacing
    start_x = (window_width - total_button_width) // 2
    button_y = grid_height + 20

    for index, label in enumerate(BUTTONS):
        rect = pygame.Rect(start_x + index * (button_width + spacing), button_y, button_width, button_height)
        if rect.collidepoint(mouse_pos):
            return label.lower().replace(" ", "_")
    return None


def solve_visual(screen, solver, cell_size, grid_offset, row_number=None, algorithm_name=None):
    """
    Animates the solving process step-by-step with dynamic highlighting.
    Tracks the number of steps and the time taken to solve.
    Logs the row number, steps, and time taken for statistical analysis.
    """
    print("Starting solver visualization...")
    steps = 0  # Track the number of steps
    solved = False

    start_time = time.time()  # Start the timer

    for board_state, solving_cell in solver.solve_with_steps():
        steps += 1
        draw_board(screen, board_state.get_board(), solving_cell=solving_cell, cell_size=cell_size, grid_offset=grid_offset)
        pygame.display.flip()
        pygame.time.delay(100)  # Adjust delay for smoother animation
        if solving_cell is None:  # Solved
            solved = True
            break

    end_time = time.time()  # End the timer
    time_taken = end_time - start_time

    # Log results
    if algorithm_name and row_number is not None:
        logger.info(
            f"Row: {row_number}, Algorithm: {algorithm_name}, Steps: {steps}, Time: {time_taken:.2f} seconds"
        )

    if solved:
        print("Solver visualization completed. Sudoku Solved!")
        print(f"Number of steps: {steps}")
        print(f"Time taken: {time_taken:.2f} seconds")
    else:
        print("Solver visualization completed. No solution found.")
        print(f"Number of steps: {steps}")
        print(f"Time taken: {time_taken:.2f} seconds")

    
def handle_grid_click(mouse_pos, cell_size, grid_offset):
    """
    Checks if a grid cell was clicked and returns its coordinates (column, row).
    
    Args:
        mouse_pos (tuple): The position of the mouse click (x, y).
        cell_size (int): The size of each cell in the Sudoku grid.
        grid_offset (tuple): The top-left corner offset of the grid (x_offset, y_offset).

    Returns:
        tuple: (col, row) if a cell was clicked, otherwise None.
    """
    x, y = mouse_pos
    x_offset, y_offset = grid_offset

    # Check if the click is within the grid boundaries
    if x_offset <= x < x_offset + cell_size * GRID_SIZE and y_offset <= y < y_offset + cell_size * GRID_SIZE:
        row = (y - y_offset) // cell_size
        col = (x - x_offset) // cell_size
        return col, row  # Return grid coordinates as (col, row)
    return None  # Return None if click is outside the grid
