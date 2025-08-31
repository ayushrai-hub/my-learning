[← Back to Curriculum](../README.md)

---

# Streaming Data & ML Engineering

- **Apache Kafka & Event Streaming**

  - Kafka architecture: brokers, topics, partitions, replicas, leaders, followers
  - Producer patterns: batching, compression, idempotence, transactional producers
  - Consumer patterns: consumer groups, offset management, rebalancing, backpressure
  - Kafka Connect: source connectors, sink connectors, distributed mode, transforms
  - Schema evolution: Avro, Protobuf, JSON Schema, compatibility types, registry
  - Stream processing: Kafka Streams, KSQL, stateful processing, windowing
  - Operations: monitoring, scaling, replication, disaster recovery, performance tuning

- **Apache Flink & Stream Processing**

  - Flink architecture: JobManager, TaskManager, checkpointing, state backends
  - DataStream API: transformations, windowing, watermarks, event time processing
  - Stateful processing: keyed state, operator state, checkpointing, recovery
  - Windowing: tumbling, sliding, session windows, custom windows, triggers
  - Watermarks: event time, processing time, late data handling, out-of-order events
  - Fault tolerance: exactly-once processing, checkpointing, savepoints, recovery
  - Performance: parallelism, resource allocation, backpressure, optimization

- **Stream Processing Patterns & Architecture**

  - Windowing strategies: time-based, count-based, session-based, custom windows
  - Watermark generation: periodic, punctuated, custom watermark strategies
  - Late data handling: allowed lateness, side outputs, reprocessing strategies
  - Stream joins: window joins, interval joins, temporal joins, performance considerations
  - Aggregations: tumbling aggregations, sliding aggregations, custom aggregators
  - Pattern detection: CEP, FlinkCEP, complex event processing, rule engines
  - Exactly-once semantics: idempotent operations, transactional sinks, end-to-end guarantees

- **MLOps for Streaming Systems**

  - Real-time feature engineering: streaming transformations, feature stores, consistency
  - Online model serving: model deployment, A/B testing, canary releases, rollbacks
  - Stream-based training: online learning, incremental updates, concept drift adaptation
  - Model monitoring: performance metrics, data drift, model drift, alerting
  - Feature drift detection: statistical tests, distribution monitoring, adaptation
  - Streaming ML pipelines: training pipelines, inference pipelines, orchestration
  - Edge deployment: model compression, quantization, edge inference, synchronization

- **Advanced LLM Techniques**

  - Parameter-efficient fine-tuning: LoRA, AdaLoRA, QLoRA, prefix tuning, adapters
  - Model compression: quantization, pruning, distillation, hardware-specific optimization
  - Inference optimization: batching, caching, speculative decoding, parallel sampling
  - Multi-modal models: vision-language models, audio processing, cross-modal understanding
  - Retrieval-augmented generation: context retrieval, knowledge integration, factual accuracy
  - Agent frameworks: tool usage, planning, memory, multi-agent systems
  - Safety measures: content filtering, alignment, red teaming, robustness testing

- **Vector Search & Embeddings**

  - Embedding models: sentence transformers, OpenAI, domain-specific, multilingual
  - Vector databases: architecture, indexing, querying, performance optimization
  - Similarity search: cosine similarity, dot product, Euclidean distance, custom metrics
  - Hybrid search: vector + keyword search, ranking fusion, relevance tuning
  - Semantic search applications: document retrieval, recommendation systems, Q&A
  - Vector operations: clustering, classification, anomaly detection, dimensionality reduction
  - Production considerations: scalability, latency, consistency, cost optimization

- **ML Model Serving & Deployment**
  - Batch inference: scheduled processing, distributed computing, resource optimization
  - Real-time inference: low-latency serving, auto-scaling, load balancing, caching
  - Edge inference: model optimization, hardware constraints, synchronization, updates
  - Multi-model serving: model routing, ensemble methods, A/B testing, canary deployment
  - Performance optimization: model quantization, hardware acceleration, batching
  - Monitoring: latency, throughput, accuracy, resource utilization, cost tracking
  - MLOps integration: CI/CD, automated testing, deployment automation, rollback procedures
