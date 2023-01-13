import time
userinput = ""
inputmessage = "Enter A Number to choose"
student_data = {
"RollNo":[1,2,3,4],
"Name":["Rohan","Navjot","Krishan","Madhav"],
"Age":[17,18,18,18],
"Class":["11th","12th","12th","12th",],
}
def spacetype(u):
    for i in range(60):
        print(u,end="")
        time.sleep(0)
    print()

def header():
    global userinput
    global inputmessage
    spacetype('-')
    print("Welcome to Student Data Managment System")
    spacetype('-')
    time.sleep(1)
    print("1. View Student Data")
    print("2. Add New Student Data")
    print("3. Edit Student Data")
    print("4. Delete Student Data\n5. q for Quit")
    time.sleep(1)
    
    userinput = input(inputmessage+":")
    time.sleep(1)
    
def add_student():
    global student_data
    addRollNo = int(input("Enter Student Roll No:"))
    addName = input("Enter Student Name:")
    addClass = input("Enter Student Class:")
    print("Adding New Data......")
    time.sleep(1)
    student_data.get("RollNo").append(addRollNo)
    student_data.get("Name").append(addName)
    student_data.get("Class").append(addClass)
    print("New Student Data Added")
    
def edit_student(RollNo):
    global student_data
    time.sleep(1)
    if RollNo in student_data["RollNo"]:
        RollNoStu = student_data.get("RollNo").index(RollNo)
        NewName = input("Enter New Name to change or Enter for Next(N)")
        NewClass = input("Enter New Class to change or Enter for Next(N)")
        if NewName != "N":
            student_data.get("Name")[RollNoStu]=NewName
        if NewClass != "N":
            student_data.get("Class")[RollNoStu]=NewClass
        print("Editing......")
        time.sleep(1)
        print("Name And Class Succesfully Changed")
        time.sleep(1)
    else:
        print("Roll Number Not Found")
def delete_student(RollNo):
    global student_data
    
    if RollNo in student_data["RollNo"]:
        RollNoStu = student_data.get("RollNo").index(RollNo)
        print("Deleting.....")
        time.sleep(1)
        student_data.get("RollNo").remove(student_data.get("RollNo")[RollNoStu])
        student_data.get("Class").remove(student_data.get("Class")[RollNoStu])
        student_data.get("Name").remove(student_data.get("Name")[RollNoStu])
        print("Done! Data Deleted")
    else:
        print("Roll No Not Found")
        
def viewStudent():
    print("Roll No.","Name\t\t","Class\t\t","\n")
    global student_data
    i=0
    if len(student_data["RollNo"]) > 0:
        while i < len(student_data["RollNo"]):
            #print(student_data["RollNo"][i])
            print(student_data["RollNo"][i],"\t",student_data["Name"][i],"\t",student_data["Class"][i],"\t")
            time.sleep(1)
            i+=1
    else:
        print("No Data Found..")
        
spacetype("*")
header()
spacetype("*")

while True:
    if userinput == "1":
        spacetype("-")
        viewStudent()
        header()
    elif userinput == "2":
        spacetype("-")
        add_student()
        header()
    elif userinput == "3":
        spacetype("-")
        RollNo = int(input('Enter Roll Number To edit:-'))
        edit_student(RollNo)
        header()
    elif userinput == "4":
        spacetype("-")
        RollNo = int(input('Enter Roll Number To Delete:-'))
        delete_student(RollNo)
        header()
    else:
        print("Thank You,...")
        break