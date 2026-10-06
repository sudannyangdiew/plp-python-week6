# Question 1 - Safe Functions

# Function 1 - safe_divide
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


# Function 2 - safe_number
def safe_number(text):
    try:
        return int(text)
    except ValueError:
        return "Not a number"


# Function 3 - get_field
def get_field(learner, key):
    try:
        return learner[key]
    except KeyError:
        return "Field not found"


# Testing the functions
if __name__ == "__main__":
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(safe_number("42"))
    print(safe_number("abc"))

    learner = {"name": "Amina", "score": 82}
    print(get_field(learner, "score"))
    print(get_field(learner, "email"))
    