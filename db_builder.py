from pymongo import MongoClient
server=MongoClient('149.89.150.100')
db=server.mydb
c=db.students
courses=open("courses.csv","r")
peeps=open("peeps.csv","r")

coursesstr=read(courses).split('\n')
for thing in coursesstr:
    thing=thing.split(',')

peepsstr=read(peeps).split('\n')
for x in peepsstr:
    x=x.split(',')

L=[]

for student in peepsstr:
    dic={}
    dic['name']=student[0]
    dic['age']=student[1]
    dic['id']=student[2]
    for c in coursesstr:
        codes
        if(student[2]==c[2]):
