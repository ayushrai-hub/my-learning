[← Back to Curriculum](../README.md)

---

# Search & Information Retrieval

- **Full-Text Search Fundamentals**

  - Inverted indexes: term frequency, document frequency, posting lists, compression
  - Text analysis: tokenization, stemming, lemmatization, stop words, synonyms
  - Scoring algorithms: TF-IDF, BM25, cosine similarity, relevance tuning
  - Index optimization: segment merging, field boosting, index warming, refresh policies
  - Query parsing: boolean queries, phrase queries, wildcard queries, fuzzy matching
  - Performance tuning: shard sizing, replica strategies, caching, query optimization
  - Multilingual search: language detection, analyzers, Unicode normalization

- **Elasticsearch & OpenSearch Architecture**

  - Cluster architecture: nodes, shards, replicas, master election, split-brain prevention
  - Index management: templates, mappings, settings, lifecycle policies, rollover
  - Query DSL: match queries, bool queries, aggregations, scripting, filters vs queries
  - Performance optimization: routing, field data, doc values, circuit breakers
  - Monitoring: cluster health, node stats, slow logs, search profiler, hot threads
  - Security: authentication, authorization, field-level security, audit logging
  - Operations: backup/restore, reindexing, cluster upgrades, capacity planning

- **Vector Search & Embeddings**

  - Dense vector representations: word2vec, GloVe, BERT, sentence transformers
  - Approximate Nearest Neighbor: LSH, random projection, product quantization
  - Vector databases: Faiss, Milvus, Qdrant, Pinecone, Weaviate, performance comparison
  - HNSW algorithm: hierarchical navigable small world graphs, construction, search
  - Embedding models: text, image, audio, multimodal, fine-tuning, evaluation
  - Hybrid search: combining dense and sparse retrieval, ranking fusion, reranking
  - Vector indexing: IVF, PQ, HNSW, LSH, trade-offs, memory usage, query latency

- **Semantic Search & Ranking**

  - Neural ranking models: BERT, RankNet, LambdaMART, learning to rank
  - Query understanding: intent classification, entity recognition, query expansion
  - Relevance feedback: click-through rates, dwell time, user behavior signals
  - Personalization: user profiles, collaborative filtering, content-based filtering
  - A/B testing: ranking experiments, statistical significance, metric evaluation
  - Evaluation metrics: precision, recall, F1, NDCG, MAP, MRR, click-through rates
  - Real-time learning: online learning, bandit algorithms, exploration vs exploitation

- **Knowledge Graphs & Graph Search**

  - Graph data models: property graphs, RDF, labeled property graphs, schema design
  - Graph databases: Neo4j, Amazon Neptune, ArangoDB, TigerGraph, performance tuning
  - Query languages: Cypher, SPARQL, Gremlin, graph traversal patterns, optimization
  - Graph algorithms: PageRank, centrality measures, community detection, path finding
  - Knowledge extraction: entity linking, relation extraction, ontology alignment
  - Graph embeddings: node2vec, GraphSAGE, graph neural networks, representation learning
  - Reasoning: inference rules, ontologies, semantic reasoning, consistency checking

- **Search Analytics & Optimization**

  - Search metrics: query volume, zero-results rate, click-through rate, conversion rate
  - Query analysis: popular queries, long-tail queries, query clustering, intent analysis
  - Result analysis: position bias, result diversity, freshness, authority signals
  - User behavior: search sessions, query refinement, abandonment patterns
  - Performance monitoring: query latency, index size, resource utilization, errors
  - Continuous improvement: relevance tuning, A/B testing, machine learning integration
  - Business intelligence: search-driven insights, revenue attribution, ROI measurement

- **Enterprise Search & Discovery**
  - Content ingestion: crawlers, connectors, document processing, metadata extraction
  - Security integration: access control, user permissions, content filtering
  - Federated search: multiple data sources, result aggregation, deduplication
  - Search interfaces: faceted search, autocomplete, query suggestions, result snippets
  - Content management: document lifecycle, versioning, approval workflows
  - Compliance: data retention, audit trails, privacy regulations, content governance
  - User experience: search analytics, personalization, mobile optimization, accessibility
