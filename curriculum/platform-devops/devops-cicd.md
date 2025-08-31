[← Back to Curriculum](../README.md)

---

# DevOps & Infrastructure-as-Code

- **Container Orchestration Strategies**

  - Docker Compose: multi-service applications, development environments
  - Docker Swarm: native clustering, service discovery, load balancing
  - Stack deployment: compose files, secrets management, rolling updates
  - Service mesh integration: traffic management, security, observability
  - Container registry: private registries, image scanning, vulnerability management
  - Multi-environment deployment: development, staging, production parity
  - Migration strategies: lift-and-shift, containerization, modernization

- **Terraform & Infrastructure Management**

  - HCL syntax: resources, data sources, variables, outputs, functions
  - State management: remote backends, state locking, collaboration
  - Modules: reusability, versioning, composition, testing
  - Providers: AWS, Azure, GCP, Kubernetes, third-party integrations
  - Drift detection: plan analysis, state reconciliation, compliance
  - Workspace management: environment separation, variable scoping
  - Advanced patterns: for_each, count, dynamic blocks, conditional logic

- **Helm Templating & Release Management**

  - Chart structure: templates, values, dependencies, hooks
  - Templating: Go templates, functions, conditionals, loops
  - Values hierarchy: default, environment-specific, command-line overrides
  - Chart dependencies: subcharts, requirements, version management
  - Semantic releases: versioning, changelog generation, automation
  - Testing: chart testing, validation, lint checking
  - Security: signing, verification, RBAC integration

- **GitOps & Continuous Deployment**

  - Argo CD: application definitions, sync policies, health checks
  - Flux: GitOps toolkit, source controller, kustomize controller
  - Git workflows: branching strategies, pull requests, approval processes
  - Declarative configuration: desired state, drift detection, reconciliation
  - Multi-cluster deployment: cluster management, federation, policies
  - Progressive delivery: canary deployments, blue-green, feature flags
  - Rollback strategies: automatic rollback, manual intervention, testing

- **Artifact Management & Promotion**

  - Immutable artifacts: container images, Helm charts, binary packages
  - Artifact repositories: Harbor, Nexus, Artifactory, cloud registries
  - Promotion pipelines: environment progression, approval gates, testing
  - Vulnerability scanning: image scanning, dependency analysis, compliance
  - Signing and verification: Cosign, Notary, supply chain security
  - Retention policies: cleanup, storage optimization, compliance
  - Multi-region replication: disaster recovery, performance optimization

- **Serverless & Function-as-a-Service**

  - Serverless platforms: AWS Lambda, Azure Functions, Google Cloud Functions
  - Event-driven architecture: triggers, event sources, processing patterns
  - Cold start optimization: runtime selection, memory allocation, caching
  - Serverless frameworks: Serverless Framework, SAM, Terraform
  - Cost optimization: right-sizing, scheduling, resource allocation
  - Monitoring: distributed tracing, metrics, logging, alerting
  - Trade-offs: vendor lock-in, latency, scaling limitations, cost models

- **FinOps & Cost Management**
  - Cost visibility: dashboards, reporting, allocation, chargeback
  - Resource optimization: right-sizing, reserved instances, spot instances
  - Cost alerts: budget monitoring, anomaly detection, automated responses
  - Tagging strategies: resource organization, cost allocation, governance
  - Multi-cloud cost management: comparison, optimization, migration
  - Capacity planning: forecasting, growth modeling, budget planning
  - Governance: policies, approval workflows, compliance, auditing
