## Python: Try-Except Practice

### Overview

In this project, you'll learn how to use the `try-except` block to catch and handle exceptions that pop up when you run your code.

A `try-except` block can help keep your script from crashing when the user enters incorrect or unexpected input.

### Coding

- Complete the practice scripts below
- Use comments to label each script in your `main.py` file

#### Doing Addition
One common problem when prompting users to enter numbers occurs when people input text instead of numbers. When you try to convert the input to an **integer**, you'll get a `ValueError`.

- Write a script that prompts the user to enter two **integers**
- In your `except` clause, catch the `TypeError` if either input value is not a number, and print a friendly error message that tells the user you were expecting a number
- Also add an `else` clause to your script underneath your `except` clause
- In your `else` clause, find the sum of the two integers and use an f-string to print and display the sum of the two numbers
- Test your script first by entering two numbers and then by entering some text instead of a number

