#!/usr/bin/python3

import json

testDict = {
  'name' : ['Bryan', 'Sana', 'Bijan', 'Troy', 'Meredith', 'Arash', 'Ramesh', 'Ramin', 'Hemanth'],
  'gender' : ['male', 'female', 'male', 'male', 'female', 'male', 'female', 'male', 'male'],
  'age' : [0, 0, 24, 0, 25, 0, 24, 0, 0]
}


# json = json.dumps(testDict, sort_keys=True, indent=1)
# f = open("testOutput.json","w")
# f.write(json)
# f.close()

# reads in the json file to be parsed
file = open('testOutput.json', 'r')
fin = json.load(file)
file.close()

# displays each key within the dictionary concatenated together
person = zip(fin.get('name'), fin.get('age'), fin.get('gender'))
for i in person:
  print(i)

# calculates the number of 0's in the list
age = fin.get('age')
count=0
for i in range(len(age)):
  if age[i] == 0:
    count= (count+1)
score = (count/10)
print ("Score = " + str(score))

# writes the static and dynamic data to a text file formatted together
# static = zip(fin.get('visited static patterns'), fin.get('user static response'))
# dynamic = zip(fin.get('visited dynamic patterns'), fin.get("user dynamic response"))
# f = open('output.txt', 'w+')
# f.write("Static Pattern \t | \t User Response\n")
# for i in static:
#   f.write(str(i) + "\n")
# f.write("Dynamic Pattern \t | \t User Response\n")
# for j in dynamic:
#   f.write(str(dynamic) + "\n")
