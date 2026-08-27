def student_info(*marks):
    print(marks)
student_info(10,20,30,40,50,60,70,80)



def student_info(**data):
    print(data)
student_info(name = "tanisha",city = "nagpur",age = "twenty")



def college_fees(**data):
    print(data)
college_fees(data_science = 100000,data_analytics = 220000,python_fullstack = 50000)


def institutes_name(*names):
    print(names)
institutes_name("rays_tech","arc_tech","it_vedant","universal")