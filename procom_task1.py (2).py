pip install ortools

import ortools


from ortools.sat.python import cp_model


model = cp_model.CpModel()

a = model.NewIntVar(1, 3, 'a') 
b = model.NewIntVar(1, 3, 'b')
c = model.NewIntVar(1, 3, 'c')


model.Add(a != b) 
model.Add(b != c)
model.Add(a != c)


solver = cp_model.CpSolver()


solution_printer = cp_model.VarArraySolutionPrinter([a, b, c])

solver.parameters.enumerate_all_solutions = True

solver.Solve(model, solution_printer)


print("optimal", cp_model.OPTIMAL)

print("Feasible", cp_model.FEASIBLE)

print("InFeasible", cp_model.INFEASIBLE)
print("UNKNOWN", cp_model.UNKNOWN)









# # Custom class to print feasible solutions
# class FeasibleSolutionPrinter(cp_model.CpSolverSolutionCallback):
#     def __init__(self, variables):
#         cp_model.CpSolverSolutionCallback.__init__(self)
#         self.variables = variables
#         self.solution_count = 0

#     def on_solution_callback(self):
#         self.solution_count += 1
#         print(f"Feasible Solution {self.solution_count}: ", end="")
#         for var in self.variables:
#             print(f"{var.Name()} = {self.Value(var)}", end="  ")
#         print()

# # Enable finding multiple solutions
# solution_printer = FeasibleSolutionPrinter([x, y, z])
# solver.parameters.enumerate_all_solutions = True

# # Solve the model and find all feasible solutions
# status = solver.Solve(model, solution_printer)

# # If no feasible solution was found
# if solution_printer.solution_count == 0:
#     print("No feasible solution found.")









from ortools.sat.python import cp_model

model = cp_model.CpModel()
alice = model.NewIntVar(0, 2, 'x')
bob= model.NewIntVar(0, 2, 'y')
charlie= model.NewIntVar(0, 2, 'z')

c1=model.Add(alice!=bob)
c2=model.Add(bob!=0)

solver=cp_model.CpSolver()
solver.solve(model)


#Import the google ortools library to solve the csp problem
from ortools.sat.python import cp_model

# Declare the model and bind it with CpModel which is already present in ortools library
model = cp_model.CpModel()

#Declaring the set of variables for csp
num_vals = 3
x = model.new_int_var(0, num_vals - 1, "x")
y = model.new_int_var(0, num_vals - 1, "y")
z = model.new_int_var(0, num_vals - 1, "z")

#Declaring Constraints
model.add(x != y)

#output:-
# <ortools.sat.python.cp_model.Constraint at 0x7ec6e989bd50>


# # Create the solver
solver = cp_model.CpSolver()
solution_printer = cp_model.VarArraySolutionPrinter([x, y, z])
solver.parameters.enumerate_all_solutions = True

# Solve the problem
solver.Solve(model, solution_printer)








from ortools.sat.python import cp_model

# Create the model
model = cp_model.CpModel()

# Define variables with domain {0, 1, 2}
num_vals = 3
x = model.NewIntVar(0, num_vals - 1, "x")
y = model.NewIntVar(0, num_vals - 1, "y")
z = model.NewIntVar(0, num_vals - 1, "z")

# Add constraint: x != y
model.Add(x != y)

# Create solver
solver = cp_model.CpSolver()

# Solve the model
status = solver.Solve(model)
print(status)
# Display solver status in a readable way
status_mapping = {
    cp_model.OPTIMAL: "OPTIMAL",
    cp_model.FEASIBLE: "FEASIBLE",
    cp_model.INFEASIBLE: "INFEASIBLE",
    cp_model.UNKNOWN: "UNKNOWN"
}

print(f"Solver Status: {status_mapping.get(status, 'UNKNOWN')} ({status})")

# Print solution if feasible or optimal
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f"x = {solver.Value(x)}")
    print(f"y = {solver.Value(y)}")
    print(f"z = {solver.Value(z)}")
else:
    print("No feasible solution found.")


from ortools.sat.python import cp_model

# Create the model
model = cp_model.CpModel()

# Define variables with domain {0, 1, 2}
num_vals = 3
x = model.NewIntVar(0, num_vals - 1, "x")
y = model.NewIntVar(0, num_vals - 1, "y")
z = model.NewIntVar(0, num_vals - 1, "z")

# Add constraints that conflict
model.Add(x != y)    # x and y must be different
model.Add(x == y)    # x and y must be same → conflict
model.Add(z == 0)    # extra constraint for demonstration

# Create solver
solver = cp_model.CpSolver()

# Solve the model
status = solver.Solve(model)
print(status)

# Display solver status in a readable way
status_mapping = {
    cp_model.OPTIMAL: "OPTIMAL",
    cp_model.FEASIBLE: "FEASIBLE",
    cp_model.INFEASIBLE: "INFEASIBLE",
    cp_model.UNKNOWN: "UNKNOWN"
}

print(f"Solver Status: {status_mapping.get(status, 'UNKNOWN')} ({status})")

# Print solution if feasible or optimal
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f"x = {solver.Value(x)}")
    print(f"y = {solver.Value(y)}")
    print(f"z = {solver.Value(z)}")
else:
    print("No feasible solution found.")












#Import the google ortools library to solve the csp problem
from ortools.sat.python import cp_model

# Declare the model and bind it with CpModel which is already present in ortools library
model = cp_model.CpModel()

#Declaring the set of variables for csp
num_vals = 3
x = model.new_int_var(0, num_vals - 1, "x")
y = model.new_int_var(0, num_vals - 1, "y")
z = model.new_int_var(0, num_vals - 1, "z")

#Declaring Constraints
model.add(x != y)

#output:-
# <ortools.sat.python.cp_model.Constraint at 0x7ec6e989bd50>

solver = cp_model.CpSolver()
status = solver.solve(model)
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f"x = {solver.value(x)}")
    print(f"y = {solver.value(y)}")
    print(f"z = {solver.value(z)}")
else:
    print("No solution found.")


l=[[1 for _ in range(10)] for _ in range(10)]
l

size=4
import random
a= (random.randint(0, size-1), random.randint(0, size-1))







import math      # Used for mathematical operations like square root
import random    # Used to generate random start and goal positions
from ortools.sat.python import cp_model   # Import OR-Tools CP-SAT solver

# Class representing the grid environment
class GridEnvironment:
    def __init__(self, size):
        self.size = size   # Size of the grid (e.g., 10x10)

        # Create a grid filled with zeros
        self.grid = [[0 for _ in range(size)] for _ in range(size)]

        # Randomly generate the start position inside the grid
        self.start = (random.randint(0, size-1), random.randint(0, size-1))

        # Randomly generate the goal position inside the grid
        self.goal = (random.randint(0, size-1), random.randint(0, size-1))

    # Function to solve the CSP problem
    def solve_csp(self):

        # Create a CSP model
        model = cp_model.CpModel()

        # Extract x and y coordinates of start and goal positions
        x1, y1 = self.start
        x2, y2 = self.goal

        # -------- Variables --------

        # Calculate horizontal distance between start and goal
        a = abs(x2 - x1)

        # Calculate vertical distance between start and goal
        b = abs(y2 - y1)

        c = model.NewIntVar(0, self.size * 2, 'c')

        # Variables to store squared values
        a_sq = model.NewIntVar(0, self.size**2, 'a_sq')
        b_sq = model.NewIntVar(0, self.size**2, 'b_sq')
        c_sq = model.NewIntVar(0, self.size**2, 'c_sq')


        # Define a_sq = a * a
        model.AddMultiplicationEquality(a_sq, [a, a])

        # Define b_sq = b * b
        model.AddMultiplicationEquality(b_sq, [b, b])

        # Define c_sq = c * c
        model.AddMultiplicationEquality(c_sq, [c, c])

        # Apply Pythagorean theorem: c² = a² + b²
        model.Add(c_sq == a_sq + b_sq)

        # -------- Solve the model --------

        # Create solver object
        solver = cp_model.CpSolver()

        # Solve the CSP model
        status = solver.Solve(model)

        # If a valid solution is found
        if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:

            # Return base, height, and calculated hypotenuse
            return a, b, solver.Value(c)

            # (This line will never execute because return is above)
            print(a, b, solver.Value(c))

        # If solver fails, calculate distance using normal math formula
        return a, b, math.sqrt(a**2 + b**2)


    # Function to display results
    def display(self):

        # Print start and goal positions
        print(f"Start Position: {self.start}")
        print(f"Goal Position: {self.goal}")

        # Solve the CSP problem and get distances
        a, b, c = self.solve_csp()

        # Display calculated distances
        print(f"Calculated Distances: Base={a}, Height={b}, Hypotenuse={c:.2f}")


environment = GridEnvironment(10)

# Run the simulation and display results
environment.display()

import heapq   
import math    

class DronePathPlanner:
    def __init__(self, grid, start, goal):
        self.grid = grid   
        self.start = start 
        self.goal = goal  

        
        self.rows = len(grid)
        self.cols = len(grid[0])

        
        self.directions = [
            (-1,0),(1,0),(0,-1),(0,1),   
            (-1,-1),(-1,1),(1,-1),(1,1) 
        ]

        # Cost of diagonal movement calculated using Pythagoras theorem
        self.cost = math.sqrt(2)

    def is_valid(self, x, y):
        """Check if the cell is inside the grid and not an obstacle."""

    
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] == 1


    def ucs(self):
        """Uniform Cost Search to find the shortest path."""

       
        priority_queue = [(0, self.start)]

        visited = set()  # Keep track of visited nodes

        
        parent = {self.start: None}

        
        while priority_queue:

            
            cost, (x, y) = heapq.heappop(priority_queue)

           
            if (x, y) in visited:
                continue

           
            visited.add((x, y))

            # If goal is reached, reconstruct and return the path
            if (x, y) == self.goal:
                return self.reconstruct_path(parent)

            # Explore all possible movement directions
            for dx, dy in self.directions:

                # Calculate new position
                new_x, new_y = x + dx, y + dy

                # Check if new position is valid and not visited
                if self.is_valid(new_x, new_y) and (new_x, new_y) not in visited:

                    # Add the new position to the priority queue with updated cost
                    heapq.heappush(priority_queue, (cost + self.cost, (new_x, new_y)))

                    # Store parent to track the path later
                    parent[(new_x, new_y)] = (x, y)

        # If no path is found
        return None


    def reconstruct_path(self, parent):
        """Reconstruct the path from goal to start."""

        path = []  # List to store the final path

        node = self.goal  # Start from the goal node

        # Follow the parent nodes until reaching the start node
        while node:
            path.append(node)
            node = parent[node]

        # Reverse the path so it goes from start → goal
        return path[::-1]


grid = [
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1]
]

start = (0, 0)  
goal = (4, 4)  

drone = DronePathPlanner(grid, start, goal)


shortest_path = drone.ucs()

if shortest_path:
    print("Shortest Path:", shortest_path)
else:
    print("No valid path found!")










import sys
import time
from ortools.sat.python import cp_model

model = cp_model.CpModel()

board_size = 8
queens = [model.new_int_var(0, board_size - 1, f"x_{i}") for i in range(board_size)]

# All rows must be different.
model.add_all_different(queens)

# No two queens can be on the same diagonal.
model.add_all_different(queens[i] + i for i in range(board_size))
model.add_all_different(queens[i] - i for i in range(board_size))

diag1 = []


for i in range(board_size):

    q1 = model.NewIntVar(0, 2 * board_size, 'diag1_%i' % i)

    diag1.append(q1)

   
    model.Add(q1 == queens[i] + i)

model.AddAllDifferent(diag1)



import time
from ortools.sat.python import cp_model


class NQueenSolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate N-Queens solutions with a visual board and timing info."""


    def __init__(self, queens: list[cp_model.IntVar]):
       
        cp_model.CpSolverSolutionCallback.__init__(self)

        self.__queens = queens

      
        self.__solution_count = 0

        self.__start_time = time.time()

    @property
    def solution_count(self) -> int:
       
        return self.__solution_count

    def on_solution_callback(self):
    
        current_time = time.time()

        
        print(
            f"Solution {self.__solution_count}, "
            f"time = {current_time - self.__start_time:.2f} s"
        )

        
        self.__solution_count += 1

        
        all_queens = range(len(self.__queens))

       
        for i in all_queens:  
            for j in all_queens:  

                if self.value(self.__queens[j]) == i:
                    print("Q", end=" ")  
                else:
                    print("_", end=" ")  
            print()
        print()  

solver = cp_model.CpSolver()
solution_printer = NQueenSolutionPrinter(queens)
solver.parameters.enumerate_all_solutions = True
solver.solve(model, solution_printer)



print("optimal",cp_model.OPTIMAL)
print("Feasible",cp_model.FEASIBLE)
print("InFeasible",cp_model.INFEASIBLE)
print("UNKNOWN",cp_model.UNKNOWN)








from ortools.sat.python import cp_model

# ---------------- Create model ----------------
model = cp_model.CpModel()

# ---------------- Integer Variables ----------------
x = model.NewIntVar(0, 10, 'x')
y = model.NewIntVar(-5, 5, 'y')

# ---------------- Boolean Variables ----------------
b1 = model.NewBoolVar('b1')
b2 = model.NewBoolVar('b2')

# Example constraint: x + y = 5
model.Add(x + y == 5)


start = model.NewIntVar(0, 10, 'start')
duration = 5 
interval = model.NewFixedSizeIntervalVar(start, duration, 'interval_task')


optional_interval = model.NewOptionalFixedSizeIntervalVar(start, duration, b1, 'optional_task')

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("Integer Variables:")
    print("x =", solver.Value(x))
    print("y =", solver.Value(y))

    print("\nBoolean Variables:")
    print("b1 =", solver.Value(b1))
    print("b2 =", solver.Value(b2))

    print("\nInterval Variable:")
    print("Start =", solver.Value(start))
    print("Duration =", duration)
    print("End =", solver.Value(start) + duration)  # End time

    print("\nOptional Interval Variable:")
    # Only print if b1 is 1
    if solver.Value(b1) == 1:
        print("Optional task is active")
        print("Start =", solver.Value(start))
        print("Duration =", duration)
        print("End =", solver.Value(start) + duration)
    else:
        print("Optional task is inactive (b1=0)")
else:
    print("No solution found!")

from ortools.sat.python import cp_model

# Create model
model = cp_model.CpModel()

# Define variables
x = model.NewIntVar(0, 10, "x")
y = model.NewIntVar(0, 10, "y")
z = model.NewIntVar(0, 10, "z")

# Applying constraints
model.Add(x + y <= 10)
model.AddAllDifferent([x, y, z])

# Allowed combinations for x,y
model.AddAllowedAssignments([x, y], [(1, 2), (3, 4)])

# Forbidden combinations
model.AddForbiddenAssignments([x, y], [(1, 1), (2, 2)])

# Min and Max targets (separate variables)
min_target = model.NewIntVar(0, 10, "min_target")
max_target = model.NewIntVar(0, 10, "max_target")

model.AddMinEquality(min_target, [x, y, z])
model.AddMaxEquality(max_target, [x, y, z])

# Division constraint
num = model.NewIntVar(1, 10, "num")
denom = model.NewIntVar(1, 5, "denom")
div_target = model.NewIntVar(0, 10, "div_target")
model.AddDivisionEquality(div_target, num, denom)

# Multiplication constraint
factors = [model.NewIntVar(1, 5, f"f{i}") for i in range(2)]
prod_target = model.NewIntVar(1, 25, "prod_target")
model.AddMultiplicationEquality(prod_target, factors)

# Solver
solver = cp_model.CpSolver()
status = solver.Solve(model)

# Output results if feasible
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:

    print("Solution Found\n")

    print("x =", solver.Value(x))
    print("y =", solver.Value(y))
    print("z =", solver.Value(z))

    print("\nMinimum value =", solver.Value(min_target))
    print("Maximum value =", solver.Value(max_target))

    print("\nDivision result =", solver.Value(div_target))
    print("Numerator =", solver.Value(num))
    print("Denominator =", solver.Value(denom))

    print("\nProduct result =", solver.Value(prod_target))
    print("Factors =", [solver.Value(f) for f in factors])

else:
    print("No feasible solution found.")














