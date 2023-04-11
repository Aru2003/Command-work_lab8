person = {}
person.setdefault('Aruzhan', {'age': 21, 'profession': 'Programing'})
person.setdefault('Nurila', {'age': 21, 'profession': 'Teacher'})
person.update({'Aruzhan': {'age': 19, 'Birthday': 'May'}})
res = person.copy()
print(res)

removed_person = person.pop('Nurila')
print(f'pop: {removed_person}')

for k in person.keys(): 
    print(k)
  
clear_person_dict = person.clear()
print(clear_person_dict)

