[← Back to Curriculum](../README.md)

---

# GraphQL & Advanced API Patterns

- **GraphQL Schema Architecture**

  - Schema-first design: type definitions, resolvers, schema composition
  - Type system: scalars, objects, interfaces, unions, enums, input types
  - Schema directives: custom logic, field transformation, access control
  - Schema composition: modular schemas, schema stitching, federation
  - Schema evolution: additive changes, deprecation, breaking changes, versioning
  - Documentation: descriptions, examples, schema introspection, tooling
  - Validation: schema validation, query validation, custom rules, security

- **Resolver Patterns & Data Loading**

  - Resolver functions: field resolution, context passing, error handling
  - Data loader pattern: batching, caching, N+1 problem solution, performance
  - Resolver chaining: nested resolvers, data dependencies, optimization
  - Async resolvers: promise handling, parallel execution, error propagation
  - Context management: request context, user authentication, database connections
  - Resolver composition: higher-order resolvers, middleware, cross-cutting concerns
  - Performance optimization: query analysis, resolver caching, database optimization

- **Query Optimization & Performance**

  - N+1 query problem: identification, DataLoader solution, batching strategies
  - Query complexity analysis: depth limiting, cost analysis, timeout handling
  - Caching strategies: field-level caching, query caching, CDN integration
  - Persisted queries: query whitelisting, automatic persisted queries, security
  - Query batching: multiple queries, request optimization, latency reduction
  - Lazy loading: on-demand data fetching, performance trade-offs, user experience
  - Monitoring: query performance, resolver timing, error tracking, usage analytics

- **Real-time Features & Subscriptions**

  - Subscription implementation: WebSocket transport, event-driven updates
  - Event filtering: subscription arguments, dynamic filtering, personalization
  - Subscription lifecycle: connection management, cleanup, error handling
  - Scaling subscriptions: connection management, message broadcasting, clustering
  - Authentication: subscription-level auth, field-level auth, token refresh
  - Rate limiting: subscription limits, event throttling, resource protection
  - Monitoring: active subscriptions, event delivery, connection health

- **Federation & Microservices**

  - Apollo Federation: gateway, subgraphs, entity resolution, composition
  - Schema stitching: remote schemas, delegation, type merging, conflicts
  - Service boundaries: domain-driven design, data ownership, autonomy
  - Cross-service queries: entity references, join strategies, performance
  - Distributed caching: federated cache, invalidation, consistency
  - Error handling: partial failures, error propagation, fallback strategies
  - Deployment: gateway deployment, subgraph versioning, rollout strategies

- **Security & Access Control**

  - Authentication: JWT tokens, OAuth integration, session management
  - Authorization: field-level permissions, role-based access, dynamic rules
  - Query depth limiting: recursive query prevention, complexity analysis
  - Rate limiting: query-based limits, field-based limits, user-based quotas
  - Input validation: argument validation, sanitization, injection prevention
  - Introspection control: production security, schema hiding, development tools
  - Audit logging: query logging, access tracking, compliance, monitoring

- **GraphQL vs REST Trade-offs**
  - Flexibility: client-driven queries, over-fetching prevention, under-fetching solution
  - Complexity: learning curve, tooling requirements, caching challenges
  - Performance: query optimization, N+1 problems, network efficiency
  - Caching: HTTP caching limitations, custom caching strategies, CDN integration
  - Tooling: development tools, debugging, monitoring, ecosystem maturity
  - Migration: REST to GraphQL, coexistence strategies, gradual adoption
  - Use case fit: API aggregation, mobile apps, real-time features, data exploration
