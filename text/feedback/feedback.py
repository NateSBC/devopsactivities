

student_names = input("Enter student names seperated by a comma: ")
student_names = student_names.split(",")
student_names = [name.strip() for name in student_names]

for name in student_names:

  understanding_num = {1: "Low",2: "OK",3: "Good",4: "Great"}
  contribution_num = {1: "Low",2: "OK",3: "Good",4: "Great"}
  lab_completion_num = {1: "20",2: "40",3: "60",4: "80"}

  #student_score = {}
  print(f"enter score for {name}")
  understanding_level = int(input("Understanding Level (1-4): "))
  contribution_level = int(input("Contribution Level (1-4): "))
  lab_completion_level = int(input("Lab Level (1-4): "))


  feedback = f"General comments\n{name} demonstrated {understanding_num[understanding_level]} & {contribution_num[contribution_level]} \n\n Lab Completion\n{name} completed around {lab_completion_num[lab_completion_level]} of the labs"
  filename =f"{name}_feedback.txt"
  with open(filename, "w") as file:
    file.write(feedback)





#understanding_level = 1-4
# contribution = {1: "1",2: "2",3: "3",4: "4"}
# lab_completion = {1: "1",2: "2",3: "3",4: "4"}
# punctuality = {1: "1",2: "2",3: "3",4: "4"}
# engagement = {1: "1",2: "2",3: "3",4: "4"}
# further_learning = {1: "1",2: "2",3: "3",4: "4"}


