# 🗄️ Databases & Storage Systems

## Executive Summary
Database systems form the foundation of data persistence and retrieval in modern applications. This curriculum covers relational and NoSQL databases, distributed systems, caching strategies, and advanced storage patterns. Students will master database design, optimization techniques, and the selection of appropriate storage solutions for different use cases, from traditional OLTP to modern analytical workloads.

## Core Concepts
Effective database design requires understanding:
- **Relational Design**: Normalization, indexing, query optimization, transactions
- **NoSQL Systems**: Key-value, document, columnar, graph database patterns
- **Distributed Databases**: Sharding, replication, consistency models, consensus
- **Caching Systems**: In-memory storage, cache patterns, invalidation strategies
- **Storage Engines**: LSM-trees, B-trees, MVCC, write-ahead logging
- **Analytical Systems**: Time-series, OLAP, data warehousing, real-time analytics

### Why This Matters (2024 Perspective)
Databases power 99% of applications and handle massive data growth:
- Global database market exceeds $100B annually (2024 Gartner)
- NoSQL adoption grew 40% in enterprises (2024 surveys)
- Distributed databases handle 70% of cloud workloads
- Caching reduces latency by 10-100x in high-performance systems

## Prerequisites
- Basic SQL knowledge and CRUD operations
- Understanding of data structures and algorithms
- Familiarity with system design concepts
- Basic knowledge of networking and distributed systems

## Learning Objectives
- [ ] Design normalized relational database schemas with proper indexing
- [ ] Choose appropriate NoSQL databases for different data models
- [ ] Implement distributed database patterns (sharding, replication, consensus)
- [ ] Apply caching strategies for performance optimization
- [ ] Understand storage engine internals and optimization techniques
- [ ] Design analytical systems for time-series and OLAP workloads

## Key Technologies & Tools
| Technology | Version (2024) | Purpose |
|------------|----------------|---------|
| PostgreSQL | 16            | Advanced relational database with extensions |
| MongoDB    | 7.0           | Document database for flexible schemas |
| Redis      | 7.2           | In-memory data store and caching |
| Cassandra  | 4.1           | Distributed wide-column store |
| ClickHouse | 23.12         | High-performance analytical database |
| TimescaleDB| 2.13          | Time-series database built on PostgreSQL |

## Relational Database Design

### Data Modeling
- Entity-relationship modeling and diagram creation
- Cardinality and relationship types (1:1, 1:N, N:M)
- Primary key and foreign key constraints
- Surrogate vs natural keys

### Normalization
- First Normal Form (1NF): Atomic values and repeating groups
- Second Normal Form (2NF): Partial dependency removal
- Third Normal Form (3NF): Transitive dependency elimination
- Boyce-Codd Normal Form (BCNF): Determinant analysis
- Denormalization strategies for performance

### Schema Design
- Table structure and data type selection
- Constraint implementation (CHECK, UNIQUE, NOT NULL)
- Trigger usage for business rules and auditing
- View creation for abstraction and security

### Indexing Strategies
- B-tree indexes for range queries and sorting
- Hash indexes for equality lookups
- Bitmap indexes for low-cardinality columns
- Composite indexes for multi-column queries
- Partial and functional indexes
- Index maintenance and reorganization

### Query Optimization
- Execution plan analysis and interpretation
- Statistics collection and histogram usage
- Cost-based optimization understanding
- Query rewrite and transformation techniques

### Transaction Management
- ACID properties and their guarantees
- Isolation levels: READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE
- Locking mechanisms: shared, exclusive, row-level, table-level
- Deadlock detection and resolution
- Savepoints and transaction rollback

## NoSQL Database Families

### Key-Value Stores
- Redis data structures and commands
- DynamoDB partition keys and sort keys
- Consistency models and eventual consistency
- Use cases: caching, session storage, real-time analytics

### Document Databases
- MongoDB document structure and BSON format
- Flexible schema design and migration
- Indexing strategies: single field, compound, geospatial
- Aggregation framework for complex queries

### Column-Family Stores
- Cassandra data model: keyspaces, tables, columns
- Wide column design for time-series data
- Consistency levels: ONE, QUORUM, ALL
- Replication strategies and snitch configuration

### Graph Databases
- Neo4j property graph model (nodes, relationships, properties)
- Cypher query language fundamentals
- Traversal algorithms and shortest path finding
- Use cases: social networks, recommendation systems

### CAP Theorem Trade-offs
- Consistency, Availability, Partition tolerance triangle
- PACELC theorem: latency vs consistency in normal operation
- BASE properties for eventually consistent systems
- Real-world examples and compromise strategies

### Polyglot Persistence
- Choosing the right database for specific workloads
- Data modeling differences across database types
- Migration strategies between database systems
- Multi-database architecture patterns

## Distributed Database Concepts

### Sharding Strategies
- Horizontal partitioning across multiple nodes
- Shard key selection and distribution
- Consistent hashing for load balancing
- Rebalancing and resharding operations
- Cross-shard queries and scatter-gather patterns

### Replication Patterns
- Master-slave replication for read scaling
- Multi-master replication and conflict resolution
- Synchronous vs asynchronous replication
- Replication lag and eventual consistency

### Consistency Models
- Strong consistency guarantees
- Eventual consistency and convergence
- Causal consistency and session guarantees
- Linearizability and serializability

### Consensus Algorithms
- Paxos algorithm: roles, phases, quorum requirements
- Raft consensus: leader election, log replication
- ZooKeeper atomic broadcast (ZAB)
- Practical implementations in distributed systems

### Distributed Transactions
- Two-phase commit (2PC) protocol
- Three-phase commit (3PC) improvements
- Saga pattern for long-running transactions
- Compensation and rollback strategies

### Conflict Resolution
- Last-write-wins strategy
- Vector clocks for causality tracking
- Conflict-free replicated data types (CRDTs)
- Merge strategies and reconciliation

## Caching & In-Memory Systems

### Redis Patterns
- Cache-aside pattern: lazy loading from database
- Write-through: synchronous cache updates
- Write-behind: asynchronous cache updates
- Cache invalidation strategies

### Cache Invalidation
- Time-to-live (TTL) expiration
- Manual invalidation with cache keys
- Event-driven invalidation
- Cache tagging for selective invalidation

### Distributed Caching
- Consistent hashing for cache distribution
- Cache coherence and consistency
- Hot spot mitigation strategies
- Cache clustering and replication

### Pub/Sub Messaging
- Redis channels and publish/subscribe pattern
- Pattern matching with wildcards
- Scalability considerations and partitioning
- Message persistence and reliability

### Redis Data Structures
- Strings: basic operations and bit operations
- Lists: queues, stacks, capped collections
- Sets: unique value storage and set operations
- Sorted sets: ranking and scoring
- Hashes: field-value pairs and memory efficiency
- Streams: append-only logs with consumer groups

### Persistence Options
- RDB snapshots: point-in-time backups
- Append-only file (AOF): write-ahead logging
- Hybrid persistence approaches
- Durability vs performance trade-offs

## Storage Engines & Internals

### LSM-Tree Architecture
- Write optimization through sequential I/O
- Memtable and SSTable structure
- Compaction strategies: level-based, size-tiered
- Bloom filters for read optimization
- Write amplification and space amplification

### B+ Tree Implementation
- Balanced tree structure for read optimization
- Page-based storage and buffer management
- Leaf node chaining for range queries
- Index organization and clustering

### Write-Ahead Logging
- WAL purpose and durability guarantees
- Log sequence numbers (LSN) and checkpointing
- Recovery process and crash consistency
- Performance implications and optimization

### Multi-Version Concurrency Control
- Version chains and tuple visibility
- Snapshot isolation implementation
- Garbage collection of old versions
- Read/write conflict resolution

### Buffer Management
- LRU page replacement algorithm
- Clock algorithm variations
- Dirty page flushing and write-back policies
- Buffer pool sizing and monitoring

### Storage Formats
- Row-based storage: OLTP optimization
- Columnar storage: analytical query performance
- PAX (Partition Attributes Across): hybrid approach
- Compression techniques: dictionary, run-length, delta encoding

## Time-Series & Analytical Systems

### Time-Series Databases
- InfluxDB data model and InfluxQL
- TimescaleDB PostgreSQL extension
- Retention policies and data lifecycle
- Continuous queries and aggregations

### Data Compression
- Delta encoding for numerical sequences
- Run-length encoding for repeated values
- Dictionary compression for categorical data
- Time-series specific compression algorithms

### Downsampling Techniques
- Aggregation functions (avg, min, max, percentile)
- Retention policy automation
- Hierarchical storage management
- Query optimization for compressed data

### Analytical Databases
- ClickHouse columnar storage and vectorized execution
- BigQuery serverless analytical processing
- Snowflake multi-cluster architecture
- Performance optimization techniques

### OLAP vs OLTP
- Workload characteristics and requirements
- Schema design differences (star, snowflake)
- Indexing strategies and query patterns
- Scalability and performance considerations

### Data Warehousing
- Star schema: fact tables and dimension tables
- Snowflake schema: normalized dimensions
- Slowly changing dimensions (SCD) handling
- ETL/ELT pipeline design

## Advanced Database Topics

### CAP vs PACELC
- CAP theorem limitations and extensions
- PACELC: choosing between latency and consistency
- Real-world system design implications
- Trade-off analysis and decision frameworks

### HTAP Systems
- Hybrid transactional/analytical processing
- Real-time analytics on transactional data
- TiDB and other HTAP implementations
- Use cases and performance characteristics

### Lakehouse Architecture
- Data lake flexibility with data warehouse performance
- Delta Lake, Apache Hudi, Apache Iceberg
- Unified batch and streaming analytics
- Schema enforcement and data quality

### Database as a Service
- Managed database offerings (RDS, Cloud SQL, Cosmos DB)
- Serverless databases and auto-scaling
- Multi-region deployment and failover
- Cost optimization and resource management

### Multi-Model Databases
- Single database supporting multiple data models
- ArangoDB, OrientDB, Couchbase implementations
- Use case consolidation and complexity reduction
- Migration and adoption strategies

### Emerging Technologies
- Blockchain databases and distributed ledgers
- Quantum-resistant cryptographic databases
- Vector databases for AI/ML workloads
- Edge databases for IoT and mobile applications

## Related Concepts

### Prerequisites
- [Data Structures & Algorithms](../../01-foundations/data-structures-algorithms/README.md)
- [System Design](../../architecture-testing/system-design/README.md)

### Next Level Topics
- [Data Engineering](../../06-data-engineering/README.md)
- [Distributed Systems](../../architecture-testing/sre-reliability/README.md)
- [Performance Engineering](../../08-performance-engineering/README.md)

### Complementary Skills
- [Backend Frameworks](backend-frameworks/README.md)
- [API Design](api-design/README.md)
- [DevOps & Cloud](../../05-devops-cloud/README.md)

## Resources

### Books
- **Designing Data-Intensive Applications** by Martin Kleppmann
  \$49.99, 576 pages, O'Reilly - Comprehensive guide to data systems and trade-offs
- **Database Internals** by Alex Petrov
  \$59.99, 376 pages, O'Reilly - Deep dive into storage engines and distributed systems
- **Seven Databases in Seven Weeks (2nd Edition)** by Luc Perkins et al.
  \$39.99, 432 pages, Pragmatic Bookshelf - Practical introduction to multiple database types

### Courses
- **Database Systems** - Stanford University (free CS145)
  Free, comprehensive - Relational database theory and design
- **Distributed Systems** - MIT 6.824 (free)
  Free, advanced - Distributed database concepts and algorithms
- **MongoDB University** - university.mongodb.com
  Free, practical - Document database design and operations

### Documentation
- **PostgreSQL Documentation** - postgresql.org/docs
  Free, comprehensive - Official PostgreSQL reference and tutorials
- **Redis Documentation** - redis.io/documentation
  Free, detailed - In-memory database patterns and commands
- **Cassandra Documentation** - cassandra.apache.org/doc
  Free, extensive - Distributed database operations and best practices

### Tools
- **pgAdmin** - pgadmin.org
  Free - PostgreSQL administration and development
- **MongoDB Compass** - mongodb.com/products/compass
  Free - GUI for MongoDB development and analysis
- **RedisInsight** - redis.com/redis-enterprise/redis-insight
  Free - Redis GUI for development and monitoring

## Assessment Criteria

### Relational Design
- ✅ Design normalized database schemas with proper relationships
- ✅ Implement appropriate indexing strategies for query performance
- ✅ Apply transaction isolation levels correctly
- ✅ Optimize queries using execution plan analysis

### NoSQL Selection
- ✅ Choose appropriate NoSQL databases for specific use cases
- ✅ Understand CAP theorem trade-offs and BASE properties
- ✅ Design data models for different NoSQL families
- ✅ Implement polyglot persistence patterns

### Distributed Systems
- ✅ Design sharding strategies for horizontal scaling
- ✅ Implement replication patterns with consistency guarantees
- ✅ Apply consensus algorithms in distributed environments
- ✅ Handle distributed transactions and conflict resolution

### Caching & Performance
- ✅ Implement various caching patterns and strategies
- ✅ Configure Redis data structures for different use cases
- ✅ Apply cache invalidation techniques appropriately
- ✅ Optimize for cache performance and memory usage

### Storage & Analytics
- ✅ Understand storage engine internals (LSM, B-tree)
- ✅ Design time-series data models and retention policies
- ✅ Implement analytical database patterns and optimizations
- ✅ Apply compression and downsampling techniques

### Career Readiness Indicators
- **Database Administrator**: Design and optimize relational databases
- **Data Engineer**: Build data pipelines and analytical systems
- **Backend Engineer**: Choose and implement appropriate storage solutions
- **System Architect**: Design distributed database architectures
- **Performance Engineer**: Optimize database systems for scale and efficiency
