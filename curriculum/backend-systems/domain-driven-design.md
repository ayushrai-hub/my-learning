[← Back to Curriculum](../README.md)

---

# Domain-Driven Design & Microservices

- **Domain Modeling & Strategic Design**

  - Ubiquitous language: shared vocabulary, domain experts, team alignment
  - Bounded contexts: model boundaries, context mapping, integration patterns
  - Domain events: business events, event storming, temporal modeling
  - Context mapping: partnership, shared kernel, customer-supplier, conformist
  - Subdomain classification: core, supporting, generic domains
  - Strategic design: context boundaries, team organization, evolution

- **Tactical Design Patterns**

  - Aggregates: consistency boundaries, invariants, transaction scope
  - Entities: identity, lifecycle, behavior encapsulation
  - Value objects: immutability, equality, side-effect-free functions
  - Domain services: stateless operations, cross-aggregate behavior
  - Repositories: aggregate persistence, query interfaces, abstractions
  - Factories: complex creation logic, aggregate reconstruction
  - Domain events: intra-aggregate, inter-aggregate, eventual consistency

- **Event-Driven Architecture**

  - Domain events: business significance, temporal aspects, causality
  - Event sourcing: event streams, aggregate reconstruction, projections
  - Sagas: long-running processes, compensation, coordination patterns
  - Process managers: stateful coordination, timeout handling
  - Event stores: append-only, versioning, snapshotting strategies
  - Projections: read models, eventual consistency, rebuilding mechanisms
  - Outbox pattern: transactional consistency, at-least-once delivery

- **Microservices Architecture**

  - Service boundaries: business capabilities, data ownership, team structure
  - API gateway: routing, authentication, rate limiting, transformation
  - Service discovery: client-side, server-side, service mesh integration
  - Inter-service communication: synchronous vs asynchronous trade-offs
  - Data consistency: eventual consistency, distributed transactions, compensation
  - Service decomposition: strangler fig, database-per-service, shared data
  - Distributed system challenges: network partitions, latency, failures

- **Communication Patterns**

  - gRPC: protocol buffers, streaming, performance, type safety
  - REST: resource modeling, HTTP semantics, statelessness, caching
  - GraphQL: schema stitching, federation, N+1 problem, caching
  - Message queues: asynchronous communication, decoupling, reliability
  - Event streaming: Kafka, event sourcing, CQRS integration
  - Request-response: synchronous, blocking, error handling
  - Publish-subscribe: loose coupling, fan-out, event distribution

- **Backend-for-Frontend & Micro-frontends**

  - BFF pattern: client-specific APIs, data aggregation, transformation
  - API composition: multiple service calls, data merging, error handling
  - Micro-frontends: independent deployment, technology diversity, integration
  - Module federation: runtime composition, shared dependencies, versioning
  - Cross-cutting concerns: authentication, logging, monitoring, security
  - Team organization: full-stack ownership, Conway's law implications
  - Integration strategies: build-time, runtime, server-side composition

- **Observability & Cross-Service Tracing**
  - Distributed tracing: trace propagation, span correlation, sampling
  - Correlation IDs: request tracking, log correlation, debugging
  - Service maps: dependency visualization, performance bottlenecks
  - Health checks: liveness, readiness, dependency health
  - Circuit breakers: failure isolation, cascading failure prevention
  - Bulkhead pattern: resource isolation, failure containment
  - Monitoring strategies: golden signals, SLIs/SLOs, alerting
- Ubiquitous language, bounded contexts
- Aggregates, entities, value objects, invariants
- Domain events, sagas, transactional outbox
- API gateway, service discovery, service mesh
- gRPC vs REST vs GraphQL
- Backend-for-frontend (BFF) & micro-frontends
- Trace propagation & cross-service observability
