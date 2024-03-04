scientists = ("Albert", "Niels", "J.Robert", "Isaac", "Alan")
(Einstein, Bohr, Oppenheimer, Newton, Turing) = scientists

scientistSurname = input("Write one surname of famous scientists: Einstein, Bohr, Oppenheimer, Newton, Turing: ")

if scientistSurname == 'Einstein':
    print(Einstein)
elif scientistSurname == 'Bohr':
    print(Bohr)
elif scientistSurname == 'Oppenheimer':
    print(Oppenheimer)
elif scientistSurname == 'Newton':
    print(Newton)
elif scientistSurname == 'Turing':
    print(Turing)
else:
    print("Your write wrong name!")
