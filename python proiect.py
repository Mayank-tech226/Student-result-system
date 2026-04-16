# Main list to store student records
# Each record will be: [Roll, Name, Marks1, Marks2, Marks3, Total, Percentage, Status]
student_database = []

def main():
    while True:
        print("\n================================")
        print("  STUDENT RESULT RECORD SYSTEM  ")
        print("================================")
        print("1. Add New Student Result")
        print("2. Display All Results")
        print("3. Search Result by Roll No")
        print("4. Delete a Record")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ")

        if choice == '1':
            print("\n--- Enter Student Details ---")
            roll = input("Enter Roll Number: ")
            name = input("Enter Full Name: ")
            
            # Getting marks for three subjects
            m1 = int(input("Enter Programming Marks: "))
            m2 = int(input("Enter Maths Marks: "))
            m3 = int(input("Enter English Marks: "))

            # Calculations
            total = m1 + m2 + m3
            percentage = round((total / 300) * 100, 2)
            
            if percentage >= 40:
                status = "PASS"
            else:
                status = "FAIL"

            # Create the student record list
            new_record = [roll, name, m1, m2, m3, total, percentage, status]
            student_database.append(new_record)
            print("\n>>> Record added successfully!")

        elif choice == '2':
            if not student_database:
                print("\nDatabase is empty!")
            else:
                print("\n--- ALL STUDENT RESULTS ---")
                print("Roll | Name | Prog | Math | Eng | Total | % | Status")
                print("-" * 60)
                for s in student_database:
                    print(f"{s[0]} | {s[1]} | {s[2]} | {s[3]} | {s[4]} | {s[5]} | {s[6]}% | {s[7]}")

        elif choice == '3':
            search_roll = input("\nEnter Roll No to search: ")
            found = False
            for s in student_database:
                if s[0] == search_roll:
                    print("\n--- Record Found ---")
                    print(f"Name: {s[1]}\nTotal: {s[5]}\nPercentage: {s[6]}%\nStatus: {s[7]}")
                    found = True
                    break
            if not found:
                print("\nStudent record not found.")

        elif choice == '4':
            del_roll = input("\nEnter Roll No to delete: ")
            found = False
            for i in range(len(student_database)):
                if student_database[i][0] == del_roll:
                    student_database.pop(i)
                    print(f"\nRecord for {del_roll} deleted.")
                    found = True
                    break
            if not found:
                print("\nNo record found to delete.")

        elif choice == '5':
            print("Closing the system. Goodbye!")
            break
            
        else:
            print("Invalid Option! Please try again.")

if __name__ == "__main__":
    main()