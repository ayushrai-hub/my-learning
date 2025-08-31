[← Back to Curriculum](../README.md)

---

# Databases & Storage Systems

- **Relational Database Design**

  - Relational modeling: entities, relationships, cardinality
  - Normalization: 1NF, 2NF, 3NF, BCNF, denormalization trade-offs
  - Schema design: primary keys, foreign keys, constraints, triggers
  - Indexing strategies: B-tree, hash, bitmap, composite indexes
  - Query optimization: execution plans, statistics, cost-based optimization
  - Isolation levels: read uncommitted, read committed, repeatable read, serializable
  - ACID properties: atomicity, consistency, isolation, durability

- **NoSQL Database Families**

  - **Key-Value Stores**: Redis, DynamoDB, simple operations, caching patterns
  - **Document Databases**: MongoDB, CouchDB, flexible schema, JSON storage
  - **Column-Family**: Cassandra, HBase, wide columns, time-series data
  - **Graph Databases**: Neo4j, Amazon Neptune, relationships, traversals
  - CAP theorem: consistency, availability, partition tolerance trade-offs
  - BASE properties: basically available, soft state, eventual consistency
  - Polyglot persistence: right tool for the job, data modeling

- **Distributed Database Concepts**

  - Sharding strategies: horizontal partitioning, shard keys, rebalancing
  - Replication: master-slave, master-master, synchronous vs asynchronous
  - Consistency models: strong, eventual, causal, session consistency
  - Consensus algorithms: Paxos, Raft, leader election, log replication
  - Distributed transactions: 2PC, 3PC, saga pattern, compensation
  - Conflict resolution: last-write-wins, vector clocks, CRDTs
  - Partition tolerance: split-brain, quorum systems, failure detection

- **Caching & In-Memory Systems**

  - Redis patterns: cache-aside, write-through, write-behind, refresh-ahead
  - Cache invalidation: TTL, manual, event-driven, cache tags
  - Distributed caching: consistent hashing, cache coherence, hot spots
  - Pub/Sub messaging: Redis channels, pattern matching, scalability
  - Data structures: strings, lists, sets, sorted sets, hashes, streams
  - Persistence: RDB snapshots, AOF logging, hybrid approaches
  - High availability: Redis Sentinel, Redis Cluster, failover

- **Storage Engines & Internals**

  - LSM-trees: write optimization, compaction, level-based vs size-tiered
  - B+ trees: read optimization, page structure, buffer pool management
  - Write-ahead logging: durability, recovery, checkpoint mechanisms
  - MVCC: multi-version concurrency control, snapshot isolation, garbage collection
  - Buffer management: LRU, clock algorithm, dirty page handling
  - Storage formats: row-based, columnar, hybrid (PAX), compression
  - File organization: heap files, sorted files, hash files, clustered indexes

- **Time-Series & Analytical Systems**

  - Time-series databases: InfluxDB, TimescaleDB, OpenTSDB, retention policies
  - Data compression: delta encoding, run-length encoding, dictionary compression
  - Downsampling: aggregation functions, retention policies, storage optimization
  - Analytical databases: ClickHouse, BigQuery, Snowflake, columnar storage
  - OLAP vs OLTP: workload characteristics, optimization strategies
  - Data warehousing: star schema, snowflake schema, fact/dimension tables
  - Real-time analytics: stream processing, materialized views, incremental updates

- **Advanced Database Topics**
  - CAP vs PACELC: consistency, availability, partition tolerance, latency
  - HTAP systems: hybrid transactional/analytical processing, real-time analytics
  - Lake-house architectures: data lakes, data warehouses, unified analytics
  - Database as a Service: managed databases, serverless, auto-scaling
  - Multi-model databases: document, graph, key-value in single system
  - Blockchain databases: immutability, consensus, distributed ledger
  - Quantum-resistant cryptography: post-quantum algorithms, migration strategies
- Relational modelling, normalization, indexes, isolation levels
- NoSQL families: key-value, document, column, graph
- Sharding & replication; consensus (Paxos/Raft)
- Redis patterns (cache-aside, write-through, pub/sub)
- LSM-trees, time-series stores
- CAP vs PACELC; HTAP & lake-house architectures
