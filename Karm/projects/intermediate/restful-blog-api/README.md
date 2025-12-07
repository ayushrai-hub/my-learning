# Project: RESTful Blog API

**Difficulty:** Intermediate
**Time Estimate:** 16 hours
**Skills Tested:** REST API design, database relationships, authentication, API documentation

## Overview
Build a complete REST API for a blogging platform that allows users to create accounts, write blog posts, leave comments, and manage content. This project focuses on building a production-ready API with proper authentication, data validation, and comprehensive documentation.

## Learning Objectives
- [ ] Master REST API design principles and HTTP methods
- [ ] Implement user authentication and authorization with JWT
- [ ] Work with database relationships and foreign keys
- [ ] Create comprehensive API documentation
- [ ] Handle request validation and error responses
- [ ] Implement pagination and filtering for large datasets

## Requirements

### Functional Requirements
1. User registration and login with JWT authentication
2. CRUD operations for blog posts with categories and tags
3. Comment system allowing nested comments on posts
4. User profile management with avatar uploads
5. Search and filter posts by title, category, author, date
6. Like/vote system for posts and comments
7. Admin features for content moderation

### Technical Requirements
- **Framework:** FastAPI or Node.js with Express
- **Database:** PostgreSQL with SQLAlchemy or Prisma
- **Authentication:** JWT tokens with refresh token rotation
- **Validation:** Pydantic or Joi schemas
- **Documentation:** Auto-generated API docs (Swagger/OpenAPI)
- **Testing:** Integration tests with real database
- **Deployment:** Docker containerization

## Architecture

### System Design
```
blog_api/
├── models/           # Database models (User, Post, Comment, Category)
├── schemas/          # Request/response validation schemas
├── routers/          # API endpoint routers
├── auth/            # Authentication and authorization
├── database/        # Database connection and configuration
├── utils/           # Helper functions and utilities
├── tests/           # Integration tests
└── main.py          # FastAPI application entry point
```

### Database Schema
```
users
├── id (primary key)
├── username (unique)
├── email (unique)
├── password_hash
├── full_name
├── bio
├── avatar_url
└── created_at

posts
├── id (primary key)
├── title
├── slug (unique)
├── content (markdown)
├── excerpt
├── featured_image
├── status (draft/published)
├── user_id (foreign key)
├── category_id (foreign key)
├── created_at
└── updated_at

comments
├── id (primary key)
├── content
├── post_id (foreign key)
├── user_id (foreign key)
├── parent_id (self-reference for nested comments)
└── created_at
```

## Implementation Guide

### Phase 1: Setup & Foundation (4 hours)
1. **Project scaffolding** - Set up FastAPI project with Poetry/npm
2. **Database setup** - PostgreSQL schema with migrations
3. **Authentication** - JWT token generation and validation
4. **User model** - Registration and login endpoints

### Phase 2: Core Features (8 hours)
1. **Post CRUD** - Create, read, update, delete posts
2. **Comments** - Add comments to posts with nested structure
3. **Categories** - Organize posts into categories
4. **Search & filtering** - Query posts with multiple filters
5. **File uploads** - Handle image uploads for posts/avatars

### Phase 3: Enhancement & Security (4 hours)
1. **Pagination** - Implement cursor-based pagination
2. **Rate limiting** - Protect against abuse
3. **Input validation** - Comprehensive request validation
4. **Error handling** - Proper HTTP status codes and messages

## Testing Strategy

### Integration Tests
- Test user registration, login, JWT validation
- Test CRUD operations on posts and comments
- Test search and filtering functionality
- Test authentication requirements
- Test error responses and edge cases

### API Tests
- Use pytest with httpx for API endpoint testing
- Test JSON request/response validation
- Test database state changes
- Test concurrent user operations

## Success Criteria
- [x] User can register, login, and receive JWT tokens
- [x] User can create, edit, delete, and view blog posts
- [x] Posts support categories, tags, and draft/published states
- [x] Users can comment on posts with nested comment threads
- [x] API supports search and filtering with pagination
- [x] All endpoints require proper authentication
- [x] API validates all input data with helpful error messages
- [x] Complete OpenAPI documentation with examples
- [x] Comprehensive integration tests (>80% coverage)
- [x] Dockerfile for containerized deployment

## Bonus Challenges
- [ ] **Real-time Updates:** WebSocket integration for live comments
- [ ] **Email Notifications:** Send emails for new comments, posts
- [ ] **Markdown Support:** Render post content with markdown
- [ ] **Analytics:** Track post views, popular content
- [ ] **API Versioning:** Support multiple API versions

## API Endpoints

### Authentication
```http
POST /auth/register - User registration
POST /auth/login - User login
POST /auth/refresh - Refresh JWT token
GET /auth/me - Get current user profile
```

### Posts
```http
GET /posts - List posts with filtering/pagination
GET /posts/{id} - Get single post with comments
POST /posts - Create new post
PUT /posts/{id} - Update post
DELETE /posts/{id} - Delete post
GET /posts/search?q={query} - Search posts
```

### Comments
```http
GET /posts/{id}/comments - Get post comments
POST /posts/{id}/comments - Add comment to post
PUT /comments/{id} - Update comment
DELETE /comments/{id} - Delete comment
POST /comments/{id}/replies - Reply to comment
```

### Categories
```http
GET /categories - List all categories
POST /categories - Create category (admin only)
GET /categories/{id}/posts - Get posts in category
```

## Example Usage

```bash
# Get JWT token
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "johndoe", "password": "secret"}'

# Create a blog post
curl -X POST http://localhost:8000/posts \
  -H "Authorization: Bearer eyJ0eXAi..." \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Blog Post",
    "content": "# Hello World\nThis is my first post!",
    "category_id": 1,
    "status": "published"
  }'

# Get posts with pagination
curl "http://localhost:8000/posts?page=1&limit=10&category=tech"
```

## Portfolio Presentation

### GitHub README Structure
```markdown
# RESTful Blog API 📝

[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-blue.svg)](https://www.postgresql.org/)

A production-ready REST API for a blogging platform built with FastAPI.

## Features
- User authentication with JWT tokens
- CRUD operations for blog posts and comments
- Category-based post organization
- Search and filtering capabilities
- Comprehensive API documentation
- Docker containerization

## API Documentation
🌐 **Interactive API Docs:** http://localhost:8000/docs

## Installation
```bash
# Clone repository
git clone https://github.com/yourusername/blog-api.git
cd blog-api

# Install dependencies
poetry install

# Set up PostgreSQL database
createdb blog_api_dev

# Run migrations
alembic upgrade head

# Start server
uvicorn main:app --reload
```

## Testing
```bash
# Run tests
pytest

# Run with coverage
pytest --cov=blog_api --cov-report=html
```
```

### Demo Video Script (2 minutes)
1. **Intro (30s):** "I built a complete REST API for a blogging platform using FastAPI and PostgreSQL"
2. **Architecture (60s):** "Walk through the API structure, database schema, authentication flow"
3. **Demo (30s):** "Show creating posts, adding comments, searching content"

## Interview Talking Points
- "I designed a REST API following industry best practices with proper status codes and resource naming"
- "Implemented JWT authentication with refresh tokens for security"
- "Used FastAPI's automatic documentation generation to provide clear API contracts"
- "Structured the database with proper relationships and constraints"
- "Wrote comprehensive tests to ensure API reliability"

## Related Projects
- **Prerequisite:** Simple CRUD API with in-memory storage
- **Next Level:** Full-stack blog application with React frontend
- **Enterprise Version:** Multi-tenant blogging platform with admin panel
