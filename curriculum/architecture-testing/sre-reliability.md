[← Back to Curriculum](../README.md)

---

# Site Reliability Engineering (Deep Dive)

- **SLI, SLO & Error Budget Management**

  - Service Level Indicators: availability, latency, throughput, error rate, quality metrics
  - Service Level Objectives: target setting, business alignment, user experience focus
  - Error budgets: calculation, burn rate, policy enforcement, trade-off decisions
  - SLO compliance: monitoring, alerting, reporting, continuous improvement
  - Multi-tier SLOs: user-facing, infrastructure, dependency SLOs, cascading effects
  - SLO evolution: refinement, historical analysis, business requirement changes
  - Stakeholder communication: SLO reporting, incident impact, business alignment

- **Reliability Engineering Practices**

  - Fault tolerance: redundancy, graceful degradation, circuit breakers, bulkheads
  - Chaos engineering: failure injection, steady-state hypothesis, blast radius control
  - Capacity planning: growth modeling, resource forecasting, performance testing
  - Change management: deployment practices, rollback procedures, risk assessment
  - Incident management: response procedures, escalation, communication, post-mortems
  - Reliability testing: load testing, chaos testing, disaster recovery testing
  - Automation: toil reduction, self-healing systems, automated remediation

- **Toil Reduction & Automation**

  - Toil identification: manual work, repetitive tasks, no enduring value, reactive work
  - Automation opportunities: cost-benefit analysis, ROI calculation, prioritization
  - Runbook automation: procedure documentation, script development, error handling
  - Self-service platforms: developer tools, infrastructure provisioning, deployment pipelines
  - Monitoring automation: alert tuning, auto-remediation, intelligent routing
  - Capacity automation: auto-scaling, resource optimization, predictive scaling
  - Process improvement: workflow optimization, tool consolidation, knowledge sharing

- **Incident Response & Management**

  - Incident classification: severity levels, impact assessment, escalation criteria
  - Response procedures: incident commander, communication lead, technical lead roles
  - War room coordination: collaboration tools, status updates, decision making
  - Escalation procedures: on-call rotation, escalation paths, external communication
  - Post-incident review: blameless post-mortems, root cause analysis, action items
  - Incident metrics: MTTR, MTBF, incident frequency, customer impact, trends
  - Continuous improvement: process refinement, tooling enhancement, training

- **Monitoring & Observability Strategy**
  - Monitoring philosophy: proactive vs reactive, signal vs noise, actionable alerts
  - Observability pillars: metrics, logs, traces, correlation, context
  - Alert design: symptom-based alerts, SLO-based alerts, escalation policies
  - Dashboard design: operational dashboards, executive dashboards, drill-down capabilities
  - On-call practices: rotation schedules, handoff procedures, escalation policies
  - Tool selection: monitoring tools, APM solutions, log aggregation, cost considerations
  - Data retention: storage policies, archival strategies, compliance requirements
