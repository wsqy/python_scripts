class Person():
    add = 'qy'


q1 = Person()
q2 = Person()

print(Person.add)
q1.add = "yuan"
print(q1.add)
print(q2.add)
