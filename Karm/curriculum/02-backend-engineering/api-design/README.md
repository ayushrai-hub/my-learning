# 🌐 API Design & REST Architecture

## Executive Summary
API Design forms the foundation of modern software systems, enabling seamless integration between frontend and backend systems. This curriculum focuses on RESTful API architecture, HTTP specifications, and scalable service design using Python/FastAPI. Students will master professional API development practices, including versioning, authentication, documentation, and performance optimization for 2024-2025 industry standards.

## Core Concepts
Understanding API design requires mastery of:
- **HTTP Specifications**: Methods, status codes, headers, content negotiation
- **REST Principles**: Resource orientation, statelessness, uniform interfaces
- **API Lifecycle**: Design, documentation, versioning, deprecation
- **Security Patterns**: Authentication, authorization, rate limiting, input validation
- **Performance Considerations**: Caching, pagination, efficient data structures
- **Contract-First Development**: OpenAPI specifications, API testing strategies

### Why This Matters (2024 Perspective)
In 2024-2025, API design directly impacts business success:
- API economy reached $15T market value (Statista 2024)
- 83% of organizations use APIs for digital transformation (Gartner)
- Microservices adoption requires robust API contracts and governance
- AI integrations increasingly depend on well-designed API interfaces

## Prerequisites
- Programming Fundamentals (functions, classes, error handling)
- Basic networking concepts (HTTP, TCP/IP)
- Database fundamentals (CRUD operations, relationships)
- JSON/XML data interchange understanding

## Learning Objectives
- [ ] Design RESTful APIs following industry standards and best practices
- [ ] Implement proper HTTP status codes, methods, and content negotiation
- [ ] Create comprehensive API documentation with OpenAPI specifications
- [ ] Implement authentication and authorization patterns securely
- [ ] Optimize API performance with caching, pagination, and efficient querying
- [ ] Apply API versioning strategies for backward compatibility

## Key Technologies & Tools
| Technology | Version (2024) | Purpose |
|------------|----------------|---------|
| FastAPI    | 0.104.0       | High-performance async API framework with auto-validation |
| Pydantic   | v2.5          | Data validation and serialization with JSON schema |
| SQLAlchemy | 2.0           | Modern ORM with async support and type safety |
| OpenAPI    | 3.0.3         | API specification and documentation standard |
| Postman    | 10.19         | API testing, documentation, and collaboration |
| Redis      | 7.2           | High-performance caching and session storage |

## Hands-On Example
Let's build a complete e-commerce product API with modern practices:

```python
from fastapi import FastAPI, HTTPException, Depends, Query, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum
import json
import asyncio
import aioredis
import uvicorn

# Security
security = HTTPBearer()

# Redis connection (would be configured in production)
redis = None  # aioredis.from_url("redis://localhost")

# Enums
class ProductCategory(str, Enum):
    ELECTRONICS = "electronics"
    CLOTHING = "clothing"
    BOOKS = "books"
    HOME = "home"
    SPORTS = "sports"

class ProductStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    DISCONTINUED = "discontinued"

# Pydantic Models
class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200, description="Product name")
    description: str = Field(..., max_length=2000, description="Product description")
    price: float = Field(..., gt=0, le=100000, description="Product price in USD")
    category: ProductCategory
    inventory_count: int = Field(..., ge=0, description="Available inventory")
    sku: str = Field(..., min_length=1, max_length=50, description="Stock keeping unit")

    @validator('sku')
    def sku_alphanumeric(cls, v):
        if not v.replace('-', '').replace('_', '').isalnum():
            raise ValueError('SKU must be alphanumeric with optional hyphens/underscores')
        return v

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=2000)
    price: Optional[float] = Field(None, gt=0, le=100000)
    category: Optional[ProductCategory]
    inventory_count: Optional[int] = Field(None, ge=0)
    status: Optional[ProductStatus]

class ProductResponse(ProductBase):
    id: int
    status: ProductStatus
    created_at: datetime
    updated_at: datetime
    rating: Optional[float] = Field(None, ge=0, le=5)

    class Config:
        from_attributes = True

class PaginatedResponse(BaseModel):
    items: List[ProductResponse]
    total: int
    page: int
    page_size: int
    pages: int

# In-memory storage (replace with database in production)
products_db = {}
product_id_counter = 1

# FastAPI App
app = FastAPI(
    title="E-Commerce Product API",
    description="Modern RESTful API for product management with OpenAPI 3.0 specification",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://yourfrontend.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Authentication dependency (simplified)
async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Mock authentication - replace with JWT/OAuth in production."""
    token = credentials.credentials
    if token != "valid-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
    return {"user_id": 1, "role": "admin"}

# Redis caching helper
async def get_cached_product(product_id: int) -> Optional[Dict]:
    """Get product from cache if available."""
    if not redis:
        return None
    try:
        data = await redis.get(f"product:{product_id}")
        return json.loads(data) if data else None
    except:
        return None

async def set_cached_product(product_id: int, product_data: Dict, ttl: int = 300):
    """Cache product data with TTL."""
    if redis:
        await redis.set(f"product:{product_id}", json.dumps(product_data), ex=ttl)

# Routes
@app.post("/api/v1/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    product: ProductCreate,
    current_user: Dict = Depends(get_current_user)
):
    """Create a new product with input validation."""
    global product_id_counter

    # Check SKU uniqueness (replace with database constraint)
    if any(p["sku"] == product.sku for p in products_db.values()):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="SKU already exists"
        )

    product_data = {
        "id": product_id_counter,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "category": product.category,
        "inventory_count": product.inventory_count,
        "sku": product.sku,
        "status": ProductStatus.ACTIVE,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
        "rating": None
    }

    products_db[product_id_counter] = product_data

    # Cache the new product
    await set_cached_product(product_id_counter, product_data)

    product_id_counter += 1
    return ProductResponse(**product_data)

@app.get("/api/v1/products", response_model=PaginatedResponse)
async def list_products(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    category: Optional[ProductCategory] = None,
    min_price: Optional[float] = Query(None, ge=0),
    max_price: Optional[float] = Query(None, ge=0),
    search: Optional[str] = Query(None, min_length=1, max_length=100),
    sort_by: Optional[str] = Query("created_at", regex="^(name|price|created_at|rating)$"),
    sort_order: Optional[str] = Query("desc", regex="^(asc|desc)$")
):
    """List products with advanced filtering, pagination, and sorting."""
    # Filter products
    filtered_products = list(products_db.values())

    if category:
        filtered_products = [p for p in filtered_products if p["category"] == category]

    if min_price is not None:
        filtered_products = [p for p in filtered_products if p["price"] >= min_price]

    if max_price is not None:
        filtered_products = [p for p in filtered_products if p["price"] <= max_price]

    if search:
        search_lower = search.lower()
        filtered_products = [
            p for p in filtered_products
            if search_lower in p["name"].lower() or search_lower in p["description"].lower()
        ]

    # Sort products
    reverse = sort_order == "desc"
    if sort_by == "name":
        filtered_products.sort(key=lambda x: x["name"], reverse=reverse)
    elif sort_by == "price":
        filtered_products.sort(key=lambda x: x["price"], reverse=reverse)
    elif sort_by == "rating":
        filtered_products.sort(key=lambda x: x["rating"] or 0, reverse=reverse)
    else:  # created_at
        filtered_products.sort(key=lambda x: x["created_at"], reverse=reverse)

    # Paginate
    total = len(filtered_products)
    start = (page - 1) * page_size
    end = start + page_size
    paginated_products = filtered_products[start:end]

    return PaginatedResponse(
        items=[ProductResponse(**p) for p in paginated_products],
        total=total,
        page=page,
        page_size=page_size,
        pages=(total + page_size - 1) // page_size
    )

@app.get("/api/v1/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int):
    """Get a specific product by ID with caching."""
    # Try cache first
    cached_product = await get_cached_product(product_id)
    if cached_product:
        return ProductResponse(**cached_product)

    if product_id not in products_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    product = products_db[product_id]

    # Cache for future requests
    await set_cached_product(product_id, product)

    return ProductResponse(**product)

@app.put("/api/v1/products/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: int,
    product_update: ProductUpdate,
    current_user: Dict = Depends(get_current_user)
):
    """Update an existing product partially or fully."""
    if product_id not in products_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    product = products_db[product_id]
    update_data = product_update.dict(exclude_unset=True)

    # Validate price bounds if updating price
    if "price" in update_data:
        if not (0 < update_data["price"] <= 100000):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Price must be between 0 and 100000"
            )

    product.update(update_data)
    product["updated_at"] = datetime.utcnow()

    # Update cache
    await set_cached_product(product_id, product)

    return ProductResponse(**product)

@app.delete("/api/v1/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: int,
    current_user: Dict = Depends(get_current_user)
):
    """Soft delete a product by setting status to discontinued."""
    if product_id not in products_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    product = products_db[product_id]
    product["status"] = ProductStatus.DISCONTINUED
    product["updated_at"] = datetime.utcnow()

    # Invalidate cache
    if redis:
        await redis.delete(f"product:{product_id}")

@app.get("/api/v1/products/search/suggestions")
async def search_suggestions(
    q: str = Query(..., min_length=1, max_length=100, description="Search query")
):
    """Provide search suggestions based on product names."""
    suggestions = []
    query_lower = q.lower()

    for product in products_db.values():
        if product["status"] == ProductStatus.ACTIVE and query_lower in product["name"].lower():
            suggestions.append({
                "id": product["id"],
                "name": product["name"],
                "category": product["category"]
            })

    return {"suggestions": suggestions[:10]}  # Limit to 10 suggestions

# Health check endpoint
@app.get("/health")
async def health_check():
    """API health check endpoint for load balancers and monitoring."""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow(),
        "version": "1.0.0",
        "products_count": len(products_db)
    }

# Startup and shutdown events
@app.on_event("startup")
async def startup_event():
    """Initialize resources on startup."""
    global redis
    try:
        redis = await aioredis.from_url("redis://localhost", encoding="utf-8")
        print("Redis connection established")
    except Exception as e:
        print(f"Redis connection failed: {e}")

@app.on_event("shutdown")
async def shutdown_event():
    """Clean up resources on shutdown."""
    if redis:
        await redis.close()
        print("Redis connection closed")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
```

This implementation demonstrates:
- **RESTful Design**: Proper resource naming, HTTP methods, and status codes
- **Comprehensive Validation**: Pydantic models with automatic schema generation
- **Performance Optimization**: Redis caching and efficient pagination
- **Security Patterns**: Bearer token authentication and CORS handling
- **Production Ready**: Error handling, logging, input validation, and health checks
- **Modern Features**: Async/await patterns, type hints, and OpenAPI documentation

## Common Pitfalls

### 1. REST Resource Design Issues
```python
# ❌ POOR: Action-based endpoints instead of resource-oriented
GET /api/getUserInfo
POST /api/createProduct
DELETE /api/removeOrder

# ✅ CORRECT: Resource-oriented design
GET /api/users/{userId}
POST /api/products
DELETE /api/orders/{orderId}
```

### 2. Ignoring HTTP Status Codes Properly
```python
# ❌ WRONG: Using 200 OK for errors
@app.post("/users")
def create_user(user_data):
    if user_exists(user_data.email):
        return {"error": "User exists"}, 200  # Bad practice
    
    return {"user": create_user(user_data)}, 200

# ✅ CORRECT: Use appropriate status codes
@app.post("/users", status_code=201)
def create_user(user_data):
    if user_exists(user_data.email):
        raise HTTPException(409, "User already exists")  # 409 Conflict
    
    return {"user": create_user(user_data)}
```

### 3. Poor Pagination Implementation
```python
# ❌ INEFFICIENT: Load all data then slice (O(total) time/space)
@app.get("/products")
def get_products(page=1, limit=20):
    all_products = db.query(Product).all()  # Loads EVERYTHING
    start = (page - 1) * limit
    return all_products[start:start + limit]

# ✅ EFFICIENT: Database-level pagination (O(limit) time/space)
@app.get("/products")
def get_products(page=1, limit=20):
    return db.query(Product).offset((page-1) * limit).limit(limit).all()
```

## Best Practices (2024 Standards)

### API Design Principles
- **Resource Naming**: Use plural nouns (`/users`, not `/user`), hierarchical (`/users/{id}/posts`)
- **HTTP Methods**: GET (read), POST (create), PUT (full update), PATCH (partial update), DELETE (remove)
- **Status Codes**: 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 500 Server Error
- **Versioning**: URL versioning (`/api/v1/`), header versioning, or content negotiation

### Documentation & Specification
- **OpenAPI 3.0**: Auto-generated from code annotations and models
- **Comprehensive Examples**: Real request/response examples for all endpoints
- **Error Documentation**: Clear error codes and messages
- **Interactive Testing**: Swagger UI or ReDoc for testing endpoints

### Performance & Scalability
- **Caching**: Redis for frequently accessed data, HTTP caching headers
- **Rate Limiting**: Protect against abuse with burst and sustained limits
- **Pagination**: Cursor-based for better performance, avoid offset-based
- **Async Processing**: Use async frameworks for I/O-bound operations

### Security Standards
- **HTTPS Only**: Enforce SSL/TLS encryption
- **Token-Based Auth**: JWT or OAuth2 for session management
- **Input Validation**: Schema validation, sanitization, size limits
- **CORS Configuration**: Domain-specific CORS, preflight handling
- **Security Headers**: Content Security Policy, HSTS, X-Frame-Options

## Advanced Topics

### GraphQL Integration
```python
from graphene import ObjectType, String, Schema
from graphene_fastapi import GraphQLApp

class ProductGraphQL(ObjectType):
    name = String()
    description = String()
    price = String()

    def resolve_price(parent, info):
        return f"${parent['price']:.2f}"

# Add GraphQL endpoint alongside REST
app.add_route("/graphql", GraphQLApp(schema=Schema(query=ProductGraphQL)))
```

### Event-Driven APIs with Webhooks
```python
from fastapi import BackgroundTasks
import httpx

@app.post("/webhooks/register")
def register_webhook(url: str, events: List[str]):
    """Register webhook URL for specific events."""
    # Store webhook configuration
    store_webhook(url, events)

async def trigger_webhook(url: str, event: str, data: Dict):
    """Send webhook notification asynchronously."""
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            await client.post(url, json={"event": event, "data": data})
    except Exception as e:
        log_webhook_failure(url, event, str(e))

@app.post("/products", background_tasks: BackgroundTasks)
def create_product(product_data: ProductCreate):
    product = create_product_logic(product_data)
    background_tasks.add_task(
        trigger_webhook,
        f"{webhook_url}/product-created",
        "product.created",
        product
    )
    return product
```

### API Gateway Patterns
```python
# Kong Gateway Configuration (YAML)
_format_version: "3.0"
services:
  - name: product-api
    url: http://product-service:8000
    routes:
      - name: products-route
        paths:
          - /api/v1/products
        methods:
          - GET
          - POST
        plugins:
          - name: rate-limiting
            config:
              minute: 100
              hour: 5000
          - name: jwt
            config:
              secret_is_base64: false
```

## Related Concepts

### Prerequisites
- [HTTP Fundamentals](../networking/http-basics.md)
- [Database Operations](../backend/databases.md)
- [Authentication Patterns](../security/auth-patterns.md)

### Next Level Topics
- [GraphQL APIs](../advanced/graphql-design.md)
- [Microservices Communication](../backend/microservices.md)
- [API Gateway Patterns](../platform/api-gateways.md)
- [Performance Optimization](../performance/api-optimization.md)

### Complementary Skills
- [Database Design](../backend/database-modeling.md)
- [Security Implementation](../security/api-security.md)
- [Load Testing](../testing/api-testing.md)

## Resources

### Books
- **API Design Patterns (2024)** by JJ Geewax
  \$49.99, 480 pages, Manning - Comprehensive guide to modern API design
- **RESTful Web APIs (2nd Edition, 2024)** by Leonard Richardson & Mike Amundsen
  \$59.99, 545 pages, O'Reilly - REST principles and hypermedia concepts
- **Build APIs You Won't Hate (Revised 2024)** by Phil Sturgeon
  \$39.99, 300 pages, Apress - Practical API development lessons

### Courses
- **API Design and Management** - Microsoft Learn (free)
  Microsoft Learn, 12 hours, Free - Azure API Management focused
- **REST API Design, Development & Management** - LinkedIn Learning
  LinkedIn Learning, 2 hours, \$29.99/month - Theory to practice
- **Building APIs with Node.js** - Pluralsight
  Pluralsight, 4 hours, \$29/month - Implementation-focused

### Documentation
- **OpenAPI 3.0 Specification** - openapis.org
  Free, official - Complete API specification standard
- **FastAPI Documentation** - fastapi.tiangolo.com
  Free, comprehensive - Async Python API framework
- **REST API Guidelines** - github.com/Microsoft/api-guidelines
  Free, Microsoft - Enterprise API standards

### Tools & Platforms
- **Postman** - postman.com (free tier)
  API testing and documentation platform
- **SwaggerHub** - swaggerhub.com (free for public APIs)
  API design and documentation collaboration
- **Stoplight** - stoplight.io (free tier)
  API design, testing, and governance

## Assessment Criteria

### RESTful Design Fundamentals
- ✅ Applies proper HTTP methods and status codes consistently
- ✅ Designs resource-oriented URIs with clear hierarchy and naming
- ✅ Implements content negotiation (JSON/XML) appropriately
- ✅ Uses appropriate headers for caching, authentication, and metadata

### API Documentation Quality
- ✅ Provides comprehensive OpenAPI/Swagger documentation
- ✅ Includes detailed request/response examples for all endpoints
- ✅ Documents error responses with specific error codes
- ✅ Maintains up-to-date API contract with versioning information

### Security Implementation
- ✅ Implements authentication correctly (JWT, OAuth, API keys)
- ✅ Applies authorization checks for resource access control
- ✅ Validates and sanitizes all input data properly
- ✅ Configures HTTPS, CORS, and security headers correctly

### Performance & Optimization
- ✅ Implements efficient pagination (cursor-based preferred)
- ✅ Applies appropriate caching strategies (HTTP + Redis)
- ✅ Optimizes database queries to prevent N+1 problems
- ✅ Handles rate limiting and abuse prevention properly

### Error Handling & Reliability
- ✅ Provides meaningful error messages and appropriate status codes
- ✅ Implements graceful degradation for service failures
- ✅ Uses proper logging and monitoring for API operations
- ✅ Handles concurrency and race conditions appropriately

### Code Quality & Testing
- ✅ Uses proper data validation schemas (Pydantic, Joi, etc.)
- ✅ Implements comprehensive API tests (unit, integration, contract)
- ✅ Applies consistent code formatting and documentation standards
- ✅ Follows framework-specific best practices and conventions

### Production Readiness
- **API Gateway Integration**: Load balancing, routing, transformation
- **Monitoring & Observability**: Metrics, logging, alerting, tracing
- **Scalability Patterns**: Horizontal scaling, database optimization
- **API Governance**: Standardization, documentation, lifecycle management

### Career Readiness Indicators
- **Junior API Developer**: Can build basic CRUD APIs with authentication
- **Mid-Level Engineer**: Designs scalable APIs with comprehensive documentation
- **Senior Engineer**: Implements API gateways, microservices coordination
- **Architect**: Defines API standards, cross-team governance, cloud-native APIs

## REST API Design Principles

### Richardson Maturity Model
- **Level 0**: RPC-style with single URI endpoint (SOAP, XML-RPC)
- **Level 1**: Resource identification with multiple URIs
- **Level 2**: HTTP verbs with proper status codes and headers
- **Level 3**: HATEOAS with hypermedia controls and discoverability

### HATEOAS Implementation
- Hypermedia as the Engine of Application State
- Self-describing messages with link relations
- API discoverability without prior knowledge
- Runtime client navigation through links

### RFC 7807 Problem Details
- Standardized error response format
- Machine-readable error information
- Problem type URIs and extension members
- Content negotiation for error formats

## Advanced REST Patterns

### Pagination Strategies
- **Offset-based**: `?page=2&limit=20` - Simple but performance issues with large offsets
- **Cursor-based**: `?cursor=abc123&limit=20` - Efficient for real-time data
- **Seek method**: `?seek=2024-01-01&limit=20` - Database-efficient for time-series

### Filtering & Searching
- Query parameter filters: `?status=active&category=electronics`
- Complex expressions: `?price[gte]=100&price[lte]=500`
- Full-text search: `?q=laptop&fields=name,description`
- Security considerations for dynamic filters

### Sorting & Field Selection
- Multi-field sorting: `?sort=name,-price,created_at`
- Sparse fieldsets: `?fields=id,name,price` to reduce payload
- Related resource inclusion: `?include=category,reviews`

### Bulk Operations
- Batch requests: Multiple operations in single request
- Partial failures: Atomic vs non-atomic batch processing
- Response aggregation: Individual operation results
- Rate limiting considerations for bulk endpoints

### Idempotency Keys
- Safe retry mechanisms for network failures
- Server-side idempotency key storage and validation
- Time-to-live for key expiration
- Conflict resolution for concurrent requests

### Conditional Requests
- ETag headers for resource versioning
- If-Match/If-None-Match preconditions
- Last-Modified/If-Modified-Since for time-based conditions
- Optimistic concurrency control implementation

## gRPC & Protocol Buffers

### Protocol Definition
- .proto file syntax and structure
- Service definitions with RPC methods
- Message types and field definitions
- Import statements and package organization

### Code Generation
- Multi-language client and server stubs
- Language-specific naming conventions
- Build integration and dependency management
- Generated code customization and extension

### Streaming Patterns
- Unary RPC: Simple request-response
- Server streaming: Server sends multiple messages
- Client streaming: Client sends multiple messages
- Bidirectional streaming: Both send messages independently

### Interceptors & Middleware
- Authentication interceptors for security
- Logging and metrics collection
- Request/response transformation
- Error handling and retry logic

### Load Balancing & Service Discovery
- Client-side load balancing algorithms
- Service registry integration
- Health checking and circuit breakers
- Connection pooling and multiplexing

### Error Handling
- gRPC status codes and error details
- Custom error messages and metadata
- Deadline exceeded and cancellation handling
- Retry policies and backoff strategies

## GraphQL Schema Design

### Schema Definition Language
- Type system: Object, Interface, Union, Enum, Scalar types
- Schema structure: Query, Mutation, Subscription roots
- Field definitions with arguments and return types
- Directives for metadata and behavior modification

### Query Optimization
- N+1 query problem identification and resolution
- DataLoader pattern for batch loading
- Caching strategies at field and query levels
- Query complexity analysis and limiting

### Mutation Design
- Input object types for mutation arguments
- Payload types for mutation responses
- Error handling in mutation results
- Transaction boundaries and consistency

### Subscription Implementation
- Real-time data streaming over WebSocket
- Subscription filtering and authorization
- Connection management and cleanup
- Scalability considerations for pub/sub

### Schema Evolution
- Backward compatible changes (adding fields)
- Breaking changes identification and planning
- Deprecation warnings and migration guides
- Schema versioning strategies

### Federation Architecture
- Schema stitching for microservices
- Gateway implementation and routing
- Cross-service type references
- Entity ownership and responsibility

## Asynchronous API Patterns

### Webhooks Implementation
- Callback URL registration and validation
- Event payload signing and verification
- Retry policies with exponential backoff
- Webhook delivery tracking and analytics

### Server-Sent Events (SSE)
- Event stream establishment and connection management
- Event formatting and data serialization
- Client reconnection handling
- Browser compatibility and fallbacks

### WebSocket Communication
- Connection handshake and protocol upgrade
- Message framing and binary/text data
- Heartbeat and ping/pong for connection health
- Connection pooling and scaling strategies

### CloudEvents Standard
- Standardized event format across platforms
- Event metadata and context attributes
- Routing and filtering capabilities
- Multi-protocol event transport

### Event-Driven APIs
- Publish-subscribe messaging patterns
- Event sourcing integration
- CQRS read model updates
- Eventual consistency handling

### Long Polling
- Connection management and timeout handling
- Server resource allocation
- Fallback strategies for older clients
- Performance implications and alternatives

## API Documentation & Developer Experience

### OpenAPI Specification
- Schema definition with accurate type information
- Request/response examples and schemas
- Authentication requirements documentation
- API versioning and deprecation indicators

### Interactive Documentation
- Swagger UI for API exploration and testing
- ReDoc for comprehensive documentation presentation
- Try-it-out functionality for endpoint testing
- Code generation for multiple languages

### SDK Generation
- Automatic client library generation
- Language-specific SDKs with proper types
- Version management and distribution
- Documentation integration

### Developer Onboarding
- Getting started guides with authentication
- Code examples in popular languages
- Common use cases and integration patterns
- Troubleshooting and support resources

### API Changelog Management
- Version history and change documentation
- Breaking changes announcement and migration guides
- Deprecation timelines and communication
- Community notification strategies

## API Lifecycle Management

### Versioning Strategies
- URL path versioning: `/api/v1/`, `/api/v2/`
- Header-based versioning: `Accept-Version` header
- Content negotiation: `Accept` header with media types
- Semantic versioning for API evolution

### Deprecation Process
- Feature announcement and communication
- Migration period definition and support
- Sunset timeline and final removal
- Backward compatibility maintenance

### Rate Limiting & Abuse Prevention
- Request quota management per user/API key
- Burst vs sustained rate limiting
- Fair usage policies and tier definitions
- Abuse detection and automated blocking

### Analytics & Monitoring
- Usage metrics collection and analysis
- Performance monitoring and bottleneck identification
- Error rate tracking and alerting
- Geographic and temporal usage patterns

### Monetization Strategies
- Usage-based pricing models
- Subscription tiers and feature access
- API key management and rotation
- Billing integration and reporting

### API Governance
- Design standards and review processes
- Documentation quality assurance
- Security and compliance requirements
- Cross-team collaboration and ownership
