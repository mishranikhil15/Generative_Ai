
def max_salary(employees):
    # print(employees)
    n=len(employees)
    max=0
    for i in range(0,n):
        if(int(employees[i]["salary"])>max):
            max=employees[i]["salary"]
    # print(max)
    for i in range(0,n):
         if(int(employees[i]["salary"])==max):
            print(employees[i])
            

employees=[
    {"name":"John","salary":3000,"designation":"developer"},
    {"name":"Emma","salary":4000,"designation":"manager"},
    {"name":"kelly","salary":3500,"designation":"tester"},
]

max_salary(employees)
