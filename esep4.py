names_str = input("Введите имена студентов через пробел: ")
names = names_str.split()

filtered_names = [name for name in names if "ва" in name]
filtered_names_tuple = tuple(filtered_names)

print("Имена, содержащие 'ва':", " ".join(filtered_names_tuple))