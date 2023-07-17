company = {
    'employees': {
        'John': {'age': 35, 'job_title': 'Manager'},
        'Emma': {'age': 28, 'job_title': 'Software Engineer'},
        'Kelly': {'age': 41, 'job_title': 'Senior Developer'},
        'Sam': {'age': 30, 'job_title': 'Software Engineer'},
        'Mark': {'age': 37, 'job_title': 'Senior Manager'},
        'Sara': {'age': 32, 'job_title': 'Software Engineer'},
    }
}

# print(average_age_of_employees_with_s_job_title(company))  # 31.0






def average_age(company):
    # print(company)
    employees = company['employees']
    total_age = 0
    num_employees = len(employees)

    for employee in employees.values():
        total_age += employee['age']

    average_age = total_age / num_employees
    print(average_age)
  
average_age(company);    
