## Python Exceptions

Read the info below so you can:

1. understand what an *exception* is
2. what *handling an exception* means
3. what *throws* or *raises* an exception means
4. why handling exceptions is important

### What is an Exception?

In Python, an **exception** is an error that occurs when you run your script. When something goes wrong (e.g., the user tries to divide by zero, or attempts to access an item in a list that doesn’t exist), Python **throws/raises** an exception. 

### Handling Exceptions

To put it another way, an **exception** is a signal that something went wrong when the user tried to run your script.  As a programmer, you can **handle** (*manage* or *deal with*) specific types of exceptions.

### Why Handle Exceptions?

Exceptions are bad because they can cause your script to crash, and users quickly get frustrated when they run a script that keeps crashing.

As a programmer, you should try to (1) anticipate exceptions and (2) try to write code that can handle exceptions (so your script doesn't crash).

### Example of an Exception

Here’s a simple example of an exception:

```python
x = 5
y = 0
result = x / y  # This raises a ZeroDivisionError
print(result)
```

**Explanation:**
- When we attempt to divide by zero, Python raises a `ZeroDivisionError`. This is an exception that tells us we cannot divide a number by zero.
