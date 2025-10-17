#!/usr/bin/env python3
"""
Project Euler CLI
Usage: ./euler.py <problem_number>
"""

import sys
import importlib
import time
from pathlib import Path


def solve_problem(problem_num: int):
    """Load and solve a specific Project Euler problem."""
    try:
        # Import the solution module
        module_name = f"solutions.problem_{problem_num:03d}"
        module = importlib.import_module(module_name)

        # Get the solve function
        if not hasattr(module, 'solve'):
            print(f"Error: Problem {problem_num} doesn't have a solve() function")
            return False

        print(f"Solving Project Euler Problem {problem_num}...")

        # Time the solution
        start_time = time.time()
        result = module.solve()
        end_time = time.time()

        print(f"Answer: {result}")
        print(f"Time: {end_time - start_time:.6f} seconds")
        return True

    except ModuleNotFoundError:
        print(f"Error: Solution for problem {problem_num} not found")
        print(f"Create: solutions/problem_{problem_num:03d}.py")
        return False
    except Exception as e:
        print(f"Error running problem {problem_num}: {e}")
        return False


def create_new_solution(problem_num: int):
    """Create a new solution template."""
    solutions_dir = Path("solutions")
    solutions_dir.mkdir(exist_ok=True)

    file_path = solutions_dir / f"problem_{problem_num:03d}.py"

    if file_path.exists():
        print(f"Error: Solution for problem {problem_num} already exists")
        return False

    template = f'''"""
Project Euler Problem {problem_num}: [Problem Title]

[Problem description]
"""


def solve():
    """Solve Project Euler Problem {problem_num}."""
    # TODO: Implement solution
    return 0
'''

    file_path.write_text(template)
    print(f"Created: {file_path}")
    print(f"Edit the file and implement your solution in the solve() function")
    return True


def list_solved_problems():
    """List all solved problems."""
    solutions_dir = Path("solutions")
    if not solutions_dir.exists():
        print("No solutions directory found")
        return

    solved = []
    for file in solutions_dir.glob("problem_*.py"):
        if file.name != "__init__.py":
            try:
                num = int(file.stem.split("_")[1])
                solved.append(num)
            except (ValueError, IndexError):
                continue

    if solved:
        solved.sort()
        print("Solved problems:")
        for i, num in enumerate(solved, 1):
            print(f"{num:3d}", end="")
            if i % 10 == 0:
                print()
            else:
                print("  ", end="")
        if len(solved) % 10 != 0:
            print()
        print(f"\nTotal: {len(solved)} problems solved")
    else:
        print("No problems solved yet")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  ./euler.py <problem_number>  - Solve a specific problem")
        print("  ./euler.py new <number>     - Create new solution template")
        print("  ./euler.py list             - List all solved problems")
        sys.exit(1)

    arg = sys.argv[1]

    if arg == "list":
        list_solved_problems()
        return

    if arg.startswith("new"):
        if len(sys.argv) != 3:
            print("Usage: ./euler.py new <problem_number>")
            sys.exit(1)
        try:
            problem_num = int(sys.argv[2])
            if problem_num < 1:
                print("Error: Problem number must be positive")
                sys.exit(1)
            create_new_solution(problem_num)
        except ValueError:
            print("Error: Please provide a valid problem number")
            sys.exit(1)
        return

    try:
        problem_num = int(arg)
        if problem_num < 1:
            print("Error: Problem number must be positive")
            sys.exit(1)
        solve_problem(problem_num)
    except ValueError:
        print("Error: Please provide a valid problem number, 'new', or 'list'")
        sys.exit(1)


if __name__ == "__main__":
    main()