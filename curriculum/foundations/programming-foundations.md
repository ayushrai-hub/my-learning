[← Back to Curriculum](../README.md)

---

# Programming Foundations (Python)

- **Syntax & Flow Control**

  - Variables, naming conventions, PEP 8 style guide
  - Data types: int, float, str, bool, None, type hints
  - Control structures: if/elif/else, for/while loops, break/continue
  - Exception handling: try/except/else/finally, custom exceptions
  - Context managers: with statements, **enter**/**exit**
  - Comprehensions: list, dict, set comprehensions, generator expressions

- **Core Standard Library**

  - `pathlib`: Path objects, file operations, cross-platform paths
  - `collections`: defaultdict, Counter, deque, namedtuple, ChainMap
  - `itertools`: chain, cycle, repeat, combinations, permutations, groupby
  - `datetime`: datetime objects, timezones, parsing, formatting, timedelta
  - `subprocess`: Popen, run, shell=False security, pipes, timeouts
  - `json`: encoding/decoding, custom serializers, JSONEncoder/JSONDecoder
  - `re`: regex patterns, compile, match vs search, groups, flags
  - `os` vs `pathlib`: environment variables, process management

- **Static Typing & Type Safety**

  - `typing` module: List, Dict, Optional, Union, Callable, TypeVar
  - Generic types, bounded TypeVars, covariance/contravariance
  - Protocol classes for structural subtyping
  - `mypy` configuration, incremental checking, stub files
  - Type narrowing, isinstance checks, cast() function
  - Literal types, Final, ClassVar annotations

- **Environment & Dependency Management**

  - Virtual environments: venv, virtualenv, conda environments
  - Poetry: pyproject.toml, lock files, dependency groups, scripts
  - Pipx: isolated CLI tool installation, upgrade management
  - Dependency pinning strategies: exact, compatible, semantic versioning
  - Requirements files: requirements.txt, dev-requirements.txt, constraints.txt
  - Environment variables, .env files, python-dotenv

- **Testing Fundamentals**

  - `pytest` basics: test discovery, naming conventions, assert statements
  - Fixtures: scope (function, class, module, session), autouse, parametrize
  - Mocking: unittest.mock, patch decorators, MagicMock, side_effects
  - Test organization: conftest.py, test classes, markers
  - Coverage analysis: pytest-cov, branch coverage, coverage reports
  - Property-based testing introduction with Hypothesis

- **Logging & Debugging**

  - Structured logging: loguru, structlog, JSON formatting
  - Log levels, handlers, formatters, filters
  - Print debugging vs proper logging practices
  - Debugging tools: pdb, ipdb, IDE debuggers, breakpoints
  - Profiling basics: cProfile, line_profiler, memory_profiler
  - Error tracking: Sentry integration, exception context

- **CLI Development & Packaging**
  - `argparse`: parsers, subcommands, argument types, help text
  - `typer`: type hints for CLI, rich output, progress bars
  - Click framework: decorators, commands, groups, options
  - Entry points, console_scripts in setup.py/pyproject.toml
  - Distribution: wheel building, PyPI publishing, twine
  - CLI best practices: exit codes, stdin/stdout/stderr, signals
