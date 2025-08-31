[← Back to Curriculum](../README.md)

---

# Production Debugging & eBPF

- **eBPF Fundamentals & Architecture**

  - eBPF virtual machine: bytecode, verifier, JIT compilation, safety guarantees
  - Program types: kprobes, uprobes, tracepoints, XDP, socket filters, cgroup programs
  - Maps: hash maps, arrays, ring buffers, per-CPU maps, LRU maps, data sharing
  - Helper functions: kernel API access, map operations, packet manipulation, time functions
  - Program lifecycle: loading, verification, attachment, execution, unloading
  - Security model: privilege requirements, verifier constraints, capability checks
  - Performance considerations: overhead, context switching, memory usage, scalability

- **Dynamic Tracing & Instrumentation**

  - Kprobes: kernel function tracing, entry/exit points, argument capture, return values
  - Uprobes: userspace function tracing, library calls, application instrumentation
  - Tracepoints: static kernel instrumentation, stable ABI, event categories
  - USDT probes: userspace static tracing, application-defined probe points
  - Function graph tracing: call graphs, execution flow, performance analysis
  - Dynamic instrumentation: runtime patching, hot code paths, minimal overhead
  - Probe management: attachment strategies, filtering, aggregation, data collection

- **System Observability & Monitoring**

  - bcc toolkit: ready-made tools, Python bindings, rapid prototyping, examples
  - bpftrace: high-level language, one-liners, scripting, awk-like syntax
  - Performance monitoring: CPU usage, memory allocation, I/O patterns, network traffic
  - Security monitoring: system calls, file access, network connections, privilege escalation
  - Application tracing: function calls, latency measurement, error tracking, resource usage
  - Container monitoring: cgroup integration, namespace awareness, multi-tenant environments
  - Custom metrics: business logic tracing, KPI monitoring, real-time dashboards

- **Production Debugging Techniques**

  - Live debugging: production systems, minimal impact, safety considerations
  - Core dump analysis: crash investigation, memory forensics, debugging symbols
  - Heap analysis: memory leaks, allocation patterns, object lifecycle, reference tracking
  - Stack trace analysis: call paths, error propagation, performance bottlenecks
  - Log correlation: distributed tracing, request IDs, timeline reconstruction
  - Performance regression: before/after comparison, bisection, root cause analysis
  - Incident response: debugging workflows, escalation procedures, knowledge capture

- **Advanced Debugging & Profiling**

  - Continuous profiling: always-on profiling, production overhead, data retention
  - Flame graphs: visualization, interpretation, optimization opportunities, tooling
  - Off-CPU analysis: blocking operations, I/O wait, lock contention, scheduler delays
  - Memory profiling: allocation tracking, leak detection, fragmentation analysis
  - Network debugging: packet capture, connection tracking, latency analysis
  - Distributed debugging: cross-service tracing, correlation, causality tracking
  - Automated debugging: anomaly detection, root cause analysis, self-healing systems

- **Debugging Tools & Ecosystem**

  - GDB integration: eBPF program debugging, kernel debugging, userspace debugging
  - Perf integration: hardware counters, sampling, call graphs, annotation
  - Ftrace integration: kernel tracing, function graphs, event correlation
  - Systemd integration: service monitoring, journal correlation, resource tracking
  - Container debugging: Docker, Kubernetes, runtime integration, isolation challenges
  - Cloud debugging: managed services, remote debugging, distributed systems
  - IDE integration: development workflows, testing, deployment, monitoring

- **Security & Compliance Considerations**
  - Privilege management: CAP_BPF, CAP_SYS_ADMIN, unprivileged eBPF, security policies
  - Data privacy: sensitive data handling, anonymization, compliance requirements
  - Audit trails: debugging activities, access logs, change tracking, compliance reporting
  - Production safety: testing procedures, rollback plans, impact assessment
  - Performance impact: overhead measurement, SLA compliance, resource limits
  - Vulnerability management: eBPF security, kernel updates, patch management
  - Incident documentation: debugging procedures, lessons learned, knowledge base
