[← Back to Curriculum](../README.md)

---

# Real-Time Systems & Streaming

- **Stream Processing Fundamentals**

  - Event streams: ordered sequences, partitioning, replication, durability
  - Stream vs batch processing: latency, throughput, complexity, use cases
  - Event time vs processing time: timestamps, clock skew, out-of-order events
  - Windowing concepts: tumbling, sliding, session, custom windows, triggers
  - Watermarks: progress indicators, completeness estimation, late data handling
  - State management: keyed state, operator state, checkpointing, recovery
  - Backpressure: flow control, buffering, dropping, load shedding

- **Windowing & Time Semantics**

  - Time-based windows: fixed intervals, sliding intervals, session gaps
  - Count-based windows: fixed count, sliding count, custom triggers
  - Session windows: activity-based grouping, timeout configuration, merging
  - Custom windows: business logic, irregular intervals, complex triggers
  - Window lifecycle: creation, accumulation, triggering, purging, late arrivals
  - Allowed lateness: grace periods, side outputs, reprocessing strategies
  - Time zone handling: UTC normalization, local time processing, DST considerations

- **Exactly-Once Processing Guarantees**

  - At-most-once: message loss, no duplicates, performance benefits
  - At-least-once: no message loss, potential duplicates, idempotency requirements
  - Exactly-once: no loss, no duplicates, complexity, performance trade-offs
  - Idempotent operations: deterministic functions, side-effect management
  - Transactional guarantees: ACID properties, distributed transactions, coordination
  - Checkpointing: state snapshots, recovery points, consistency guarantees
  - End-to-end exactly-once: source to sink guarantees, system design considerations

- **Backpressure & Flow Control**

  - Backpressure detection: queue lengths, processing rates, latency monitoring
  - Flow control mechanisms: rate limiting, buffering, dropping, load balancing
  - Buffering strategies: in-memory, persistent, overflow handling, sizing
  - Load shedding: priority-based dropping, sampling, graceful degradation
  - Auto-scaling: horizontal scaling, vertical scaling, trigger conditions
  - Circuit breakers: failure detection, recovery, cascading failure prevention
  - Monitoring: throughput, latency, error rates, resource utilization

- **Stream Joins & Complex Processing**

  - Window joins: time-based correlation, join conditions, performance optimization
  - Stream-table joins: enrichment, lookup, caching, consistency considerations
  - Temporal joins: point-in-time lookups, versioned data, historical context
  - Interval joins: range-based correlation, overlapping events, efficiency
  - Join performance: partitioning, co-location, state size, memory management
  - Complex event processing: pattern detection, rule engines, state machines
  - Multi-stream processing: correlation, synchronization, ordering guarantees

- **Aggregations & Analytics**

  - Tumbling aggregations: non-overlapping windows, reset behavior, triggers
  - Sliding aggregations: overlapping windows, incremental computation, efficiency
  - Session aggregations: activity-based grouping, timeout handling, merging
  - Custom aggregators: user-defined functions, state management, serialization
  - Approximate aggregations: HyperLogLog, Count-Min Sketch, bloom filters
  - Real-time metrics: counters, gauges, histograms, percentiles, alerting
  - Multi-level aggregations: hierarchical rollups, drill-down capabilities

- **Late Data & Out-of-Order Processing**
  - Late arrival handling: allowed lateness, side outputs, reprocessing
  - Out-of-order processing: buffering, sorting, watermark advancement
  - Reprocessing strategies: full recomputation, incremental updates, versioning
  - Data correction: retroactive updates, audit trails, consistency maintenance
  - Time travel: historical queries, point-in-time recovery, versioning
  - Monitoring: late data metrics, processing delays, data quality indicators
  - Business impact: SLA considerations, accuracy vs latency trade-offs
