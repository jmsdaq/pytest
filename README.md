## Pytest-Centric Backend Testing Project
Welcome! This repository is built to showcase **pytest-driven testing** for a modular backend application. Designed with a QA mindset, it emphasizes clean, structured unit testing and smooth CI/CD integration via GitLab pipelines.

## Highlights
- **Pytest-Focused Testing:** Comprehensive unit tests for business logic and RESTful API endpoints.
- **Modular Architecture:** Includes models for `User`, `Product`, and `ShoppingCart`, with Flask routes for user and cart management.
- **GitLab CI/CD:** Automated pipeline to run tests and generate actionable reports on every commit.

## Project Layout
```bash
.  
├── app/  
│   ├── __init__.py       # Initializes the Flask app  
│   ├── models.py         # User, Product, and Order models  
│   ├── routes.py         # REST API endpoints  
│   ├── shopping_cart.py  # ShoppingCart functionality  
├── tests/  
│   └── test_app.py       # Pytest test cases  
├── .gitlab-ci.yml        # GitLab CI/CD pipeline configuration  
├── requirements.txt      # Project dependencies  
└── README.md             # You're reading it now!  
```
## Setup
1. Clone the Repository:

```bash
git clone <repo_url>  
```
2. Install Dependencies:

```bash
pip install -r requirements.txt  
```

3. Run the Application:
```bash
python app.py
```

## Running Tests
- Run all tests:
```bash
pytest
```

- For detailed reports:
```bash
pytest -v --maxfail=1 --disable0warnings
```

## CI/CD Integration
The GitLab pipeline `(.gitlab-ci.yml)` ensures:

- Automated testing on every push.
- Easy integration of test reports for quick analysis.