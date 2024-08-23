# Function to register a new dorm.
def register_dorm():
    dorm_name = input("Enter the dorm name to register: ")
    # ASK FOR LSU ID (Step 2)
    # ASK FOR PASSWORD (Step 3)
    # ASK SECURITY QUESTION (Step 4)
    security_answer = input("Set your security answer: ")

# This stores the credentials in a dictionary.
# This can also be extended to a text file if we choose to do that.
credentials = {
    "example_dorm": {
        # LSUID contains an int.
        "LSUID": "12345678",
        "password": "password123",
        "security_question": "What is your favorite color?",
        "security_answer": "purple"
    }
}

    # Store credentials with password and security answer...
    credentials[dorm_name] = {
        "LSUID": lsuid,
        "password": password,
        "security_question": security_question,
        "security_answer": security_answer
    }
    print("Dorm registered successfully!")

# Validate dorm_name...
def login(dorm_name):
    if dorm_name not in credentials:
        print("Dorm not found.")
        return False

    # Validate LSUID (three attempts allowed) [Step 2]. 
        for attempt in range(3):
        lsuid = input("Enter your LSUID: ")

    # Validate password (three attempts allowed) [Step 3].
    for attempt in range(3):
        password = input("Enter your password: ")
        # CODE HERE

    # Validate security question (three attempts allowed) [Step 4].
      print(credentials[dorm_name]["security_question"])
    for attempt in range(3):
        security_answer = input("Enter the answer to your security question: ")
        if security_answer == credentials [dorm_name]["security_answer"]:
            print("Security answer accepted. Login successful!")
            return True
        else:
            print(f"Incorrect. Attempt {attempts + 1}")
else:
        print("Maximum attempts reached.")
        return False

# Step 1 
# This is a while loop that continues until the user is done.
while True:
    action = input("Type 'register' to register a dorm or 'login' to access a dorm: ").strip().lower()

# This captures user input.
    if action == 'register':
        # Calls the register_dorm function, registers a new dorm.
        register_dorm()
    elif action == 'login':
        dorm_name = input("Enter the dorm name to access: ")
        if login(dorm_name):
            print("Welcome to your dorm!")
        else:
            print("Login failed. Access denied.")
    else:
        print("Invalid option. Please try again.")

    # Contains a boolean.
    continue_prompt = input("Do you want to continue? (yes/no): ").strip().lower()
    if continue_prompt != 'yes':
        print("Goodbye!")
        break
