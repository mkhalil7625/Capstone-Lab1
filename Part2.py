number_of_classes = int(input("How many classes are you taking this semester?"))
list_of_classess = []
for i in range (number_of_classes):
    classes = input('enter name of class: ')
    list_of_classess +=[classes]
print('The classes you are taking are: ')
for c in list_of_classess:
    print(c)

