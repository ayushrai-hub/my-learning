[← Back to Curriculum](../README.md)

---

# Intermediate Python & Tooling

- **Object-Oriented vs Functional Programming**

  - Class design: single responsibility, composition over inheritance
  - Magic methods: **str**, **repr**, **eq**, **hash**, **call**
  - Property decorators: @property, setter, deleter
  - Class methods vs static methods vs instance methods
  - Abstract base classes: ABC, abstractmethod, register
  - Functional programming: map, filter, reduce, partial, functools
  - Immutable data structures, pure functions, side effects
  - Method chaining, fluent interfaces

- **Advanced Iteration & Async Programming**

  - Iterator protocol: **iter**, **next**, StopIteration
  - Generator functions: yield, send, throw, close methods
  - Coroutines: async/await syntax, asyncio event loop
  - Async context managers: **aenter**, **aexit**
  - Async iterators: **aiter**, **anext**
  - asyncio patterns: gather, create_task, wait_for, timeout
  - Async libraries: aiohttp, aiofiles, asyncpg, motor

- **Type System & Protocols**

  - Context managers: contextlib, ExitStack, suppress
  - `typing.Protocol`: structural subtyping, runtime_checkable
  - Generic classes: TypeVar constraints, bound parameters
  - Overloads: @overload decorator, multiple signatures
  - NewType for domain modeling, type aliases
  - Literal types, TypedDict, NotRequired/Required (3.11+)
  - Type guards: TypeGuard, user-defined type guards

- **Concurrency & Parallelism**

  - Threading: Thread class, locks, RLock, Condition, Semaphore
  - GIL implications, CPU-bound vs I/O-bound tasks
  - Multiprocessing: Process, Pool, Queue, shared memory
  - `concurrent.futures`: ThreadPoolExecutor, ProcessPoolExecutor
  - Async vs threading vs multiprocessing trade-offs
  - Thread safety, race conditions, deadlocks
  - Queue patterns: producer-consumer, work queues

- **Performance Analysis & Optimization**

  - Profiling tools: cProfile, profile, pstats analysis
  - Line profiling: line_profiler, kernprof, @profile decorator
  - Memory profiling: memory_profiler, tracemalloc, objgraph
  - Performance monitoring: py-spy, Austin, profiling in production
  - Benchmarking: timeit, pytest-benchmark, statistical significance
  - Optimization strategies: algorithmic, data structure, caching

- **Package Management & Distribution**
  - Wheel format: binary distributions, platform tags, ABI tags
  - Semantic versioning: major.minor.patch, pre-releases, metadata
  - Setup.py vs pyproject.toml: PEP 517/518, build backends
  - Package metadata: author, license, classifiers, keywords
  - Dependency specification: version specifiers, extras_require
  - Publishing workflow: test PyPI, production PyPI, CI/CD integration
