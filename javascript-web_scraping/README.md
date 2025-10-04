# JavaScript - Web Scraping

## Description
This project introduces the concept of **web scraping** using JavaScript. You will learn how to read and write files, make HTTP requests, and process JSON data using Node.js. The project also demonstrates how to interact with APIs such as the **Star Wars API (SWAPI)** and **JSONPlaceholder**.

## Learning Objectives
By the end of this project, you should be able to:
- Explain why JavaScript programming is amazing.
- Manipulate and parse JSON data.
- Use the `request` module and the Fetch API to make HTTP requests.
- Read and write files using the `fs` (File System) module in Node.js.

## Requirements
- All files will be interpreted on **Ubuntu 14.04 LTS** using **Node.js (version 10.14.x)**.
- Your code should be **semistandard** compliant.
- All files must be executable and end with a new line.
- The first line of all your files should be:
  ```
  #!/usr/bin/node

  ```
- You are **not allowed** to use `var`.

## Setup Instructions

### Install Node.js 10

curl − sLhttps ://deb.nodesource.com/setup_10.x|sudo − Ebash − sudo apt-get install -y nodejs


### Install semistandard

$ sudo npm install semistandard --global


### Install request module

sudonpminstallrequest −−global export NODE_PATH=/usr/lib/node_modules


> **Note:** The `request` module has been deprecated since February 2020, but it remains a simple and effective tool for learning web scraping.

---

## Project Tasks

### 0. Readme
**File:** `0-readme.js`  
Reads and prints the content of a file.  
- The first argument is the file path.  
- The file is read in UTF-8.  
- If an error occurs, print the error object.

### 1. Write me
**File:** `1-writeme.js`  
Writes a string to a file.  
- The first argument is the file path.  
- The second argument is the string to write.  
- If an error occurs, print the error object.

### 2. Status code
**File:** `2-statuscode.js`  
Displays the status code of a GET request.  
- The first argument is the URL to request.  
- Prints: `code: <status code>`.

### 3. Star wars movie title
**File:** `3-starwars_title.js`  
Prints the title of a Star Wars movie by episode number.  
- The first argument is the movie ID.  
- Uses the API: `https://swapi-api.alx-tools.com/api/films/:id`.

### 4. Star wars Wedge Antilles
**File:** `4-starwars_count.js`  
Prints the number of movies where the character “Wedge Antilles” (ID 18) appears.  
- The first argument is the API URL: `https://swapi-api.alx-tools.com/api/films/`.

### 5. Loripsum
**File:** `5-request_store.js`  
Gets the contents of a webpage and stores it in a file.  
- The first argument is the URL to request.  
- The second argument is the file path to store the response.  
- The file must be UTF-8 encoded.

### 6. How many completed?
**File:** `6-completed_tasks.js`  
Computes the number of tasks completed by user ID.  
- The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos`.  
- Only prints users with completed tasks.

---

## Repository Structure

alu-higher_level_programming/
└── javascript-web_scraping/
    ├── 0-readme.js
    ├── 1-writeme.js
    ├── 2-statuscode.js
    ├── 3-starwars_title.js
    ├── 4-starwars_count.js
    ├── 5-request_store.js
    ├── 6-completed_tasks.js
    └── README.md


---

## Author
**Alieu O. Jobe**
