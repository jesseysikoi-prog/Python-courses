try:
    num1, num2 = eval(input("Enter two numbers, separated by  comma : "))
    result = num1 / num2
    print("result is", result)
except ZeroDivisionError:
    print("Division by zero is error !!")
except SyntaxError:
    print("comma is missing, enter numbers separated by comma like this 1,2")
except:
    print("Wrong input")
else:
    print("no exception")
finally:
    print("This will excecute no matter what")