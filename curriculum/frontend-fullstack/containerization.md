[← Back to Curriculum](../README.md)

---

# Containerization & Orchestration (Docker → Kubernetes)

- **Container Fundamentals & Linux Primitives**

  - Namespaces: PID, network, mount, UTS, IPC, user, cgroup isolation
  - Cgroups: resource limiting, memory, CPU, I/O, device access control
  - Union filesystems: OverlayFS, AUFS, device mapper, layer management
  - OCI specification: image format, runtime spec, distribution spec
  - Container runtimes: runc, crun, gVisor, Firecracker, security models
  - Image layers: layer caching, deduplication, optimization strategies
  - Security: capabilities, seccomp, AppArmor, SELinux, rootless containers

- **Docker Advanced Techniques**

  - Multi-stage builds: build optimization, security, artifact separation
  - BuildKit: parallel builds, cache mounts, secrets, SSH forwarding
  - Distroless images: minimal attack surface, security hardening
  - Image optimization: layer ordering, .dockerignore, multi-arch builds
  - Registry operations: pushing, pulling, manifest inspection, cleanup
  - Docker Compose: service orchestration, networking, volumes, scaling
  - Development workflows: hot reloading, debugging, testing in containers

- **Kubernetes Architecture & Components**

  - Control plane: API server, etcd, scheduler, controller manager
  - Node components: kubelet, kube-proxy, container runtime interface
  - API objects: pods, services, deployments, configmaps, secrets
  - Networking: cluster networking, service discovery, ingress controllers
  - Storage: persistent volumes, storage classes, dynamic provisioning
  - Security: RBAC, pod security standards, network policies
  - High availability: control plane HA, etcd clustering, disaster recovery

- **Workload Management & Deployment Strategies**

  - Deployments: rolling updates, blue-green, canary deployments
  - StatefulSets: ordered deployment, persistent storage, stable networking
  - DaemonSets: node-level services, log collection, monitoring agents
  - Jobs & CronJobs: batch processing, scheduled tasks, cleanup
  - Rollout strategies: maxSurge, maxUnavailable, readiness probes
  - Resource management: requests, limits, quality of service classes
  - Pod disruption budgets: availability guarantees, maintenance windows

- **Package Management & Configuration**

  - Helm charts: templating, values, dependencies, hooks, testing
  - Kustomize: declarative configuration, overlays, patches, transformations
  - Operators: custom resources, controllers, lifecycle management
  - Custom Resource Definitions: API extensions, validation, versioning
  - GitOps: Argo CD, Flux, declarative deployments, drift detection
  - Configuration management: ConfigMaps, Secrets, environment variables
  - Multi-environment deployment: staging, production, feature branches

- **Scaling & Performance**

  - Horizontal Pod Autoscaler: CPU, memory, custom metrics scaling
  - Vertical Pod Autoscaler: right-sizing, resource recommendations
  - Cluster autoscaler: node scaling, cost optimization, multi-zone
  - Performance tuning: resource allocation, node affinity, taints/tolerations
  - Load balancing: service types, ingress, traffic distribution
  - Monitoring: metrics collection, alerting, performance analysis
  - Capacity planning: resource forecasting, cost optimization

- **Networking & Service Mesh**

  - CNI plugins: Calico, Flannel, Weave, Cilium, network policies
  - Ingress controllers: NGINX, Traefik, HAProxy, SSL termination
  - Gateway API: next-generation ingress, traffic management, security
  - Service mesh: Istio, Linkerd, Consul Connect, traffic management
  - Network policies: micro-segmentation, security, compliance
  - DNS: service discovery, external DNS, custom DNS policies
  - Load balancing: session affinity, traffic splitting, health checks

- **Storage & Data Management**

  - Container Storage Interface: volume plugins, dynamic provisioning
  - Storage classes: performance tiers, replication, backup policies
  - Persistent volumes: lifecycle, access modes, reclaim policies
  - Volume snapshots: backup, restore, cloning, disaster recovery
  - StatefulSet storage: ordered provisioning, stable storage, scaling
  - Data protection: backup strategies, disaster recovery, testing
  - Performance: IOPS, throughput, latency optimization

- **Security & Compliance**

  - Pod Security Standards: restricted, baseline, privileged policies
  - RBAC: roles, bindings, service accounts, least privilege
  - Network policies: ingress, egress, namespace isolation
  - Image security: vulnerability scanning, admission controllers
  - Supply chain security: SBOM, SLSA, image signing, provenance
  - Runtime security: falco, threat detection, anomaly detection
  - Compliance: CIS benchmarks, security frameworks, audit logging

- **Troubleshooting & Operations**
  - kubectl debugging: logs, exec, port-forward, proxy commands
  - `kubectl debug`: ephemeral containers, debugging utilities
  - Node problem detector: hardware issues, kernel problems, monitoring
  - Cluster diagnostics: resource usage, network connectivity, DNS resolution
  - Performance analysis: resource utilization, bottleneck identification
  - Log aggregation: centralized logging, log parsing, alerting
  - Incident response: runbooks, escalation procedures, post-mortems
