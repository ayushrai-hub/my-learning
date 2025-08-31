[← Back to Curriculum](../README.md)

---

# Software Design & Patterns

- **SOLID Principles & Design Fundamentals**

  - Single Responsibility: cohesion, separation of concerns, modularity
  - Open/Closed: extension vs modification, plugin architectures
  - Liskov Substitution: behavioral subtyping, contract compliance
  - Interface Segregation: client-specific interfaces, role-based design
  - Dependency Inversion: abstractions, dependency injection, IoC containers
  - Composition over inheritance: flexibility, loose coupling
  - Law of Demeter: minimal knowledge principle, method chaining

- **GRASP Principles & Responsibility Assignment**

  - Information Expert: data and behavior co-location
  - Creator: object creation responsibilities, factory patterns
  - Controller: system events, use case coordination
  - Low Coupling: dependency minimization, interface design
  - High Cohesion: focused responsibilities, single purpose
  - Polymorphism: behavior variation, strategy pattern
  - Pure Fabrication: artificial classes, service objects
  - Indirection: decoupling, adapter patterns, proxies
  - Protected Variations: change isolation, stable interfaces

- **Gang of Four Design Patterns**

  - **Creational**: Singleton, Factory Method, Abstract Factory, Builder, Prototype
  - **Structural**: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy
  - **Behavioral**: Observer, Strategy, Command, State, Template Method, Chain of Responsibility
  - Pattern selection criteria: problem context, trade-offs, alternatives
  - Anti-patterns: overuse, inappropriate application, complexity
  - Modern alternatives: functional programming, composition patterns

- **Architectural Patterns & Styles**

  - Hexagonal Architecture: ports and adapters, dependency direction
  - Clean Architecture: dependency rule, use cases, entities
  - Onion Architecture: layers, dependency inversion, core isolation
  - Layered Architecture: separation of concerns, abstraction levels
  - Model-View-Controller: separation, user interface patterns
  - Component-based: reusability, composition, encapsulation

- **CQRS & Event Sourcing**

  - Command Query Responsibility Segregation: read/write separation
  - Command handlers: business logic, validation, side effects
  - Query handlers: data retrieval, projections, optimization
  - Event sourcing: event streams, state reconstruction, audit trails
  - Event stores: append-only, versioning, snapshotting
  - Projections: read models, eventual consistency, rebuilding
  - Sagas: long-running processes, compensation, coordination

- **Microservices vs Modular Monolith**

  - Service boundaries: business capabilities, data ownership
  - Distributed system challenges: network, consistency, complexity
  - Modular monolith: internal boundaries, deployment simplicity
  - Migration strategies: strangler fig, database decomposition
  - Service communication: synchronous vs asynchronous, protocols
  - Data consistency: eventual consistency, distributed transactions
  - Operational complexity: monitoring, debugging, deployment

- **Documentation & Communication**

  - Architecture Decision Records (ADRs): context, decision, consequences
  - C4 model: context, containers, components, code diagrams
  - Sequence diagrams: interaction flows, timing, lifelines
  - System documentation: architecture overview, design rationale
  - API documentation: contracts, examples, versioning
  - Knowledge sharing: design reviews, tech talks, wikis

- **Evolutionary Refactoring Techniques**
  - Code smells: identification, prioritization, technical debt
  - Refactoring techniques: extract method, move field, rename
  - Evolutionary design: incremental improvement, feedback loops
  - Legacy system modernization: strangler fig, branch by abstraction
  - Testing during refactoring: safety nets, regression prevention
  - Performance refactoring: profiling, optimization, measurement
- SOLID, GRASP, GoF 23 patterns
- Hexagonal / clean / onion architecture
- CQRS & event sourcing
- Modular monolith vs microservices
- ADRs, C4 & sequence diagrams
- Evolutionary refactoring techniques
