# Backend Engineering - Comprehensive Assessment

## Skill Overview
**Core Competencies:**
- API Design & Development
- Database Architecture & Optimization
- System Design & Scalability
- Security Implementation
- Performance Optimization
- Microservices Architecture

**Industry Expectations:**
| Level      | Expected Skills                    | Timeline  |
|------------|-----------------------------------|-----------|
| Junior     | CRUD APIs, basic databases, single microservices | 0-2 years |
| Mid-Level  | Complex APIs, database optimization, multiple services, scaling | 2-4 years |
| Senior     | System design, architecture decisions, performance, leadership | 4-7 years |
| Expert     | Platform architecture, innovation, team scaling, product strategy | 7+ years  |

---

## Level 1: Foundation Assessment (Junior)

### Theoretical Questions (10 questions)
1. **Question:** What is REST, and what are the key constraints?
   - **Answer Guide:** Stateless, cacheable, uniform interface, client-server separation. Most companies use REST incorrectly as any HTTP API.
   - **Scoring:** 5 - All key constraints, practical trade-offs

2. **Question:** Explain the differences between PUT, POST, and PATCH.
   - **Answer Guide:** POST creates, PUT replaces entirely, PATCH modifies partially. PUT should be idempotent, POST is not.
   - **Scoring:** 5 - Correct technical differences + use cases

3. **Question:** What are the main types of database relationships?
   - **Answer Guide:** One-to-one, one-to-many, many-to-many. When to use each type with real-world examples.
   - **Scoring:** 5 - All three types + practical scenarios

4. **Question:** How does database normalization work? Explain normal forms.
   - **Answer Guide:** 1NF (single values), 2NF (removes partial dependencies), 3NF (removes transitive dependencies). Trade-offs.
   - **Scoring:** 5 - Correct normal forms + performance implications

5. **Question:** What is ACID in databases?
   - **Answer Guide:** Atomicity, Consistency, Isolation, Durability. Examples of when BASE is preferred over ACID.
   - **Scoring:** 5 - All properties + event streaming example

6. **Question:** Explain OAuth 2.0 flow types.
   - **Answer Guide:** Authorization Code, Implicit, Resource Owner Password, Client Credentials. Security implications.
   - **Scoring:** 5 - Flow types + security considerations

7. **Question:** What is horizontal vs vertical scaling?
   - **Answer Guide:** Horizontal adds more machines, vertical adds more power to existing. Trade-offs and when to use each.
   - **Scoring:** 5 - Clear distinction + real-world examples

8. **Question:** How do you handle database migrations in production?
   - **Answer Guide:** Backward compatibility, rollbacks, zero-downtime deployments. Tools like Flyway/Liquibase.
   - **Scoring:** 5 - Zero-downtime approach + rollback strategy

9. **Question:** What is caching, and where can you cache in a web application?
   - **Answer Guide:** Client-side, CDN, web server, application, database. Cache invalidation strategies.
   - **Scoring:** 5 - All cache layers + invalidation problems

10. **Question:** Explain the concept of database indexing.
    - **Answer Guide:** B-tree structures, composite indexes, when to index, index maintenance costs.
    - **Scoring:** 5 - Technical details + performance trade-offs

### Code Reading Challenges (5 challenges)
```python
# Challenge 1: API Endpoint with Error Handling
@app.get("/users/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return {"user": user}
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
```

**Task:** Explain what happens when user_id=999 (user doesn't exist). What status code is returned? What error handling is in place?
**Success Criteria:** Correctly identifies 404 status, database connection errors return 500, proper logging.

### Debugging Exercises (3 exercises)
```python
# Bug: N+1 Query Problem
@app.get("/posts/{post_id}/comments")
def get_post_comments(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    comments = []
    for comment in post.comments:  # N+1 query issue
        comments.append({
            "id": comment.id,
            "text": comment.text,
            "author": comment.author.name  # Additional N queries
        })
    return comments
```

**Task:** Identify the performance problem and suggest two solutions.
**Expected Fixes:** Eager loading with joinedload() or selectinload(), or batch loading with contains_eager().

### Implementation Tasks (2 tasks, 30-60 min each)
**Task 1:** Build a REST API for a blog with posts and comments.
- **Requirements:** CRUD operations, foreign key relationships, error handling, input validation
- **Test Cases:** POST /posts → 201, GET /posts/1 → 200, GET /posts/999 → 404, POST /posts/1/comments
- **Success Criteria:** Working FastAPI app, proper status codes, no SQL injection, input validation

---

## Level 2: Intermediate Assessment (Mid-Level)

### Theoretical Questions (8 questions)
11. **Question:** How do you design for eventual consistency in distributed systems?
12. **Question:** What are CQRS and Event Sourcing patterns and when to use them?
13. **Question:** Explain database connection pooling and its benefits.
14. **Question:** How do you implement rate limiting in APIs?
15. **Question:** What is the difference between eager and lazy loading?

### Architectural Questions (5 questions)
16. **Question:** How would you design a notification system that handles 10M users?
17. **Question:** What database would you choose for time-series data vs graph data?
18. **Question:** How do you handle API versioning in microservices?

### Optimization Challenges (3 challenges)
**Challenge:** Optimize this query for 100k posts:
```sql
SELECT p.*, u.name, COUNT(c.id) as comment_count
FROM posts p
LEFT JOIN users u ON p.user_id = u.id
LEFT JOIN comments c ON p.id = c.post_id
WHERE p.created_at > '2024-01-01'
GROUP BY p.id, u.name
ORDER BY p.created_at DESC
LIMIT 20
```

### Integration Tasks (3 tasks)
**Task:** Implement JWT authentication with refresh tokens
**Task:** Add Redis caching layer to existing API
**Task:** Implement database transaction management

### Medium Projects (2 projects, 2-4 hours each)
**Project 1:** E-commerce API
**Project 2:** Chat application backend

---

## Level 3: Advanced Assessment (Senior)

### System Design Challenges (3 challenges)
**Challenge 1:** Design a URL shortener service like bit.ly that handles 1000 requests/second.
**Requirements:** High availability, short URLs, analytics, custom domains.

**Challenge 2:** Design a distributed file storage system like Dropbox.
**Requirements:** Files up to 1GB, versioning, sharing, offline sync.

### Performance Optimization (2 tasks)
**Task 1:** Optimize slow API endpoint from 5s to <200ms response time.
**Task 2:** Handle database migration for 100GB table with zero downtime.

### Complex Implementations (2 tasks)
**Task 1:** Implement Saga pattern for distributed transactions.
**Task 2:** Build a custom ORM for PostgreSQL.

---

## Level 4: Expert Assessment (Staff+/Principal)

### Comprehensive Architecture Design (1 challenge)
**Challenge:** Design the backend architecture for a social media platform like Twitter.

### Open-Ended Optimization (1 challenge)
**Challenge:** Optimize cloud costs by 50% for a high-traffic e-commerce site.

### Technical Leadership Scenario (1 scenario)
**Scenario:** Lead migration from monolith to microservices for a banking system.

---

## Project Portfolio Requirements

### Backend Engineer Projects

### Project 1: Task Management API
**Difficulty:** Beginner
**Time:** 12 hours
**Skills Tested:** REST API, Database, Authentication

**Overview:** Build a REST API for task management with user authentication, CRUD operations, and assignment features.

**Functional Requirements:**
1. User registration and login with JWT
2. Create, read, update, delete tasks
3. Assign tasks to users
4. API documentation with OpenAPI

**Technical Requirements:**
- **Language:** Node.js 20 or Python 3.12
- **Database:** PostgreSQL 15+
- **Testing:** Jest/Pytest with 80%+ coverage
- **Docs:** Swagger/OpenAPI
- **Auth:** JWT with refresh tokens

**Success Criteria:**
- [x] All endpoints working
- [x] Proper error handling
- [x] Authentication works
- [x] Database schemas correct
- [x] Tests pass

### Project 2: E-Commerce Backend
**Difficulty:** Intermediate
**Time:** 32 hours
**Skills Tested:** Complex API, Microservices, Performance

**Overview:** Build the backend for an e-commerce platform with products, orders, payments integration.

---

## Assessment Rubrics

### Scoring Guide (1-5 Scale)
**1 - Insufficient:** Cannot explain basic concepts, poor understanding
**3 - Competent:** Knows concepts, can implement basic features
**5 - Excellent:** Deep understanding, production-ready, best practices

### Mastery Indicators
- ✅ **When you've passed:** Can design and implement production APIs
- ✅ **Portfolio proof:** 3+ backend projects with real users
- ✅ **Interview readiness:** Can explain trade-offs, scale solutions
