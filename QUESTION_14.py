#    Can one block of except statements handle multiple exception?

""" 
Yes, in Python, you can use a single except block to handle multiple 
exceptions by specifying them as a tuple inside the except statement. 
This approach allows you to group similar exception types together and 
handle them with the same block of code. Here’s how you can handle multiple 
exceptions in a single except block:
"""

try:
    # Code that might raise exceptions
    x = int(input("Enter a number: "))
    result = 10 / x
except (ZeroDivisionError, ValueError):
    # Handle both ZeroDivisionError and ValueError
    print("Error: Invalid input or division by zero!")
except IOError:
    # Handle IOError separately
    print("Error: An IOError occurred.")
except Exception as e:
    # Handle any other exceptions not caught above
    print(f"Error: An unexpected error occurred: {str(e)}")
else:
    # Execute if no exceptions were raised
    print(f"Result: {result}")
finally:
    # Always execute after try/except, regardless of exceptions
    print("Execution complete.")
