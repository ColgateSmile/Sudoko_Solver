
# Sudoku Solver

A Python-based Sudoku Solver that uses two distinct algorithms, **Naive Backtracking** and **Constraint Satisfaction Problem (CSP)**, to solve Sudoku puzzles with visualization and interactive features. This project combines efficient solving techniques, educational value, and an intuitive user interface.

---

## **Features**

### **1. Algorithms**
- **Naive Backtracking Solver**:
  - A basic brute force method that tries every possible number for each empty cell.
  - Guarantees a solution if one exists, but can be slow for complex puzzles.

- **CSP Solver (Constraint Propagation)**:
  - A smarter algorithm that reduces the search space by applying constraints (row, column, and sub-grid rules).
  - Uses the **Minimum Remaining Values (MRV)** heuristic to prioritize cells with the fewest possible values.
  - Falls back to backtracking when constraints cannot determine a value.

---

### **2. Visualization**
- Watch the solving process in real-time, with:
  - Highlighted solving cells.
  - Backtracking steps clearly visualized.
  - Dynamic animations to track the algorithm's progress.

---

### **3. Manual Play**
- Solve puzzles interactively:
  - Select a cell and input values.
  - Get real-time feedback on correct and incorrect entries.
  - Play alongside or independently of the solver.

---

### **4. Performance Metrics**
- Logs the following for each algorithm:
  - **Number of steps**.
  - **Time taken** to solve the puzzle.
- Saves results to a log file for statistical analysis and performance comparison.

---

### **5. Puzzle Management**
- Load new puzzles from a CSV file containing thousands of Sudoku puzzles.
- Reset or clean the board to start fresh.

---

### **6. Adaptive User Interface**
- The GUI adjusts dynamically to screen size.
- Buttons and the Sudoku grid are centered and scale properly for different resolutions.

---

## **Getting Started**

### **1. Prerequisites**
- Python 3.9 or higher.
- Required libraries:
  - `pygame`
  - `numpy`

### **2. Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sudoku-solver.git
   ```
2. Navigate to the project directory:
   ```bash
   cd sudoku-solver
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### **3. Running the Application**
Run the main script:
```bash
python main.py
```

---

## **How It Works**

### **Algorithms**
- **Naive Backtracking**:
  - Tries all possible values in each empty cell.
  - Backtracks when a conflict arises.
- **CSP Solver**:
  - Reduces possible values using constraints and the MRV heuristic.
  - Falls back to backtracking when necessary.

### **User Interaction**
- Click on cells to select and input values.
- Press buttons to solve using the algorithms, clean the board, or load new puzzles.

---

## **Project Structure**
```
sudoku-solver/
├── main.py                   # Entry point of the application
├── input/                    # Folder containing Sudoku CSV file
│   └── sudoku.csv
├── solvers/                  # Solving algorithms
│   ├── naive_solver.py
│   ├── wise_solver.py
│   └── base_solver.py
├── gui/                      # GUI-related code
│   ├── visualize.py
│   └── __init__.py
├── loaders/                  # Puzzle loaders
│   ├── csv_loader.py
│   └── base_loader.py
├── solver_performance.log    # Log file for performance metrics
└── README.md                 # Project documentation
```

---

## **Future Enhancements**
- Add support for custom Sudoku puzzle input via the GUI.
- Optimize the CSP solver for larger grid sizes (e.g., 16x16 Sudoku).
- Add statistical charts for algorithm performance directly in the application.

---

## **Contributing**
Contributions are welcome! Feel free to submit issues and pull requests to improve the project.

---

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**
- Inspired by the challenge of solving Sudoku with AI techniques.
- Built with love and `pygame`! 🎮

## **examle compariosn of the 2 algorithems: **
## **CSP based algorithem 48 moves 7 secoonds to solve: **
![Sudoku Solver - CSP 0503seconds 48 moves](https://github.com/user-attachments/assets/c579add9-dd86-468f-89bf-1744df573e3e)

## **Brute Force based algorithem 426 moves 47 secoonds to solve: **
![Naive_bruteForce](https://github.com/user-attachments/assets/f52b1c73-f1bf-4ff1-9b52-6daa035e1883)
