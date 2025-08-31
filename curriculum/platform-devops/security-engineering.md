[← Back to Curriculum](../README.md)

---

# Security & Compliance

- **Threat Modeling & Risk Assessment**

  - STRIDE methodology: Spoofing, Tampering, Repudiation, Information disclosure, DoS, Elevation
  - OWASP Top-10: injection, broken authentication, sensitive data exposure, XXE, broken access control
  - CWE classification: common weakness enumeration, vulnerability categories
  - Attack surface analysis: entry points, data flows, trust boundaries
  - Risk assessment: likelihood, impact, risk matrix, mitigation strategies
  - Security architecture review: design patterns, security controls, defense in depth
  - Compliance frameworks: SOC 2, ISO 27001, NIST, GDPR, HIPAA requirements

- **Secrets Management & Cryptography**

  - HashiCorp Vault: secret engines, authentication methods, policies, audit logging
  - Cloud KMS: key management, encryption at rest, key rotation, access controls
  - SOPS: encrypted configuration files, key management, GitOps integration
  - Secret rotation: automated rotation, zero-downtime updates, monitoring
  - Key derivation: PBKDF2, scrypt, Argon2, salt generation, iteration counts
  - Symmetric encryption: AES, ChaCha20, block modes, padding, IV generation
  - Asymmetric encryption: RSA, ECC, key exchange, digital signatures, PKI

- **Identity & Access Management**

  - OAuth2 flows: authorization code, implicit, client credentials, device flow
  - OpenID Connect: identity tokens, userinfo endpoint, discovery, claims
  - JWT security: signing algorithms, key management, token validation, expiration
  - mTLS: mutual authentication, certificate management, client certificates
  - SPIFFE/SPIRE: workload identity, attestation, federation, trust domains
  - Zero-trust architecture: never trust, always verify, least privilege access
  - Identity federation: SAML, OIDC, cross-domain authentication, SSO

- **Web Application Security**

  - CORS: origin validation, preflight requests, credential handling, security implications
  - Content Security Policy: directive types, nonce, hash, reporting, bypass prevention
  - CSRF protection: tokens, SameSite cookies, double-submit cookies, origin validation
  - Click-jacking: X-Frame-Options, CSP frame-ancestors, UI redressing attacks
  - Input validation: sanitization, encoding, parameterized queries, type checking
  - Session management: secure cookies, session fixation, timeout, invalidation
  - Security headers: HSTS, X-Content-Type-Options, X-XSS-Protection, Referrer-Policy

- **Static & Dynamic Analysis**

  - SAST tools: SonarQube, Checkmarx, Veracode, CodeQL, custom rules
  - DAST tools: OWASP ZAP, Burp Suite, Nessus, automated scanning, false positives
  - Container scanning: Trivy, Clair, Anchore, vulnerability databases, base image security
  - Dependency scanning: Snyk, OWASP Dependency Check, license compliance, supply chain
  - Code review: security-focused reviews, automated checks, training, guidelines
  - Penetration testing: methodology, scope, reporting, remediation verification
  - Bug bounty programs: scope definition, reward structure, disclosure policies

- **Supply Chain Security**

  - SBOM generation: software bill of materials, formats (SPDX, CycloneDX), tooling
  - Sigstore: keyless signing, transparency logs, verification, Cosign integration
  - in-toto: supply chain metadata, attestations, layout policies, verification
  - Provenance: build attestations, source code integrity, reproducible builds
  - Dependency management: pinning, vulnerability scanning, license compliance
  - Container security: base image selection, minimal images, runtime protection
  - CI/CD security: pipeline security, secret management, artifact integrity

- **Compliance & Governance**
  - Regulatory compliance: GDPR, CCPA, HIPAA, PCI-DSS, SOX requirements
  - Data classification: sensitivity levels, handling requirements, retention policies
  - Privacy by design: data minimization, purpose limitation, consent management
  - Audit logging: security events, access logs, integrity protection, retention
  - Incident response: detection, containment, eradication, recovery, lessons learned
  - Security training: awareness programs, secure coding, phishing simulation
  - Policy management: security policies, procedures, standards, enforcement
