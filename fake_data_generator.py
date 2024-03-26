from faker import Faker

fake = Faker()  # Create a Faker object for generating fake data

# Function to generate all types of fake data
def everything():
    print(fake.name(), ", ", fake.email(), ", ", fake.job(), ", ", fake.address())

# Display the options for generating fake data
print("--------- Generate ---------------")
print("1. Name")
print("2. Email")
print("3. Job")
print("4. Address")
print("5. Everything on the list")
print("----------------------------------")

# Prompt the user to choose an option
user_input = int(input("Choose Option (enter the number):- "))
print("----------------------------------")

# Dictionary to map user input to corresponding fake data generation functions
options = {
    1: fake.name(),
    2: fake.email(),
    3: fake.job(),
    4: fake.address(),
    5: everything
}

# Check if the user input is valid and generate the corresponding fake data
if user_input in options:
    result = options[user_input]  # Get the fake data generation function
    if user_input == 5:
        result()  # Generate everything if the user chooses option 5
    else:
        print(f"Result: {result}")  # Print the generated fake data (if its ofc not 5)
else:
    print("Please try again with a valid option.")  # Prompt the user to choose a valid option
