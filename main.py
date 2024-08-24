# Function to register a new dorm.
def register_dorm():
    dorm_name = input("Enter the dorm name to register: ")
    lsu_id = input("Enter LSU ID number: ")
    password = input("Set your password: ")  
    security_question = input("Set your security question: ")
    security_answer = input("Set your security answer: ")

    # Store credentials with password and security answer...
    credentials[dorm_name] = {
        "LSUID": lsu_id,
        "password": password,
        "security_question": security_question,
        "security_answer": security_answer
    }
    print("Dorm registered successfully!")

# This stores the credentials in a dictionary.
credentials = {
    "example_dorm": {
        # LSUID contains an int.
        "LSUID": "12345678",
        "password": "password123",
        "security_question": "What is your favorite color?",
        "security_answer": "purple"
    }
}

# Validate dorm_name...
def login(dorm_name):
    if dorm_name not in credentials:
        print("Dorm not found.")
        return False

    # Validate LSUID (three attempts allowed) [Step 2].
    for attempt in range(3):
        lsuid = input("Enter your LSUID: ")

        # First if-else block with three elif statements
        if len(lsuid) != 9:
            print("LSUID must be 9 digits long.")
            return
        elif not lsuid.isdigit():
            print("LSUID must contain only numbers.")
            return
        elif lsuid[0] != '8':  # Additional check for the LSUID (e.g., starts with '8')
            print("LSUID must start with '8'.")
            return
        elif lsuid != credentials[dorm_name]["LSUID"]:
            print(f"Incorrect LSUID. Attempt {attempt + 1}")
        else:
            print("LSUID recognized")
            break
    else:
        print("Max LSUID attempts reached")
        return False

    # Validate password (three attempts allowed) [Step 3].
    for attempt in range(3):
        password = input("Enter your password: ")

        # Second if-else block with three elif statements
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            return
        elif password.isnumeric():
            print("Password cannot be all numbers.")
            return
        elif password.islower():  # Additional check for password (e.g., must include an uppercase letter)
            print("Password must contain at least one uppercase letter.")
            return
        elif password != credentials[dorm_name]["password"]:
            print(f"Incorrect password. Attempt {attempt + 1}")
        else:
            print("Password accepted")
            break
    else:
        print("Max password attempts reached")
        return False

    # Validate security question (three attempts allowed) [Step 4].
    print(credentials[dorm_name]["security_question"])
    for attempt in range(3):
        security_answer = input("Enter the answer to your security question: ")
        if security_answer == (credentials[dorm_name]["security_answer"]):
            print("Security answer accepted. Login successful!")
            return True
        else:
            print(f"Incorrect. Attempt {attempt + 1}")
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
