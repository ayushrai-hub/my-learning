[← Back to Curriculum](../README.md)

---

# Version Control & Collaboration

- **Git Internals & Advanced Operations**

  - Git object model: blobs, trees, commits, tags, refs
  - Hash-based content addressing: SHA-1, content integrity
  - Index/staging area: partial commits, interactive staging
  - Reflog: reference history, recovery operations, expiration
  - Hooks: pre-commit, post-receive, custom automation
  - Git configuration: global, local, system levels, aliases

- **Branching Strategies & Workflow Patterns**

  - Trunk-based development: short-lived branches, continuous integration
  - Git Flow: feature, develop, release, hotfix branches
  - GitHub Flow: feature branches, pull requests, deploy from main
  - Release trains: scheduled releases, feature freezes, stabilization
  - Branch protection rules: required reviews, status checks
  - Merge strategies: merge commits, squash, rebase, fast-forward

- **Commit Management & History**

  - Conventional Commits: type, scope, breaking changes, automation
  - Commit message best practices: imperative mood, body structure
  - Interactive rebase: squashing, reordering, editing, splitting
  - Cherry-picking: selective commit application, conflict handling
  - Signed commits: GPG signatures, verification, trust chains
  - History rewriting: risks, coordination, force-push alternatives

- **Code Review & Collaboration**

  - Pull request workflow: creation, review, approval, merge
  - Review best practices: constructive feedback, knowledge sharing
  - Code review checklists: functionality, security, performance, style
  - Review tools: GitHub, GitLab, Bitbucket, Azure DevOps
  - Pair programming: driver-navigator, remote pairing, benefits
  - Async collaboration: time zones, documentation, communication

- **Monorepo & Multi-Repository Management**

  - Monorepo benefits: code sharing, atomic changes, tooling consistency
  - Submodules: external dependencies, version pinning, update strategies
  - Subtrees: code sharing, history preservation, merge strategies
  - Sparse checkout: partial repository clones, performance optimization
  - Build systems: Bazel, Nx, Rush, dependency management
  - Code ownership: CODEOWNERS files, review assignments

- **GitHub Actions & CI/CD Integration**

  - Workflow syntax: triggers, jobs, steps, actions marketplace
  - Matrix builds: multiple environments, parallel execution, optimization
  - Reusable workflows: DRY principles, organization-level sharing
  - Custom actions: JavaScript, Docker, composite actions
  - Secrets management: repository, organization, environment secrets
  - Security: OIDC, least privilege, supply chain protection

- **Release Management & Automation**
  - Semantic versioning: major, minor, patch, pre-release identifiers
  - Automated versioning: conventional commits, version bumping
  - CHANGELOG generation: conventional commits, release notes
  - Release pipelines: build, test, package, deploy, notify
  - Artifact management: binaries, containers, packages, signing
  - Rollback strategies: blue-green, canary, feature flags
- Git object model, reflog recovery
- Branching strategies (trunk, Git-flow, release trains)
- Conventional Commits, signed tags
- PR etiquette, code-review checklists
- Submodules & subtrees, monorepo basics
- GitHub Actions: matrix builds, reusable workflows, secrets
- Auto-generated CHANGELOG & release pipelines
