#   When is the finally block executed?

""" 
After a try block: The finally block always executes after the 
execution of the try block, regardless of whether an exception was raised or not.

After an except block: If an exception is raised in the try block
 and caught by an except block, the finally block is executed after the except block.

After an else block: If no exceptions are raised in the try block, 
the else block (if present) executes, and then the finally block is executed.

"""


try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
else:
    print(f"Result: {result}")
finally:
    print("Execution complete.")
