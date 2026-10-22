# Lab 5: Static Code Analysis — Issue Documentation

## Issues Identified and Fixed

| Issue                    | Type            | Description                                                                 | Fix Applied                                                                 |
| ------------------------ | --------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Mutable default argument | Bug             | The `dates=[]` argument could retain mutable state across function calls.   | Changed the default to `None` and initialized the list inside the function. |
| Unsafe `eval()`          | Security        | `eval()` could execute arbitrary Python expressions.                        | Replaced it with a restricted AST-based arithmetic evaluator.               |
| Bare exception           | Reliability     | `except: pass` silently ignored errors.                                     | Added explicit checks for student and book records.                         |
| Missing docstrings       | Maintainability | The module and functions lacked documentation.                              | Added descriptive docstrings.                                               |
| Global state handling    | Maintainability | Global reassignment made state harder to manage.                            | Used a configuration dictionary and updated the loan dictionary in place.   |
| File handling            | Reliability     | Files were manually opened and closed.                                      | Used context managers and explicit UTF-8 encoding.                          |
| Unused import            | Style           | The `os` import was unused.                                                 | Removed the import.                                                         |
| Naming and formatting    | Style           | The code contained a nonconforming function name and formatting violations. | Renamed `renewBook` to `renew_book` and corrected formatting.               |

## Final Analysis Results

- **Pylint:** 10.00/10
- **Bandit:** No issues identified.
- **Flake8:** No violations reported.
