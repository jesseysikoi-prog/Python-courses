# Number Calculator in Python

def main():
    print("🔢 Simple Number Calculator 🔢")
    try:
        num = int(input("Enter a number: "))

        square = num ** 2
        cube = num ** 3

        # Factorial calculation
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i

        print(f"Square of {num} = {square}")
        print(f"Cube of {num} = {cube}")
        print(f"Factorial of {num} = {factorial}")

    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
