from student_info import students
option=""
def see_all_students():
    all_students=""
    while all_students.casefold()!="y".casefold() or all_students.casefold()!="n".casefold:
        all_students=input("Enter 'Y' to see an updated list of students and their scores or enter 'N' to exit: ")
        if all_students.casefold()=="y".casefold():
            # Print the final dictionary of Students and their subject-score pairs
            print()
            for student, score in students.items():
                print(student, score)
            print()
            break
        elif all_students.casefold()=="n".casefold():
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
    subjects=["Maths", "Science", "History"]
    scores=[] #Empty list to hold the value for scores

    # Enter scores for all three subjects: Math, Science, History

    #Accept value for math scores and handle invalid errors
    while True:
        try:
            math_score=int(input("Math score: "))
        except ValueError as e:
            print(f"INVALID! Your entry must be a number") #Print an error message if entry is not a number
            continue
        if math_score <0 or math_score >100:
            print(f"'{math_score}' is invalid!\n{name}'s score has to be between 0 and 100") #Print an error message if score is out of range
            continue
        else:
            scores.append(math_score)
            break
    #Accept value for science score and handle invalid errors
    while True:
        try:
            science_score=int(input("Science score: "))
        except ValueError as e:
            print(f"INVALID! Your entry must be a number") #Print an error message if entry is not a number
            continue
        if science_score <0 or science_score >100:
            print(f"'{science_score}' is invalid!\n{name}'s score has to be between 0 and 100") #Print an error message if score is out of range
            continue
        else:
            scores.append(science_score)
            break
    while True:
        try:
            history_score=int(input("History score: "))
        except ValueError:
            print(f"INVALID! Your entry must be a number") #Print an error message if entry is not a number
            continue
        if history_score <0 or history_score >100:
            print(f"'{history_score}' is invalid!\n{name}'s score has to be between 0 and 100") #Print an error message if score is out of range
            continue
        else:
            scores.append(history_score)
            break

    score_value=list(zip(subjects, scores)) #ZippinG the subject an scores into tuples and constructint them into a list
    students[name]=score_value #   Entering a new value into the students dictionary

    see_all_students()


def calculate_student_average_score(student_name):
    if students.get(student_name) != None:#If student is found
        grade_data = students[student_name]#Accessing the student's scores
        no_of_subjects=len(grade_data)#number of subjects pulled from the length of the grade_data list
        total_grades=grade_data[0][1]+grade_data[1][1]+grade_data[2][1]#Sum of all scores
        average_grade=total_grades/no_of_subjects
        print(f"{student_name}'s average score is {round(average_grade)}")
    else:#If student is not found
        print (f"{student_name} not found.\nDouble check your spelling or add a new student in the main menu")

def find_top_student():
    average_scores=[]
    score_list=[]
    top_student=""
    for student, subjects in students.items():
        no_of_subjects=len(subjects)#number of subjects pulled from the length of the subjects list
        total_grades=subjects[0][1]+subjects[1][1]+subjects[2][1]#Sum of all scores
        score_list.append(round(total_grades/no_of_subjects))
        #pair students and their average grades in a dictionary
        stud_grade_pair={student:round(total_grades/no_of_subjects)}
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
        if math_grade<50:
            #Print a message if math score is below 50
            print(f"{student} is failing math with a score of {math_grade}")

        science_grade=subjects[1][1]
        if science_grade<50:
            #Print a message if math score is below 50
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
        average_scores.append(stud_grade_pair)
        for item in average_grades:
            pass

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


