from pymongo import MongoClient
server=MongoClient('149.89.150.100')
db=server.mydb
c=db.students
c.delete_many({})

import csv
courses=open("courses.csv","r")
peeps=open("peeps.csv","r")
masterDict = {}
peepsstr=csv.reader(peeps)
peepsstr.next()
for x in peepsstr:
    peep = {}
    peep['name'] = x[0]
    peep['age'] = x[1]
    peep['id'] = x[2]
    peep['courses'] = []
    masterDict[peep['id']] = peep

coursesstr=csv.reader(courses)
for course in coursesstr:
    for people in masterDict:
        if masterDict[people]['id'] == course[2]:
            masterDict[course[2]]['courses'].append({course[0] : course[1]})
print masterDict

for x in masterDict:
    print masterDict[x]
    c.insert_one(masterDict[x])

