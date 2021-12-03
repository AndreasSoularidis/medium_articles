import json

students = []

''' 
    Prints the menu of the program
'''
def print_menu():
    print("\n1. Insert Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Exit")


'''
    Inserts a new student in the system. The user insert manually the
    elements of the student.
'''
def insert_student():
    id = input("ID: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    semester = input("Semester: ")
    courses = []
    while True:
        new_course = input("Give the course title or -1 for exit: ")
        if new_course == "-1":
            break
        courses.append(new_course)

    student_dictionary = {
        "id" : id,
        "first_name": first_name,
        "last_name": last_name,
        "semester": semester,
        "courses" : courses
    }

    students.append(student_dictionary)


'''
    This methos find and return the student with the given id
    if there is no student with the given id the method returns None
'''
def find_student(id):
    for student in students:
        if student["id"] == id:
            return student
    # Student not found
    return None


'''
    This method print the data of the student. First call the find_student() method to find the student with
    the given id. If the returned student is not None, it prints the data of the student. 
    Otherwise print an appropriate message.
'''
def print_student_details(id):
    selected_student = find_student(id)

    if selected_student is not None:
        print(f"Student ID: {selected_student['id']}\t First Name: {selected_student['first_name']}\tLast Name: {selected_student['last_name']}\t Semester: {selected_student['semester']}")
    
        print("Courses in the current semester")
        for course in selected_student['courses']:
            print(course)
    else:
        print(f"Error: Student with ID {id} does not exist")


''' 
    This method find and delete the student with the given id
    If there is no student with a given id, an appropriate message is printed
'''
def delete_student(id):
    selected_student = find_student(id)

    if selected_student is not None:
        students.remove(selected_student)
        print(f"Error: Student with ID {id} deleted")
    else:
        print(f"Error: Student with ID {id} does not exist")


'''
    This method read the data from the students.json file that is stored in the same directory.
'''
def read_data():
    global students
    with open("students.json", mode = "r") as file:
        students = json.load(file)


'''
    This method store the data to the students.json file that is stored in the same directory.
'''
def store_data():
    with open("students.json", mode = "w") as file:
        json.dump(students, file)


'''
    This method is the main function of the program
'''
def main():

    while True:
        read_data()
        print_menu()
        try:
            choice = int(input("Enter yout choice: "))
        except ValueError:
            print("Invalid input. Please enter a number")
        else:
            if choice == 1:
                insert_student()
            elif choice == 2:
                id = input("Enter the ID of the student: ")
                print_student_details(id)
            elif choice == 3:
                id = input("Enter the ID of the student: ")
                delete_student(id)   
            elif choice == 4:
                store_data()
                print("Program terminated")
                break     
            else:
                print("Invalid input")


if __name__ == '__main__':
    main()



