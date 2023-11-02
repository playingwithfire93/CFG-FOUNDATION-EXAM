"""Section 3: Python Challenge  [25 marks]
You are tasked with calculating the minimum classes we need to have so we know how many people to employ. Write a function which when given a number of students, calculates and prints out a string for your proposed number of classes, and a dictionary showing the allocation.
Key Constraints:
⦁	The maximum size of a class is 30
⦁	There needs to be a minimum of 2 classes
⦁	The distribution of each class should be as even as possible.
⦁	We want to hire as little people as possible - so where possible focus on bigger classes, and less of them!
Inputs/Outputs:
⦁	If 31 was the input, the output would be:
Proposed Allocation: 2 classes
{'Class 1': 16, 'Class 2': 15}
⦁	If 59 was the input, the output would be:
Proposed Allocation: 2 classes
{'Class 1': 30, 'Class 2': 29}
⦁	If 87 was the input, the output would be:
Proposed Allocation: 3 classes
{'Class 1': 29, 'Class 2': 29, 'Class 3': 29}
"""
def calculate_students_per_class(num_students):
    max_per_class = 30
    min_classes = 2

    # Calculate the minimum number of classes needed.
    num_classes = max(min_classes, (num_students + max_per_class - 1) // max_per_class)

    # Calculate the even distribution of students per class.
    students_per_class = num_students // num_classes
    remainder = num_students % num_classes

    # Create a dictionary to store the class allocations.
    allocation = {}

    for i in range(num_classes):
        # Distribute the remaining students evenly.
        if i < remainder:
            # If there are remaining students, assign an extra student to this class.
            allocation[f'Class {i + 1}'] = students_per_class + 1
        else:
            # Assign an equal number of students to this class.
            allocation[f'Class {i + 1}'] = students_per_class

    return num_classes, allocation

#Add a while loop so we can check the allocations of the students without having to re-run the code.
while True:
    ask = input('Do you want to know how many students we can allocate per class? (y/n): ')
    if ask == 'y':
        try:
            num_students = int(input('Number of students: '))
            # Ensure that the number of students is a positive integer.
            if num_students < 0:
                print("Please enter a valid positive number of students.")
                continue
            # Calculate the number of classes and their allocations.
            num_classes, allocation = calculate_students_per_class(num_students)
            print(f'Proposed Allocation: {num_classes} classes')
            print(allocation)
        except ValueError:
            print("Invalid input. Please enter a valid number of students.")
    else:
        break
