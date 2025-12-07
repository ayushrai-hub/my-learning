# 🧪 Programming Foundations - Comprehensive Assessment

## Skill Overview
**Core Competencies:**
- Python 3.12 syntax and semantics mastery
- Algorithmic thinking and problem decomposition
- Type safety with type hints and validation
- Memory management and performance optimization
- Testing and debugging proficiency

**Industry Expectations:**
| Level      | Expected Skills                    | Timeline  |
|------------|-----------------------------------|-----------|
| Junior     | Basic syntax, simple algorithms, debugging | 0-6 months |
| Mid-Level  | Complex data structures, optimization, testing | 6-18 months |
| Senior     | Architecture decisions, performance tuning, mentoring | 18-36 months |
| Expert     | System design, framework development, teaching | 3+ years  |

---

## Level 1: Foundation Assessment (Junior)

### Theoretical Questions (10 questions)
1. **What is the difference between `==` and `is` operators in Python?**
   - **Answer Guide:** `==` compares values, `is` compares object identity. Use `==` for value comparison, `is` for singleton checks. Never use `is` for string/numeric comparison.
   - **Scoring:** 5pts - Correct explanation of both operators and use cases

2. **Explain Python's variable scope resolution (LEGB rule).**
   - **Answer Guide:** Local → Enclosed → Global → Built-in. Variables are searched in this order. `global`/`nonlocal` keywords modify scope.
   - **Scoring:** 5pts - Complete explanation with examples

3. **What is the difference between lists and tuples in Python?**
   - **Answer Guide:** Lists are mutable, tuples immutable. Tuples can be dictionary keys. Lists have more methods. Performance: tuples slightly faster.
   - **Scoring:** 5pts - Covers mutability, use cases, performance

4. **Explain the concept of list comprehensions.**
   - **Answer Guide:** Concise way to create lists. `[expression for item in iterable if condition]`. More readable and often faster than loops.
   - **Scoring:** 5pts - Syntax, benefits, examples

5. **What are Python decorators and how do they work?**
   - **Answer Guide:** Functions that modify other functions. Syntax `@decorator`. Return wrapper function. Common uses: logging, caching, authentication.
   - **Scoring:** 5pts - Syntax, mechanism, practical uses

6. **Explain the difference between shallow and deep copying.**
   - **Answer Guide:** Shallow copy: new container, same object references. Deep copy: completely independent copy. Use `copy.copy()` vs `copy.deepcopy()`.
   - **Scoring:** 5pts - Mechanism difference and implications

7. **What is the purpose of `__init__.py` files?**
   - **Answer Guide:** Make directories Python packages. Can contain package initialization code. Enables relative imports.
   - **Scoring:** 5pts - Purpose and functionality

8. **Explain Python's garbage collection mechanism.**
   - **Answer Guide:** Reference counting + cyclic garbage collector. Automatic memory management. Can manually trigger with `gc.collect()`.
   - **Scoring:** 5pts - How it works, advantages

9. **What are context managers and when would you use them?**
   - **Answer Guide:** `with` statement objects. Implement `__enter__`/`__exit__`. Use cases: file handling, database connections, locks.
   - **Scoring:** 5pts - Purpose, implementation, examples

10. **Explain the difference between generators and regular functions.**
    - **Answer Guide:** Generators yield values incrementally using `yield`. Memory efficient for large sequences. Iterator protocol.
    - **Scoring:** 5pts - Syntax, behavior difference, use cases

### Code Reading Challenges (5 challenges)
```python
# Challenge 1: What does this function return for input [1, 2, 3, 2, 1]?
from collections import Counter

def find_duplicates(nums):
    seen = set()
    duplicates = []
    for num in nums:
        if num in seen:
            if num not in duplicates:
                duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

# Expected: [2]
# Logic: Uses set for O(1) lookups, list to maintain order and uniqueness
```

```python
# Challenge 2: What is the time complexity and output?
def process_list(items):
    result = []
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i] + items[j] == 10:
                result.append((i, j))
    return result

# Input: [2, 3, 7, 8, 5]
# Expected: [(0, 3), (1, 2), (2, 4)] - pairs that sum to 10
# Complexity: O(n²)
```

```python
# Challenge 3: Predict the output
def mystery_function(n):
    if n <= 1:
        return 1
    return n * mystery_function(n - 1)

print(mystery_function(5))

# Expected: 120 (5! = 5 × 4 × 3 × 2 × 1)
# This is factorial calculation using recursion
```

```python
# Challenge 4: What happens with this code?
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

c1 = Counter()
c2 = Counter()
print(Counter.get_count())  # ?

# Expected: 2
# Class variable shared among all instances
```

```python
# Challenge 5: Memory usage analysis
def create_matrix(n):
    return [[0] * n for _ in range(n)]  # Good

def create_matrix_bad(n):
    return [[0] * n] * n  # Bad - all rows reference same list!

# The bad version creates shared references - modifying one row affects all
```

**Success Criteria for Code Reading:**
- [ ] Identify the algorithm/purpose in plain English
- [ ] Determine time/space complexity
- [ ] Predict output for given inputs
- [ ] Point out potential bugs or improvements
- [ ] Explain why the approach is good/bad

### Debugging Exercises (3 exercises)
```python
# Exercise 1: Fix the infinite loop
def factorial_iterative(n):
    result = 1
    while n > 0:  # Bug: should be n > 1 or handle n=0,1
        result *= n
        n -= 1  # Bug: infinite loop if n negative
    return result

# Fixed version:
def factorial_iterative(n):
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers")
    result = 1
    while n > 1:  # Changed condition
        result *= n
        n -= 1
    return result
```

```python
# Exercise 2: Fix the type error
from typing import List

def sum_positive(numbers: List[int]) -> int:
    total = 0
    for num in numbers:
        if num > 0:
            total += num  # MyPy error: incompatible types
    return total

# Issue: total initialized as int=0, but could be sum of floats
# Fix: Change type annotation or ensure int inputs
def sum_positive(numbers: List[int]) -> int:
    return sum(num for num in numbers if num > 0)
```

```python
# Exercise 3: Fix the logical error
def is_palindrome(text: str) -> bool:
    text = text.lower().replace(" ", "")
    return text == text[::-1]  # This works!

# Wait, this one is actually correct. What would be a common mistake?
# Common mistake: forgetting to handle case sensitivity or spaces
# Another: not handling unicode properly
def is_palindrome_buggy(text: str) -> bool:
    return text == text[::-1]  # Missing preprocessing
```

**Success Criteria for Debugging:**
- [ ] Identify the specific problem (syntax/logic/performance)
- [ ] Explain why it fails with the given input
- [ ] Provide correct solution with explanation
- [ ] Suggest ways to prevent similar bugs (type hints, testing)

### Implementation Tasks (2 tasks, 30-60 min each)
**Task 1:** Word Frequency Analyzer (40 min)
- **Requirements:**
  - Implement function that takes text string and returns dict of word frequencies
  - Case insensitive, ignore punctuation, sort by frequency descending
  - Handle contractions properly (don't → don, t)
  - Use type hints and proper error handling

- **Test Cases:**
  ```python
  # Input: "Hello world! Hello Python. World world."
  # Expected: {'world': 3, 'hello': 2, 'python': 1}
  ```

- **Success Criteria:**
  - [ ] Handles punctuation correctly (!.,?)
  - [ ] Case insensitive matching
  - [ ] Sorts by frequency then alphabetically
  - [ ] Uses proper data structures (Counter recommended)
  - [ ] Includes docstring and type hints
  - [ ] Handles edge cases (empty string, single word)

**Task 2:** Shopping Cart System (50 min)
- **Requirements:**
  - Classes: Product, Cart, Customer
  - Add/remove products, calculate totals with tax
  - Apply discount codes (percentage or fixed amount)
  - Generate receipt with itemized breakdown
  - Input validation and error handling

- **Success Criteria:**
  - [ ] Product class with name, price, quantity validation
  - [ ] Cart class with add/remove/item counting methods
  - [ ] Tax calculation (assume 8.25% rate)
  - [ ] Discount system (percent: "SAVE10", fixed: "FIXED5")
  - [ ] Receipt formatting with proper alignment
  - [ ] Comprehensive error handling

---

## Level 2: Intermediate Assessment (Mid-Level)

### Architectural Questions (5 questions)
1. **Design a simple logging system that supports multiple log levels and outputs.**
   - Answer should cover: classes, enums for levels, strategy pattern for outputs
   - Include: file rotation, performance considerations

2. **Explain the trade-offs between different Python testing frameworks.**
   - pytest vs unittest vs doctest: productivity, features, learning curve

3. **How would you implement a thread-safe counter in Python?**
   - threading.Lock vs concurrent.futures vs asyncio considerations

4. **Design a configuration management system for a Python application.**
   - Environment variables, config files, validation, type safety

5. **Explain how to optimize memory usage in Python applications.**
   - Generators, __slots__, weak references, profiling tools

### Optimization Challenges (3 challenges)
**Challenge 1:** Optimize Fibonacci calculation
```python
# Naive recursive: O(2^n)
def fib_recursive(n):
    if n < 2:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# Optimize to O(n) time, O(1) space
# Hint: iterative approach
```

**Challenge 2:** Find most frequent element in list
```python
# O(n) time, O(n) space using Counter
# Optimize to O(n) time, O(1) extra space using Boyer-Moore algorithm
def majority_element(nums):
    # Return element appearing more than n/2 times
    # Hint: candidate elimination approach
```

**Challenge 3:** String processing optimization
```python
# Given list of strings, find all anagrams
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["ate","eat","tea"], ["nat","tan"], ["bat"]]

# Implement efficiently using character count signatures
```

### Integration Tasks (3 tasks)
**Task 1:** File Processor with Progress Tracking
- Process large text files (100MB+) line by line
- Show progress bar using tqdm
- Extract statistics: word count, line count, top 10 words
- Handle encoding detection and malformed lines

**Task 2:** HTTP Client with Retry Logic
- Implement robust HTTP client using requests
- Exponential backoff retry strategy
- Circuit breaker pattern for failing endpoints
- Async support for concurrent requests

**Task 3:** Data Validation Pipeline
- Build validation system for user registration
- Email format, password strength, uniqueness checks
- Rate limiting to prevent abuse
- Comprehensive error messages

### Medium Projects (2 projects, 2-4 hours each)

#### Project 1: Task Management CLI Application
**Difficulty:** Intermediate/Advanced
**Time:** 3 hours
**Skills Tested:** OOP, file I/O, data structures, error handling

**Requirements:**
- Command-line interface for task management
- Add, list, complete, delete, search tasks
- JSON persistence with backup system
- Priority levels and due dates
- Interactive menu system

**Technical Specifications:**
- Use dataclasses or Pydantic for data models
- Implement proper exception hierarchy
- Add progress saving and loading
- Include comprehensive tests
- CLI argument parsing with argparse

**Rubric:**
- [ ] Clean architecture with separation of concerns
- [ ] Comprehensive test coverage (>80%)
- [ ] Proper error handling and user feedback
- [ ] Efficient data structures and algorithms
- [ ] Well-documented code with type hints

#### Project 2: Simple Key-Value Store
**Difficulty:** Intermediate
**Time:** 4 hours
**Skills Tested:** Data structures, persistence, threading

**Requirements:**
- In-memory key-value store with persistence
- Basic operations: get, set, delete, exists
- TTL (time-to-live) support
- Snapshotting to disk on interval
- Concurrent access with thread safety

**Technical Specifications:**
- Use dictionary for storage
- Implement LRU cache for memory bounds
- JSON serialization for persistence
- Threading.Lock for concurrent access
- Background thread for periodic snapshots

---

## Level 3: Advanced Assessment (Senior)

### System Design Challenges (3 challenges)
**Challenge 1:** Design a URL Shortening Service
- Requirements: shorten URLs, redirect, analytics
- Scale: 1M+ URLs, high availability
- Technical considerations:
  - Database design (sharding, replication)
  - Caching strategy (Redis clusters)
  - Analytics aggregation
  - Rate limiting and abuse prevention

**Challenge 2:** Multi-Tenant Task Queue System
- Multiple applications sharing worker pool
- Priority queues, dead letter queues
- Monitoring and alerting
- Fair resource allocation

**Challenge 3:** Real-time Collaborative Editor
- Operational Transformation or CRDTs
- Conflict resolution strategies
- Performance at scale (100+ concurrent users)
- Offline-first capabilities

### Performance Optimization (2 tasks)
**Task 1:** Optimize Large File Processing
- Given 10GB CSV file with financial transactions
- Calculate daily totals and detect anomalies
- Memory usage < 500MB, processing time < 10 min
- Techniques: streaming, chunking, multiprocessing

**Task 2:** Database Query Optimization
- E-commerce product catalog with 1M+ products
- Complex filtering: category, price range, search terms
- Pagination with consistent ordering
- Response time < 100ms, handle 1000+ concurrent users

### Complex Implementations (2 tasks)
**Task 1:** Build a Plugin System
- Dynamic loading of Python modules
- Hook system for extensibility
- Configuration management
- Error isolation between plugins

**Task 2:** Implement a Simple ORM
- Basic CRUD operations mapping to SQL
- Relationship handling (one-to-many, many-to-many)
- Query building with method chaining
- Transaction support and connection pooling

---

## Level 4: Expert Assessment (Staff+/Principal)

### Comprehensive Architecture Design (1 challenge)
**Design a Complete Web Framework**
- Similar to Flask/Django but minimal
- Features: routing, middleware, templating, ORM
- Extensions system like Flask plugins
- Production deployment considerations

**Requirements Analysis:**
- URL routing with parameter extraction
- Request/response middleware pipeline
- Template engine with inheritance
- Database abstraction layer
- Session management and security
- Configuration and application lifecycle

### Open-Ended Optimization (1 challenge)
**Optimize Python Application Performance by 10x**
- Given a slow application (bottlenecks identified)
- Apply all available optimization techniques
- Profile before/after, document improvements
- Maintain code readability and maintainability

**Techniques to Apply:**
- Algorithm optimization
- Memory profiling and reduction
- Cython compilation for critical paths
- Concurrent processing where appropriate
- Database query optimization
- Caching strategies at multiple levels

### Technical Leadership Scenario (1 scenario)
**Lead a Code Review and Mentoring Session**

**Context:** Junior developer submitted a 200-line function with performance issues.

**Your Tasks:**
1. Identify all performance bottlenecks
2. Provide constructive feedback
3. Suggest multiple refactoring approaches
4. Explain trade-offs between solutions
5. Guide junior developer through improvements

**Evaluation Criteria:**
- Technical accuracy in problem identification
- Empathy and clear communication
- Multiple solution approaches
- Teaching effectiveness
- Code quality standards maintained

---

## Project Portfolio Requirements

### Project 1: E-Commerce Platform Backend
**Difficulty:** Advanced
**Time:** 40 hours
**Skills Tested:** Full-stack backend, databases, APIs, security, performance

**Overview:** Complete e-commerce backend with products, orders, payments, and admin panel.

**Functional Requirements:**
1. User registration and authentication (JWT)
2. Product catalog with search and filtering
3. Shopping cart and checkout process
4. Order management and fulfillment
5. Admin dashboard with analytics
6. Payment integration (Stripe/PayPal)
7. Email notifications and invoices
8. Inventory management and alerts

**Technical Requirements:**
- **Language/Framework:** Python 3.12, FastAPI 0.104, SQLAlchemy 2.0
- **Database:** PostgreSQL 16 with proper indexing and partitioning
- **Authentication:** JWT with refresh tokens, password hashing
- **Testing:** pytest with >80% coverage, integration tests
- **Documentation:** OpenAPI 3.0, comprehensive README
- **Performance:** <500ms response time, handle 10k+ concurrent users
- **Security:** HTTPS, input validation, SQL injection prevention
- **Monitoring:** Logging, metrics, health checks

**Success Criteria:**
- [ ] All authentication flows working correctly
- [ ] Product search returns results in <100ms
- [ ] Checkout process handles race conditions
- [ ] Admin dashboard shows real-time metrics
- [ ] Code follows repository patterns and is maintainable
- [ ] Comprehensive test suite with CI/CD pipeline

---

## Assessment Rubrics

### Scoring Guide (1-5 Scale)
**1 - Insufficient:**
- Major conceptual errors in Python fundamentals
- Cannot solve basic algorithmic problems
- Code is unreadable and poorly structured
- No understanding of testing or debugging

**3 - Competent:**
- Solid understanding of basic Python concepts
- Can solve most algorithmic problems with guidance
- Writes functional code with some best practices
- Basic debugging skills and testing awareness

**5 - Excellent:**
- Deep understanding of Python internals and best practices
- Consistently writes optimized, readable, well-tested code
- Excellent problem-solving skills with multiple approaches
- Can teach concepts and review code effectively

### Mastery Indicators
- ✅ **When you've passed:** Can build production-quality applications independently
- ✅ **Portfolio proof:** 5+ projects demonstrating full-stack capabilities
- ✅ **Interview readiness:** Confidently solve LeetCode medium/hard problems
- ✅ **Teaching ability:** Can explain concepts to beginners clearly

---

## Assessment Administration Guidelines

### Time Limits
- Level 1: 2 hours total
- Level 2: 4 hours total
- Level 3: 6 hours total
- Level 4: 8 hours (design/planning) + 1 week (implementation)

### Scoring Methodology
- **Theoretical Questions:** Binary (correct/incorrect) with partial credit
- **Code Reading:** Holistic evaluation of understanding
- **Debugging:** Process quality more important than final answer
- **Implementation Tasks:** 30% logic, 30% efficiency, 40% quality

### Certification Levels
- **Certified Junior Developer:** Pass Level 1 (70%+) + 2 projects
- **Certified Mid-Level Developer:** Pass Level 2 (75%+) + 4 projects
- **Certified Senior Developer:** Pass Level 3 (80%+) + 6 projects
- **Certified Expert Developer:** Pass Level 4 (85%+) + 8 projects

### Retake Policy
- Unlimited retakes allowed
- Must demonstrate improvement or new learning
- Previous results available for comparison
- Portfolio projects continuously updatable

### Recognition
- Digital certificates with unique IDs
- LinkedIn badge integration
- Employer-verifiable skill endorsements
- Access to exclusive Karm community and resources
