def perform_operation(num1, num2, operation):
    result = 0
    match operation:
        case "add":
            result = num1 + num2
        case "subtract":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num2 == 0:
                error = "Cannot divide by zero"
                return error
            result = num1 /num2 
    return result