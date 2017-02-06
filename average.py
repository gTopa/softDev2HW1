from pymongo import MongoClient
server=MongoClient('149.89.150.100')
db=server.mydb
c=db.students

def getAvg(grades):
    tot=0.0
    for x in grades:
        for y in x:
            tot+=x[y]
    return tot/len(grades)

def printStuff():
    cursor=c.find()
    for x in cursor:
        print x['name']
        print '\n'
        print x['id']
        print '\n'
        grades = []
        for i in x['courses']:
            for name in i:
                grades.append(i[name])
        print getAvg(x['grades'])
        print '\n\n'
