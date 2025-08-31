[← Back to Curriculum](../README.md)

---

# Data Warehousing & Analytics

- **Dimensional Modeling & Schema Design**

  - Star schema: fact tables, dimension tables, denormalization, query performance
  - Snowflake schema: normalized dimensions, storage efficiency, join complexity
  - Fact table design: additive, semi-additive, non-additive measures, grain definition
  - Dimension design: slowly changing dimensions (SCD), hierarchies, surrogate keys
  - Conformed dimensions: shared dimensions, data consistency, enterprise data warehouse
  - Bridge tables: many-to-many relationships, factless fact tables, event modeling
  - Temporal modeling: time dimensions, snapshot facts, transaction facts, accumulating snapshots

- **OLAP & Multidimensional Analysis**

  - OLAP cubes: dimensions, measures, hierarchies, aggregations, pre-computation
  - MDX queries: multidimensional expressions, axis specification, calculated members
  - Drill operations: drill-down, drill-up, drill-through, slice and dice
  - ROLAP vs MOLAP vs HOLAP: storage models, performance trade-offs, scalability
  - Aggregation design: materialized views, summary tables, incremental refresh
  - Cube processing: full processing, incremental processing, partition management
  - Performance optimization: indexing, partitioning, compression, caching

- **Data Lakes vs Data Warehouses**

  - Architecture patterns: data lake, data warehouse, lakehouse, data mesh
  - Storage formats: Parquet, ORC, Delta Lake, Iceberg, Hudi, compression strategies
  - Schema evolution: schema-on-read vs schema-on-write, backward compatibility
  - Data governance: cataloging, lineage, quality, security, compliance
  - Query engines: Spark, Presto, Trino, Athena, BigQuery, performance comparison
  - Cost optimization: storage tiers, lifecycle policies, query optimization
  - Metadata management: data catalogs, discovery, lineage, impact analysis

- **ETL vs ELT Patterns**

  - ETL approach: extract, transform, load, data staging, transformation logic
  - ELT approach: extract, load, transform, cloud-native, scalability benefits
  - Change Data Capture: log-based CDC, trigger-based CDC, timestamp-based CDC
  - Debezium: connector ecosystem, schema evolution, exactly-once delivery
  - Data pipeline orchestration: dependency management, error handling, monitoring
  - Incremental processing: delta loads, merge strategies, conflict resolution
  - Data quality: validation rules, profiling, cleansing, monitoring

- **dbt & Modern Analytics Engineering**

  - dbt Core: models, tests, documentation, macros, packages, version control
  - Model organization: staging, intermediate, marts, naming conventions
  - Testing: data tests, schema tests, custom tests, continuous integration
  - Documentation: model documentation, column descriptions, data lineage
  - Macros: reusable SQL, Jinja templating, custom functions, packages
  - Incremental models: strategies, performance optimization, state management
  - dbt Cloud: scheduling, monitoring, IDE, collaboration, deployment

- **Business Intelligence & Visualization**

  - BI tool integration: Tableau, Power BI, Looker, data connections, performance
  - Dashboard design: KPI dashboards, operational dashboards, executive dashboards
  - Self-service analytics: data modeling, user training, governance, security
  - Embedded analytics: white-label solutions, API integration, customization
  - Mobile BI: responsive design, offline capabilities, touch interfaces
  - Real-time analytics: streaming data, live dashboards, alerting, notifications
  - Performance optimization: query caching, pre-aggregation, indexing strategies

- **Advanced Analytics & Data Science Integration**
  - Statistical analysis: descriptive, diagnostic, predictive, prescriptive analytics
  - Machine learning integration: feature engineering, model deployment, monitoring
  - Time series analysis: forecasting, seasonality, trend analysis, anomaly detection
  - A/B testing: experimental design, statistical significance, result interpretation
  - Advanced visualizations: network graphs, geospatial analysis, interactive dashboards
  - Data storytelling: narrative structure, visual design, audience engagement
  - Collaborative analytics: shared workspaces, version control, peer review
