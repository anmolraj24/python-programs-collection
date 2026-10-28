"""
Main CLI Application for Python Programs Collection
Interactive entry point to test and benchmark:
1. Factorial calculation
2. Fibonacci sequence
3. Structure-to-dictionary conversion
"""

import sys
from factorial import factorial_iterative, factorial_recursive, compare_factorial_performance
from fibonacci import fibonacci_iterative, fibonacci_series, fibonacci_matrix
from structure_to_dict import StudentRecord, SkillLevel, Project, to_dict
import json


def show_menu():
    print("\n" + "=" * 50)
    print("      PYTHON PROGRAMS COLLECTION - NEEV RUPARELIYA")
    print("=" * 50)
    print("1. Calculate Factorial (Iterative & Recursive)")
    print("2. Benchmark Factorial Algorithms")
    print("3. Generate Fibonacci Series / Nth Term")
    print("4. Compute Giant Fibonacci (Matrix Exponentiation)")
    print("5. Convert Complex Object Structure to Dictionary")
    print("6. Run All Unit Tests")
    print("0. Exit")
    print("=" * 50)


def run_cli():
    while True:
        show_menu()
        choice = input("Enter your choice (0-6): ").strip()

        if choice == "1":
            try:
                num = int(input("Enter non-negative integer: ").strip())
                ans = factorial_iterative(num)
                print(f"\nResult: {num}! = {ans}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            try:
                num = int(input("Enter number to benchmark (e.g., 300): ").strip())
                compare_factorial_performance(n=num)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            try:
                count = int(input("How many Fibonacci terms to display?: ").strip())
                series = fibonacci_series(count)
                print(f"\nFirst {count} terms: {series}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            try:
                n = int(input("Enter index n (e.g. 500, 1000): ").strip())
                ans = fibonacci_matrix(n)
                print(f"\nF({n}) = {ans}")
                print(f"Total digits: {len(str(ans))}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "5":
            record = StudentRecord("CSE-101", "Neev Rupareliya", ["Python", "DSA"], SkillLevel.ADVANCED)
            record.add_project(Project("Portfolio", ["HTML", "CSS", "JS"], True))
            result = to_dict(record)
            print("\nConverted Object -> Dictionary (JSON representation):")
            print(json.dumps(result, indent=2))

        elif choice == "6":
            import unittest
            suite = unittest.defaultTestLoader.discover("tests")
            runner = unittest.TextTestRunner(verbosity=2)
            runner.run(suite)

        elif choice == "0":
            print("Exiting. Have a great day!")
            break

        else:
            print("Invalid selection. Please choose an option between 0 and 6.")


if __name__ == "__main__":
    run_cli()
