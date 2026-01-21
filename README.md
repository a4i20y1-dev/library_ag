# Agile Library Management System

This project is a simple Library Management System developed using Agile methodology. The system was implemented incrementally across three sprints and uses Python, Git, and unit testing to demonstrate core software engineering practices.

---

## Features

### Sprint-1
- Add new books with unique book IDs
- Prevent duplicate book entries

### Sprint-2
- Borrow a book
- Return a borrowed book
- Prevent borrowing of an already borrowed book

### Sprint-3
- Generate a formatted report showing:
  - Book ID
  - Title
  - Author
  - Status (available / borrowed)

---

## Technologies Used
- Python 3
- Git & GitHub
- unittest (Python testing framework)

---

## Project Structure

src/ - Application source code
tests/ - Unit tests
docs/ - User stories and traceability


## Running Tests

From the project root directory, run:

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v


Git Workflow

Feature branches were created for each sprint

Sprint branches were merged into main

Tags (v0.1, v0.2, v0.3) mark sprint releases

