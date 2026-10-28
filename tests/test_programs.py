import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import unittest
from factorial import factorial_iterative, factorial_recursive, factorial_memoized
from fibonacci import fibonacci_iterative, fibonacci_series, fibonacci_matrix, fibonacci_memoized
from structure_to_dict import to_dict, StudentRecord, SkillLevel, Project, Coordinate


class TestFactorial(unittest.TestCase):
    def test_factorial_base_cases(self):
        self.assertEqual(factorial_iterative(0), 1)
        self.assertEqual(factorial_iterative(1), 1)
        self.assertEqual(factorial_recursive(0), 1)
        self.assertEqual(factorial_recursive(1), 1)
        self.assertEqual(factorial_memoized(0), 1)

    def test_factorial_standard_values(self):
        self.assertEqual(factorial_iterative(5), 120)
        self.assertEqual(factorial_recursive(5), 120)
        self.assertEqual(factorial_memoized(5), 120)
        self.assertEqual(factorial_iterative(10), 3628800)

    def test_factorial_errors(self):
        with self.assertRaises(ValueError):
            factorial_iterative(-5)
        with self.assertRaises(TypeError):
            factorial_iterative("5")  # type: ignore


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_sequence(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(fibonacci_series(10), expected)

    def test_fibonacci_nth_term(self):
        self.assertEqual(fibonacci_iterative(0), 0)
        self.assertEqual(fibonacci_iterative(1), 1)
        self.assertEqual(fibonacci_iterative(7), 13)
        self.assertEqual(fibonacci_matrix(7), 13)
        self.assertEqual(fibonacci_memoized(7), 13)

    def test_fibonacci_large_terms(self):
        # F(30) is 832040
        self.assertEqual(fibonacci_iterative(30), 832040)
        self.assertEqual(fibonacci_matrix(30), 832040)


class TestStructureToDict(unittest.TestCase):
    def test_primitives_and_lists(self):
        self.assertEqual(to_dict(42), 42)
        self.assertEqual(to_dict("hello"), "hello")
        self.assertEqual(to_dict([1, 2, 3]), [1, 2, 3])

    def test_nested_objects(self):
        student = StudentRecord("U1", "Anmol", ["Python"], SkillLevel.BEGINNER)
        student.add_project(Project("Web", ["HTML"], True))
        d = to_dict(student)
        
        self.assertIsInstance(d, dict)
        self.assertEqual(d["student_id"], "U1")
        self.assertEqual(d["name"], "Anmol")
        self.assertEqual(d["level"], "Beginner")
        self.assertEqual(d["projects"][0]["name"], "Web")
        self.assertTrue(d["projects"][0]["is_active"])

    def test_namedtuple(self):
        coord = Coordinate(12.5, 45.2, "PointA")
        d = to_dict(coord)
        self.assertEqual(d, {"x": 12.5, "y": 45.2, "label": "PointA"})


if __name__ == "__main__":
    unittest.main()
