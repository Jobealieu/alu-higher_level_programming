# Python - Network #1

This project focuses on learning network programming in Python using `urllib` and `requests` packages to interact with web services and APIs.

## Description

This project covers fundamental concepts of network programming in Python, including:
- Fetching internet resources with urllib
- Decoding HTTP response bodies
- Using the requests package for HTTP operations
- Making various types of HTTP requests (GET, POST, PUT, etc.)
- Handling JSON data from external services
- Error handling for HTTP requests

## Learning Objectives

By the end of this project, you should be able to explain:
- How to fetch internet resources with the Python package `urllib`
- How to decode `urllib` body response
- How to use the Python package `requests`
- How to make HTTP GET requests
- How to make HTTP POST/PUT/etc. requests
- How to fetch JSON resources
- How to manipulate data from an external service

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- First line of all files should be exactly `#!/usr/bin/python3`
- Code should use PEP 8 style (version 1.7)
- All files must be executable
- All modules should have documentation
- Use `get()` method to access dictionary values
- Code should not be executed when imported (use `if __name__ == "__main__":`)

## Files

| File | Description |
|------|-------------|
| `0-hbtn_status.py` | Fetches status using urllib |
| `1-hbtn_header.py` | Displays X-Request-Id header value using urllib |
| `2-post_email.py` | Sends POST request with email parameter using urllib |
| `3-error_code.py` | Handles HTTP errors using urllib |
| `4-hbtn_status.py` | Fetches status using requests |
| `5-hbtn_header.py` | Displays X-Request-Id header value using requests |
| `6-post_email.py` | Sends POST request with email parameter using requests |
| `7-error_code.py` | Handles HTTP errors using requests |
| `8-json_api.py` | Interacts with JSON API for user search |
| `10-my_github.py` | Uses GitHub API with authentication |

## Usage Examples

### Task 0: Basic status fetch with urllib

bash
./0-hbtn_status.py

### Task 1: Get header value with urllib

bash
./1-hbtn_header.py https://intranet.hbtn.io

### Task 2: POST email with urllib

bash
./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com

### Task 8: Search API

bash
./8-json_api.py a

### Task 10: GitHub API

bash
./10-my_github.py username personal_access_token

## Resources

- [Quickstart with Requests package](https://requests.readthedocs.io/en/latest/user/quickstart/)
- [Requests package documentation](https://requests.readthedocs.io/en/latest/)
- [urllib documentation](https://docs.python.org/3/library/urllib.html)

## Author

**Alieu O. Jobe**
- GitHub: [Your GitHub username]
- Project: ALU Higher Level Programming

## Repository Information

- **GitHub repository**: `alu-higher_level_programming`
- **Directory**: `python-network_1`
- **School**: ALU (African Leadership University)
- **Instructor**: Guillaume, CTO at Holberton School

## Project Timeline

- **Start**: July 19, 2025 12:00 AM
- **End**: August 1, 2025 11:59 PM
- **Weight**: 1

---

*This project is part of the ALU Higher Level Programming curriculum focusing on network programming fundamentals in Python.*
