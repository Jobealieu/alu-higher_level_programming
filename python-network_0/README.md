
n - Network #0

This repository contains solutions to tasks related to HTTP requests and responses using Bash scripts. The tasks focus on using `curl` to interact with web servers and retrieve or manipulate data.

## Project Overview

This project is part of the ALU Higher-Level Programming curriculum. It introduces concepts related to HTTP, including:

- Understanding URLs, domains, and subdomains
- HTTP request methods (GET, POST, DELETE, etc.)
- HTTP response codes and headers
- Using `curl` to send requests and handle responses

## Requirements

- All scripts are written in Bash.
- Scripts must be tested on Ubuntu 20.04 LTS.
- Each script must be exactly 3 lines long.
- All scripts must be executable.
- The `curl` command is used in silent mode (`-s`).

## Tasks

### 0. cURL body size
Write a Bash script that:
- Takes in a URL as an argument.
- Sends a request to the URL.
- Displays the size of the response body in bytes.

**File:** `0-body_size.sh`

---

### 1. cURL to the end
Write a Bash script that:
- Sends a `GET` request to a URL.
- Displays the body of the response if the status code is `200`.

**File:** `1-body.sh`

---

### 2. cURL Method
Write a Bash script that:
- Sends a `DELETE` request to a URL.
- Displays the body of the response.

**File:** `2-delete.sh`

---

### 3. cURL only methods
Write a Bash script that:
- Takes in a URL.
- Displays all HTTP methods the server will accept.

**File:** `3-methods.sh`

---

### 4. cURL headers
Write a Bash script that:
- Sends a `GET` request to a URL.
- Includes a custom header: `X-HolbertonSchool-User-Id: 98`.
- Displays the body of the response.

**File:** `4-header.sh`

---

### 5. cURL POST parameters
Write a Bash script that:
- Sends a `POST` request to a URL.
- Includes two parameters: `email=test@gmail.com` and `subject=I will always be here for PLD`.
- Displays the body of the response.

**File:** `5-post_params.sh`

---

## Repository Structure


alu-higher_level_programming/
└── python-network_0/
    ├── 0-body_size.sh
    ├── 1-body.sh
    ├── 2-delete.sh
    ├── 3-methods.sh
    ├── 4-header.sh
    ├── 5-post_params.sh
    └── README.md


## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/alu-higher_level_programming.git
   cd alu-higher_level_programming/python-network_0

   ```

2. Make the scripts executable:
   ```bash
   chmod +x *.sh

   ```

3. Run the scripts:
   ```bash
   ./0-body_size.sh <URL>

   ```

## Author

This project is part of the ALU curriculum and was completed by Alieu O. Jobe.
