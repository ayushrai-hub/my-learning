[← Back to Curriculum](../README.md)

---

# Message Queues & Event-Driven Architecture

- **Message Broker Architectures**

  - RabbitMQ: AMQP protocol, exchanges, queues, routing, clustering, federation
  - NATS: publish-subscribe, request-reply, clustering, JetStream persistence
  - Apache Pulsar: multi-tenancy, geo-replication, tiered storage, functions
  - Apache Kafka: distributed log, partitioning, replication, ecosystem integration
  - Amazon Kinesis: managed streaming, sharding, scaling, AWS integration
  - Broker selection: throughput, latency, durability, scalability, operational complexity
  - Hybrid architectures: multi-broker deployments, protocol bridging, migration

- **Delivery Guarantees & Reliability**

  - At-most-once delivery: fire-and-forget, potential message loss, high performance
  - At-least-once delivery: acknowledgments, retries, duplicate handling, idempotency
  - Exactly-once delivery: transactional semantics, complexity, performance impact
  - Message durability: persistence, replication, disk vs memory storage
  - Acknowledgment patterns: auto-ack, manual-ack, batch acknowledgments
  - Failure handling: dead letter queues, retry policies, circuit breakers
  - End-to-end reliability: producer to consumer guarantees, monitoring, alerting

- **Partitioning & Scalability**

  - Partitioning strategies: key-based, round-robin, custom partitioning
  - Partition assignment: consumer groups, rebalancing, sticky assignment
  - Scaling patterns: horizontal scaling, partition splitting, consumer scaling
  - Load balancing: even distribution, hot partitions, monitoring, rebalancing
  - Consumer groups: parallel processing, fault tolerance, offset management
  - Producer patterns: batching, compression, async vs sync, error handling
  - Performance tuning: throughput optimization, latency reduction, resource allocation

- **Event Formats & Schema Management**

  - CloudEvents: standard format, metadata, content types, extensions
  - AsyncAPI: event-driven API specification, documentation, code generation
  - Apache Avro: schema evolution, binary serialization, compatibility rules
  - Protocol Buffers: language-neutral, backward compatibility, performance
  - JSON Schema: validation, documentation, tooling, human readability
  - Schema registry: centralized management, versioning, compatibility checking
  - Evolution strategies: backward, forward, full compatibility, breaking changes

- **Message Ordering & Consistency**

  - Global ordering: single partition, performance limitations, use cases
  - Partial ordering: per-key ordering, partition-level guarantees, scalability
  - Causal ordering: happens-before relationships, vector clocks, complexity
  - Message timestamps: producer time, broker time, consumer time, clock skew
  - Ordering guarantees: within partition, across partitions, trade-offs
  - Consistency models: eventual consistency, strong consistency, session consistency
  - Conflict resolution: last-writer-wins, vector clocks, application-specific logic

- **Data Retention & Cleanup**

  - Retention policies: time-based, size-based, compaction, deletion
  - Log compaction: key-based retention, tombstone records, cleanup policies
  - Tiered storage: hot, warm, cold storage, cost optimization, access patterns
  - Archival strategies: long-term storage, compliance, retrieval, lifecycle management
  - Cleanup procedures: automated cleanup, manual intervention, monitoring
  - Storage optimization: compression, deduplication, indexing, query performance
  - Compliance: data governance, privacy regulations, audit trails, retention schedules

- **Error Handling & Recovery**
  - Dead letter queues: failed message handling, analysis, reprocessing
  - Retry mechanisms: exponential backoff, jitter, max retries, circuit breakers
  - Poison messages: detection, isolation, handling, prevention
  - Error classification: transient, permanent, retriable, non-retriable
  - Recovery strategies: replay, reprocessing, skip, manual intervention
  - Monitoring: error rates, queue depths, processing latency, alerting
  - Incident response: escalation procedures, runbooks, post-mortem analysis
