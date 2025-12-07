# 🐚 Unix Shell & Build Tooling

## Executive Summary
Unix shell proficiency and build tooling mastery are essential for modern software development, enabling efficient workflow automation, system administration, and development environment management. This curriculum covers advanced shell scripting, text processing tools, build systems, and automation patterns used in professional development environments. Students will master command-line productivity, automation scripts, and build pipeline optimization for scalable development workflows.

## Core Concepts
Command-line mastery requires understanding:
- **Shell Scripting**: Bash scripting, error handling, portability, debugging
- **Text Processing**: grep, awk, sed, jq for data manipulation and analysis
- **Build Systems**: Make, CMake, Ninja, Bazel for compilation and artifact management
- **Task Automation**: Invoke, Nox, Tox, Just for workflow orchestration
- **Package Management**: System and language package managers, distribution
- **Development Environment**: Dotfiles, shell configuration, editor integration

### Why This Matters (2024 Perspective)
Shell and build tool expertise directly impacts developer productivity:
- 70% of development time involves command-line operations (surveys)
- Build tool optimization can reduce CI/CD times by 50-80%
- Shell scripting prevents 40% of manual deployment errors
- Modern development relies on 200+ CLI tools and automation scripts

## Prerequisites
- Basic command-line usage (cd, ls, mkdir, rm)
- Understanding of file systems and permissions
- Familiarity with text editors
- Basic programming concepts

## Learning Objectives
- [ ] Master advanced shell scripting with error handling and debugging
- [ ] Apply text processing tools for data manipulation and analysis
- [ ] Configure and optimize build systems for different project types
- [ ] Implement task automation for development workflows
- [ ] Manage packages and dependencies across different platforms
- [ ] Set up productive development environments with customization

## Key Technologies & Tools
| Technology | Version (2024) | Purpose |
|------------|----------------|---------|
| Bash       | 5.2           | Unix shell with advanced scripting features |
| Make       | 4.4           | Build automation and dependency management |
| CMake      | 3.28          | Cross-platform build system configuration |
| Ninja      | 1.11          | Fast build system with low overhead |
| ripgrep    | 14.0          | Fast text search with regex support |
| tmux       | 3.4           | Terminal multiplexer for session management |

## Advanced Bash & POSIX Scripting

### Shell Safety and Error Handling
- `set -euo pipefail`: Exit on errors, undefined variables, pipe failures
- Error handling patterns: trap commands, cleanup functions, rollback
- Exit codes: Standard codes, custom codes, error propagation
- Defensive scripting: Input validation, boundary checking, logging

### Variable Expansion and Arrays
- Parameter expansion: `${variable:-default}`, `${variable//search/replace}`
- Array operations: Indexed arrays, associative arrays, iteration
- String manipulation: Substring extraction, case conversion, trimming
- Command substitution: `$(command)` vs backticks, nesting considerations

### Quoting and Escaping
- Single vs double quotes: Variable expansion, command execution
- Escaping special characters: Backslash escaping, here documents
- Common pitfalls: Whitespace handling, globbing, word splitting
- Best practices: Consistent quoting, readability, maintenance

### Process Substitution and Redirection
- Process substitution: `<(command)`, `>(command)` for input/output
- Named pipes (FIFOs): `mkfifo`, inter-process communication
- File descriptors: Redirection, duplication, custom descriptors
- Advanced redirection: `tee`, `exec`, descriptor manipulation

### Signal Handling
- Signal types: SIGTERM, SIGINT, SIGHUP, custom signals
- Trap commands: Signal catching, cleanup execution, graceful shutdown
- Background processes: Job control, process groups, disowning
- Signal safety: Atomic operations, reentrancy considerations

### Debugging and Profiling
- `set -x`: Execution tracing, command expansion display
- `bash -x`: Script debugging, verbose execution
- shellcheck: Static analysis, common mistake detection
- Profiling: Execution timing, bottleneck identification, optimization

### Portability Considerations
- POSIX compliance: Standard commands, shell features
- Shell detection: bash vs zsh vs sh compatibility
- Cross-platform scripts: macOS, Linux, WSL differences
- Environment detection: OS version, available tools, fallbacks

## Text Processing & Data Manipulation

### Grep Family and Search Tools
- grep variants: Basic grep, egrep (extended), fgrep (fixed strings)
- ripgrep (rg): Performance optimization, gitignore respect, binary file skipping
- Regex patterns: Basic vs extended syntax, common patterns, performance
- Search options: Case sensitivity, line numbers, context, inversion

### Awk Programming
- Field processing: `$1`, `$2`, `NF`, `NR` variables
- Pattern-action paradigm: Conditions and actions
- Built-in functions: String manipulation, arithmetic, formatting
- Advanced features: Arrays, functions, multiple files processing

### Sed Stream Editing
- Basic operations: Substitution (`s/pattern/replacement/`), deletion, insertion
- Line addressing: Single lines, ranges, patterns, hold space
- Advanced commands: Transform, branch, label operations
- In-place editing: Backup files, multiple operations, safety

### JSON Processing with jq
- Filter syntax: Object property access, array indexing, slicing
- Transformations: Object construction, array manipulation, value extraction
- Complex queries: Recursive descent, conditionals, function calls
- Streaming: Large file processing, memory efficiency, incremental parsing

### Modern CLI Tools
- fd: Find replacement with intuitive syntax and performance
- bat: Cat replacement with syntax highlighting and git integration
- exa: Ls replacement with colors, icons, and tree view
- delta: Diff replacement with syntax highlighting and within-line changes
- fzf: Fuzzy finder for command-line fuzzy completion
- Integration patterns: Tool chaining, output processing, automation

### Pipeline Optimization
- Buffering strategies: Line vs block buffering, performance impact
- Parallel processing: `xargs -P`, `parallel`, concurrent execution
- Memory management: Large file handling, streaming vs loading
- Error handling: Pipeline failure detection, partial result processing

### Data Validation and Processing
- Schema validation: JSON Schema, XML validation, format checking
- Data integrity: Checksums, format verification, corruption detection
- Error recovery: Partial processing, fallback strategies, logging
- Performance monitoring: Processing speed, resource usage, bottlenecks

## Build Systems & Automation

### Make Fundamentals
- Target definitions: Dependencies, commands, automatic variables
- Makefile syntax: Rules, variables, functions, conditionals
- Pattern rules: Generic rules for file transformations
- Include files: Modular makefiles, shared configurations

### CMake Build System
- Configuration phase: `CMakeLists.txt`, configure_file, option()
- Generator selection: Ninja, Make, Visual Studio, platform-specific
- Find modules: Package detection, library finding, path resolution
- Package configuration: `find_package()`, target linking, properties

### Ninja Build System
- Build file syntax: Rules, builds, variables, pools
- Dependency tracking: Input/output dependencies, implicit dependencies
- Parallel execution: Job pools, resource limits, optimization
- Performance advantages: Low overhead, fast incremental builds

### Bazel/Buck Build Systems
- Hermetic builds: Isolated environments, reproducible builds
- Remote caching: Build artifact sharing, distributed compilation
- Build language: Starlark syntax, custom rules, macros
- Large codebase scaling: Incremental builds, dependency optimization

### Gradle Build Automation
- Dependency management: Maven/Ivy repositories, version resolution
- Multi-project builds: Settings, subprojects, composite builds
- Plugin ecosystem: Core plugins, community plugins, custom plugins
- Task definition: Custom tasks, incremental builds, up-to-date checks

### Remote Caches and Distribution
- Build artifact caching: Local and remote cache storage
- Cache invalidation: Content-based hashing, manual purging
- Distributed compilation: Remote workers, build distribution
- Cache optimization: Hit rate monitoring, cache warming strategies

## Task Runners & Workflow Automation

### Invoke Task Runner
- Python-based tasks: Function decorators, parameter handling
- Task organization: Namespaces, collections, auto-discovery
- Configuration: Invoke files, runtime configuration, environment handling
- Integration: Pre-commit hooks, CI/CD pipelines, development workflows

### Nox Testing Automation
- Session-based testing: Environment isolation, dependency management
- Multi-Python support: Version matrix testing, interpreter selection
- Configuration: `noxfile.py`, session parameters, conditional execution
- CI/CD integration: Automated testing, artifact generation

### Tox Testing Orchestration
- Multi-environment testing: Python version matrix, dependency isolation
- Configuration: `tox.ini`, environment factors, command specification
- Integration: CI/CD pipelines, development workflow automation
- Advanced features: Parallel execution, reporting, custom environments

### Just Command Runner
- Recipe-based tasks: Simple syntax, variable substitution
- Cross-platform support: Windows, macOS, Linux compatibility
- Dependency management: Task ordering, parallel execution
- Integration: Development workflows, deployment automation

### Task Orchestration Patterns
- Dependency graphs: Task relationships, execution ordering
- Parallel execution: Concurrent task running, resource management
- Error handling: Failure propagation, cleanup tasks, rollback
- Monitoring: Progress tracking, logging, execution timing

### Environment Management
- Virtual environments: venv, conda, pyenv isolation
- Dependency management: requirements.txt, Pipfile, poetry.lock
- Environment variables: Configuration, secrets, runtime settings
- Containerization: Docker, podman for isolated environments

## Package Management & Distribution

### System Package Managers
- apt (Debian/Ubuntu): Package installation, dependency resolution, updates
- yum/dnf (Red Hat): RPM package management, repository configuration
- Homebrew (macOS): Formula installation, cask applications, taps
- Package dependencies: Automatic resolution, conflict detection, upgrades

### Language Package Managers
- pip (Python): Package installation, virtual environment support
- npm/yarn/pnpm (JavaScript): Dependency management, workspace support
- cargo (Rust): Crate management, workspace organization
- go modules (Go): Dependency versioning, module management

### Container Package Management
- Multi-stage builds: Build optimization, image layer reduction
- Base image selection: Alpine, Debian, distroless considerations
- Layer caching: Dependency installation, build artifact optimization
- Security scanning: Vulnerability detection, base image updates

### Artifact Repositories
- Nexus Repository: Universal repository manager, format support
- Artifactory: Binary repository management, metadata support
- Package signing: GPG signatures, integrity verification
- Security features: Access control, audit logging, compliance

### Dependency Resolution
- Version conflicts: Resolution strategies, dependency hell avoidance
- Lock files: Reproducible builds, exact version pinning
- Semantic versioning: Compatibility ranges, update strategies
- Dependency auditing: Security vulnerabilities, license compliance

### Distribution Strategies
- Binary packages: Pre-compiled distributions, platform-specific builds
- Source packages: Build-time compilation, customization options
- Universal packages: Cross-platform compatibility, single artifact
- Container images: OCI standards, registry distribution

## Development Environment Setup

### Dotfiles Management
- Version control: Git repository organization, synchronization
- Modular configuration: Topic-based organization, conditional loading
- Cross-machine setup: Automated installation, backup restoration
- Privacy considerations: Sensitive data exclusion, encryption

### Shell Configuration
- Alias management: Command shortcuts, productivity improvements
- Function definitions: Complex operations, parameter handling
- Prompt customization: Git status, current directory, color schemes
- Tab completion: Command completion, option suggestions, custom completions

### Editor Integration
- Vim/Neovim: Plugin management, LSP integration, terminal integration
- Emacs: Configuration frameworks, package management, extensibility
- VS Code: Extension ecosystem, remote development, terminal integration
- Language servers: Protocol standardization, multi-editor support

### Terminal Multiplexers
- tmux sessions: Window management, pane splitting, session persistence
- Screen compatibility: Legacy support, basic multiplexing
- Configuration: Keybindings, status bars, automatic startup
- Workflow integration: Development environments, remote work

### Development Containers
- Dev containers specification: JSON configuration, tool installation
- Consistent environments: Dependency management, version pinning
- Remote development: VS Code integration, seamless debugging
- Team standardization: Shared configurations, onboarding simplification

### Local Development Optimization
- Hot reloading: File watching, automatic rebuilds, browser refresh
- Development servers: Live reload, API mocking, error overlays
- Debugging setup: Breakpoints, variable inspection, performance profiling
- Workflow automation: Pre-commit hooks, linting, testing integration

### Cross-Platform Compatibility
- Windows considerations: WSL integration, path handling, tool compatibility
- macOS specifics: Homebrew integration, system preferences
- Linux variants: Distribution differences, package manager variations
- Unified workflows: Shell script compatibility, tool selection

## Related Concepts

### Prerequisites
- [Programming Fundamentals](../../01-foundations/programming-fundamentals/README.md)
- [Version Control](../../01-foundations/version-control/README.md)

### Next Level Topics
- [DevOps & CI/CD](../../05-devops-cloud/devops-cicd/README.md)
- [Containerization](../../05-devops-cloud/containerization/README.md)
- [Build Tools & Performance](../../05-devops-cloud/build-systems/README.md)

### Complementary Skills
- [System Programming](../../02-backend-engineering/operating-systems/README.md)
- [API Design](../../02-backend-engineering/api-design/README.md)
- [Testing Strategies](../../architecture-testing/testing-strategies/README.md)

## Resources

### Books
- **The Linux Command Line (2nd Edition)** by William Shotts
  \$39.99, 504 pages, No Starch Press - Comprehensive command-line guide
- **Classic Shell Scripting** by Arnold Robbins & Nelson H.F. Beebe
  \$44.99, 560 pages, O'Reilly - Advanced shell scripting techniques
- **Effective DevOps** by Jennifer Davis & Katherine Daniels
  \$49.99, 400 pages, O'Reilly - Build system automation and tooling

### Courses
- **Linux Command Line Basics** - freeCodeCamp (YouTube)
  Free, 4 hours - Essential command-line skills for beginners
- **Advanced Bash Scripting Guide** - TLDP (online)
  Free, comprehensive - In-depth bash scripting reference
- **CMake Best Practices** - vector-of-bool (GitHub)
  Free, practical - Modern CMake usage and patterns

### Documentation
- **Bash Manual** - gnu.org/software/bash/manual
  Free, authoritative - Complete Bash reference manual
- **GNU Make Manual** - gnu.org/software/make/manual
  Free, comprehensive - Make build system documentation
- **CMake Documentation** - cmake.org/documentation
  Free, extensive - CMake build system reference

### Tools & Communities
- **tldr-pages** - tldr.sh
  Community-driven - Simplified command documentation
- **explainshell** - explainshell.com
  Interactive - Command-line tool explanation and breakdown
- **Command Line Heroes** - redhat.com/command-line-heroes
  Podcast series - Stories of command-line tool development

## Assessment Criteria

### Shell Scripting Proficiency
- ✅ Write safe, portable shell scripts with proper error handling
- ✅ Use advanced variable expansion and array operations effectively
- ✅ Implement signal handling and cleanup procedures correctly
- ✅ Debug shell scripts using tracing and profiling tools

### Text Processing Mastery
- ✅ Apply grep, awk, sed for complex text manipulation tasks
- ✅ Process JSON and structured data using jq and modern tools
- ✅ Optimize pipelines for performance and memory efficiency
- ✅ Validate and transform data using command-line tools

### Build System Configuration
- ✅ Configure Make, CMake, and Ninja for different project types
- ✅ Implement incremental builds and dependency management
- ✅ Optimize build performance using parallel execution and caching
- ✅ Debug build issues and resolve dependency conflicts

### Automation and Workflow
- ✅ Implement task runners for development workflow automation
- ✅ Set up multi-environment testing with Nox and Tox
- ✅ Create cross-platform scripts with proper portability
- ✅ Integrate automation into CI/CD pipelines

### Package Management
- ✅ Manage system and language packages across platforms
- ✅ Configure artifact repositories and distribution strategies
- ✅ Resolve dependency conflicts and maintain lock files
- ✅ Implement security scanning and license compliance

### Development Environment
- ✅ Set up productive shell environments with customization
- ✅ Configure editors and tools for efficient development
- ✅ Implement terminal multiplexing and session management
- ✅ Create reproducible development environments

### Career Readiness Indicators
- **Junior Developer**: Navigate file systems and run basic commands
- **Mid-Level Engineer**: Write automation scripts and configure build systems
- **Senior Engineer**: Design CI/CD pipelines and optimize development workflows
- **DevOps Engineer**: Manage infrastructure automation and deployment scripts
- **Engineering Manager**: Establish development standards and tooling guidelines
