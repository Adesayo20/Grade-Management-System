from student_info import students


option=""
def see_all_students() ->None:
    """
    This function prompts the user to either display a list of students and their scores or exit.
    It handles the input validation, ensuring the user can only enter 'Y' or 'N'.
    If input is neither 'y' nor 'n', it then provides feedback to the user about the invalid input

    :return: None
    """
    # Infinite loop to repeatedly prompt the user until valid input is received (or until they exit)
    while True:
        option=input("Enter 'Y' to see an updated list of students and their scores or enter 'N' to exit: ").casefold()

        #If user inputs 'y', iterate over the final dictionary, print the names of students and their subject-score pairs, and exit the loop.
        if option=="y":
            print("\nSTUDENT SCORES")
            for student, score in students.items():
                print(student, score)
            print()
            break
        #If user inputs 'n', exit the loop
        elif option == "n":
            break
        # If input is neither 'y' nor 'n', provide feedback to the user about the invalid input
        else:
            print("Invalid input, please enter 'Y' or 'N'.")

def validate_score(subject):
    """

    :param subject:
    :return:
    """
    while True:
        try:
            score=int(input(f"{subject} score: "))
        except ValueError:
            print(f"INVALID! Your entry must be a number") #Print an error message if entry is not a number
            continue
        if score < 0 or score > 100:
            print(f"'{score}' is invalid!\nScore has to be between 0 and 100") #Print an error message if score is out of range
            continue
        else:
            return score #Return the valid value of score
            break

def add_student():
    """
    This function adds a student and their scores for three subjects (Math, Science, History).
    It prompts the user to enter the student's name and valid scores for each subject.
    Name must not contain numbers and must be separated by a space
    Scores must be integers between 0 and 100.
    :return:None
    """
    while True:
        name=input("Enter the student's first and last name: " )
        if " " not in name:#Check if name does not contain a space
            print (f"{name} is INVALID!\nEnter a first and last name separated by a space")
            continue
        if any(char.isnumeric() for char in name):#Check if name contains a numeric value
            print(f"{name} is INVALID!\nThe name cannot contain a number!")
        else:
            break


    any_topics=next(iter(students.values()))
    subjects=[subject for subject, score in any_topics]
    score=[] #Empty list to hold the value for scores

    # Call the validate_score() function to validate the score for all three subjects and append their value to the var 'score_list'
    math_score=validate_score(subjects[0])
    score.append(math_score)

    science_score=validate_score(subjects[1])
    score.append(science_score)

    history_score=validate_score(subjects[1])
    score.append(history_score)

    score_value=list(zip(subjects, score)) #Zipping the subject an scores into tuples and constructing them into a list

    #Enter a new key:value pair into the global students dictionary
    students[name]=score_value

    # Call the see_all_students() function if the user wishes to see the new student in the global dictionary
    see_all_students()


def calculate_student_average_score(student_name: str) ->None:
    """
    This function calculates and prints the average score of a student if the student exists
    in the `students` dictionary. If the student is not found, it prints an error message.

    :param student_name: The name of the student whose average score is to be calculated.
    :return: None
    """
    if students.get(student_name) != None:#If student is found
        #bind the list containing the student's scores to the variable 'grade_data'
        grade_data = students[student_name]

        #Pull the number of subjects from the length of the grade_data list
        no_of_subjects=len(grade_data)

        #Sum up all grades by accessing the scores in the tuple for each subject in 'grade_data'
        total_grades=sum(score for subject, score in grade_data)

        #calculate average grade
        average_grade=round(total_grades/no_of_subjects)

        print(f"{student_name}'s average score is {average_grade}")

    else:#If student is not found
        print (f"{student_name} not found.\nDouble check your spelling or add a new student in the main menu")

def find_top_student():
    """
     This function ind the student with the highest average score.

     :param students: A dictionary where keys are student names and values are lists of tuples,
                      each containing a subject and the corresponding score.
     :return: None
     """
    average_scores=[]
    score_list=[]
    top_student=""
    for student, subjects in students.items():
        #bind each student's dictionary value to the variable 'grade_data'

        #Pull the number of subjects from the length of the grade_data list
        no_of_subjects=len(subjects)

        #Sum up all grades by accessing the scores in the tuple for each subject in 'grade_data'
        total_grades=sum(score for _, score in subjects)

        #calculate average grade
        average_grade=round(total_grades/no_of_subjects)

        #Bind each student's average grade to a list of every student's scores
        score_list.append(average_grade)

        #pair each student's average grade with their name in a new dictionary
        stud_grade_pair= {student:average_grade}

        average_scores.append(stud_grade_pair)
    max_value=max(score_list)
    for item in average_scores:
        for name, value in item.items():
            if value==max_value:
                top_student=name
    print(f"The top student is {top_student} with an average score of {max_value}")
    print()


def view_failing_students():
    for student, subjects in students.items():
        math_grade=subjects[0][1]
        if math_grade<40:
            #Print a message if math score is below 40
            print(f"{student} is failing math with a score of {math_grade}")

        science_grade=subjects[1][1]
        if science_grade<50:
            #Print a message if math score is below 40
            print(f"{student} is failing science with a score of {science_grade}")

        history_grade=subjects[2][1]
        if history_grade<50:
            #Print a message if math score is below 50
            print(f"{student} is failing history with a score of {history_grade}")
    print()

def update_student_grade(student_name):
    if students.get(student_name) != None:#If student is found
        while True:
            subject=input("Enter the subject you want to update")
            ######HELPPPPP
        while True:
            try:
                score_value=int("Enter a value")
            except ValueError:
                print("INVALID! Value must be an integer")
                continue
            if score_value < 0 or score_value > 100:
                print(f"INVALID\n{student_name}'s new score has to be between 0 and 100")
            else:
                break

    else:#If student is not found
        print (f"{student_name} not found.\nDouble check your spelling or add a new student in the main menu")


def remove_student(student_name):
    if students.get(student_name) != None:#If student is found
        del students[student_name]
        print(f"Deleted {student_name}!")
    else:#If student is not found
        print (f"{student_name} does not exist.\nYou can't delete non-existent data")

    see_all_students()


def display_all_students_and_average_grades():
    average_grades=[]
    for student, subjects in students.items():
        no_of_subjects=len(subjects)#number of subjects pulled from the length of the subjects list
        total_grades=subjects[0][1]+subjects[1][1]+subjects[2][1]#Sum of all scores
        stud_grade_pair={student:round(total_grades/no_of_subjects)}
        average_grades.append(stud_grade_pair)

    for item in average_grades:
        for student, average_grade in item.items():
            print(student, average_grade)

while option != 8:
    print("SELECT FROM THE OPTIONS BELOW:")
    print("Select '1' to add a student")
    print("Select '2' to view the average grade of a student")
    print("Select '3' to find the top student")
    print("Select '4' to view failing students")
    print("Select '5' to Update a student's grade")
    print("Select '6' to remove student")
    print("Select '7' to 7 to Display all students and their average grades")
    print("Select '8' to exit")
    print("-------------------")
    print()
    while True:
        try:
            option=int(input("Enter an option:"))
        except ValueError as e:
            print(f"INVALID! Your entry must be a number between 1 and 8")
            continue
        if option <1 or option >8:
            print(f"'{option}' INVALID! Your entry must be between 1 and 8")
            continue
        else:
            break

    if option==1:
        add_student()
    elif option==2:
        student_name=input("Enter a student's name to calculate their average score: ".casefold())
        calculate_student_average_score(student_name)
    elif option == 3:
        find_top_student()
    elif option ==4:
        view_failing_students()
    elif option== 5:
        student_name=input("Enter a student's name to upgrade their grade")
        update_student_grade(student_name)
    elif option == 6:
        student_name=input("Enter a student's name to delete them!")
        remove_student(student_name)
    elif option== 7:
        display_all_students_and_average_grades()


