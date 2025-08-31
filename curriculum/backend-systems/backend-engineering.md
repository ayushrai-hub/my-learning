[← Back to Curriculum](../README.md)

---

# Backend Engineering (FastAPI)

- **ASGI vs WSGI Fundamentals**

  - WSGI protocol: synchronous, request-response, middleware
  - ASGI protocol: asynchronous, WebSockets, HTTP/2, long polling
  - Application servers: Gunicorn, uWSGI, Uvicorn, Hypercorn
  - Performance characteristics: throughput, latency, resource usage
  - Deployment considerations: process management, scaling strategies
  - Protocol adapters: WSGI-to-ASGI, legacy application integration
  - Event loop integration: asyncio, uvloop, performance optimization

- **Pydantic Models & Validation**

  - Model definition: field types, constraints, default values
  - Validation: built-in validators, custom validators, root validators
  - Serialization: JSON encoding, custom encoders, alias generation
  - Settings management: environment variables, configuration files
  - Model inheritance: base models, mixins, composition patterns
  - Generic models: TypeVar, parameterized types, reusability
  - Performance: model compilation, validation caching, optimization

- **Dependency Injection & Architecture**

  - Dependency system: function parameters, class dependencies
  - Dependency scopes: request, application, custom lifetimes
  - Sub-dependencies: nested injection, dependency graphs
  - Dependency overrides: testing, configuration, environment-specific
  - Provider patterns: factory functions, class-based providers
  - Async dependencies: database connections, external services
  - Security dependencies: authentication, authorization, rate limiting

- **API Design & OpenAPI Integration**

  - REST resource modeling: nouns vs verbs, resource hierarchies
  - HTTP methods: GET, POST, PUT, PATCH, DELETE semantics
  - Status codes: appropriate usage, error handling, client guidance
  - OpenAPI generation: automatic documentation, schema validation
  - API versioning: URL path, headers, content negotiation
  - Response models: serialization, field filtering, nested resources
  - Request validation: path parameters, query parameters, request bodies

- **Authentication & Authorization**

  - OAuth2 flows: authorization code, client credentials, PKCE
  - JWT tokens: structure, claims, signing, verification, expiration
  - Refresh token rotation: security, user experience, storage
  - RBAC implementation: roles, permissions, hierarchies
  - Scopes: fine-grained permissions, API access control
  - Session management: stateful vs stateless, security considerations
  - Multi-factor authentication: TOTP, SMS, email verification
  - API key management: generation, rotation, rate limiting

- **Advanced Features & Real-time Communication**

  - Pagination: offset-based, cursor-based, performance considerations
  - Filtering: query parameters, complex filters, security validation
  - Sorting: multiple fields, custom sort orders, performance impact
  - Background tasks: Celery integration, task queues, job scheduling
  - WebSockets: connection management, broadcasting, scaling
  - Server-Sent Events: real-time updates, connection handling
  - File uploads: multipart forms, streaming, validation, storage
  - Caching: response caching, dependency caching, cache invalidation

- **Database Integration & ORM**

  - Async database drivers: asyncpg, aiomysql, motor, performance
  - Connection pooling: pool size, connection lifecycle, monitoring
  - Transaction management: ACID properties, isolation levels, rollback
  - SQLAlchemy async: Core vs ORM, session management, relationships
  - Query optimization: N+1 problems, eager loading, query analysis
  - Database migrations: Alembic, schema versioning, deployment strategies
  - Connection resilience: retry logic, circuit breakers, failover

- **Testing & Quality Assurance**
  - Test client: TestClient, async testing, request simulation
  - Dependency overrides: mock services, test databases, isolation
  - Fixture management: pytest fixtures, database setup, cleanup
  - Integration testing: database, external services, end-to-end
  - Performance testing: load testing, stress testing, benchmarking
  - API contract testing: schema validation, backward compatibility
  - Security testing: authentication, authorization, input validation
- ASGI vs WSGI
- Pydantic models & settings, dependency injection
- REST resource modelling, OpenAPI generation/versioning
- OAuth2, JWT, refresh-token rotation, RBAC scopes
- Pagination, filtering, background tasks, WebSockets/SSE
- Async DB drivers, connection pooling, transactions
