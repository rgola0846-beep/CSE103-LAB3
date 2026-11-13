# CSE103 Lab 3 — GitHub Collaboration & API Interaction

**Student:** Rohit  
**GitHub:** [rgola0846-beep](https://github.com/rgola0846-beep)  
**Repository:** https://github.com/rgola0846-beep/CSE103-LAB3

## Overview
This repository demonstrates Git repository setup, version tracking, GitHub collaboration workflows, Markdown documentation, debugging practices, and working with a public JSON API using Python.

## Project structure
```text
CSE103-LAB3/
├── README.md
├── .gitignore
├── CHANGELOG.md
├── MARKDOWN_GUIDE.md
├── main.py
├── api_client.py
├── sample_users.json
└── tests/
    └── test_api_client.py
```

## Requirements
- Python 3.9 or newer
- Internet connection only when running the live API request

## Run the Python examples
```bash
python main.py
python api_client.py
```

`api_client.py` requests the public JSONPlaceholder `/users` endpoint, displays selected fields, and saves the response to `users.json`. If the network is unavailable, it reports the error clearly.

## Lab coverage
- Q3.1: Create and manage Git repositories
- Q3.2: Track and commit changes
- Q3.3: Push projects to GitHub
- Q3.4: Create Markdown documentation
- Q3.5: Access public APIs and analyze JSON data
- Q3.6: Debug common programming and workflow errors

## Author
Rohit — CSE103 Lab 3
