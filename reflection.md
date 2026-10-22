# Lab 5: Static Code Analysis — Reflection

### 1. What is static code analysis?

Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities, and style violations.

### 2. What are the purposes of Pylint, Bandit, and Flake8?

- **Pylint:** Checks code quality, naming conventions, documentation, and potential programming problems.
- **Bandit:** Identifies potentially insecure Python coding patterns.
- **Flake8:** Checks Python style and formatting issues.

### 3. What issues were identified and fixed?

The issues included a mutable default argument, unsafe use of `eval()`, a bare exception handler, missing docstrings, global-state handling, file-handling problems, an unused import, and naming and formatting violations.

### 4. How did static analysis improve the program?

Static analysis helped identify security risks, improve readability, eliminate style violations, and make the code easier to maintain. The final Pylint score was 10/10, Bandit reported no issues, and Flake8 reported no violations.

### 5. Why is static analysis important?

Static analysis helps developers identify potential problems early, improve code quality, reduce security risks, and maintain consistent coding standards.
