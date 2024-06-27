# Write python program that user to enter only odd numbers, else will raise an exception.


def get_odd_number():
    while True:
        try:
            number = int(input("Enter an odd number: "))
            if number % 2 == 0:
                raise ValueError("Entered number is even. Please enter an odd number.")
            else:
                return number
        except ValueError as ve:
            print(ve)

# Example usage
try:
    odd_number = get_odd_number()
    print(f"Entered odd number is: {odd_number}")
except KeyboardInterrupt:
    print("\nUser interrupted the input process.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
