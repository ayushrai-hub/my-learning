[← Back to Curriculum](../README.md)

---

# System Design & Scalability Drills

- **Scalability Fundamentals & Patterns**

  - Horizontal vs vertical scaling: trade-offs, cost analysis, implementation complexity
  - Load distribution: round-robin, weighted, least connections, consistent hashing
  - Stateless design: session management, external state storage, microservice principles
  - Caching strategies: application cache, distributed cache, CDN, database cache
  - Database scaling: read replicas, sharding, federation, CQRS, event sourcing
  - Asynchronous processing: message queues, event-driven architecture, eventual consistency
  - Auto-scaling: metrics-based, predictive, cost optimization, scaling policies

- **Distributed Systems Challenges**

  - CAP theorem: consistency, availability, partition tolerance, trade-offs, real-world implications
  - Consistency models: strong, eventual, causal, session, monotonic consistency
  - Consensus algorithms: Raft, PBFT, proof-of-stake, leader election, split-brain prevention
  - Distributed transactions: 2PC, 3PC, saga pattern, compensation, rollback strategies
  - Clock synchronization: NTP, logical clocks, vector clocks, timestamp ordering
  - Failure detection: heartbeats, phi accrual, gossip protocols, network partitions
  - Byzantine fault tolerance: malicious actors, consensus, blockchain applications

- **High Availability & Fault Tolerance**

  - Redundancy strategies: active-passive, active-active, N+1, geographic distribution
  - Circuit breakers: failure detection, fallback mechanisms, recovery, configuration
  - Bulkhead pattern: resource isolation, failure containment, service boundaries
  - Timeout strategies: connection timeouts, read timeouts, retry policies, exponential backoff
  - Health checks: endpoint monitoring, dependency checks, graceful degradation
  - Disaster recovery: RTO, RPO, backup strategies, failover procedures, testing
  - Chaos engineering: failure injection, steady-state hypothesis, blast radius control

- **Performance & Capacity Planning**

  - Capacity modeling: Little's law, queuing theory, utilization targets, growth projections
  - Performance testing: load testing, stress testing, endurance testing, spike testing
  - Bottleneck identification: profiling, monitoring, resource utilization, queue analysis
  - Scaling triggers: CPU, memory, I/O, custom metrics, predictive scaling
  - Cost optimization: resource right-sizing, reserved instances, spot instances, scheduling
  - Performance budgets: latency targets, throughput requirements, error rate limits
  - Monitoring: SLIs, SLOs, error budgets, alerting, dashboards, trend analysis

- **Data Architecture & Storage**

  - Data partitioning: horizontal, vertical, functional, hash-based, range-based
  - Sharding strategies: consistent hashing, directory-based, entity groups, cross-shard queries
  - Replication: master-slave, master-master, multi-master, conflict resolution
  - Data consistency: ACID, BASE, eventual consistency, strong consistency, trade-offs
  - Storage systems: relational, NoSQL, NewSQL, time-series, graph, document databases
  - Data lakes: schema-on-read, data formats, query engines, governance, security
  - Caching: application cache, database cache, distributed cache, cache invalidation

- **API Design & Integration**

  - Rate limiting: token bucket, leaky bucket, sliding window, distributed rate limiting
  - API versioning: URL versioning, header versioning, content negotiation, deprecation
  - Authentication: OAuth, JWT, API keys, mutual TLS, service-to-service auth
  - Idempotency: idempotent operations, idempotency keys, duplicate detection, retry safety
  - Pagination: offset-based, cursor-based, performance implications, consistency
  - Bulk operations: batch APIs, streaming, partial failures, transaction semantics
  - Error handling: error codes, error messages, retry policies, circuit breakers

- **System Design Interview Patterns**
  - Requirements gathering: functional, non-functional, scale estimation, constraints
  - High-level design: system components, data flow, API design, technology choices
  - Detailed design: database schema, algorithms, protocols, error handling
  - Scale estimation: QPS, storage, bandwidth, memory, cost analysis
  - Trade-off analysis: consistency vs availability, latency vs throughput, cost vs performance
  - Failure scenarios: single points of failure, cascading failures, recovery strategies
  - Monitoring: metrics, logging, alerting, dashboards, operational procedures
