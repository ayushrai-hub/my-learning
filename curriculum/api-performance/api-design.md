[← Back to Curriculum](../README.md)

---

# API Design & Documentation

- **REST API Design Principles**

  - REST maturity model: Level 0-3, Richardson Maturity Model, HATEOAS
  - Resource modeling: nouns vs verbs, hierarchical resources, collection patterns
  - URI design: naming conventions, path parameters, query parameters, versioning
  - HTTP methods: GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD semantics
  - Status codes: 2xx success, 3xx redirection, 4xx client error, 5xx server error
  - HATEOAS: hypermedia controls, discoverability, state transitions, client coupling
  - RFC 7807: problem details, error standardization, machine-readable errors

- **Advanced REST Patterns**

  - Pagination strategies: offset-based, cursor-based, seek method, performance
  - Filtering: query parameters, complex filters, security considerations, validation
  - Sorting: multiple fields, custom orders, performance impact, default behavior
  - Field selection: sparse fieldsets, projection, bandwidth optimization
  - Bulk operations: batch requests, partial failures, transaction semantics
  - Idempotency: idempotency keys, safe retries, duplicate detection, caching
  - Conditional requests: ETags, If-Match, If-None-Match, optimistic concurrency

- **gRPC & Protocol Buffers**

  - Protocol definition: .proto files, service definitions, message types
  - Code generation: multi-language support, client libraries, server stubs
  - Streaming patterns: unary, server streaming, client streaming, bidirectional
  - Interceptors: authentication, logging, metrics, error handling, middleware
  - Load balancing: client-side, server-side, health checking, service discovery
  - Error handling: status codes, error details, retry policies, deadlines
  - Performance: binary protocol, HTTP/2, multiplexing, compression

- **GraphQL Schema Design**

  - Schema definition: types, fields, arguments, directives, documentation
  - Query optimization: N+1 problem, DataLoader, batching, caching strategies
  - Mutation design: input types, payload types, error handling, validation
  - Subscription patterns: real-time updates, filtering, authentication, scaling
  - Schema evolution: versioning, deprecation, breaking changes, migration
  - Federation: schema stitching, gateway patterns, service boundaries
  - Security: query depth limiting, rate limiting, introspection control, authorization

- **Asynchronous API Patterns**

  - Webhooks: callback URLs, security, retry policies, payload verification
  - Server-Sent Events: real-time updates, connection management, fallback strategies
  - WebSockets: bidirectional communication, connection lifecycle, scaling challenges
  - CloudEvents: standardized event format, routing, filtering, transformation
  - Event-driven APIs: publish-subscribe, event sourcing, eventual consistency
  - Long polling: connection management, timeout handling, resource usage
  - Push notifications: mobile push, web push, delivery guarantees, personalization

- **API Documentation & Developer Experience**

  - OpenAPI specification: schema definition, code generation, validation
  - Interactive documentation: Swagger UI, ReDoc, try-it-out functionality
  - SDK generation: multi-language support, versioning, distribution, maintenance
  - Code examples: multiple languages, common use cases, error scenarios
  - Getting started guides: authentication, first API call, common workflows
  - Changelog: version history, breaking changes, migration guides, deprecation
  - Community: forums, support channels, feedback collection, contribution guidelines

- **API Lifecycle Management**
  - Versioning strategies: URL path, header, content negotiation, semantic versioning
  - Deprecation process: announcement, migration period, sunset timeline, communication
  - Breaking changes: impact assessment, migration tools, backward compatibility
  - Rate limiting: quota management, throttling, fair usage, abuse prevention
  - Analytics: usage metrics, performance monitoring, error tracking, user behavior
  - Monetization: pricing tiers, usage-based billing, API keys, subscription management
  - Governance: API standards, review processes, compliance, security policies
