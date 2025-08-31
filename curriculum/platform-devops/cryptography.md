[← Back to Curriculum](../README.md)

---

# Cryptography & PKI

- **Cryptographic Primitives & Algorithms**

  - Symmetric encryption: AES modes (GCM, CBC, CTR), ChaCha20-Poly1305, key sizes
  - Asymmetric encryption: RSA, ECC curves (P-256, P-384, P-521), key generation
  - Hash functions: SHA-256, SHA-3, BLAKE2, collision resistance, preimage resistance
  - Message authentication: HMAC, GMAC, authenticated encryption, tag verification
  - Key derivation: HKDF, PBKDF2, scrypt, Argon2, salt generation, iteration tuning
  - Random number generation: CSPRNG, entropy sources, seeding, testing
  - Cryptographic protocols: TLS, SSH, IPSec, protocol analysis, implementation flaws

- **Public Key Infrastructure**

  - Certificate authorities: root CA, intermediate CA, certificate chains, trust stores
  - X.509 certificates: structure, extensions, validation, revocation (CRL, OCSP)
  - Certificate lifecycle: issuance, renewal, revocation, key escrow, backup
  - PKI deployment: enterprise PKI, web PKI, code signing, email encryption
  - Trust models: hierarchical, web of trust, TOFU, certificate transparency
  - Key management: generation, storage, distribution, rotation, destruction
  - HSM integration: hardware security modules, key protection, performance

- **Hardware Security & Trusted Execution**

  - Trusted Execution Environments: Intel SGX, AMD SEV, ARM TrustZone, isolation
  - Intel TDX: trust domains, memory encryption, attestation, migration
  - AMD SEV-SNP: secure nested paging, attestation, memory integrity
  - AWS Nitro Enclaves: isolated compute, attestation, cryptographic processing
  - vTPM: virtual trusted platform module, measured boot, attestation
  - Secure boot: boot chain verification, signed bootloaders, UEFI security
  - Hardware root of trust: TPM, HSM, secure elements, key provisioning

- **Remote Attestation & Confidential Computing**

  - Attestation protocols: challenge-response, quote generation, verification
  - Key release policies: conditional key access, policy enforcement, audit trails
  - Confidential containers: encrypted memory, runtime protection, orchestration
  - Kubernetes confidential workloads: pod security, encrypted communication
  - Encrypted memory pages: page-level encryption, memory isolation, performance
  - Secure multi-party computation: privacy-preserving computation, protocols
  - Homomorphic encryption: computation on encrypted data, practical applications

- **Code Signing & Software Integrity**

  - Cosign: keyless signing, transparency logs, policy enforcement, verification
  - Sigstore ecosystem: Fulcio CA, Rekor transparency log, policy controller
  - Measured boot: boot component measurement, PCR extension, attestation
  - Secure boot chains: bootloader signing, kernel verification, module signing
  - Software attestation: build provenance, supply chain verification, SLSA
  - Binary transparency: verifiable builds, reproducible builds, audit trails
  - Update mechanisms: secure updates, rollback protection, integrity verification

- **Post-Quantum Cryptography**
  - Quantum threat: Shor's algorithm, Grover's algorithm, timeline estimates
  - NIST standardization: Kyber, Dilithium, SPHINCS+, algorithm selection
  - Migration strategies: hybrid approaches, crypto-agility, risk assessment
  - Implementation challenges: performance, key sizes, interoperability
  - Protocol updates: TLS 1.3, SSH, IPSec, backward compatibility
  - Risk assessment: current vs future threats, migration timeline, priorities
  - Testing and validation: algorithm testing, implementation verification
