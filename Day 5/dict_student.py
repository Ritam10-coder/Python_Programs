student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'Data Analysis'],
    'country': 'USA',
    'city': 'New York',
    'address': {
        'street': '5th Avenue',
        'zipcode': '10001'
    }
}
length = len(student)
print("Length of student dictionary:", length)
skills = student['skills']
print("Skills:", skills)
print("Data type of skills:", type(skills))
student['skills'].extend(['Machine Learning', 'Communication'])
print("Updated skills:", student['skills'])
keys = list(student.keys())
print("Dictionary keys:", keys)
values = list(student.values())
print("Dictionary values:", values)
