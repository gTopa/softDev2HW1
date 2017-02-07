import csv
from pymongo import MongoClient
server=MongoClient('149.89.150.100')
db=server.mydb
c=db.students
c.delete_many({})

t=db.teachers
t.delete_many({})

courses=open("courses.csv","r")
peeps=open("peeps.csv","r")
teachers = open("teachers.csv","r")

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
coursesstr.next()
for course in coursesstr:
    for people in masterDict:
        if masterDict[people]['id'] == course[2]:
            masterDict[course[2]]['courses'].append({course[0] : course[1]})

for x in masterDict:
    c.insert_one(masterDict[x])
    
teachersstr = csv.reader(teachers)
teachersstr.next()
tdict = {}
for x in teachersstr:
    xdict = {}
    xdict['teacher'] = x[1]
    xdict['code'] = x[0]
    xdict['period'] = x[2]
    tdict[x[0]] = xdict


for x in tdict:
    cursor=c.find()
    stud_ids=[]
    for y in cursor:
        for code in y['courses']:
            if x in code:
                stud_ids.append(y['id'])
    tdict[x]['students']=stud_ids

t.insert_one(tdict)    

