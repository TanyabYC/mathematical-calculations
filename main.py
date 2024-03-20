# Import required to exit the application/program
import sys

# Creating a PI constant variable
PI = 3.14159


# Function to check whether the parameter number is a palindrome
def is_palindrome(num):

    # Create and initialise variables
    number = str(num)
    reverse = ""

    # Loop through the number string in reverse to assign the character found at the index to reverse
    for index in reversed(range(0, len(number))):
        reverse += number[index]

    # Return false unless the number and reverse variables are the same
    return number == reverse


# Function to calculate and return the area of a square
def area_square(square_width):

    # Calculate and return the result
    return square_width * square_width


# Function to calculate and return the area of a circle
def area_circle(circle_radius):

    # Calculate and return the result
    return PI * (circle_radius * circle_radius)


# Function to display the menu and return the option chosen by the user
def display_menu():

    # Display menu
    print("Calculations")

    print("1. Calculate area of a square")

    print("2. Calculate area of a circle")

    print("3. Display palindromes up to 1,000")

    print("4. Exit")

    # Get the menu option from the user
    option = input("Enter an option: ")

    # Return the menu option chosen by the user
    return option


# Create and initialise a variable to indicate whether a task is completed
taskCompleted = False

# Loop while the task is not completed
while not taskCompleted:

    # Add white space before the menu display
    print()

    # Display menu and get the menu option chosen by the user
    menu_option = display_menu()

    # Error checking menu option entered by user - must be a valid number
    if menu_option == "1" or menu_option == "2" or menu_option == "3" or menu_option == "4":

        menu_option = int(menu_option)

        # Display the area of a square to the user
        if menu_option == 1:
            # Heading
            print("\n**** Area of a square ***")

            # Retrieve width from the user
            width = int(input("Enter width of square (cm): "))

            print("The area of a square of " + str(width) + "cm = " + str(area_square(width)) + "cm squared")

        # Display the area of a circle to the user
        if menu_option == 2:
            # Heading
            print("\n**** Area of a circle ****")

            # Retrieve radius from the user
            radius = float(input("Enter radius of circle (cm): "))

            print("The area of a circle of " + str(radius) + "cm = " + str(area_circle(radius)) + "cm squared")

        # Display palindrome numbers to the user
        if menu_option == 3:

            # Heading
            print("\n**** Palindromes ****")

            # Loop through number range of 0 to 1000
            for i in range(1001):

                # Check whether index number is a palindrome number
                if is_palindrome(i):
                    # Display palindrome number to the user
                    print(i)

        # Exit the application
        if menu_option == 4:
            # Exit the while loop
            taskCompleted = True

    # Menu option chosen by the user is invalid
    else:
        print("\nOops! Incorrect option entered!\nPlease enter a valid number.")

# Close the application
print(sys.exit("You have exited the application!"))
