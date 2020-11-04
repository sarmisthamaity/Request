import requests
import json 
from pprint import pprint

def AvailableUrl(link):
    res=requests.get(link)
    return res.text
url="http://saral.navgurukul.org/api/courses" 
response = AvailableUrl(url)
pprint(response)

my_file=open("courses.json","w")
data=my_file.write(response)
dicts=json.loads(response)
# print (dicts)
lis=[ ]
lits=[ ]
# course_id=0
available_list=dicts["availableCourses"]
i=0
def AvailableCourseOfList():
    available_list=dicts["availableCourses"]
    print (available_list)
    for key in range(0,len(available_list)):
        name=(available_list[key]["name"])
        name_id=(available_list[key]["id"])
        print (key+1,name_id,name)
    userchoose_course=int(input("choose your course: "))
    course_id=userchoose_course
    for i in range(0,len(available_list)):
        lis.append(available_list[i]["id"])
        # print (lis)
        lits.append(available_list[i]["name"])
        # print (lits)
        if (course_id-1)==i:
            print ("**********")
            print ("this is user choose course")
            print (available_list[i]["id"],available_list[i]["name"])
            print ("********")
            api=("http://saral.navgurukul.org/api/courses/"+(available_list[i]["id"])+"/exercises")
            rest=requests.get(api).text
            print (available_list[i]["id"],"UUUU")            
            my_file=open("sarmi.json","w")
            # files=my_file.write(data)
            data_dump=json.dump(rest,my_file)
            # print (data_dump)
            my_file.close()
            data_read=open("sarmi.json","r")
            data_load=json.load(data_read) 
            # print (data_load)
            var=json.loads(data_load)
            vari=[ ]
            coun=1
            empty_lis=[ ]
            for j in var:
                for m in var[j]:
                    print (m["slug"])
                    empty_lis.append(m["slug"])
                    vari.append(m["name"])
                    print (coun,m["name"])
                    # print (vari)
                    coun=coun+1
                    count=1
                    print ("++++childExercises++++")
                    for s in (m["childExercises"]):
                        print ("++++childExercises++++")
                        print ("\t",count,s["name"])
                        count=count+1
            slug_user=(input("do u want slug y/n: "))
            if slug_user=="Y" or slug_user=="y":
                exercise_slug=int(input("enter ur number: "))
                print ("this forslug::  ",empty_lis[exercise_slug-1])
            elif slug_user=="N" or slug_user=="n":
                print ("nothing")
            again_exercise_slug=int(input("enter ur exercise number: "))
            print ("u are succesfully ")
AvailableCourseOfList()
print (available_list[i]["id"], "UUUUUUUUUUUUUUUUUUUUUUUUUUU")
api=("http://saral.navgurukul.org/api/courses/"+(available_list[i]["id"])+"/exercises")
def CallingApiAgain():
    print (available_list[i]["id"], "UUUUUUUUUUUUUUUUUUUUUUUUUUU")
    rest=requests.get(links).text
    return rest.text                                                                            
    AvailableCourseOfList(available_list[i]["id"])                                               
    api=("http://saral.navgurukul.org/api/courses/"+(available_list[i]["id"])+"/exercises")
    rest=requests.get(api).text
    print (api)     
    my_file=open("sarmi.json","w")                                           
    # files=my_file.write(data)                                       
    data_dump=json.dump(rest,my_file)
    again_dump=json.dumps(data_dump)
    print (data_dump)
    my_file.close()
    data_read=open("sarmi.json","r")                        
    data_load=json.load(data_read)                                   
    print (data_load)
    var=json.loads(data_load)                                              
    for j in var:
        for m in var[j]:
            print (m["name"])
CallingApiAgain()




