[← Back to Curriculum](../README.md)

---

# Operating Systems, Networking & Concurrency

- **Process & Thread Management**

  - Process lifecycle: creation, execution, termination, zombie processes
  - Process scheduling: round-robin, priority-based, CFS, real-time scheduling
  - Thread models: user-space, kernel-space, hybrid threading
  - Thread synchronization: mutexes, semaphores, condition variables, barriers
  - Thread pools: work queues, task distribution, load balancing
  - Context switching: overhead, CPU registers, stack management
  - NUMA architecture: memory locality, CPU affinity, performance optimization

- **Memory Management & Virtual Memory**

  - Virtual memory: address translation, page tables, TLB optimization
  - Memory mapping: `mmap`, shared memory, memory-mapped files
  - Paging: demand paging, page replacement algorithms, working set
  - Memory allocation: heap management, memory pools, garbage collection
  - Memory protection: segmentation, access control, buffer overflow prevention
  - Cache hierarchy: L1/L2/L3 caches, cache coherence, false sharing
  - Memory profiling: leak detection, fragmentation analysis, allocation patterns

- **I/O Systems & Multiplexing**

  - I/O models: blocking, non-blocking, asynchronous, signal-driven
  - `select`: file descriptor sets, timeout handling, limitations
  - `epoll` (Linux): edge-triggered, level-triggered, performance characteristics
  - `kqueue` (BSD): event filters, kevent structure, cross-platform considerations
  - `io_uring` (Linux): submission/completion queues, zero-copy, performance
  - Reactor pattern: event demultiplexing, handler dispatch
  - Proactor pattern: asynchronous completion, callback handling

- **Network Protocols & Communication**

  - TCP fundamentals: connection establishment, flow control, congestion control
  - UDP characteristics: connectionless, unreliable, broadcast/multicast
  - QUIC protocol: multiplexing, 0-RTT, connection migration, HTTP/3
  - TLS handshake: certificate validation, cipher negotiation, session resumption
  - OCSP stapling: certificate revocation, performance optimization
  - Network performance: bandwidth-delay product, buffer sizing, window scaling
  - Socket programming: bind, listen, accept, connect, send, receive

- **DNS & Service Discovery**

  - DNS resolution: recursive, iterative, caching, TTL management
  - DNS record types: A, AAAA, CNAME, MX, TXT, SRV records
  - DNSSEC: digital signatures, chain of trust, validation process
  - DNS over HTTPS/TLS: privacy, security, performance implications
  - Service discovery: DNS-SD, mDNS, Consul, etcd integration
  - Load balancing: round-robin, weighted, health checks, failover
  - CDN integration: geographic distribution, edge caching, origin shielding

- **Load Balancing & High Availability**

  - Layer 4 load balancing: TCP/UDP, connection-based, session persistence
  - Layer 7 load balancing: HTTP, application-aware, content-based routing
  - Load balancing algorithms: least connections, response time, hash-based
  - Health checking: active, passive, circuit breakers, graceful degradation
  - Session affinity: sticky sessions, distributed session storage
  - High availability: active-passive, active-active, split-brain prevention
  - Failover mechanisms: automatic detection, recovery procedures, monitoring

- **Concurrency Primitives & Lock-Free Programming**
  - Mutex implementations: futex, adaptive spinning, priority inheritance
  - Reader-writer locks: shared-exclusive access, writer starvation prevention
  - Compare-and-swap: atomic operations, ABA problem, memory ordering
  - Lock-free data structures: queues, stacks, hash tables, performance trade-offs
  - Memory barriers: acquire-release semantics, sequential consistency
  - Atomic operations: load, store, exchange, fetch-and-add operations
  - Wait-free algorithms: progress guarantees, helping mechanisms, complexity
- Processes, threads, schedulers, NUMA
- Virtual memory, `mmap`, paging
- I/O multiplexing (`select`, `epoll`, `kqueue`, `io_uring`)
- TCP/UDP, QUIC & HTTP/3; TLS handshake, OCSP stapling
- DNS resolution & DNSSEC; L4/L7 load-balancers
- Concurrency primitives (mutex, RW-lock, CAS, lock-free queues)
