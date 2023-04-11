#создание словоря
commentators_name = {}
#ввод имен и коментарий 
while True:
    line = input()
  #ввод пустой сторки приводит к остоновке процесса
    if not line:
        break
    name, comment = line.split(":")
  #Похожие имена считаются только один раз
    commentators_name[name] = None

print('Число коментаторов:',len(commentators_name))