# PLP Python Week 6: Error Handling Assignment

## Overview of Files

* `safe_tools.py` - Contains three defensive programming functions (`safe_divide`, `safe_number`, and `get_field`) that use `try/except` blocks to handle runtime exceptions (`ZeroDivisionError`, `ValueError`, and `KeyError`) gracefully without crashing.

## Reflection

### Why can an `if` check not catch `"abc"` on its own?

An `if` statement evaluates boolean conditions, but converting `"abc"` with `int("abc")` raises a runtime `ValueError` exception during execution before an `if` condition could even process the value. While an `if` statement can check string formats (e.g., using `.isdigit()`), it cannot prevent Python's built-in `int()` conversion function from raising an exception when handed invalid non-numeric text—making `try/except` the essential tool for catching runtime type conversion failures.
