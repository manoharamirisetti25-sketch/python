
print("===== SMART CAMPUS MANAGEMENT SYSTEM =====")

# Student records:
# [ID, Name, Attendance, Marks, Event, Resource, Quantity]

students = []

# Nested list for campus resources
resources = [
    ["Projector", 2],
    ["Laptop", 5],
    ["Sports Kit", 3]
]

while True:

    print("\n========== MAIN MENU ==========")
    print("1. Add Student")
    print("2. Register for Event")
    print("3. Allocate Resource")
    print("4. View Student Records")
    print("5. Campus Summary Report")
    print("6. View Available Resources")
    print("0. Exit")

    choice = input("Enter your choice: ")

    # 1. Add student
    if choice == "1":

        student_id = input("Enter Student ID: ")

        duplicate = False

        for student in students:
            if student[0] == student_id:
                duplicate = True

        if duplicate:
            print("Student ID already exists!")

        else:
            name = input("Enter student name: ")
            attendance = float(input("Enter attendance percentage: "))
            marks = float(input("Enter marks: "))

            if (0 <= attendance <= 100 and
                    0 <= marks <= 100):

                students.append([
                    student_id, name, attendance,
                    marks, "No", "None", 0
                ])

                print("Student added successfully!")

            else:
                print("Invalid attendance or marks!")

    # 2. Event registration
    elif choice == "2":

        student_id = input("Enter Student ID: ")
        found = False

        for student in students:

            if student[0] == student_id:
                found = True

                if student[4] == "No":
                    student[4] = "Yes"
                    print("Event registration successful!")

                else:
                    print("Student already registered!")

        if found == False:
            print("Student not found!")

    # 3. Resource allocation
    elif choice == "3":

        student_id = input("Enter Student ID: ")
        found = False

        for student in students:

            if student[0] == student_id:
                found = True

                if student[5] != "None":
                    print("Resource already allocated!")
                    break

                print("\nAvailable Resources:")

                for i in range(len(resources)):
                    print(i + 1, resources[i][0],
                          "- Available:", resources[i][1])

                resource_choice = int(
                    input("Choose resource number: ")
                )

                if 1 <= resource_choice <= len(resources):

                    resource = resources[resource_choice - 1]

                    if resource[1] > 0:

                        student[5] = resource[0]
                        student[6] = 1
                        resource[1] = resource[1] - 1

                        print("Resource allocated successfully!")

                    else:
                        print("Resource out of stock!")

                else:
                    print("Invalid resource choice!")

        if found == False:
            print("Student not found!")

    # 4. View student records
    elif choice == "4":

        print("\n========== STUDENT RECORDS ==========")

        if len(students) == 0:
            print("No student records available.")

        else:
            for student in students:

                sid, name, attendance, marks, event, resource, qty = student

                print("\nStudent ID:", sid)
                print("Name:", name)
                print("Attendance:", attendance, "%")
                print("Marks:", marks)
                print("Event Registered:", event)
                print("Allocated Resource:", resource)
                print("Resource Quantity:", qty)

    # 5. Campus summary report
    elif choice == "5":

        print("\n========== CAMPUS SUMMARY ==========")

        total_students = len(students)
        total_attendance = 0
        total_marks = 0
        event_count = 0
        allocated_count = 0

        for student in students:

            total_attendance += student[2]
            total_marks += student[3]

            if student[4] == "Yes":
                event_count += 1

            if student[5] != "None":
                allocated_count += 1

        print("Total Students:", total_students)

        if total_students > 0:
            print("Average Attendance:",
                  round(total_attendance / total_students, 2), "%")

            print("Average Marks:",
                  round(total_marks / total_students, 2))

        print("Event Registrations:", event_count)
        print("Students with Resources:", allocated_count)

        print("\nRemaining Campus Resources:")

        for resource in resources:
            name, quantity = resource
            print(name, ":", quantity)

    # 6. View available resources
    elif choice == "6":

        print("\n========== RESOURCE AVAILABILITY ==========")

        for resource in resources:
            name, quantity = resource
            print(name, ":", quantity)

    # 0. Exit
    elif choice == "0":

        print("Thank you for using Smart Campus System!")
        break

    else:
        print("Invalid choice! Please try again.")
