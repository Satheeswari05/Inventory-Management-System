
# Inventory Management System

## Project Overview
A Python-based Inventory Management System demonstrating
Object-Oriented Programming, custom exception handling,
file persistence, and automated unit testing.

## Features
- Add, view, update, search and delete products
- Electronics and Grocery product categories
- Inheritance, encapsulation and polymorphism
- Custom exception handling
- JSON and CSV data persistence
- Automated testing using pytest
- Code coverage measurement

## Technologies Used
- Python 3
- Object-Oriented Programming
- JSON
- CSV
- Pytest
- Pytest-Cov

## Project Structure
inventory/
    product.py
    inventory.py
    exceptions.py
    storage.py

data/
tests/
main.py
requirements.txt

## Installation

Install dependencies:

pip install -r requirements.txt

## Run Application

python main.py

## Run Tests

python -m pytest -v

## Check Code Coverage

python -m pytest --cov=inventory --cov-report=term-missing

## Test Results

- Total Tests: 30
- Passed: 30
- Failed: 0
- Code Coverage: 93%

## Author
Your Name
