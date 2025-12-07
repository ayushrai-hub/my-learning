# 🔍 Programming Fundamentals

## Executive Summary
Programming fundamentals form the bedrock of all software development. This curriculum focuses on core programming concepts using Python 3.12, emphasizing problem-solving, algorithmic thinking, and production-quality code practices. Students will master fundamental concepts applicable to any programming language while building expertise in modern Python development.

## Core Concepts
Understanding programming fundamentals requires grasping:
- **Variables and Data Types**: Numbers, strings, booleans, collections (lists, dicts, sets)
- **Control Flow**: Conditional statements, loops, error handling
- **Functions**: Definition, parameters, return values, scope
- **Data Structures**: Arrays, lists, objects, and their operations
- **Algorithms**: Basic searching, sorting, and problem-solving patterns
- **Modularity**: Code organization, reusable components
- **Input/Output**: Reading/writing files, user interaction

### Why This Matters (2024 Perspective)
In 2024-2025, fundamentals remain crucial:
- 40% of coding interview failures stem from weak fundamentals (per LinkedIn data)
- Python usage grew 30% in enterprise systems (2024 Stack Overflow survey)
- Type hinting adoption reached 85% in professional Python codebases

## Prerequisites
- Basic computer literacy
- No prior programming experience required
- Text editor or IDE (VS Code recommended)
- Willingness to think logically and solve problems

## Learning Objectives
- [ ] Explain core programming concepts clearly and accurately
- [ ] Write clean, readable Python code following PEP 8 standards
- [ ] Solve algorithmic problems with optimal time/space complexity
- [ ] Debug programs systematically using print statements and debugging tools
- [ ] Apply best practices: type hints, docstrings, error handling

## Key Technologies & Tools
| Technology | Version (2024) | Purpose |
|------------|----------------|---------|
| Python    | 3.12          | Core language with pattern matching, improved error messages |
| pytest    | 8.0           | Testing framework with advanced parametrization |
| mypy      | 1.8           | Static type checker for Python |
| black     | 24.1          | Code formatter (PEP 8 compliant) |
| flake8    | 7.0           | Linter for code quality |

## Hands-On Example
Let's build a simple task management system demonstrating key concepts:

```python
# task_manager.py
from typing import List, Dict, Optional
from datetime import datetime
import json

class TaskManager:
    """A simple task management system demonstrating programming fundamentals."""

    def __init__(self):
        self.tasks: List[Dict] = []
        self.next_id = 1

    def add_task(self, title: str, description: str = "", priority: str = "medium") -> int:
        """
        Add a new task to the manager.

        Args:
            title: Task title (required)
            description: Optional description
            priority: Priority level (low, medium, high)

        Returns:
            Task ID for reference

        Raises:
            ValueError: If title is empty or priority invalid
        """
        if not title.strip():
            raise ValueError("Task title cannot be empty")

        if priority not in ["low", "medium", "high"]:
            raise ValueError("Priority must be 'low', 'medium', or 'high'")

        task = {
            "id": self.next_id,
            "title": title,
            "description": description,
            "priority": priority,
            "completed": False,
            "created_at": datetime.now().isoformat()
        }

        self.tasks.append(task)
        self.next_id += 1
        return task["id"]

    def complete_task(self, task_id: int) -> bool:
        """Mark a task as completed. Returns True if found, False otherwise."""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return True
        return False

    def get_tasks(self, completed: Optional[bool] = None) -> List[Dict]:
        """Get tasks filtered by completion status."""
        if completed is None:
            return self.tasks.copy()

        return [task for task in self.tasks if task["completed"] == completed]

    def get_high_priority_tasks(self) -> List[Dict]:
        """Demonstrates list comprehension and filtering."""
        return [task for task in self.tasks if task["priority"] == "high" and not task["completed"]]

    def save_to_file(self, filename: str) -> None:
        """Save current tasks to JSON file."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump({"tasks": self.tasks, "next_id": self.next_id}, f, indent=2)
        except IOError as e:
            print(f"Error saving tasks: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load tasks from JSON file."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.tasks = data.get("tasks", [])
                self.next_id = data.get("next_id", 1)
        except FileNotFoundError:
            print(f"File {filename} not found, starting with empty task list")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading tasks: {e}")

# Demonstrate usage
def main():
    """Main function demonstrating the TaskManager."""
    manager = TaskManager()

    # Add some tasks
    task1 = manager.add_task("Learn Python fundamentals", "Complete basic programming concepts", "high")
    task2 = manager.add_task("Practice algorithms", "Solve coding problems daily", "medium")
    task3 = manager.add_task("Build portfolio project", "Create something impressive", "high")

    # Complete a task
    manager.complete_task(task1)

    # Show high priority tasks
    high_priority = manager.get_high_priority_tasks()
    print(f"High priority tasks: {len(high_priority)}")

    # Save and load demonstration
    manager.save_to_file("tasks.json")
    new_manager = TaskManager()
    new_manager.load_from_file("tasks.json")
    print(f"Loaded {len(new_manager.tasks)} tasks from file")

if __name__ == "__main__":
    main()
```

This example demonstrates:
- **Classes and objects** for encapsulation
- **Type hints** for better code quality
- **Error handling** with try/except
- **File I/O** for persistence
- **List comprehensions** for concise filtering
- **Docstrings** for documentation

## Common Pitfalls

### 1. Mutable Default Arguments
```python
# ❌ WRONG: Mutable default argument
def add_item(item, items=[]):
    items.append(item)
    return items

result1 = add_item("a")  # ['a']
result2 = add_item("b")  # ['a', 'b'] - shared list!

# ✅ CORRECT: None as default
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### 2. Variable Scope Confusion
```python
# ❌ WRONG: UnboundLocalError
def increment_counter():
    counter += 1  # 'counter' used before assignment

# ✅ CORRECT: Declare global or use nonlocal
counter = 0
def increment_counter():
    global counter
    counter += 1
```

### 3. String Concatenation in Loops
```python
# ❌ INEFFICIENT: O(n²) complexity
result = ""
for item in large_list:
    result += item  # Creates new string each time

# ✅ EFFICIENT: Use join or list comprehension
result = "".join(item for item in large_list)
```

## Best Practices (2024 Standards)

### Code Quality
- **Use type hints**: `mypy` catches 60%+ of bugs at development time
- **Write docstrings**: Every function deserves documentation
- **Follow PEP 8**: Use `black` formatter consistently
- **Write tests first**: `testing` mindset prevents bugs

### Performance
- **Use built-in functions**: `sum()`, `len()`, `max()` are optimized C code
- **Prefer list comprehensions**: More readable and often faster than loops
- **Profile before optimizing**: Premature optimization is the root of all evil

### Error Handling
- **Handle specific exceptions**: Catch `ValueError`, not `Exception`
- **Use context managers**: `with open()` for file handling
- **Log errors**: Use `logging` module instead of print statements

## Advanced Topics

### Pattern Matching (Python 3.10+)
```python
def process_data(data):
    match data:
        case {"type": "user", "name": name, **rest}:
            return f"Processing user {name}"
        case ["item", *items]:
            return f"Processing {len(items)} items"
        case value if isinstance(value, str):
            return f"String: {value}"
        case _:
            return "Unknown data type"
```

### Decorators for Cross-Cutting Concerns
```python
import time
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.2f}s")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "Done"
```

### Generators for Memory Efficiency
```python
def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a  # Suspends function, returns value
        a, b = b, a + b
        count += 1

# Use memory-efficient iteration
for num in fibonacci_generator(1000000):  # Uses ~constant memory
    print(num)
```

## Core Standard Library

### pathlib
- Path objects for cross-platform file system operations
- File operations: reading, writing, moving, deleting files
- Directory operations: creating, listing, traversing directories
- Path manipulation: joining, resolving, relative/absolute paths

### collections
- defaultdict: Dictionary with default factory for missing keys
- Counter: Counting hashable objects, most_common operations
- deque: Double-ended queue for efficient appends/pops from both ends
- namedtuple: Factory for creating tuple subclasses with named fields
- ChainMap: Single view of multiple mappings

### itertools
- chain: Concatenate multiple iterables
- cycle: Infinite iterator cycling through elements
- repeat: Infinite iterator repeating an element
- combinations/permutations: Generate combinations/permutations of elements
- groupby: Group consecutive elements by key function

### datetime
- datetime objects with date and time components
- Timezone-aware datetime handling
- Parsing and formatting dates/times
- timedelta for date/time arithmetic and differences

### subprocess
- Popen for running external commands
- run() function for simple command execution
- Security considerations: shell=False parameter
- Pipes for stdin/stdout/stderr redirection
- Timeout handling for long-running processes

### json
- Encoding/decoding JSON data
- Custom serializers for complex objects
- JSONEncoder/JSONDecoder classes for advanced customization
- Handling of special data types (datetime, custom classes)

### re (Regular Expressions)
- Regex pattern compilation and matching
- match vs search operations
- Groups and capturing subgroups
- Regex flags for case-insensitive, multiline matching

### os vs pathlib
- Environment variables access and management
- Process management and system information
- File system operations (legacy vs modern approaches)

## Static Typing & Type Safety

### typing Module
- List, Dict, Optional, Union for basic type annotations
- Callable for function type hints
- TypeVar for generic type variables
- Generic types with type parameters

### Advanced Typing Concepts
- Bounded TypeVars with constraints
- Covariance and contravariance in generics
- Protocol classes for structural subtyping (duck typing)
- Literal types for exact value constraints

### mypy Integration
- Configuration options and setup
- Incremental type checking
- Stub files (.pyi) for third-party libraries
- Type narrowing techniques
- isinstance checks and cast() function
- Final and ClassVar annotations for class-level typing

## Environment & Dependency Management

### Virtual Environments
- venv module for isolated Python environments
- virtualenv for enhanced virtual environment management
- conda environments for data science workflows
- Activation and deactivation procedures

### Poetry
- pyproject.toml configuration file
- Lock files for reproducible builds
- Dependency groups for development vs production
- Script definitions and entry points

### Pipx
- Isolated installation of CLI tools
- Upgrade management for installed tools
- Global tool availability without environment conflicts

### Dependency Management
- Version pinning strategies (exact, compatible, semantic)
- Requirements files: requirements.txt, dev-requirements.txt
- Constraints files for security updates
- Environment variables and .env files
- python-dotenv for environment file loading

## Testing Fundamentals

### pytest Basics
- Test discovery and naming conventions
- Assert statements and test outcomes
- Test organization and structure

### Fixtures
- Function, class, module, and session scope fixtures
- Autouse fixtures for automatic setup/teardown
- Parametrize decorator for data-driven tests

### Mocking
- unittest.mock module usage
- patch decorators for function/class mocking
- MagicMock and side_effects for complex behavior
- Context managers for temporary patches

### Test Organization
- conftest.py for shared fixtures and configuration
- Test classes and methods
- Markers for test categorization and filtering

### Coverage Analysis
- pytest-cov integration
- Branch coverage measurement
- Coverage reports and thresholds

### Advanced Testing
- Property-based testing with Hypothesis
- Introduction to test-driven development principles

## Logging & Debugging

### Structured Logging
- loguru library for enhanced logging
- structlog for structured JSON logging
- Log formatting and serialization

### Log Management
- Log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Handlers, formatters, and filters
- Log rotation and file handling

### Debugging Practices
- Print debugging vs proper logging approaches
- Debugging tools: pdb, ipdb, IDE debuggers
- Breakpoints and step-through debugging

### Profiling
- cProfile for performance profiling
- line_profiler for line-by-line analysis
- memory_profiler for memory usage tracking

### Error Tracking
- Sentry integration for production error monitoring
- Exception context and stack traces
- Error aggregation and alerting

## CLI Development & Packaging

### argparse
- Argument parsers and subcommands
- Argument types and validation
- Help text generation and formatting

### typer
- Type hints for CLI argument parsing
- Rich output and progress bars
- Automatic help generation

### Click Framework
- Decorator-based command definition
- Command groups and nesting
- Options and arguments handling

### Packaging
- Entry points and console_scripts
- setup.py and pyproject.toml configurations
- Wheel building and distribution
- PyPI publishing with twine

### CLI Best Practices
- Exit codes and error handling
- stdin/stdout/stderr usage
- Signal handling for graceful shutdowns

## Related Concepts

### Prerequisites
- [Computer Science Basics](../00-prerequisites/computer-science-basics.md)
- [Setup Development Environment](../00-prerequisites/dev-setup.md)

### Next Level Topics
- [Data Structures & Algorithms](../01-advanced/data-structures-algorithms.md)
- [Software Design Patterns](../03-architectures/design-patterns.md)
- [Test-Driven Development](../02-testing/tdd-fundamentals.md)

### Complementary Skills
- [Version Control](../backend-systems/version-control.md)
- [Debugging Techniques](../production-debugging/debugging-fundamentals.md)

## Resources

### Books
- **Python Crash Course (3rd Edition, 2024)** by Eric Matthes
  \$39.99, 550 pages, No Starch Press - Perfect for absolute beginners with practical projects
- **Automate the Boring Stuff with Python (2nd Edition)** by Al Sweigart
  \$29.99, 592 pages, No Starch Press - Learn by building useful automation scripts
- **Python for Everybody** by Charles Severance (free)
  Online book with video lectures - Comprehensive Python fundamentals

### Courses
- **Python Programming Specialization** - University of Michigan (Coursera)
  Coursera, ~6 months, \$49/month - Professional certificate with peer grading
- **Complete Python Bootcamp 2024** - Jose Portilla (Udemy)
  Udemy, 22 hours, \$12.99 sale - From zero to hero with real projects
- **Python Fundamentals (2024)** - Microsoft Learn (free)
  MS Learn, 8 hours, Free - Structured learning path with hands-on labs

### Documentation
- **Python 3.12 Official Documentation** - python.org
  Free, comprehensive, up-to-date - Primary reference for language features
- **Real Python Tutorials** - realpython.com
  Paid (\$29/month), high-quality articles - In-depth explanations with examples
- **Python Enhancement Proposals** - peps.python.org
  Free, developer discussions - Understand language evolution

### Interactive Platforms
- **Codecademy Python** - codecademy.com (free tier available)
- **LeetCode Python Problems** - leetcode.com/problemset/all/
- **HackerRank Python** - hackerrank.com/domains/tutorials/python

## Assessment Criteria

### Foundational Understanding
- ✅ Can explain variables, data types, and scope clearly
- ✅ Can trace through code with loops and conditionals manually
- ✅ Understands function parameters, return values, and side effects
- ✅ Can identify and fix common syntax errors (indentation, missing colons)
- ✅ Applies proper naming conventions consistently

### Problem Solving
- ✅ Breaks down problems into smaller, manageable components
- ✅ Selects appropriate data structures for given requirements
- ✅ Writes algorithms with correct logic and edge case handling
- ✅ Optimizes solutions for time and space complexity (basic analysis)

### Code Quality
- ✅ Writes PEP 8 compliant code (auto-formatted with black)
- ✅ Uses type hints for all function parameters and return values
- ✅ Includes docstrings for all classes, functions, and methods
- ✅ Implements proper error handling with specific exception types
- ✅ Organizes code logically with meaningful variable/function names

### Practical Application
- ✅ Can build simple command-line applications (todo list, calculator)
- ✅ Implements file I/O for data persistence (JSON, CSV)
- ✅ Creates modular code with proper separation of concerns
- ✅ Tests code manually with various inputs and edge cases
- ✅ Can read and understand code written by others

### Debugging & Troubleshooting
- ✅ Uses print statements strategically for debugging
- ✅ Can interpret error messages to identify root causes
- ✅ Handles edge cases and unexpected input gracefully
- ✅ Validates assumptions with systematic testing

### Career Readiness Indicators
- **Junior Developer**: Passes algorithmic coding interviews (LeetCode easy/medium)
- **Portfolio Ready**: Can build and explain 3-5 functional projects
- **Interview Prepared**: Confident discussing space/time complexity tradeoffs
- **Foundation Solid**: Ready to learn frameworks without getting overwhelmed
