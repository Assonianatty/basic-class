def grade_checker():
    try:
        score = int(input("Enter your score (0-100): "))

        if score < 0 or score > 100:
            print("Invalid input! Please enter a score between 0 and 100.")
            return

        if score >= 90:
            grade = "A"
            message = "Excellent work! You’ve mastered the material!"
        elif score >= 80:
            grade = "B"
            message = "Great job! Keep pushing for that A!"
        elif score >= 70:
            grade = "C"
            message = "Good effort! A little more practice and you’ll improve."
        elif score >= 60:
            grade = "D"
            message = "You passed, but keep working hard to get better."
        else:
            grade = "F"
            message = "Don’t give up! Study more and you’ll do better next time."

        print(f"Your grade: {grade}")
        print(message)

    except ValueError:
        print("Invalid input! Please enter a number.")

# Run the program
grade_checker()