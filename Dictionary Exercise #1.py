
room_number = {'CS101':3004,'CS102':4501,'CS103':6755,'NT110':1244,'CM241':1411}
instructor_name = {'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
meeting_time = {'CS101':'8:00 a.m.','CS102':'9:00 a.m.','CS103':'10:00 a.m.','NT110':'11:00 a.m.','CM241':'1:00 p.m.'}

course_name = input("\nWhat is your course number?\n")
print("Room number is:",room_number[course_name])
print("Instructor name is:",instructor_name[course_name])
print("Meeting time is:",meeting_time[course_name])