# Initialize an empty dictionary to store student data
student_data = {}

# Function to add a new student
def add_student():
    roll_number = input("Enter student's roll number: ")
    name = input("Enter student's name: ")
    student_data[roll_number] = {'Name': name, 'Scores': {}}
    print(f"Student {name} with roll number {roll_number} has been added.")

# Function to add a score for a student
def add_score():
    roll_number = input("Enter student's roll number: ")
    if roll_number in student_data:
        subject = input("Enter subject: ")
        score = float(input("Enter score: "))
        student_data[roll_number]['Scores'][subject] = score
        print(f"Score {score} for {subject} has been added for {student_data[roll_number]['Name']}.")
    else:
        print("Student not found. Please add the student first.")

# Function to calculate the average score for a student
def calculate_average():
    roll_number = input("Enter student's roll number: ")
    if roll_number in student_data:
        scores = student_data[roll_number]['Scores']
        if scores:
            average = sum(scores.values()) / len(scores)
            print(f"Average score for {student_data[roll_number]['Name']} is {average:.2f}.")
        else:
            print("No scores available for this student.")
    else:
        print("Student not found. Please add the student first.")

# Main menu loop
while True:
    print("\nStudent Result Management System")
    print("1. Add Student")
    print("2. Add Score")
    print("3. Calculate Average Score")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        add_score()
    elif choice == '3':
        calculate_average()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
