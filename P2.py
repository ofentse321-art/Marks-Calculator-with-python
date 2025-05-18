Assignment_1 = int(input("Enter Assignment 1 marks: "))
Assignment_2 = int(input("Enter Assingment 2 Marks: "))
Test = int(input("Enter Formal Test Marks: "))
Assigment_1_Marks = Assignment_1 * 25 / 100
Assignment_2_Marks = Assignment_2 * 25 / 100
Test_Marks = Test * 50 / 100
Final_Mark = Assigment_1_Marks + Assignment_2_Marks + Test_Marks
if Final_Mark >= 30:
    print("Passed with", (Final_Mark),"%")
elif Final_Mark >= 29:
    Final_Mark + 1
    print("Condoned")
else:
    print("Failed with", (Final_Mark),"%")
    
    


