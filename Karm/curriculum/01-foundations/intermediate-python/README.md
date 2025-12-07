# 🔍 Intermediate Python & Tooling

## Executive Summary
Intermediate Python builds upon fundamental concepts to explore advanced language features, performance optimization, and professional development practices. This module covers object-oriented design, asynchronous programming, type systems, concurrency patterns, and production-ready tooling essential for building scalable Python applications.

## Core Concepts
Advanced Python development requires mastery of:
- **Object-Oriented Design**: Class design, inheritance patterns, magic methods
- **Functional Programming**: Pure functions, immutability, higher-order functions
- **Asynchronous Programming**: Coroutines, event loops, async/await patterns
- **Type Systems**: Advanced typing, protocols, generic programming
- **Concurrency**: Threading, multiprocessing, parallel execution
- **Performance**: Profiling, optimization, benchmarking techniques
- **Packaging**: Distribution, dependency management, publishing workflows

### Why This Matters (2024 Perspective)
Intermediate Python skills are critical for modern development:
- 75% of Python jobs require intermediate/advanced knowledge (2024 Indeed data)
- Async programming adoption grew 200% in web frameworks (2024 trends)
- Type checking usage increased 150% in enterprise codebases
- Performance optimization skills command 20-30% salary premium

## Prerequisites
- Solid understanding of Python fundamentals (variables, functions, basic OOP)
- Experience with basic data structures and algorithms
- Familiarity with virtual environments and pip
- Basic understanding of command-line operations

## Learning Objectives
- [ ] Design clean, maintainable class hierarchies using OOP principles
- [ ] Implement asynchronous operations with asyncio and async libraries
- [ ] Apply advanced type annotations and protocol-based design
- [ ] Choose appropriate concurrency models for different problem types
- [ ] Profile and optimize Python code for performance bottlenecks
- [ ] Package and distribute Python applications professionally

## Key Technologies & Tools
| Technology | Version (2024) | Purpose |
|------------|----------------|---------|
| Python    | 3.12          | Advanced language features, pattern matching |
| asyncio   | 3.12 built-in | Asynchronous programming framework |
| mypy      | 1.8           | Advanced static type checking |
| cProfile  | Built-in       | Performance profiling and analysis |
| poetry    | 1.7           | Modern dependency and packaging management |

## Object-Oriented vs Functional Programming

### Class Design Principles
- Single responsibility principle in class design
- Composition over inheritance patterns
- Magic methods implementation (__str__, __repr__, __eq__, __hash__, __call__)
- Property decorators (@property, setter, deleter)
- Class methods vs static methods vs instance methods
- Abstract base classes (ABC, abstractmethod, register)

### Functional Programming Concepts
- Functional programming paradigms in Python
- Map, filter, reduce operations
- Partial function application with functools
- Immutable data structures design
- Pure functions and side effect management
- Method chaining and fluent interfaces

## Advanced Iteration & Async Programming

### Iterator Protocol
- Iterator protocol implementation (__iter__, __next__)
- StopIteration exception handling
- Generator functions and yield statements
- Generator methods (send, throw, close)

### Coroutines and Async Programming
- Async/await syntax and coroutines
- Asyncio event loop management
- Async context managers (__aenter__, __aexit__)
- Async iterators (__aiter__, __anext__)
- Asyncio patterns (gather, create_task, wait_for, timeout)
- Popular async libraries (aiohttp, aiofiles, asyncpg, motor)

## Type System & Protocols

### Advanced Typing Features
- Context managers with contextlib (ExitStack, suppress)
- typing.Protocol for structural subtyping
- Runtime checkable protocols
- Generic classes with TypeVar constraints
- Overload decorator for multiple function signatures
- NewType for domain-specific type modeling
- Type aliases for complex type definitions
- Literal types, TypedDict, NotRequired/Required (Python 3.11+)
- Type guards and user-defined type checking

## Concurrency & Parallelism

### Threading Concepts
- Thread class usage and lifecycle
- Synchronization primitives (locks, RLock, Condition, Semaphore)
- GIL implications and limitations
- CPU-bound vs I/O-bound task characteristics

### Multiprocessing
- Process class and multiprocessing patterns
- Pool for parallel execution
- Queue for inter-process communication
- Shared memory management

### Concurrent Futures
- ThreadPoolExecutor for thread-based parallelism
- ProcessPoolExecutor for process-based parallelism
- Trade-offs between async, threading, and multiprocessing
- Thread safety and race condition prevention
- Deadlock avoidance strategies
- Producer-consumer patterns and work queues

## Performance Analysis & Optimization

### Profiling Tools
- cProfile and profile module usage
- pstats for profile analysis
- Line profiling with line_profiler and kernprof
- @profile decorator for targeted profiling

### Memory Analysis
- Memory profiling with memory_profiler
- tracemalloc for memory allocation tracking
- objgraph for object reference analysis

### Performance Monitoring
- py-spy for sampling-based profiling
- Austin for frame-based profiling
- Production profiling considerations

### Benchmarking
- timeit module for micro-benchmarking
- pytest-benchmark for test suite benchmarking
- Statistical significance in performance measurements

### Optimization Strategies
- Algorithmic improvements for better complexity
- Data structure optimization
- Caching strategies and implementations

## Package Management & Distribution

### Wheel Format
- Binary distributions and platform-specific builds
- Platform tags and ABI compatibility
- Wheel vs source distributions

### Semantic Versioning
- Major.minor.patch version scheme
- Pre-release and development version handling
- Version metadata and compatibility

### Modern Packaging
- Setup.py vs pyproject.toml comparison
- PEP 517/518 build backends
- Package metadata specification (author, license, classifiers, keywords)
- Dependency specification and extras_require

### Publishing Workflow
- Test PyPI vs production PyPI
- Package validation and testing
- CI/CD integration for automated publishing
- Security considerations in package distribution

## Related Concepts

### Prerequisites
- [Programming Fundamentals](../programming-fundamentals/README.md)
- [Data Structures & Algorithms](../data-structures-algorithms/README.md)

### Next Level Topics
- [Backend Engineering](../../02-backend-engineering/api-design/README.md)
- [System Design](../../architecture-testing/system-design/README.md)
- [Performance Engineering](../../08-performance-engineering/README.md)

### Complementary Skills
- [Version Control](../version-control.md)
- [Testing Strategies](../../architecture-testing/testing-strategies/README.md)

## Resources

### Books
- **Fluent Python (2nd Edition, 2022)** by Luciano Ramalho
  \$59.99, 1,040 pages, O'Reilly - Advanced Python idioms and best practices
- **Effective Python (2nd Edition, 2019)** by Brett Slatkin
  \$49.99, 256 pages, Addison-Wesley - 90 specific ways to write better Python
- **Python Concurrency with asyncio** by Matthew Fowler
  \$39.99, 376 pages, Manning - Comprehensive async programming guide

### Courses
- **Advanced Python Programming** - University of Michigan (Coursera)
  Coursera, ~4 months, \$49/month - Deep dive into advanced Python features
- **Async Python Mastery** - Real Python (paid)
  Real Python, 8 hours, \$39/month - Comprehensive async programming course
- **Python Performance Optimization** - LinkedIn Learning
  LinkedIn, 2 hours, Subscription - Profiling and optimization techniques

### Documentation
- **Python Asyncio Documentation** - python.org
  Free, official documentation - Complete asyncio reference
- **Mypy Documentation** - mypy-lang.org
  Free, comprehensive - Advanced type checking guide
- **Python Packaging Guide** - packaging.python.org
  Free, official - Modern packaging best practices

### Tools
- **Poetry** - python-poetry.org
  Open source, modern dependency management
- **Black** - black.readthedocs.io
  Code formatter for consistent style
- **pytest-asyncio** - GitHub
  Async testing support for pytest

## Assessment Criteria

### Object-Oriented Design
- ✅ Designs classes with single responsibility and proper encapsulation
- ✅ Implements appropriate magic methods for object behavior
- ✅ Uses inheritance and composition effectively
- ✅ Applies design patterns correctly in Python context

### Asynchronous Programming
- ✅ Writes clean async/await code with proper error handling
- ✅ Uses asyncio patterns for concurrent operations
- ✅ Integrates async libraries appropriately
- ✅ Handles async context managers and iterators

### Type System Mastery
- ✅ Applies advanced type annotations correctly
- ✅ Uses protocols for structural typing
- ✅ Implements generic classes and functions
- ✅ Creates type-safe APIs with proper overloads

### Concurrency Understanding
- ✅ Chooses appropriate concurrency model for the problem
- ✅ Implements thread-safe code with proper synchronization
- ✅ Uses multiprocessing for CPU-intensive tasks
- ✅ Avoids common concurrency pitfalls (race conditions, deadlocks)

### Performance Optimization
- ✅ Profiles code to identify bottlenecks accurately
- ✅ Applies appropriate optimization techniques
- ✅ Benchmarks changes with statistical significance
- ✅ Balances performance with code readability

### Packaging Proficiency
- ✅ Creates properly structured Python packages
- ✅ Manages dependencies with modern tools
- ✅ Publishes packages to PyPI with correct metadata
- ✅ Implements CI/CD for automated package publishing

### Career Readiness Indicators
- **Mid-Level Developer**: Can design and implement complex Python systems
- **Performance Specialist**: Proficient in profiling and optimization techniques
- **Async Expert**: Builds scalable async applications and APIs
- **Package Author**: Publishes and maintains Python packages professionally
