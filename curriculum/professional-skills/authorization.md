[← Back to Curriculum](../README.md)

---

# Authorization & Policy-as-Code

- **Access Control Models**

  - RBAC: role-based access control, roles, permissions, hierarchies, inheritance
  - ABAC: attribute-based access control, policies, attributes, dynamic evaluation
  - ReBAC: relationship-based access control, Google Zanzibar model, graph-based
  - Policy languages: XACML, Rego, Cedar, JSON-based policies, domain-specific languages
  - Fine-grained permissions: resource-level, field-level, operation-level access control
  - Temporal access: time-based policies, expiration, conditional access, context-aware
  - Multi-tenancy: tenant isolation, shared policies, tenant-specific customization

- **Policy Engines & Frameworks**

  - Open Policy Agent (OPA): Rego language, policy evaluation, decision caching
  - Cedar: Amazon's policy language, human-readable, formal verification, performance
  - Casbin: access control library, model configuration, policy storage, adapters
  - Policy lifecycle: authoring, testing, validation, deployment, monitoring, auditing
  - Policy testing: unit tests, integration tests, policy simulation, coverage analysis
  - Policy versioning: schema evolution, backward compatibility, migration strategies
  - Performance optimization: policy compilation, caching, distributed evaluation

- **Implementation Patterns**
  - Sidecar pattern: Envoy ext-authz, service mesh integration, policy enforcement points
  - Gateway enforcement: API gateway policies, rate limiting, authentication, authorization
  - Application-level: embedded policy engines, SDK integration, local evaluation
  - Webhook enforcement: external policy services, HTTP-based evaluation, scalability
  - Database-level: row-level security, column-level security, query rewriting
  - Infrastructure policies: Kubernetes admission controllers, cloud resource policies
  - CI/CD policies: deployment gates, security scanning, compliance validation
