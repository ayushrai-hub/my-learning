[← Back to Curriculum](../README.md)

---

# Chaos Engineering & Game Days

- **Chaos Engineering Principles**

  - Steady-state hypothesis: normal behavior definition, baseline metrics, success criteria
  - Real-world events: network failures, hardware failures, software bugs, human errors
  - Experimentation: controlled experiments, hypothesis testing, statistical analysis
  - Minimize blast radius: gradual rollout, safety mechanisms, abort conditions
  - Automation: chaos tools, scheduled experiments, continuous chaos, feedback loops
  - Learning culture: failure as learning, blameless post-mortems, knowledge sharing
  - Business alignment: risk tolerance, customer impact, business continuity

- **Failure Injection Techniques**

  - Network failures: latency injection, packet loss, network partitions, DNS failures
  - Resource exhaustion: CPU stress, memory pressure, disk space, file descriptors
  - Service failures: process termination, dependency failures, timeout injection
  - Infrastructure failures: instance termination, AZ failures, region outages
  - Application failures: exception injection, state corruption, race conditions
  - Security failures: certificate expiration, authentication failures, authorization bypass
  - Data failures: data corruption, replication lag, consistency violations

- **Chaos Engineering Tools**
  - Chaos Monkey: instance termination, random failures, Netflix OSS, cloud integration
  - Litmus: Kubernetes chaos, workflow orchestration, community experiments
  - Gremlin: failure as a service, comprehensive failure modes, enterprise features
  - Chaos Toolkit: open source, extensible, experiment definition, automation
  - Pumba: Docker chaos, container failures, network chaos, resource stress
  - PowerfulSeal: Kubernetes chaos, policy-driven, safety mechanisms, reporting
  - Custom tools: organization-specific, integration requirements, specialized failures
