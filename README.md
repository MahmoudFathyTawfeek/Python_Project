# csv Processor Project
This script processes csv data to print frist row.

# Features
- Virtual Environment (venv) setup.
- Dependency management via `requirements.txt`.
- CSV data parsing using `csv_processor.py`.

# How to Run
1. Activate the environment:
    source venv/Scripts/activate
2. Install requirements:
    pip install -r requirements.txt
3. Run the script:
    python csv_processor.py

============   Day 4 task =====================================================================================
task 1 - Read with curl
1. Public weather API
   - Method: GET
   - URL: https://wttr.in/Cairo?format=3
   - Status Code: 200 OK
   - Response Body: cairo: ☀️ +26°C  
2-Github user info
   - Method: GET
   - URL:  https://api.github.com/users/MahmoudFathyTawfeek
   - Status Code: 200 ok
   -Response Body:
         "login": "MahmoudFathyTawfeek",
         "id": 142318160,
         "node_id": "U_kgDOCHuaUA",
3-Redirect Chain
   - Method: GET
   - URL:  https://github.com/
   - Status Code: 200 ok
   - Response Body (frist 3 lines)
        <!DOCTYPE html>
        <html
        lang="en"
================================

 Task 2 - GitHub Explorer (Main Exercise)

In this task, I developed a Python script `github_explorer.py` to interact with the GitHub.

# Key Features:
1. Authentication: Uses a Personal Access Token (PAT) stored in an environment variable (`GITHUB_TOKEN`) for secure access.
2. Error Handling: The script gracefully handles authentication errors and API failures without crashing.
3. Pagination: Implemented a `while` loop to fetch all repositories by navigating through multiple pages (using `page` and `per_page` params).
4. Data Processing:
   - Fetched specific fields: `name`, `language`, `stargazers_count`, and `updated_at`.
   - Sorting: The output is automatically sorted by the number of stars in descending order.

# How to run:
1. Set the environment variable:
   ```bash
   export GITHUB_TOKEN="your_token_here"

======================================

Task 3 

request:
$ curl -i -X POST -d "custname=Mahmoud&size=Large&topping=cheese" https://httpbin.org/post

response:
{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "custname": "Mahmoud",
    "size": "Large",
    "topping": "cheese"
  },
  "headers": {
    "Accept": "*/*",
    "Content-Length": "42",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "curl/8.12.1",
    "X-Amzn-Trace-Id": "Root=1-69fcb559-3cd2c56452352c517781e368"
  },
  "json": null,
  "origin": "45.100.238.42",
  "url": "https://httpbin.org/post"
}
===========================================

# HTML Form vs. JSON Posting

1-What is the difference between submitting an HTML form and posting JSON?**
- **HTML Form:** Usually uses `application/x-www-form-urlencoded`. Data is sent as key-value pairs separated by `&` (e.g., `name=Mahmoud&age=25`). It is the native way browsers send data from `<form>` tags.
- **JSON Posting:** Uses `content-type: application/json`. Data is sent as a structured JSON object (e.g., `{"name": "Mahmoud", "age": 25}`). It is the standard for modern APIs and Single Page Applications (SPAs).

2-When would you use which?
- Use **HTML Forms** for simple, traditional web pages where the browser handles the submission directly.
- Use **JSON** when building modern APIs (like Frappe or REST APIs), mobile apps, or when you need to send complex/nested data structures that simple key-value pairs cannot handle easily.




