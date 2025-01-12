def perform_operation(num1, num2, operation):
    """Performs basic arithmetic operations based on the operation argument."""
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        # Handling division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."
