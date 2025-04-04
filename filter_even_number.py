#filter even numbers from a list
# This function takes a list of numbers as input and returns a list of even numbers.

def filter_even_numbers():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    even_numbers = [num for num in numbers if num % 2 == 0]
    print("Even numbers:", even_numbers)

filter_even_numbers()