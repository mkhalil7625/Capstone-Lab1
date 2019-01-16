
name = input("What is your name?")
month_born = (input("What month were you born in?"))
length_of_name = len(name)
print(f'Hello, {name}')
print(f'{name}, you have {length_of_name} letters in your name')

if month_born == 'January':
    print('Happy Birthday!!')

else:
    print('You were not born in January')


