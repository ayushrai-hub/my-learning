# 💻 Operating Systems & System Programming

## Executive Summary
Operating systems form the foundation of all computing systems, providing essential abstractions for process management, memory allocation, I/O operations, and network communication. This curriculum covers system-level programming concepts, concurrency patterns, networking protocols, and distributed system primitives essential for building scalable, reliable software systems.

## Core Concepts
System programming requires understanding:
- **Process Management**: Lifecycle, scheduling, synchronization, threading models
- **Memory Systems**: Virtual memory, paging, allocation strategies, caching hierarchy
- **I/O Operations**: Blocking/non-blocking models, multiplexing, asynchronous patterns
- **Network Programming**: Protocols, sockets, load balancing, service discovery
- **Concurrency**: Synchronization primitives, lock-free programming, parallel execution
- **System Architecture**: NUMA, cache coherence, performance optimization

### Why This Matters (2024 Perspective)
System-level knowledge is critical for modern development:
- 80% of performance issues stem from poor system understanding (industry reports)
- Concurrent programming skills command 40% salary premium
- Network programming expertise essential for microservices (85% adoption)
- System-level debugging prevents 60% of production outages

## Prerequisites
- Basic programming concepts (variables, functions, control flow)
- Understanding of computer organization (CPU, memory, I/O)
- Familiarity with C or systems programming languages
- Basic networking concepts (IP, TCP/UDP, HTTP)

## Learning Objectives
- [ ] Understand process lifecycle and thread management
- [ ] Master memory management and virtual memory concepts
- [ ] Implement efficient I/O operations and multiplexing
- [ ] Apply network protocols and socket programming
- [ ] Design concurrent systems with proper synchronization
- [ ] Optimize system performance through architectural understanding

## Key Technologies & Tools
| Technology | Version (2024) | Purpose |
|------------|----------------|---------|
| Linux Kernel| 6.6           | Operating system internals and system calls |
| eBPF       | 6.6           | Kernel observability and tracing |
| systemd    | 255           | Service management and process supervision |
| Wireshark  | 4.2           | Network protocol analysis |
| strace     | Latest         | System call tracing and debugging |
| perf       | Latest         | Performance analysis and profiling |

## Process & Thread Management

### Process Lifecycle
- Process creation: fork(), exec(), process spawning patterns
- Execution states: running, ready, blocked, terminated
- Process termination: exit codes, signal handling, cleanup
- Zombie processes: prevention, reaping, parent responsibility
- Process groups and sessions: job control, signal delivery

### Process Scheduling
- Round-robin scheduling: time quantum, context switching
- Priority-based scheduling: dynamic priorities, starvation prevention
- Completely Fair Scheduler (CFS): virtual runtime, red-black trees
- Real-time scheduling: SCHED_FIFO, SCHED_RR, deadline scheduling
- Scheduling policies: nice values, CPU affinity, load balancing

### Thread Models
- User-space threads: lightweight, fast context switching, limitations
- Kernel-space threads: OS scheduling, blocking system calls
- Hybrid threading: N:1, 1:1, M:N models, performance trade-offs
- Thread libraries: POSIX threads (pthreads), C++ threads

### Thread Synchronization
- Mutexes: mutual exclusion, deadlock prevention, priority inheritance
- Semaphores: counting semaphores, binary semaphores, producer-consumer
- Condition variables: wait/signal patterns, spurious wakeups
- Barriers: synchronization points, thread coordination
- Read-write locks: shared/exclusive access, writer preference

### Thread Pools
- Work queue implementation: task submission, worker threads
- Load balancing: task distribution, thread utilization
- Pool sizing: optimal thread count, CPU utilization
- Dynamic scaling: thread creation/destruction, resource management

### Context Switching
- Context switch overhead: register saving, stack management
- CPU registers: general purpose, floating point, SIMD registers
- Stack management: user stack, kernel stack, stack overflow
- Performance impact: cache pollution, TLB invalidation

### NUMA Architecture
- Non-uniform memory access: memory latency variation
- CPU affinity: thread pinning, memory locality optimization
- NUMA-aware allocation: memory placement, interleave policies
- Performance optimization: data placement, thread scheduling

## Memory Management & Virtual Memory

### Virtual Memory Fundamentals
- Address translation: logical to physical address mapping
- Page tables: multi-level translation, TLB optimization
- Memory protection: segmentation faults, access permissions
- Demand paging: page faults, working set management

### Memory Mapping
- mmap() system call: file-backed, anonymous mappings
- Shared memory: inter-process communication, memory regions
- Memory-mapped files: I/O optimization, large file handling
- Anonymous mappings: heap allocation, stack growth

### Paging Systems
- Page replacement algorithms: LRU, LFU, clock algorithm
- Working set model: resident set size, page fault frequency
- Page size selection: 4KB vs 2MB vs 1GB pages
- Transparent huge pages: automatic promotion, fragmentation

### Memory Allocation
- Heap management: malloc/free, memory pools, arena allocation
- Garbage collection: mark-sweep, generational, concurrent GC
- Memory fragmentation: internal/external fragmentation, compaction
- Custom allocators: slab allocation, object pools

### Memory Protection
- Segmentation: logical address spaces, protection rings
- Access control: read/write/execute permissions, guard pages
- Buffer overflow prevention: stack canaries, address randomization
- Memory sanitizers: AddressSanitizer, memory leak detection

### Cache Hierarchy
- CPU cache levels: L1 instruction/data, L2 unified, L3 shared
- Cache coherence: MESI protocol, cache invalidation, memory barriers
- False sharing: cache line contention, padding solutions
- Cache-friendly programming: spatial/temporal locality

## I/O Systems & Multiplexing

### I/O Models
- Blocking I/O: synchronous operations, thread blocking
- Non-blocking I/O: immediate returns, polling loops
- Asynchronous I/O: completion callbacks, overlapped operations
- Signal-driven I/O: signal notification, SIGIO handling

### Select System Call
- File descriptor sets: read, write, exception sets
- Timeout handling: absolute, relative timeouts
- Limitations: FD_SETSIZE limit, linear scanning
- Use cases: simple multiplexing, legacy compatibility

### Epoll (Linux)
- Edge-triggered vs level-triggered modes
- Epoll instance: epoll_create, epoll_ctl, epoll_wait
- Performance characteristics: O(1) operations, event batching
- Kernel optimizations: eventfd, signalfd integration

### Kqueue (BSD)
- Event filters: read, write, signal, timer, user events
- Kevent structure: filter, flags, fflags, data, udata
- Cross-platform considerations: Linux emulation, portability
- Advanced features: vnode monitoring, process events

### Io_uring (Linux)
- Submission queue: IORING_OP_* operations, batch submission
- Completion queue: asynchronous completion, ring buffer
- Zero-copy operations: buffer registration, fixed buffers
- Performance benefits: reduced system calls, kernel bypass

### Reactor Pattern
- Event demultiplexing: single-threaded event loop
- Handler registration: event types, callback functions
- Dispatch mechanism: event type routing, handler invocation
- Scalability considerations: thread pools, worker processes

### Proactor Pattern
- Asynchronous completion: I/O operations initiate completion
- Callback handling: completion events, result processing
- Implementation complexity: state management, error handling
- Performance advantages: overlapped I/O, completion ports

## Network Protocols & Communication

### TCP Fundamentals
- Connection establishment: three-way handshake, sequence numbers
- Flow control: sliding window, receiver advertised window
- Congestion control: slow start, congestion avoidance, fast recovery
- Connection termination: four-way handshake, TIME_WAIT state

### UDP Characteristics
- Connectionless operation: no handshake, no state maintenance
- Unreliable delivery: no acknowledgments, no retransmission
- Broadcast and multicast: one-to-many, many-to-many communication
- Use cases: real-time applications, DNS, VoIP

### QUIC Protocol
- Multiplexing: stream-based, head-of-line blocking elimination
- 0-RTT handshake: reduced connection establishment latency
- Connection migration: IP address changes, network switching
- HTTP/3 foundation: replacement for TCP+TLS in HTTP

### TLS Handshake
- Certificate validation: chain verification, revocation checking
- Cipher suite negotiation: key exchange, encryption, MAC algorithms
- Session resumption: session IDs, session tickets, PSK
- Perfect forward secrecy: ephemeral key exchange

### OCSP Stapling
- Certificate revocation checking: real-time status validation
- Stapling mechanism: server-provided OCSP responses
- Performance optimization: reduced client requests, caching
- Implementation: server configuration, client verification

### Network Performance
- Bandwidth-delay product: BDP calculation, buffer sizing
- Window scaling: TCP window size extension
- Buffer bloat: excessive buffering, latency impact
- TCP optimizations: SACK, timestamps, selective acknowledgments

## DNS & Service Discovery

### DNS Resolution Process
- Recursive resolution: client queries, authoritative servers
- Iterative resolution: NS record following, delegation
- Caching hierarchy: local resolver, ISP DNS, root servers
- TTL management: cache expiration, refresh timing

### DNS Record Types
- A/AAAA records: IPv4/IPv6 address mapping
- CNAME records: canonical name aliases
- MX records: mail server specification
- TXT records: arbitrary text data, SPF/DKIM
- SRV records: service location, priority/weight

### DNSSEC Implementation
- Digital signatures: zone signing, key signing keys
- Chain of trust: root trust anchor, validation process
- NSEC/NSEC3: authenticated denial of existence
- Rolling keys: key management, transition periods

### DNS Privacy
- DNS over HTTPS (DoH): HTTPS tunneling, privacy protection
- DNS over TLS (DoT): TLS encryption, port 853
- Performance implications: latency, caching, compatibility
- Adoption challenges: middlebox interference, firewall blocking

### Service Discovery Mechanisms
- DNS-SD (Service Discovery): service advertising, browsing
- Multicast DNS (mDNS): local network discovery, .local domains
- Service registries: Consul, etcd, ZooKeeper
- API-driven discovery: registration, health checks, lookup

### Load Balancing Strategies
- Round-robin: sequential distribution, equal weighting
- Weighted algorithms: server capacity consideration
- Least connections: current load balancing
- Hash-based: session persistence, cache affinity

## Load Balancing & High Availability

### Layer 4 Load Balancing
- TCP/UDP forwarding: connection-based routing
- Session persistence: source IP affinity, cookie insertion
- SSL termination: certificate management, performance
- Direct Server Return (DSR): return path optimization

### Layer 7 Load Balancing
- HTTP-aware routing: host/path-based routing, header inspection
- Content-based decisions: user agent, geographic location
- Application health: HTTP status code checking
- Advanced features: rate limiting, request transformation

### Load Balancing Algorithms
- Least connections: active connection count balancing
- Response time: latency-based routing decisions
- Hash-based: consistent hashing, cache hit optimization
- Random selection: simple distribution, statistical fairness

### Health Checking Mechanisms
- Active probes: periodic health checks, timeout handling
- Passive monitoring: real traffic analysis, failure detection
- Circuit breakers: failure threshold, recovery attempts
- Graceful degradation: partial failure handling

### Session Affinity
- Sticky sessions: cookie-based persistence, server affinity
- Distributed storage: Redis, database session storage
- Application-level: JWT tokens, client-side state
- Performance trade-offs: load distribution vs consistency

### High Availability Patterns
- Active-passive: standby systems, failover procedures
- Active-active: load sharing, geographic distribution
- Split-brain prevention: quorum systems, fencing
- Multi-region deployment: disaster recovery, latency optimization

## Concurrency Primitives & Lock-Free Programming

### Mutex Implementations
- Futex (Fast Userspace Mutex): userspace locking, kernel fallback
- Adaptive spinning: short wait periods, context switch avoidance
- Priority inheritance: deadlock prevention, real-time systems
- Recursive mutexes: reentrant locking, ownership tracking

### Reader-Writer Locks
- Shared-exclusive access: multiple readers, single writer
- Writer starvation prevention: fairness algorithms
- Implementation variants: write-preferring, read-preferring
- Performance characteristics: contention, throughput

### Compare-and-Swap Operations
- Atomic primitives: load, store, compare-exchange
- ABA problem: tag counters, hazard pointers, solution patterns
- Memory ordering: acquire/release semantics, sequential consistency
- Hardware support: CPU instructions, lock prefixes

### Lock-Free Data Structures
- Lock-free queues: Michael-Scott algorithm, FAA-based counters
- Lock-free stacks: elimination backoff, helping mechanisms
- Lock-free hash tables: resize operations, bucket management
- Performance trade-offs: progress guarantees, complexity

### Memory Barriers
- Acquire semantics: load-acquire, subsequent loads/stores ordering
- Release semantics: store-release, prior loads/stores ordering
- Sequential consistency: total order, expensive but correct
- Compiler barriers: optimization prevention, reordering control

### Atomic Operations
- Load operations: relaxed, acquire, sequentially consistent
- Store operations: relaxed, release, sequentially consistent
- Exchange operations: atomic swap, compare-and-exchange
- Arithmetic operations: fetch-and-add, fetch-and-subtract

### Wait-Free Algorithms
- Progress guarantees: obstruction-free, lock-free, wait-free
- Universal constructions: helping mechanisms, operation linearization
- Complexity analysis: amortized costs, worst-case bounds
- Practical considerations: space overhead, cache efficiency

## Related Concepts

### Prerequisites
- [Programming Fundamentals](../../01-foundations/programming-fundamentals/README.md)
- [Data Structures & Algorithms](../../01-foundations/data-structures-algorithms/README.md)

### Next Level Topics
- [Databases](databases/README.md)
- [Networking](../../data-streaming/streaming-data/README.md)
- [Distributed Systems](../../architecture-testing/sre-reliability/README.md)

### Complementary Skills
- [Backend Frameworks](backend-frameworks/README.md)
- [System Design](../../architecture-testing/system-design/README.md)
- [Performance Engineering](../../08-performance-engineering/README.md)

## Resources

### Books
- **Operating System Concepts (10th Edition)** by Abraham Silberschatz
  \$89.99, 1,056 pages, Wiley - Comprehensive OS theory and practice
- **The Linux Programming Interface** by Michael Kerrisk
  \$79.99, 1,566 pages, No Starch Press - Linux system programming guide
- **Computer Networking: A Top-Down Approach (8th Edition)** by Kurose & Ross
  \$99.99, 864 pages, Pearson - Networking fundamentals and protocols

### Courses
- **MIT 6.828 Operating System Engineering** - MIT (free)
  Free, comprehensive - OS implementation and design
- **Computer Networks** - Stanford CS144 (free)
  Free, practical - Network programming and protocols
- **Linux System Programming** - Pluralsight
  Paid, hands-on - Linux system calls and internals

### Documentation
- **Linux Man Pages** - man7.org/linux/man-pages
  Free, authoritative - System call documentation
- **Beej's Guide to Network Programming** - beej.us/guide/bgnet
  Free, practical - Socket programming tutorial
- **TCP/IP Illustrated** - Online resources
  Free excerpts - TCP/IP protocol implementation

### Tools
- **strace** - strace.io
  Open source - System call tracer and analyzer
- **perf** - perf.wiki.kernel.org
  Open source - Linux performance profiler
- **Wireshark** - wireshark.org
  Open source - Network protocol analyzer

## Assessment Criteria

### Process Management
- ✅ Understand process lifecycle and scheduling algorithms
- ✅ Implement thread synchronization with proper primitives
- ✅ Design thread pools for concurrent workloads
- ✅ Optimize for NUMA architectures and memory locality

### Memory Systems
- ✅ Apply virtual memory concepts and page management
- ✅ Implement memory mapping and protection mechanisms
- ✅ Optimize for cache hierarchy and memory access patterns
- ✅ Profile and debug memory-related performance issues

### I/O Operations
- ✅ Choose appropriate I/O models for different use cases
- ✅ Implement I/O multiplexing with epoll/kqueue
- ✅ Apply reactor and proactor patterns effectively
- ✅ Optimize I/O performance and resource utilization

### Network Programming
- ✅ Implement TCP/UDP socket programming
- ✅ Apply TLS and secure communication patterns
- ✅ Design load balancing and high availability systems
- ✅ Optimize network performance and reliability

### Concurrency
- ✅ Select appropriate synchronization primitives
- ✅ Implement lock-free data structures and algorithms
- ✅ Apply memory barriers and atomic operations correctly
- ✅ Analyze concurrency performance and scalability

### Career Readiness Indicators
- **Systems Programmer**: Implement low-level system interfaces and optimizations
- **Network Engineer**: Design and optimize network communication systems
- **Distributed Systems Engineer**: Build scalable, concurrent applications
- **Performance Engineer**: Profile and optimize system-level bottlenecks
- **DevOps Engineer**: Manage infrastructure with deep system understanding
