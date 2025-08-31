[← Back to Curriculum](../README.md)

---

# Machine Learning & AI Engineering

- **Data Pipeline & Feature Engineering**

  - Data ingestion: batch processing, streaming, real-time, data quality validation
  - Feature stores: offline features, online features, feature versioning, lineage
  - Data validation: schema validation, statistical validation, drift detection
  - Feature engineering: transformation, scaling, encoding, feature selection
  - Data preprocessing: cleaning, normalization, handling missing values, outliers
  - Pipeline orchestration: Airflow, Kubeflow, MLflow, dependency management
  - Data governance: privacy, compliance, access control, audit trails

- **Experiment Management & MLOps**

  - Experiment tracking: MLflow, Weights & Biases, Neptune, versioning, reproducibility
  - Hyperparameter optimization: grid search, random search, Bayesian optimization
  - Model versioning: artifact management, lineage tracking, rollback capabilities
  - Reproducibility: environment management, seed setting, deterministic training
  - A/B testing: statistical significance, power analysis, experiment design
  - Model registry: centralized storage, metadata, approval workflows, governance
  - Continuous training: automated retraining, trigger conditions, performance monitoring

- **Model Deployment & Serving**

  - Deployment patterns: batch inference, real-time serving, edge deployment
  - Online serving: REST APIs, gRPC, model servers, load balancing, caching
  - Canary deployments: gradual rollout, traffic splitting, performance monitoring
  - Shadow deployments: parallel inference, comparison, validation, risk mitigation
  - Model optimization: quantization, pruning, distillation, hardware acceleration
  - Scaling: horizontal scaling, auto-scaling, resource optimization, cost management
  - Multi-model serving: model composition, ensemble methods, routing strategies

- **Model Monitoring & Drift Detection**

  - Performance monitoring: accuracy, latency, throughput, error rates, SLAs
  - Data drift: statistical tests, distribution comparison, feature drift detection
  - Model drift: performance degradation, concept drift, adaptation strategies
  - Continual learning: online learning, incremental updates, catastrophic forgetting
  - Alerting: threshold-based, anomaly detection, escalation procedures
  - Feedback loops: human feedback, active learning, model improvement
  - Observability: logging, metrics, tracing, debugging, root cause analysis

- **Vector Databases & Semantic Search**

  - Vector databases: Pinecone, Weaviate, Chroma, Qdrant, performance comparison
  - Approximate nearest neighbor: HNSW, IVF, LSH, accuracy vs speed trade-offs
  - Embedding models: sentence transformers, OpenAI embeddings, domain-specific models
  - Retrieval-augmented generation: RAG patterns, context retrieval, answer generation
  - Semantic search: query understanding, ranking, relevance scoring, personalization
  - Vector operations: similarity search, clustering, dimensionality reduction
  - Scaling: distributed storage, sharding, replication, consistency models

- **Large Language Models & Generative AI**

  - LLM architectures: transformer models, attention mechanisms, scaling laws
  - Agentic frameworks: LangChain, AutoGen, ReAct, tool usage, planning
  - Prompt engineering: few-shot learning, chain-of-thought, prompt optimization
  - Fine-tuning: full fine-tuning, LoRA, QLoRA, parameter-efficient methods
  - Model serving: inference optimization, batching, caching, hardware acceleration
  - Safety and alignment: content filtering, bias detection, harmful content prevention
  - Cost optimization: model selection, caching, prompt optimization, batch processing

- **Responsible AI & Governance**
  - Fairness: bias detection, fairness metrics, mitigation strategies, testing
  - Explainability: model interpretability, SHAP, LIME, feature importance, transparency
  - Privacy: differential privacy, federated learning, data anonymization, compliance
  - Governance: model approval, risk assessment, compliance, audit trails
  - Ethics: ethical guidelines, review boards, impact assessment, stakeholder engagement
  - Regulatory compliance: AI regulations, documentation, reporting, accountability
  - Monitoring: bias monitoring, fairness metrics, performance across demographics

---

## 📚 Resources

### Essential Reading
- 📖 **[Hands-On Machine Learning](../resources/books/hands-on-ml-geron.pdf)** by Aurélien Géron
  - *Topics*: ML Fundamentals, Feature Engineering, Model Training
  - *Level*: Beginner to Intermediate
  - *Quality*: ⭐⭐⭐⭐⭐

### Documentation & Guides
- 🛠️ **[MLflow Documentation](https://mlflow.org/docs/latest/index.html)** - Official MLflow docs
  - *Topics*: Experiment Tracking, Model Registry, MLOps
  - *Level*: Beginner to Advanced
  - *Quality*: ⭐⭐⭐⭐⭐

- 🛠️ **[Kubeflow Documentation](https://www.kubeflow.org/docs/)** - ML workflows on Kubernetes
  - *Topics*: ML Pipelines, Kubernetes, Model Serving
  - *Level*: Intermediate to Advanced
  - *Quality*: ⭐⭐⭐⭐

### Video Tutorials
- 🎥 **[Machine Learning Engineering for Production](https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops)** - Coursera Specialization
  - *Topics*: MLOps, Production ML, Model Deployment
  - *Level*: Intermediate
  - *Quality*: ⭐⭐⭐⭐⭐

### Papers & Research
- 📄 **[Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf)** - NIPS 2015
  - *Topics*: ML Systems, Technical Debt, Production Challenges
  - *Level*: Advanced
  - *Quality*: ⭐⭐⭐⭐⭐

### Practice Datasets
- 📊 **[Kaggle Learn Datasets](https://www.kaggle.com/learn)** - Curated learning datasets
  - *Topics*: Feature Engineering, Model Training, Data Analysis
  - *Level*: Beginner to Intermediate
  - *Quality*: ⭐⭐⭐⭐

### Related Topics
See also: [Data Engineering & ETL](../data-streaming/data-engineering.md), [System Design & Scalability](../architecture-testing/system-design.md)
