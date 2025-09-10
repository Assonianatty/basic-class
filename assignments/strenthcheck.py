def password_strength_checker():
    while True:
        password = input("Enter a password: ")

        # Criteria checks
        has_upper = False
        has_lower = False
        has_digit = False

        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True

        if len(password) < 8:
            print("Password must be at least 8 characters long.")
        elif not has_upper:
            print("Password must contain at least one uppercase letter.")
        elif not has_lower:
            print("Password must contain at least one lowercase letter.")
        elif not has_digit:
            print("Password must contain at least one number.")
        else:
            print("Strong password set successfully!")
            break

# Run the program
password_strength_checker()