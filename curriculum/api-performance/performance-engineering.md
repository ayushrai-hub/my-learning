[← Back to Curriculum](../README.md)

---

# Performance Engineering & Optimization

- **Performance Profiling & Analysis**

  - CPU profiling: sampling profilers, instrumentation, flame graphs, call stacks
  - Memory profiling: heap analysis, leak detection, allocation patterns, garbage collection
  - I/O profiling: disk I/O, network I/O, file system performance, async I/O patterns
  - Lock contention: deadlock detection, lock-free algorithms, atomic operations
  - Performance tools: perf, valgrind, Intel VTune, JProfiler, py-spy, pprof
  - Continuous profiling: production profiling, overhead minimization, data collection
  - Performance regression detection: benchmarking, statistical analysis, alerting

- **CPU & Memory Optimization**

  - Cache optimization: CPU cache hierarchy, cache-friendly algorithms, data locality
  - SIMD vectorization: SSE, AVX, auto-vectorization, manual optimization
  - Branch prediction: branch-free code, lookup tables, conditional moves
  - Memory management: pool allocation, stack vs heap, memory alignment, prefetching
  - Garbage collection tuning: generational GC, concurrent GC, low-latency collectors
  - Compiler optimizations: inlining, loop unrolling, dead code elimination, PGO
  - Architecture-specific: ARM vs x86, NUMA awareness, CPU affinity, power management

- **Concurrency & Parallelism**

  - Thread pool management: sizing, work stealing, task scheduling, load balancing
  - Lock-free programming: atomic operations, memory ordering, ABA problem, hazard pointers
  - Async programming: event loops, coroutines, futures, callback hell, structured concurrency
  - Parallel algorithms: map-reduce, fork-join, parallel collections, work distribution
  - GPU computing: CUDA, OpenCL, compute shaders, memory hierarchy, kernel optimization
  - Distributed computing: message passing, shared nothing, data parallelism, fault tolerance
  - Performance modeling: Amdahl's law, Gustafson's law, scalability analysis, bottleneck identification

- **Database Performance Optimization**

  - Query optimization: execution plans, index usage, join algorithms, statistics
  - Index design: B-tree, hash, bitmap, partial, covering indexes, maintenance overhead
  - Connection pooling: pool sizing, connection lifecycle, prepared statements, caching
  - Caching strategies: query result caching, object caching, distributed caching, invalidation
  - Partitioning: horizontal, vertical, functional, sharding strategies, cross-shard queries
  - Replication: master-slave, master-master, read replicas, consistency guarantees
  - Storage optimization: compression, columnar storage, SSD vs HDD, I/O patterns

- **Network & I/O Performance**

  - Network optimization: TCP tuning, connection pooling, keep-alive, compression
  - HTTP performance: HTTP/2, HTTP/3, multiplexing, server push, caching headers
  - CDN optimization: edge caching, geographic distribution, cache invalidation, origin shielding
  - File system performance: I/O schedulers, file system choice, mount options, RAID
  - Async I/O: epoll, kqueue, io_uring, non-blocking I/O, event-driven architecture
  - Serialization: binary vs text, schema evolution, compression, zero-copy techniques
  - Load balancing: algorithms, health checks, session affinity, geographic routing

- **Load Testing & Capacity Planning**

  - Load testing tools: wrk, k6, JMeter, Locust, Artillery, cloud-based solutions
  - Test scenarios: ramp-up, steady state, spike testing, soak testing, stress testing
  - Metrics collection: throughput, latency percentiles, error rates, resource utilization
  - Bottleneck identification: profiling under load, resource saturation, queue theory
  - Capacity modeling: Little's law, queuing theory, performance prediction, scaling laws
  - Production load testing: canary testing, shadow traffic, synthetic monitoring
  - Performance budgets: SLA definition, performance regression detection, CI integration

- **Performance Monitoring & Observability**
  - APM tools: New Relic, Datadog, AppDynamics, distributed tracing integration
  - Real User Monitoring: browser performance, mobile app performance, user experience metrics
  - Synthetic monitoring: uptime checks, performance tests, multi-location monitoring
  - Performance dashboards: key metrics, alerting, trend analysis, capacity planning
  - Log analysis: performance logs, slow query logs, error correlation, pattern detection
  - Alerting: threshold-based, anomaly detection, escalation policies, noise reduction
  - Performance culture: performance reviews, optimization sprints, knowledge sharing
