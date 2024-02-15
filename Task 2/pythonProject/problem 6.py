while True:
    try:
        user_input = float(input("Enter a number: "))  # Convert input to float
        break  # Break out of the loop if input is valid
    except ValueError:
        print("Error: Please enter a numeric value.")

print("You entered:", user_input)
