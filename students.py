import csv

def main():
    I_NUMBER_INDEX = 0
    STUDENT_NAME_INDEX = 1

    students = read_list("students.csv", I_NUMBER_INDEX, STUDENT_NAME_INDEX)
    I_number = input("What is the I-number you are looking for? ")
    is_student_in_list = verify_I_number(I_number, students)
    
        
#read the students.csv file
def read_list(file_name, I_NUMBER_INDEX, STUDENT_NAME_INDEX):
    #dictionary to store the I-number as keys attatched to the student name
    students_dict = {}
    with open(file_name, 'rt') as students:
        #loop through each line of data in students.csv
        csv_students = csv.reader(students)
        next(csv_students)
        # for row in csv_students:
        #     #skip the first line
        #     if i == 0:
        #         #continue will skip this time on the loop, but start the loop again from the next integer
        #         continue
        #     else:
        for row in csv_students:
            # split_line = row.split(", ")
            key = row[I_NUMBER_INDEX]
            name = row[STUDENT_NAME_INDEX]
            students_dict[key] = name
        print (students_dict)
    return students_dict
     
#if the user inputs a I Number that is not in the list, print an error
def verify_I_number(I_number, students_dict):
    if I_number in students_dict: 
        print(students_dict[I_number])
    else: print('Invalid I-number')

main()