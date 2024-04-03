def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    if 0 in numbers[1:]:
        return "Cannot divide by zero!"
    else:
        result = numbers[0]
        for num in numbers[1:]:
            result /= num
        return result

def calculator():
    print("Welcome to Calculator with Dynamic Memory!")

    memory = []

    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Memory Clear")
        print("6. Memory Recall")
        print("7. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Exiting calculator.")
            break

        if choice in ('1', '2', '3', '4'):
            numbers = input("Enter numbers separated by space: ").split()
            numbers = [float(num) for num in numbers]

            if choice == '1':
                print("Result:", add(numbers))
            elif choice == '2':
                print("Result:", subtract(numbers))
            elif choice == '3':
                print("Result:", multiply(numbers))
            elif choice == '4':
                print("Result:", divide(numbers))

            memory = numbers
        elif choice == '5':
            memory.clear()
            print("Memory cleared.")
        elif choice == '6':
            if memory:
                print("Memory Recall:", memory)
            else:
                print("Memory is empty.")
        else:
            print("Invalid Input! Please try again.")


calculator()
