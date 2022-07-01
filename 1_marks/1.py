student_details = {}
with open("score.csv","r") as f:
    for line in f:
        token = line.split(',')    
        name = token[0]
        marks = token[1]
        # print(name,marks)
        # print (line)
        if name in student_details:
            student_details[name].append(marks)
        else:
            student_details[name] = [marks]

    for name , marks in student_details.items():
        print(name,"Max_marks",max(marks))
        print(name,"Min_marks",min(marks))
# print(student_details)
