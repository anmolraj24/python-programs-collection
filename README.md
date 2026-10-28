# Python Programs Collection

A comprehensive, production-grade collection of core Python programs covering **factorial calculation**, **Fibonacci sequence algorithms**, and **structure-to-dictionary conversion**.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 📌 Project Overview

This repository demonstrates fundamental algorithmic thinking, recursion, caching strategies, and data serialization patterns in Python. It is designed for students, interview preparation, and clean code references.

### Key Highlights
- **Factorial Calculation**: Iterative, recursive, and LRU-memoized approaches with algorithmic performance benchmarking.
- **Fibonacci Sequence**: Iterative series generator, $O(2^n)$ naive recursion, dynamic programming with caching, and $O(\log n)$ Matrix Exponentiation for computing massive Fibonacci numbers.
- **Structure-to-Dictionary Conversion**: Universal recursive serializer supporting Python Dataclasses, NamedTuples, custom classes (`__dict__`), enums, and nested structures.
- **Automated Test Suite**: Full test coverage using Python's standard `unittest` framework.

---

## 📂 Directory Structure

```text
python-programs-collection/
├── factorial.py          # Factorial implementations & performance benchmarking
├── fibonacci.py          # Fibonacci generator, memoization, & matrix exponentiation
├── structure_to_dict.py  # Universal recursive object-to-dictionary converter
├── main.py               # Interactive CLI menu runner
├── requirements.txt      # Dependencies
├── .gitignore
├── tests/
│   └── test_programs.py  # Unit test suite
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Neev2850/python-programs-collection.git
cd python-programs-collection
```

### 2. Run Interactive CLI
```bash
python main.py
```

### 3. Run Individual Modules
```bash
# Factorial demo & benchmark
python factorial.py

# Fibonacci generator & O(log n) demonstration
python fibonacci.py

# Structure to dictionary serialization
python structure_to_dict.py
```

### 4. Run Unit Tests
```bash
python -m unittest discover -s tests
```

---

## 🧠 Algorithmic Details

### 1. Factorial
- **Iterative**: $O(n)$ time, $O(1)$ space. Prevents recursion stack overflow.
- **Memoized**: `@lru_cache` accelerates repeated queries.

### 2. Fibonacci Matrix Exponentiation
Using the matrix property:
$$\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n = \begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix}$$
Computes $F_{1000}$ and beyond in sub-millisecond execution times.

---

## 👤 Author
**Neev Rupareliya**  
- B.Tech CSE Student, JECRC University  
- GitHub: [@Neev2850](https://github.com/Neev2850)  
- Portfolio: [personal-portfolio-mu-eosin-58.vercel.app](https://personal-portfolio-mu-eosin-58.vercel.app)
