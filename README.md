A comprehensive, console-based Python application developed as a part of the BCA First Year curriculum. This project focuses on managing student academic records efficiently using core programming logic and data structures.
📌 Project Overview
The Student Result Management System is designed to automate the manual task of maintaining student marks and calculating results. It provides a user-friendly menu to perform CRUD (Create, Read, Update, Delete) operations on student data.
This project demonstrates the practical application of Data Structures and Algorithms (DSA) concepts like nested lists and linear searching.
🚀 Key Features
• Data Entry: Allows the user to input unique Roll Numbers, Names, and marks for multiple subjects.
• Automatic Calculations: The system instantly calculates:
• Total Marks: Sum of all subjects.
• Percentage: Calculated based on a 300-mark scale.
• Status: Automatically assigns "PASS" or "FAIL" based on a 40% threshold.
• Search Functionality: Built-in search algorithm to find a specific student's report card using their Roll Number.
• Database Management: Ability to view the entire list of students in a clean format or delete specific records.
🛠️ Technical Specifications
• Language: Python 3.x
• Data Structure: Nested Lists (A list containing multiple sub-lists to act as a 2D database).
• Algorithm: Linear Search for finding records.
• Logic: Multi-way branching using if-elif-else and persistent execution using while loops.
📂 Project Structure & Logic
1. Input Phase: Uses input() and int() type-casting to collect data.
2. Processing Phase: Applies mathematical formulas to generate percentages.
3. Storage Phase: Uses the .append() method to save records in the master list.
4. Output Phase: Uses f-strings and loops to display data in a tabular layout.
