# ملف: match_case_calculator.py

# استقبل الرقمين من المستخدم
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# استقبل العملية اللي عايز يعملها المستخدم
operation = input("Choose the operation (+, -, *, /): ")

# استخدم match case لتنفيذ العملية
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation selected.")