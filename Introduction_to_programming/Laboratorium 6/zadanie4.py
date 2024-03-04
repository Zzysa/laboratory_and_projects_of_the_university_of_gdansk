recordsList = []
record = {}
keys = ['author', 'title', 'publisher of book', 'year of issue']

while True:
    print("1. Add a record\n2. Delete a record\n3. Modify a record\n4. Search in the database\n5. Exit\n")
    userChoice = int(input("Choose one of the option by the number: "))

    if userChoice == 1:  # dodujemy nowy rekord
        print("\n\n\n\n\n\n")
        for i in range(4):  # robimy nowy rekord
            print("Write the", keys[i], "of the record (if no information write \"-\"):", end=" ")
            addToRecord = input()
            record.update({keys[i]: addToRecord})
        recordsList.append(record)  # doajemy go listy z rekordami
        record = {}
        print("\n\n\n\n\n\n")

    if userChoice == 2:  # usuwamy wybrany rekord
        print("\n\n\n\n\n\n")
        if len(recordsList) == 0:
            print("There is no records in database :(")
        else:
            for i in range(len(recordsList)):
                print("Record number " + str(i + 1) + "  ---  " + str(recordsList[i]))
            recordNumber = int(input("\nWhat record do you want to delete (write record's number): "))
            if recordNumber > 0 and recordNumber < len(recordsList) + 1:
                recordsList.pop(recordNumber - 1)
            else:
                print("\n\n\n\n\nYou write the wrong record's number :(")
        print("\n\n\n\n\n\n")

    if userChoice == 3:  # modyfikujemy wybrany rekord
        print("\n\n\n\n\n\n")
        if len(recordsList) == 0:
            print("\n\n\n\n\nThere is no records in database :(")
        else:
            for i in range(len(recordsList)):
                print("Record number " + str(i + 1) + "  ---  " + str(recordsList[i]))
            recordNumber = int(input("\nWhat record do you want to modify (write record's number): "))
            if recordNumber > 0 and recordNumber < len(recordsList) + 1:  # sprawdzamy, żeby wybrać istniejący numer rekorda
                print("\n", recordsList[recordNumber - 1])
                print("\n1. Author\n2. Title\n3. Publisher of the book\n4. Year of issue")
                changeKeysRecord = int(input("\nWhat do you want to change in this record (write option's number): "))
                if changeKeysRecord > 0 and changeKeysRecord < 5: # sprawdzamy, żeby wybrać istniejący numer klucza
                    changeRecord = input("Write correct data: ")
                    recordsList[recordNumber - 1][keys[changeKeysRecord - 1]] = changeRecord
                else:
                    print("You choice the wrong option :(")
            else:
                print("\n\n\n\n\nYou write the wrong record's number :(")
        print("\n\n\n\n\n\n")

    if userChoice == 4:  # szukamy potrzebny nam rekord\rekordy
        print("\n\n\n\n\n\n")
        if len(recordsList) == 0:
            print("\n\n\n\n\nThere is no records in database :(")
        else:
            print("1. Author\n2. Title\n3. Publisher of the book\n4. Year of issue")
            findKeysRecord = int(input("\nBy what option do you want to find the record/records (write option's number): "))
            if findKeysRecord > 0 and findKeysRecord < len(keys) + 1:
                findRecord = input("Write correct data: ")
                for item in recordsList:
                    if item[keys[findKeysRecord - 1]] == findRecord:
                        print("\n\n", item)
            else:
                print("\n\n\n\n\nYou choice the wrong option :(")
        print("\n\n\n\n\n\n")

    if userChoice == 5:
        break
