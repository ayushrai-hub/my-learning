# Project: Personal Finance Tracker

**Difficulty:** Beginner
**Time Estimate:** 8 hours
**Skills Tested:** Python OOP, file I/O, data validation, basic statistics

## Overview
Build a personal finance tracking application that helps users manage their income and expenses. Users can add transactions, categorize spending, generate reports, and get insights into their spending habits. This project focuses on data management and simple analytics.

## Learning Objectives
- [ ] Learn object-oriented programming in Python
- [ ] Practice file input/output operations with JSON
- [ ] Implement data validation and error handling
- [ ] Create basic data analysis and reporting features
- [ ] Work with datetime objects and financial calculations

## Requirements

### Functional Requirements
1. Add income and expense transactions with categories
2. View all transactions with filtering by date/category
3. Generate monthly spending reports and summaries
4. Calculate budget vs actual spending
5. Export data to CSV for spreadsheet analysis
6. Set monthly budgets for different categories

### Technical Requirements
- **Language:** Python 3.8+
- **Storage:** JSON files for data persistence
- **Libraries:** json, datetime, csv (standard library), pandas for data analysis (optional)
- **Testing:** Unit tests for core functionalities
- **Documentation:** CLI help system and usage examples
- **Error Handling:** Invalid inputs, file operations, data corruption

## Architecture

### System Design
```
finance_tracker/
├── models/               # Data models (Transaction, Category)
├── storage/              # File operations (save/load data)
├── cli/                  # Command-line interface
├── reports/              # Report generation logic
├── budget/               # Budget management
├── tests/                # Unit tests
└── main.py               # Entry point
```

### Technology Stack
| Layer          | Technology      | Purpose              |
|----------------|-----------------|----------------------|
| Data Models    | Python classes  | Transaction/Category objects|
| Storage        | JSON            | Persistent data storage|
| CLI Interface  | argparse        | User interaction     |
| Data Analysis  | dictionaries    | Basic statistics     |
| Testing        | unittest        | Code validation      |

## Implementation Guide

### Phase 1: Setup & Foundation (2 hours)
1. **Create data models** - Transaction and Category classes
2. **Implement basic storage** - Save/load transactions to JSON
3. **Create CLI interface** - Command structure with subcommands
4. **Add transaction operations** - Add income/expense commands

### Phase 2: Core Features (4 hours)
1. **Transaction listing** - Display transactions with filtering
2. **Category management** - Add/edit/delete categories
3. **Basic reporting** - Monthly summaries and totals
4. **Budget setting** - Set limits per category

### Phase 3: Enhancement & Polish (2 hours)
1. **Advanced reporting** - Category breakdowns, trends over time
2. **Data export** - CSV export for external analysis
3. **Input validation** - Robust data validation and error messages
4. **User experience** - Progress indicators and confirmations

## Testing Strategy

### Unit Tests
- Test transaction creation and validation
- Test file save/load operations
- Test calculation functions (totals, averages)
- Test error handling for invalid data

### Integration Tests
- Test complete workflow: add transactions, generate report, export data
- Test CLI interface responses
- Test data persistence across sessions

### Manual Testing
- Test various transaction types and amounts
- Verify correct calculations and summaries
- Test edge cases (zero amounts, future dates)

## Success Criteria
- [x] Add/edit/delete transactions with proper validation
- [x] Categorize transactions and track spending by category
- [x] Generate monthly and category-specific reports
- [x] Set and track budgets against actual spending
- [x] Export transaction data to CSV format
- [x] Handle invalid inputs gracefully with helpful error messages
- [x] Code follows Python best practices and PEP 8
- [x] Includes unit tests for core business logic
- [x] Data persists between application restarts

## Bonus Challenges
- [ ] **Data Visualization:** Add simple charts using matplotlib
- [ ] **Recurring Transactions:** Support for automatic recurring income/expenses
- [ ] **Multi-Currency:** Support for different currencies with conversion
- [ ] **Goals:** Set and track financial goals (vacation fund, emergency savings)

## Example Usage

```bash
# Add income
finance_tracker add-income --amount 3000 --description "Monthly salary" --category "Work"

# Add expense
finance_tracker add-expense --amount 150 --description "Grocery shopping" --category "Food" --date 2024-01-15

# View transactions
finance_tracker list --month 2024-01

# Generate report
finance_tracker report --month 2024-01 --output monthly-report.txt

# Check budget status
finance_tracker budget-status
```

### Sample Output
```
📊 Monthly Report: January 2024
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 Total Income: $3,000.00
💸 Total Expenses: $850.00
💵 Net Amount: $2,150.00

📈 Category Breakdown:
• Work: $3,000.00 (income)
• Food: $250.00 (29.4% of expenses)
• Transportation: $350.00 (41.2% of expenses)
• Entertainment: $150.00 (17.6% of expenses)
• Utilities: $100.00 (11.8% of expenses)

🎯 Budget Status:
• Food: $250/$300 spent (83%) ✅
• Transportation: $350/$400 spent (88%) ✅
• Entertainment: $150/$200 spent (75%) ✅
```

## Portfolio Presentation

### GitHub README Structure
```markdown
# Personal Finance Tracker 💰

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)

A command-line application for tracking personal finances and spending habits.

## Features
- Track income and expenses with categories
- Monthly budget management and tracking
- Generate financial reports and summaries
- Export data to CSV for analysis
- Simple and intuitive CLI interface

## Installation
```bash
pip install -r requirements.txt
python main.py --help
```

## Usage
```bash
# Add a transaction
python main.py add-expense --amount 45.50 --description "Dinner" --category "Food"

# View monthly report
python main.py report --month 2024-01
```

## Demo
[Include terminal recording showing main features]
```

### Demo Video Script (90 seconds)
1. **Intro (20s):** "I built a personal finance tracker to help manage money and understand spending habits"
2. **Core Features (40s):** "Show adding transactions, viewing reports, checking budget status"
3. **Technical Demo (30s):** "Explain data persistence, error handling, and report generation"

### Blog Post Outline
- **Title:** "Building a Personal Finance Tracker: My Data Management Project"
- **Technical Challenges:** Handling currencies, date validation, report calculations
- **Learning Outcomes:** File I/O best practices, data validation patterns
- **Improvements:** Could add web interface, data visualization, cloud sync

## Related Projects
- **Prerequisite:** Basic Python calculator or simple data storage script
- **Next Level:** Web-based finance dashboard with database
- **Advanced Version:** Multi-user application with role-based access
