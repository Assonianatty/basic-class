students = {}  # Dictionary: { "Alice": [90, 85], "Bob": [70] }
def add_student():
    name = input("Enter student name: ")
    if name in students:
        print("Student already exists!")
    else:
        students[name] = []
        print(f"Student '{name}' added.")

def add_grade():
    name = input("Enter student name: ")
    if name not in students:
        print("Student not found!")
        return
    try:
        grade = float(input("Enter grade (0-100): "))
        if 0 <= grade <= 100:
            students[name].append(grade)
            print(f"Grade {grade} added for {name}.")
        else:
            print("Grade must be between 0 and 100.")
    except ValueError:
        print("Invalid input! Please enter a number.")

def calculate_averages():
    averages = {}
    for name, grades in students.items():
        if grades:
            averages[name] = sum(grades) / len(grades)
        else:
            averages[name] = 0
    return averages

def highest_average():
    averages = calculate_averages()
    if not averages:
        print("No students available.")
        return
    top_student = max(averages, key=averages.get)
    print(f"Top Student: {top_student} with average {averages[top_student]:.2f}")

def display_all():
    if not students:
        print("No students to display.")
        return
    print("\n=== Student Grades ===")
    print(f"{'Name':<15}{'Grades':<25}{'Average':<10}")
    print("-" * 50)
    averages = calculate_averages()
    for name, grades in students.items():
        grade_list = ", ".join(map(str, grades)) if grades else "No grades"
        print(f"{name:<15}{grade_list:<25}{averages[name]:<10.2f}")

def main():
    while True:
        print("\n=== Student Grade Tracker ===")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Calculate Averages")
        print("4. Find Top Student")
        print("5. Display All")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_grade()
        elif choice == "3":
            avgs = calculate_averages()
            for name, avg in avgs.items():
                print(f"{name}: {avg:.2f}")
        elif choice == "4":
            highest_average()
        elif choice == "5":
            display_all()
        elif choice == "6":
            print("👋 Exiting Student Grade Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")

# Run program
main()