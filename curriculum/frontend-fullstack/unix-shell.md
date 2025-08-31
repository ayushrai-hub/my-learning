[← Back to Curriculum](../README.md)

---

# Unix Shell & Build Tooling

- **Advanced Bash & POSIX Scripting**

  - Shell safety: `set -euo pipefail`, error handling, exit codes
  - Variable expansion: parameter expansion, arrays, associative arrays
  - Quoting pitfalls: single quotes, double quotes, command substitution
  - Process substitution: `<()`, `>()`, named pipes, file descriptors
  - Signal handling: trap commands, cleanup functions, graceful shutdown
  - Debugging: `set -x`, `bash -x`, shellcheck, script profiling
  - Portability: POSIX compliance, shell detection, cross-platform scripts

- **Text Processing & Data Manipulation**

  - grep family: grep, egrep, fgrep, ripgrep performance, regex patterns
  - awk programming: field processing, pattern-action, built-in variables
  - sed stream editing: substitution, deletion, line addressing, hold space
  - jq JSON processing: filters, transformations, complex queries, streaming
  - Modern alternatives: ripgrep, fd, bat, exa, delta, fzf integration
  - Pipeline optimization: buffering, parallel processing, memory usage
  - Data validation: schema checking, format verification, error handling

- **Build Systems & Automation**

  - Make fundamentals: targets, dependencies, automatic variables, patterns
  - CMake: configuration, generators, find modules, package management
  - Ninja: build speed, dependency tracking, parallel execution
  - Bazel/Buck: hermetic builds, remote caching, distributed compilation
  - Gradle: dependency management, multi-project builds, plugin ecosystem
  - Remote caches: build artifact caching, cache invalidation, distribution
  - Build optimization: incremental builds, parallel execution, profiling

- **Task Runners & Workflow Automation**

  - Invoke: Python-based tasks, parameterization, namespace organization
  - Nox: testing automation, environment management, session configuration
  - Tox: multi-environment testing, dependency isolation, CI integration
  - Just: command runner, recipe organization, cross-platform support
  - Task orchestration: dependency management, parallel execution, error handling
  - Environment management: virtual environments, dependency isolation
  - CI/CD integration: task automation, artifact generation, deployment

- **Package Management & Distribution**

  - System package managers: apt, yum, brew, package dependencies
  - Language package managers: pip, npm, cargo, go modules
  - Container package management: multi-stage builds, layer optimization
  - Artifact repositories: Nexus, Artifactory, package signing, security
  - Dependency resolution: version conflicts, lock files, reproducible builds
  - Security scanning: vulnerability detection, license compliance
  - Distribution strategies: binary packages, source packages, universal packages

- **Development Environment Setup**
  - Dotfiles management: version control, synchronization, modularity
  - Shell configuration: aliases, functions, prompt customization, completion
  - Editor integration: vim, emacs, VS Code, language servers
  - Terminal multiplexers: tmux, screen, session management, automation
  - Development containers: devcontainers, consistent environments, tooling
  - Local development: hot reloading, file watching, automatic rebuilds
  - Cross-platform compatibility: Windows, macOS, Linux considerations
