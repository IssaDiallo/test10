student = {'name': 'Issa', 'city': 'Atlanta', 'courses': ['math', 'physics', 'cs']}

student['country'] = 'USA'
# del student['city']
# city = student.pop('city')

print(len(student))
for key, value in student.items():
    print(key, value)

# print(student)
# print(city)