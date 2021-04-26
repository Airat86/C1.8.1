from class_Cat import Cat

cats = [
    Cat(name='Барсик', gender='самец', age=3),
    Cat(name='Муся', gender='самка', age=2)
]

for pet in cats:
    pet.print_cat()