# Exercise 1
student = dict(name='Alice', age=25, city='New York')

print(f"Name: {student['name']}")

student['age'] = 30

print(f"New Age: {student['age']}")

# Exercise 2
student['profession'] = 'Engineer'
student.pop('city')

print(student)

# Exercise 3
for key, value in student.items():
    print(f"Key: {key}, Value: {value}")

# Exercise 4
for key, value in student.items():
    if key == 'age':
        print(f"Value: {value}")


# Alternate answer
if 'age' in student:
    print(f"Value 2: {student['age']}")

# Exercise 5
text = "banana"

char_frequency = {}

for char in text:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

for key, value in char_frequency.items():
    print(f"Character: {key}, Frequency: {value}")

