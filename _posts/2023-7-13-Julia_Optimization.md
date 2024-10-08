---
layout: post
title: Solving Complex Puzzles Using Julia Optimization Constraint Programming
description:
image: assets/images/pic19.jpg
---

<!-- Content -->
Optimization is a powerful tool that allows us to solve a variety of complex problems, ranging from resource allocation to combinatorial puzzles. In this article, we explore two interesting applications of optimization using Julia and the JuMP library:

1. **Sudoku Solver Using Integer Programming**
2. **Grandmother Puzzle Solver Using Advanced Constraint Modeling**

Both problems illustrate the power of constraint programming for handling unique logical dependencies and constraints, making them ideal showcases for learning about optimization techniques.

<h3>Why Use Optimization?</h3>

Optimization is the process of finding the best solution from a set of feasible solutions, typically defined by a series of constraints. In combinatorial puzzles, like Sudoku or the Grandmother Puzzle, we need to balance multiple constraints simultaneously while seeking either a feasible configuration (as in Sudoku) or a unique optimal solution (as in the Grandmother Puzzle).

By modeling these puzzles using Julia and JuMP, we leverage the power of state-of-the-art solvers to explore the solution space effectively and handle complex logical relationships.

<h3>1. Sudoku Solver Using Integer Programming</h3>

Sudoku is a popular logic puzzle that involves filling a 9x9 grid with numbers from 1 to 9, ensuring that each row, column, and 3x3 sub-grid contains all numbers exactly once. While this puzzle is straightforward for humans to solve, it poses an interesting challenge for optimization algorithms due to the high number of possible configurations.

**Modeling the Sudoku Problem:**

We can model Sudoku using binary decision variables for each cell in the grid. If we let `x[i, j, k]` represent a binary variable that is 1 when cell `(i, j)` contains the number `k`, and 0 otherwise, we can define a set of constraints:

- **Single Number per Cell:** Each cell must contain exactly one number.
- **Row and Column Uniqueness:** Each number must appear exactly once in every row and every column.
- **3x3 Sub-grid Constraints:** Each sub-grid (3x3 block) must also contain every number exactly once.

In the standard Sudoku problem, we seek a feasible solution that satisfies all constraints. However, in our variation, called **Jeff-Doku**, we add an objective function to **maximize the sum of the numbers on the main diagonal** of the grid. This objective turns a simple constraint satisfaction problem into an optimization problem, allowing us to explore more sophisticated strategies.

**Results:**

Our solver successfully handles both standard Sudoku and the Jeff-Doku variant, highlighting how flexible mathematical models can be adapted for different objectives. The power of optimization lies in the ease with which we can modify constraints or add new objectives to fine-tune our solution.

<h3>2. Grandmother Puzzle Solver Using Advanced Constraints</h3>

The Grandmother Puzzle is a more complex combinatorial problem involving five grandmothers, their daughters, sons-in-law, and grandsons. The objective is to determine the family relationships based on a series of clues:

- Each grandmother has a unique daughter, son-in-law, and grandson.
- The puzzle involves a series of interdependent rules, such as: "Maxine’s daughter is not Carla," and "Tim’s mother is Cindy, who is married to Jake."

**Modeling the Grandmother Puzzle:**

We define binary variables for each possible relationship, such as `xD[g, d]`, which is 1 if grandmother `g` has daughter `d`, and 0 otherwise. Similarly, variables `xH[g, h]` and `xS[g, s]` indicate son-in-law and grandson assignments.

**Key Constraints:**

1. **Each Grandmother has One Daughter, One Son-in-Law, and One Grandson:**  
   This constraint ensures that every grandmother has exactly one family configuration.

2. **Each Role is Uniquely Assigned:**  
   No two grandmothers can share the same daughter, son-in-law, or grandson.

3. **Clue-Based Logical Dependencies:**  
   We add constraints based on the provided clues, such as "Cathy is married to Joe, but their son is not Tab."

**Results:**

After implementing these constraints, our solver identifies the correct family relationships, demonstrating how constraint programming can navigate through intricate logical rules to find a feasible solution.

<h3>Optimization with Julia and JuMP</h3>

Using Julia and the JuMP library, we were able to solve both puzzles by defining the problem constraints clearly and leveraging powerful solvers to explore the solution space. The flexibility of JuMP allowed us to model a wide range of constraints efficiently, making it an ideal tool for tackling combinatorial optimization problems.

<h3>Conclusion</h3>

The Sudoku and Grandmother Puzzle solvers illustrate the versatility and power of constraint programming in handling real-world problems. By defining relationships and dependencies mathematically, we can explore the solution space systematically and achieve optimal or feasible configurations quickly.

For a more detailed exploration of these puzzles and the code, check out the complete <a href="https://github.com/placenciohid/Resume/blob/e417cfd06f91fbb970e640462c0319219ef94920/Julia%20Optimization%20-%20Sudoki%20and%20Brain%20Puzzle.ipynb"><b>Jupyter notebook</b></a> on GitHub.