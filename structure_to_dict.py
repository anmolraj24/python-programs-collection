"""
Structure to Dictionary Conversion Module
Provides universal conversion utilities to convert custom structures,
dataclasses, namedtuples, and nested objects into clean Python dictionaries.
"""

from dataclasses import dataclass, asdict, is_dataclass
from typing import Any, Dict, List, NamedTuple, Set
from datetime import datetime, date
from enum import Enum


def to_dict(obj: Any) -> Any:
    """
    Recursively converts arbitrary Python data structures to dictionaries/primitives:
    - dataclasses -> dict
    - NamedTuples -> dict
    - custom classes with __dict__ -> dict
    - iterables (list, set, tuple) -> list
    - dict -> recursively converted dict
    - Enums -> string/value
    - dates/datetimes -> ISO 8601 strings
    - primitive types -> preserved as is
    """
    if obj is None:
        return None

    # Dataclasses
    if is_dataclass(obj) and not isinstance(obj, type):
        return {key: to_dict(val) for key, val in asdict(obj).items()}

    # NamedTuples
    if isinstance(obj, tuple) and hasattr(obj, "_asdict"):
        return {key: to_dict(val) for key, val in obj._asdict().items()}

    # Enums
    if isinstance(obj, Enum):
        return obj.value

    # Dates and Datetimes
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()

    # Dictionaries
    if isinstance(obj, dict):
        return {str(key): to_dict(val) for key, val in obj.items()}

    # Lists, Sets, Tuples
    if isinstance(obj, (list, tuple, set)):
        return [to_dict(item) for item in obj]

    # Custom Class with __dict__
    if hasattr(obj, "__dict__"):
        result = {}
        for key, val in vars(obj).items():
            if not key.startswith("_"): # Exclude private attributes
                result[key] = to_dict(val)
        return result

    # Primitives (int, float, str, bool)
    return obj


# --- Demonstration Data Models ---

class SkillLevel(Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"


@dataclass
class Project:
    name: str
    tech_stack: List[str]
    is_active: bool


class StudentRecord:
    def __init__(self, student_id: str, name: str, skills: List[str], level: SkillLevel):
        self.student_id = student_id
        self.name = name
        self.skills = skills
        self.level = level
        self.enrolled_on = datetime(2024, 8, 1, 10, 0, 0)
        self.projects: List[Project] = []

    def add_project(self, project: Project):
        self.projects.append(project)


class Coordinate(NamedTuple):
    x: float
    y: float
    label: str


if __name__ == "__main__":
    print("=== Structure to Dictionary Conversion Demo ===")
    
    # Create a complex student record
    student = StudentRecord(
        student_id="CSE-2024-042",
        name="Neev Rupareliya",
        skills=["Python", "Web Development", "Algorithms"],
        level=SkillLevel.ADVANCED
    )
    student.add_project(Project(name="Portfolio Website", tech_stack=["HTML", "CSS", "JS"], is_active=True))
    student.add_project(Project(name="Quiz App", tech_stack=["JavaScript"], is_active=False))

    coord = Coordinate(26.9124, 75.7873, "Jaipur")

    data_payload = {
        "metadata": {
            "version": "1.0.0",
            "location": coord
        },
        "student": student,
        "tags": {"btech", "cse", "2026"}
    }

    # Convert to pure dictionary
    clean_dict = to_dict(data_payload)
    
    import json
    print("\nSerialized JSON Output:")
    print(json.dumps(clean_dict, indent=2))
