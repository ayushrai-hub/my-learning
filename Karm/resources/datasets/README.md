# 📊 Practice Datasets & Sample Data

This directory contains curated datasets for learning, experimentation, and skill development across all curriculum topics. Datasets are organized by category with metadata, usage examples, and analysis guides.

## 📈 Data Science & Analytics Datasets

### `ecommerce-dataset/`
**E-commerce Customer Purchase Data**
- **Size**: 50,000+ transactions
- **Format**: CSV, JSON
- **Features**: Customer demographics, purchase history, product categories, timestamps
- **Use Cases**: Customer segmentation, recommendation systems, churn prediction
- **Analysis Examples**: RFM analysis, cohort analysis, A/B testing

### `financial-transactions/`
**Banking Transaction Dataset**
- **Size**: 100,000+ transactions
- **Format**: CSV, Parquet
- **Features**: Transaction amounts, timestamps, merchant categories, fraud labels
- **Use Cases**: Fraud detection, spending pattern analysis, risk assessment
- **Analysis Examples**: Time series analysis, anomaly detection, classification models

### `social-media-analytics/`
**Social Media Engagement Data**
- **Size**: 1M+ posts/interactions
- **Format**: JSON, CSV
- **Features**: Post content, engagement metrics, user demographics, timestamps
- **Use Cases**: Sentiment analysis, trend detection, content optimization
- **Analysis Examples**: NLP processing, network analysis, predictive modeling

## 🤖 Machine Learning Datasets

### `image-classification/`
**Labeled Image Classification Dataset**
- **Size**: 50,000+ images
- **Format**: JPEG, TFRecord
- **Categories**: 1,000 object classes
- **Use Cases**: Computer vision, transfer learning, model evaluation
- **Models**: ResNet, EfficientNet, Vision Transformers

### `text-classification/`
**Text Classification Dataset**
- **Size**: 500,000+ documents
- **Format**: CSV, JSON
- **Categories**: Sentiment, topics, intent classification
- **Use Cases**: NLP models, text analytics, chatbots
- **Models**: BERT, RoBERTa, DistilBERT

### `time-series/`
**Time Series Forecasting Data**
- **Size**: Various time ranges
- **Format**: CSV, Parquet
- **Domains**: Sales, weather, IoT sensors, financial markets
- **Use Cases**: Forecasting, anomaly detection, pattern recognition
- **Models**: LSTM, Prophet, ARIMA

## 🖥️ System Performance Datasets

### `web-server-logs/`
**Web Server Access Logs**
- **Size**: 10M+ log entries
- **Format**: Apache/Nginx log format
- **Features**: IP addresses, timestamps, URLs, response codes, user agents
- **Use Cases**: Log analysis, security monitoring, performance optimization
- **Tools**: ELK stack, Splunk, custom parsers

### `application-metrics/`
**Application Performance Metrics**
- **Size**: Time-series metrics
- **Format**: Prometheus format, CSV
- **Metrics**: CPU usage, memory, response times, error rates
- **Use Cases**: Performance monitoring, anomaly detection, capacity planning
- **Tools**: Prometheus, Grafana, custom dashboards

### `user-behavior/`
**User Interaction Analytics**
- **Size**: 1M+ user sessions
- **Format**: JSON, CSV
- **Features**: Click streams, session data, conversion funnels
- **Use Cases**: UX optimization, A/B testing, personalization
- **Tools**: Google Analytics, Mixpanel, custom tracking

## 🏗️ System Design & Architecture Datasets

### `distributed-systems-logs/`
**Distributed System Telemetry**
- **Size**: Multi-service logs and traces
- **Format**: JSON, Protocol Buffers
- **Features**: Service calls, latencies, errors, distributed traces
- **Use Cases**: System debugging, performance analysis, architecture optimization
- **Tools**: Jaeger, Zipkin, custom tracing systems

### `api-performance-data/`
**API Usage and Performance Metrics**
- **Size**: API call logs and metrics
- **Format**: JSON, CSV
- **Features**: Endpoints, response times, error rates, usage patterns
- **Use Cases**: API optimization, rate limiting, performance monitoring
- **Tools**: API gateways, monitoring tools, custom analytics

### `infrastructure-metrics/`
**Cloud Infrastructure Metrics**
- **Size**: Time-series infrastructure data
- **Format**: Prometheus, CloudWatch format
- **Features**: CPU, memory, disk, network utilization across instances
- **Use Cases**: Auto-scaling, cost optimization, capacity planning
- **Tools**: Cloud monitoring, Prometheus, Grafana

## 🔒 Security Datasets

### `network-traffic/`
**Network Packet Capture Data**
- **Size**: 1M+ packets
- **Format**: PCAP, CSV
- **Features**: Packet headers, payloads, protocols, timestamps
- **Use Cases**: Intrusion detection, traffic analysis, security monitoring
- **Tools**: Wireshark, Zeek, custom parsers

### `security-events/`
**Security Event Logs**
- **Size**: 500,000+ events
- **Format**: JSON, CEF
- **Features**: Login attempts, file access, system calls, alerts
- **Use Cases**: Threat detection, compliance monitoring, incident response
- **Tools**: SIEM systems, ELK stack, custom rules

### `malware-samples/`
**Malware Analysis Dataset** (Educational Only)
- **Size**: 10,000+ samples
- **Format**: Binary files, metadata
- **Features**: File hashes, behavior patterns, classification labels
- **Use Cases**: Malware detection, reverse engineering education
- **Tools**: Static/dynamic analysis tools, machine learning models

## 📊 Business Intelligence Datasets

### `sales-performance/`
**Sales and Revenue Data**
- **Size**: Multi-year sales records
- **Format**: CSV, Excel, database dumps
- **Features**: Products, regions, time periods, revenue metrics
- **Use Cases**: Sales forecasting, market analysis, KPI dashboards
- **Tools**: Tableau, Power BI, SQL analytics

### `customer-analytics/`
**Customer Behavior Dataset**
- **Size**: 100,000+ customers
- **Format**: CSV, JSON
- **Features**: Demographics, purchase history, engagement metrics
- **Use Cases**: Customer segmentation, lifetime value prediction, personalization
- **Tools**: Python/R analytics, ML models, BI tools

### `supply-chain/`
**Supply Chain Operations Data**
- **Size**: Complex supply network data
- **Format**: CSV, Graph format
- **Features**: Suppliers, inventory, orders, logistics
- **Use Cases**: Optimization, demand forecasting, risk analysis
- **Tools**: Graph databases, optimization solvers, analytics platforms

## 🎮 Game Development Datasets

### `game-telemetry/`
**Game Player Behavior Data**
- **Size**: 1M+ gameplay sessions
- **Format**: JSON, CSV
- **Features**: Player actions, game states, progression metrics
- **Use Cases**: Game design optimization, player retention analysis
- **Tools**: Game analytics platforms, custom dashboards

### `asset-performance/`
**Game Asset Usage Data**
- **Size**: Asset loading and performance metrics
- **Format**: JSON, binary logs
- **Features**: Load times, memory usage, render performance
- **Use Cases**: Asset optimization, performance profiling
- **Tools**: Unity analytics, custom profiling tools

## 📱 IoT & Sensor Datasets

### `sensor-network/`
**IoT Sensor Data**
- **Size**: Time-series sensor readings
- **Format**: JSON, MQTT format
- **Features**: Temperature, humidity, motion, environmental sensors
- **Use Cases**: Predictive maintenance, environmental monitoring
- **Tools**: IoT platforms, time-series databases, ML models

### `smart-city/`
**Smart City Sensor Network**
- **Size**: Multi-sensor urban data
- **Format**: JSON, GeoJSON
- **Features**: Traffic, air quality, noise, energy consumption
- **Use Cases**: Urban planning, environmental monitoring, optimization
- **Tools**: GIS systems, time-series analytics, ML platforms

## 🚀 Getting Started with Datasets

### Dataset Loading Examples

**Python (Pandas)**
```python
import pandas as pd

# Load e-commerce dataset
df = pd.read_csv('ecommerce-dataset/transactions.csv')

# Basic exploration
print(df.head())
print(df.describe())
print(df.isnull().sum())
```

**Python (PySpark)**
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Dataset Analysis").getOrCreate()
df = spark.read.csv("financial-transactions/transactions.csv", header=True)
df.show()
```

### Recommended Workflow

1. **Explore the Dataset**: Understand structure, features, and quality
2. **Data Cleaning**: Handle missing values, outliers, and inconsistencies
3. **Feature Engineering**: Create new features and transformations
4. **Analysis/Modeling**: Apply statistical methods or ML algorithms
5. **Visualization**: Create charts and dashboards to communicate insights

### Dataset Categories by Difficulty

**Beginner-Friendly**:
- `ecommerce-dataset/` - Straightforward tabular data
- `image-classification/` - Pre-processed images
- `text-classification/` - Clean text data

**Intermediate Level**:
- `time-series/` - Temporal dependencies
- `social-media-analytics/` - Unstructured data
- `web-server-logs/` - Complex parsing required

**Advanced Level**:
- `distributed-systems-logs/` - Multi-dimensional data
- `network-traffic/` - Binary protocol analysis
- `malware-samples/` - Specialized domain knowledge

## 📋 Dataset Metadata Standards

Each dataset includes:
- **README.md**: Detailed description and usage guide
- **data-dictionary.md**: Feature descriptions and data types
- **sample-analysis.ipynb**: Jupyter notebook with example analysis
- **loading-scripts/**: Code to load and preprocess data
- **LICENSE**: Usage terms and attribution requirements

## 🤝 Contributing Datasets

To add new datasets:
1. Ensure data is ethically sourced and properly licensed
2. Include comprehensive metadata and documentation
3. Provide loading and analysis examples
4. Anonymize any sensitive information
5. Test with multiple analysis tools

## ⚠️ Usage Guidelines

- **Educational Use**: Datasets are provided for learning and research
- **Privacy Compliance**: No personally identifiable information included
- **Ethical Use**: Use datasets responsibly and respect data privacy
- **Citation**: Attribute original data sources when appropriate

---

**Dataset Categories**: 15+ categories  
**Total Datasets**: 25+ curated datasets  
**Data Formats**: CSV, JSON, Parquet, Images, Logs  
**Total Size**: 50GB+ across all datasets  
**Last Updated**: December 2025
