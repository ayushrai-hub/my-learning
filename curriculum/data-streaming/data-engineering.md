[← Back to Curriculum](../README.md)

---

# Data Engineering & ETL

- **Workflow Orchestration & Pipeline Management**

  - Apache Airflow: DAG design, operators, sensors, hooks, XComs, task dependencies
  - Prefect: flows, tasks, parameters, caching, retries, notifications, cloud deployment
  - Dagster: assets, ops, graphs, resources, I/O managers, data lineage, testing
  - Pipeline design: idempotency, error handling, monitoring, alerting, recovery
  - Scheduling: cron expressions, event-driven triggers, dependencies, backfill
  - Resource management: compute allocation, memory optimization, parallel execution
  - Testing: unit tests, integration tests, data quality tests, pipeline validation

- **Data Loading & Change Data Capture**

  - Incremental loading: timestamp-based, log-based, merge strategies, upserts
  - Full loads: bulk loading, parallel processing, performance optimization, validation
  - Change Data Capture: Debezium, database logs, event sourcing, real-time sync
  - Data synchronization: source-to-target, conflict resolution, consistency models
  - Error handling: dead letter queues, retry mechanisms, data validation, alerts
  - Performance optimization: partitioning, indexing, compression, parallel processing
  - Data quality: validation rules, profiling, monitoring, anomaly detection

- **Stream Processing & Real-Time Analytics**

  - Apache Kafka: event streaming, partitioning, replication, consumer groups
  - Apache Flink: stream processing, stateful computations, windowing, watermarks
  - Spark Structured Streaming: micro-batches, continuous processing, checkpointing
  - Real-time aggregations: windowing, tumbling, sliding, session windows
  - Stream joins: window joins, stream-table joins, temporal joins, performance
  - Backpressure handling: flow control, buffering, scaling, monitoring
  - Exactly-once processing: idempotency, transactional guarantees, fault tolerance

- **Data Lake & Lakehouse Architecture**

  - Lake-house formats: Apache Iceberg, Delta Lake, Apache Hudi, ACID transactions
  - Schema evolution: backward compatibility, forward compatibility, migration strategies
  - Time travel: versioning, rollback, audit trails, compliance requirements
  - Partitioning strategies: time-based, hash-based, range-based, performance optimization
  - Compaction: file optimization, small file problems, maintenance procedures
  - Metadata management: catalogs, lineage, discovery, governance, security
  - Query optimization: predicate pushdown, column pruning, vectorization, caching

- **Data Contracts & Quality Management**

  - Schema registry: Confluent Schema Registry, Apache Avro, Protobuf, JSON Schema
  - Data contracts: API specifications, SLAs, expectations, validation rules
  - Data quality KPIs: completeness, accuracy, consistency, timeliness, validity
  - Quality monitoring: profiling, anomaly detection, drift detection, alerting
  - Data lineage: end-to-end tracking, impact analysis, compliance, debugging
  - Governance: data ownership, access control, privacy, compliance, audit trails
  - Testing: data validation, schema testing, integration testing, regression testing

- **Model Serving & MLOps Integration**

  - BentoML: model packaging, serving, deployment, scaling, monitoring
  - KServe: Kubernetes-native serving, multi-framework support, auto-scaling
  - Model deployment: containerization, versioning, A/B testing, canary releases
  - Inference pipelines: preprocessing, postprocessing, feature engineering, validation
  - Performance optimization: batching, caching, hardware acceleration, scaling
  - Monitoring: model performance, data drift, latency, throughput, error rates
  - MLOps workflows: CI/CD, automated testing, deployment automation, rollback

- **Infrastructure as Code for Data Stacks**
  - Terraform: resource provisioning, state management, modules, workspaces
  - Cloud formation: AWS infrastructure, templates, stacks, drift detection
  - Kubernetes: container orchestration, operators, custom resources, scaling
  - Data platform components: databases, message queues, compute engines, storage
  - Environment management: development, staging, production, configuration management
  - Cost optimization: resource sizing, scheduling, spot instances, reserved capacity
  - Security: access control, encryption, network security, compliance, audit logging
