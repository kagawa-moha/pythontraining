trainees = ["john",[2,["james","Mary"]]]
#1
print(trainees[1][0])
#2
print(trainees[1][1][0])
#3
trainees.append(56)
print(trainees)
#4
trainee_new = trainees [1][1]
trainee_new.insert(1, "Mike")
print(trainees)
#5
trainees[1][0] = 8
print(trainees)

#6
trainees[0][1].remove("Mary")
print(trainees)
trainees[0][1].remove("John")
print(trainees)
#7
print(len(trainees))