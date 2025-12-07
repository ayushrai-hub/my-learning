# 🗂️ Task Management CLI Tool - Build Specifications

> **Complete Build Guide**: A command-line task management application that demonstrates Python fundamentals, object-oriented design, file I/O, and CLI interface development.

**Skill Level:** Beginner → Intermediate
**Build Time:** 6-8 hours
**Portfolio Value:** ⭐⭐⭐⭐⭐ *Perfect for demonstrating practical Python skills*

---

## 🎯 PROJECT OVERVIEW

### What You'll Build
A fully functional command-line task management application that allows users to add, organize, track, and manage tasks through terminal commands. The application will persist data across sessions and provide rich functionality for personal productivity management.

### Business Requirements
**Target User:** Individual professionals who need a simple, effective way to track and manage their daily tasks and responsibilities.

**Key Features:**
- ✅ Task creation with titles, descriptions, and priority levels
- ✅ Task listing with filtering, sorting, and search capabilities
- ✅ Task completion tracking and status management
- ✅ Data persistence across application sessions
- ✅ Priority-based task organization and due date support
- ✅ User-friendly command-line interface with helpful feedback

### Core Objectives
- **Learn Python Fundamentals** - Variables, data types, control flow, functions, classes
- **Master CLI Development** - Command-line arguments, user interaction, colored output
- **Implement File I/O** - JSON serialization, data persistence, error recovery
- **Practice Best Practices** - Type hints, error handling, modular design, testing

---

## 📋 DETAILED REQUIREMENTS SPECIFICATION

### Functional Requirements

#### **Task Management Core**
1. **Add Tasks** ✅
   - Command: `python task_manager.py add "Task Title"`
   - Required: Title (1-200 characters)
   - Optional: Description, priority (low/medium/high/urgent), due date (YYYY-MM-DD)
   - Auto-generate: Unique ID, creation timestamp
   - Validation: Title required, future due dates only

2. **List Tasks** ✅
   - Command: `python task_manager.py list`
   - Display format: `[Status] Priority,ID: Title`
   - Filters: `--status pending|completed|overdue`, `--priority level`, `--search "term"`
   - Sorting: `--sort id|title|priority|created|due` (ascending/descending)
   - Show count and pagination for large lists

3. **Complete Tasks** ✅
   - Command: `python task_manager.py complete <task_id>`
   - Update status to "completed", refresh timestamp
   - Feedback: Success/warning messages
   - Validation: Task exists and isn't already completed

4. **Search Tasks** ✅
   - Command: `python task_manager.py search "keyword"`
   - Search title and description fields
   - Case-insensitive matching
   - Show match locations (title/description)

5. **Show Task Details** ✅
   - Command: `python task_manager.py show <task_id>`
   - Display: Full task information in formatted block
   - Include: Status, priority, timestamps, due date, description

6. **Delete Tasks** ✅
   - Command: `python task_manager.py delete <task_id>`
   - Confirm before deletion (optional)
   - Remove from data permanently

#### **Advanced Features**
7. **View Statistics** ✅
   - Command: `python task_manager.py stats`
   - Total tasks, completion percentages
   - Priority breakdown, overdue counts
   - Recent activity summary

8. **Mark Incomplete** ✅
   - Command: `python task_manager.py incomplete <task_id>`
   - Change completed tasks back to pending
   - Update timestamps appropriately

9. **Overdue Detection** ✅
   - Automatic overdue status for past-due tasks
   - Highlight in listings with warning indicators
   - Separate overdue from regular pending tasks

10. **Bulk Operations** ✅ (Optional bonus)
    - Clear all completed tasks: `python task_manager.py clear`
    - Bulk status updates for multiple tasks

---

### Technical Architecture

#### **What to Build:**

**File Structure:**
```
task-manager-cli/
├── README.md              # Your detailed documentation
├── requirements.txt       # Dependencies list
├── src/
│   ├── __init__.py       # Package initialization
│   ├── main.py           # Entry point (command-line interface)
│   ├── models.py         # Data models and enums
│   ├── storage.py        # File I/O operations
│   └── utils.py          # Helper functions and CLI utilities
├── tests/
│   ├── __init__.py
│   └── test_basic.py     # Basic functionality tests
├── tasks.json            # Data persistence file
└── .gitignore           # Ignore tasks.json and __pycache__
```

#### **Module Specifications:**

**1. Data Models (`models.py`):**
- **Task** class: Dataclass with id, title, description, priority, status, timestamps, due_date
- **PriorityLevel** enum: LOW, MEDIUM, HIGH, URGENT
- **TaskStatus** enum: PENDING, COMPLETED, OVERDUE
- **Methods:** `mark_completed()`, `mark_pending()`, `is_overdue()`, `update_priority()`

**2. Storage Layer (`storage.py`):**
- **TaskStorage** class: JSON file operations
- **Methods:** `save_tasks()`, `load_tasks()`, `_backup_corrupted_file()`
- **Features:** Atomic writes, data validation, error recovery, backup on corruption

**3. CLI Interface (`main.py`):**
- Use `argparse` for command-line parsing
- Implement all 7 core commands with subparsers
- Handle arguments: task_id (int), title (string), optional flags
- Validate inputs, provide helpful error messages

**4. Utilities (`utils.py`):**
- **ColorOutput** class: Detect terminal support, apply ANSI colors
- Date validation functions
- String formatting helpers
- Task statistics calculations

### Implementation Steps

#### **Phase 1: Core Data Structures (2 hours)**
1. Create `models.py` with Task class and enums
2. Implement basic Task methods and validation
3. Add JSON serialization/deserialization methods
4. Test data models independently

#### **Phase 2: File Storage (1.5 hours)**
1. Build `storage.py` with TaskStorage class
2. Implement save/load functionality
3. Add error handling and backup recovery
4. Test file operations with various scenarios

#### **Phase 3: Core CLI Operations (1.5 hours)**
1. Create `main.py` with argument parsing
2. Implement add, list, complete, delete commands
3. Add input validation and error messages
4. Test each command individually

#### **Phase 4: Advanced Features (1 hour)**
1. Implement search, show, and stats commands
2. Add filtering and sorting options
3. Include due date handling and overdue detection
4. Add color-coded output

#### **Phase 5: Polish & Testing (1 hour)**
1. Add comprehensive input validation
2. Implement help text and usage examples
3. Create basic tests for core functionality
4. Polish error messages and user experience

### Success Criteria Checklist

**✅ Core Functionality:**
- [ ] `python task_manager.py add "My first task"` works
- [ ] `python task_manager.py list` shows tasks correctly
- [ ] `python task_manager.py complete 1` updates task status
- [ ] `python task_manager.py delete 1` removes tasks
- [ ] All commands accept proper arguments and provide feedback

**✅ Data Persistence:**
- [ ] Tasks survive application restarts
- [ ] JSON file is created and properly formatted
- [ ] Corrupted files are backed up automatically
- [ ] Multiple tasks are stored and retrieved correctly

**✅ User Experience:**
- [ ] Clear help text with command examples
- [ ] Informative error messages for invalid inputs
- [ ] Consistent command-line interface
- [ ] Reasonable default values for optional parameters

**✅ Code Quality:**
- [ ] Type hints on all functions and parameters
- [ ] Docstrings for classes and methods
- [ ] Modular code organization
- [ ] PEP 8 compliant formatting

### Portfolio Presentation Value

**This project demonstrates:**
- **CLI Application Development**: Real-world command-line tools
- **Data Persistence**: File I/O with error recovery
- **Python Best Practices**: Type hints, dataclasses, enums
- **Error Handling**: Robust exception management
- **User Interface Design**: Command-line UX principles
- **Testing Fundamentals**: Unit test writing and validation

### Interview Discussion Points

**Technical Decisions:**
- Why dataclasses over regular classes?
- How does JSON serialization work?
- Why atomic file operations?

**Design Choices:**
- Module separation responsibilities
- Error handling strategies
- User input validation approach

**Scalability Considerations:**
- How would you handle 1000+ tasks?
- What changes for database storage?
- Multi-user support implications?

**Learning Takeaways:**
- Real-world CLI application development
- File system operations with Python
- Structured error handling patterns
- User experience design principles

---

**BUILD THIS PROJECT** - You'll create a fully functional task management tool that demonstrates practical Python skills, clean architecture, and professional development practices. The result will be portfolio-ready and interview-prepared! 🚀
