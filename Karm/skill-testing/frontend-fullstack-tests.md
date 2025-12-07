# Frontend Fullstack - Comprehensive Assessment

## Skill Overview
**Core Competencies:**
- React/Modern Framework Development
- Fullstack Integration & APIs
- State Management & Data Flow
- Performance Optimization
- Testing & Quality Assurance
- User Experience & Accessibility

**Industry Expectations:**
| Level      | Expected Skills                    | Timeline  |
|------------|-----------------------------------|-----------|
| Junior     | Component development, basic state, API integration | 0-2 years |
| Mid-Level  | Complex UIs, state management, fullstack features, performance | 2-4 years |
| Senior     | Architecture decisions, complex interactions, scalability, mentorship | 4-7 years |
| Expert     | Platform design, innovation, cross-team leadership, product strategy | 7+ years  |

---

## Level 1: Foundation Assessment (Junior)

### Theoretical Questions (10 questions)
1. **Question:** Explain React component lifecycle vs hooks.
   - **Answer Guide:** Class components have mounting/updating/unmounting phases, hooks use useEffect for side effects.
   - **Scoring:** 5 - Both lifecycles explained, when to use each

2. **Question:** What is the virtual DOM and why is it useful?
   - **Answer Guide:** Lightweight copy of real DOM, React compares changes efficiently. Batches updates for performance.
   - **Scoring:** 5 - Reconciliation algorithm explanation

3. **Question:** How do you manage state in React applications?
   - **Answer Guide:** useState for local, useReducer for complex, Context API for global, Redux/Zustand for app-level.
   - **Scoring:** 5 - All state management options + use cases

4. **Question:** Explain CSS specificity and the cascade.
   - **Answer Guide:** Inline > ID > class/pseudo > element/tag. !important overrides. Specificity wars create problems.
   - **Scoring:** 5 - Calculation examples + solutions (CSS modules, BEM)

5. **Question:** What are React keys and why are they important?
   - **Answer Guide:** Unique identifiers for list items, help React track which items changed/added/removed. Prevents rendering bugs.
   - **Scoring:** 5 - Reconciliation process explanation

6. **Question:** How do you handle forms in React?
   - **Answer Guide:** Controlled components (useState), uncontrolled (refs), libraries like React Hook Form for complex forms.
   - **Scoring:** 5 - Validation, performance considerations

7. **Question:** What is CORS and how do you handle it?
   - **Answer Guide:** Cross-origin restrictions, server sets headers. Preflight requests for non-simple requests.
   - **Scoring:** 5 - Security implications + solutions

8. **Question:** Explain responsive design principles.
   - **Answer Guide:** Mobile-first, fluid layouts, media queries, flexible images. CSS Grid/Flexbox for modern layouts.
   - **Scoring:** 5 - Breakpoint strategies + testing

9. **Question:** What are React hooks and rules of hooks?
   - **Answer Guide:** Functions like useState, useEffect. Only call at top level, only in React functions, not in loops/conditions.
   - **Scoring:** 5 - All rules + eslint plugin

10. **Question:** How do you optimize React app performance?
    - **Answer Guide:** React.memo, useMemo, useCallback, code splitting, lazy loading, virtualization for long lists.
    - **Scoring:** 5 - When to use each technique

### Code Reading Challenges (5 challenges)
```javascript
// Challenge 1: Component with useEffect Dependency
const UserProfile = ({ userId }) => {
  const [user, setUser] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const response = await fetch(`/api/users/${userId}`);
        if (!response.ok) throw new Error('User not found');
        const userData = await response.json();
        setUser(userData);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchUser();
  }, [userId]); // Key dependency

  if (error) return <div>Error: {error}</div>;
  if (!user) return <div>Loading...</div>;

  return <div>{user.name}</div>;
};
```

**Task:** What happens if we remove [userId] from dependencies? What if we add response to dependencies?
**Success Criteria:** Missing dependency causes stale closure bug, adding response creates infinite loop.

### Debugging Exercises (3 exercises)
```javascript
// Bug: State Update in Loop
const ShoppingCart = () => {
  const [items, setItems] = useState([]);

  const addItem = (item) => {
    items.push(item); // Bug: Direct state mutation
    setItems(items);
  };

  return (
    <div>
      {items.map(item => <div key={item.id}>{item.name}</div>)}
      <button onClick={() => addItem({id: 1, name: 'Apple'})}>Add Apple</button>
    </div>
  );
};
```

**Task:** Fix the bug and explain what was wrong.
**Expected Fixes:** Use functional update: setItems(prev => [...prev, item]). Array.push mutates original array.

### Implementation Tasks (2 tasks, 30-60 min each)
**Task 1:** Build a todo application with React.
- **Requirements:** Add/delete/complete todos, local storage, filter by status
- **Test Cases:** Add todo renders, toggle complete works, filter shows correct items
- **Success Criteria:** Working app, proper state management, no console errors

---

## Level 2: Intermediate Assessment (Mid-Level)

### Architectural Questions (5 questions)
11. **Question:** How do you structure a large React application?
12. **Question:** What state management solution for a complex app and why?
13. **Question:** How do you implement routing in a SPA?
14. **Question:** What are custom hooks and when to use them?

### Optimization Challenges (3 challenges)
**Challenge:** Optimize this slow-rendering component:
```javascript
const ProductList = ({ products }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const filtered = products.filter(p =>
    p.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div>
      <input value={searchTerm} onChange={e => setSearchTerm(e.target.value)} />
      {filtered.map(product => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
};
```

### Integration Tasks (3 tasks)
**Task:** Integrate React app with REST API
**Task:** Add authentication flow with protected routes
**Task:** Implement real-time updates with WebSocket

### Medium Projects (2 projects, 2-4 hours each)
**Project 1:** E-commerce Product Catalog
**Project 2:** Real-time Chat Interface

---

## Level 3: Advanced Assessment (Senior)

### System Design Challenges (3 challenges)
**Challenge 1:** Design a component library architecture for a design system.

### Performance Optimization (2 tasks)
**Task 1:** Reduce bundle size by 60% for a large React application.
**Task 2:** Optimize Time to Interactive for a complex dashboard.

### Complex Implementations (2 tasks)
**Task 1:** Build a custom router from scratch.
**Task 2:** Implement virtual scrolling for 100k items.

---

## Level 4: Expert Assessment (Staff+/Principal)

### Comprehensive Architecture Design (1 challenge)
**Challenge:** Design the frontend architecture for a SaaS application.

---

## Project Portfolio Requirements

### Frontend Engineer Projects

### Project 1: Task Management App
**Difficulty:** Beginner
**Time:** 16 hours
**Skills Tested:** React Fundamentals, State Management, API Integration

**Overview:** Build a modern task management application with drag-and-drop, categories, and deadlines.

**Functional Requirements:**
1. Create, edit, delete tasks with due dates
2. Drag-and-drop to reorder tasks
3. Filter by category and status
4. Real-time search
5. Dark/light theme toggle

**Technical Requirements:**
- **Framework:** React 18+ with TypeScript
- **Styling:** Tailwind CSS or styled-components
- **State:** Zustand or Redux Toolkit
- **Testing:** React Testing Library + Jest
- **Performance:** Bundle < 200KB

**Architecture:**
```
src/
├── components/
│   ├── ui/           # Reusable UI components
│   ├── tasks/        # Task-specific components
│   └── layout/       # Layout components
├── hooks/            # Custom hooks
├── stores/           # State management
├── utils/            # Helper functions
└── types/            # TypeScript types
```

**Success Criteria:**
- [x] All features working smoothly
- [x] No React console warnings
- [x] Mobile responsive
- [x] Accessibility compliant (WCAG 2.1)
- [x] Tests pass >85% coverage

### Project 2: E-Commerce Frontend
**Difficulty:** Intermediate
**Time:** 40 hours
**Skills Tested:** Complex State, Performance, Fullstack Integration

**Overview:** Build the frontend for a modern e-commerce platform with product search, cart, and checkout.

---

## Assessment Rubrics

### Scoring Guide (1-5 Scale)
**1 - Insufficient:** Basic React knowledge, many anti-patterns
**3 - Competent:** Solid fundamentals, modern patterns used correctly
**5 - Excellent:** Advanced patterns, performance optimization, clean architecture

### Mastery Indicators
- ✅ **When you've passed:** Can build complex React apps with good architecture
- ✅ **Portfolio proof:** 3+ fullstack projects with real users
- ✅ **Interview readiness:** Can explain React internals, trade-offs, performance
