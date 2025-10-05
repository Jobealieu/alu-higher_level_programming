# JavaScript - Web jQuery

## Description
This project focuses on using **JavaScript** and **jQuery** to manipulate the DOM, handle events, and interact with APIs.  
You will learn how to make web pages dynamic without reloading the page, using jQuery’s simplified syntax and built-in methods.

---

## Learning Objectives
By the end of this project, you should be able to explain the following concepts without external help:

### General
- Why jQuery makes front-end programming easier.
- How to select HTML elements in JavaScript.
- How to select HTML elements using jQuery.
- The differences between `ID`, `class`, and `tag name` selectors.
- How to modify an HTML element’s style.
- How to get and update an HTML element’s content.
- How to manipulate the DOM.
- How to make `GET` and `POST` requests using jQuery Ajax.
- How to listen and bind to DOM and user events.

---

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on **Chrome (version 57.0)**
- All files should end with a new line
- A `README.md` file at the root of the folder is mandatory
- Code must be **semistandard** compliant with the flag `--global $`
  ```
  semistandard *.js --global $

  ```
- You must use **jQuery version 3.x**
- You are **not allowed to use `var`**
- The HTML page should **not reload** for each action (use DOM manipulation and Ajax)

---

## Importing jQuery
To include jQuery in your HTML file, add the following line inside the `<head>` tag:

html
<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>


---

## Project Structure

alu-higher_level_programming/
└── javascript-web_jquery/
    ├── 0-script.js
    ├── 1-script.js
    ├── 2-script.js
    ├── 3-script.js
    ├── 4-script.js
    ├── 5-script.js
    ├── 6-script.js
    ├── 7-script.js
    ├── 8-script.js
    ├── 9-script.js
    └── README.md


---

## Tasks Overview

### 0. No jQuery
- Update the text color of the `<header>` element to red using `document.querySelector`.

### 1. With jQuery
- Update the text color of the `<header>` element to red using the jQuery API.

### 2. Click and Turn Red
- Change the `<header>` text color to red when clicking `DIV#red_header`.

### 3. Add `.red` Class
- Add the class `red` to `<header>` when clicking `DIV#red_header`.

### 4. Toggle Classes
- Toggle between `red` and `green` classes on `<header>` when clicking `DIV#toggle_header`.

### 5. List of Elements
- Add a new `<li>Item</li>` to `UL.my_list` when clicking `DIV#add_item`.

### 6. Change the Text
- Update the `<header>` text to “New Header!!!” when clicking `DIV#update_header`.

### 7. Star Wars Character
- Fetch and display a Star Wars character’s name from the API:
  ```
  https://swapi-api.alx-tools.com/api/people/5/?format=json

  ```

### 8. Star Wars Movies
- Fetch and list all Star Wars movie titles from:
  ```
  https://swapi-api.alx-tools.com/api/films/?format=json

  ```

### 9. Say Hello!
- Fetch and display “hello” in French from:
  ```
  https://fourtonfish.com/hellosalut/?lang=fr

  ```
- The script must work even when imported from the `<head>` tag.

---

## Author
**Alieu O. Jobe**
