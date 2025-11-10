#Define the higher-order function (Map operation)
def apply_operation(numbers, operation):
    return [operation(number) for number in numbers]

#Define the helper function for the "Filter" example
def filter_list(numbers, condition):
    return [number for number in numbers if condition(number)]

my_numbers = [1, 2, 3, 4, 5]
print(f"Original list: {my_numbers}")

#Use lambda to double the numbers
doubled_numbers = apply_operation(my_numbers, lambda x: x * 2)
print(f"Doubled: {doubled_numbers}")

#Use lambda to square the numbers
squared_numbers = apply_operation(my_numbers, lambda x: x ** 2)
print(f"Squared: {squared_numbers}")

#Use the filter function with lambda to get odd numbers
odd_numbers = filter_list(my_numbers, lambda x: x % 2 != 0)
print(f"Filtered (odd numbers): {odd_numbers}")