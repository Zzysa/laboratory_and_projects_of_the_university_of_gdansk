import random


def question_answers(question_number, group, option, friend_answers=None):
    if option == "normal":
        print(f"\n{question_number + 1} question:\n   {group[i][0]}\n")
        print(f"1. {group[question_number][2]}")
        print(f"2. {group[question_number][3]}")
        print(f"3. {group[question_number][4]}")
        print(f"4. {group[question_number][5]}")
    elif option == "50":
        print(f"\n{i + 1} question:\n {group[i][0]}")
        print(f"1. {group[i][2]}")
        print(f"2. {group[i][3]}")
    elif friend_answers is not None:
        print(f"\n{i + 1} question:\n {group[i][0]}")
        print(f"1. {group[i][2]} - opinia ludzi {round(friend_answers[0] * 100, 1)}%")
        print(f"2. {group[i][3]} - opinia ludzi {round(friend_answers[1] * 100, 1)}%")
        print(f"3. {group[i][4]} - opinia ludzi {round(friend_answers[2] * 100, 1)}%")
        print(f"4. {group[i][5]} - opinia ludzi {round(friend_answers[3] * 100, 1)}%")


numbers = [1, 2, 3, 4]
people_true = 150
friend_IQ = 10

while True:
    print("\nCo chcesz zrobić? \n1. Chcę grać \n2. Chcę dodać pytani(e/a)/odpowiedz(i) \n3. Wyjście")
    game_option = input("Wpisz numer opcji: ")

    helper_50_50 = True
    helper_friend = True
    helper_people = True

    if game_option == '1':
        with open("questions_answers.txt", 'r', encoding='utf-8') as f:
            lines = f.read().split('\n\n')
            groups = [group.split('\n') for group in lines]

        for i in range(len(groups)):
            options = {}

            for j in range(1, 5):
                options[j] = groups[i][j + 1]

            if i == 1:
                answer = input("Chcesz zabrać 1000 zł albo kontynujemy? Y/N\n")
                if answer == "Y\n":
                    print("Wygrałeś 1000 zł\n")
                    break
                elif answer != "N":
                    print("BŁĄD\n")

            if i == 6:
                answer = input("Chcesz zabrać 40.000 zł albo kontynujemy? Y/N\n")
                if answer == "Y\n":
                    print("Wygrałeś 40.000 zł\n")
                    break
                elif answer != "N":
                    print("BŁĄD\n")

            question_answers(i, groups, "normal")

            if helper_50_50 or helper_people or helper_friend:
                print("\nJeżeli chcesz otrzymać podpowiedź wpisz \"P\"")
                answer = input("\nWpisz numer prawidwowej odpowiedzi albo skorzystaj z podpowiedzi: ")
            else:
                answer = input("\nWpisz numer prawidwowej odpowiedzi: ")

            if helper_50_50 or helper_people or helper_friend:
                if answer == "P":
                    if helper_50_50:
                        print("Możesz skorzystać z podpowiedzi 50 na 50, jeżeli wpiszesz \"50\"")
                    if helper_people:
                        print("Możesz skorzystać z podpowiedz od ludzie na sali, jeżeli wpiszesz \"lud\"")
                    if helper_friend:
                        print("Możesz skorzystać z podpowiedz od przyjacieja, jeżeli wpiszesz \"przy\"")
                    helper = input("Wpisz jaką chcesz podpowiedz: ")

                    if helper == "50" and helper_50_50:
                        counter = 2
                        while counter != 0:
                            rand = random.randint(2, 3 + counter)
                            if groups[i][rand] != groups[i][1]:
                                groups[i].pop(rand)
                                counter -= 1

                        question_answers(i, groups, "50")

                        answer = input("Wpisz numer prawidwowej odpowiedzi: ")
                        if 0 < int(answer) < 3:
                            if groups[i][int(answer) + 1] != groups[i][1]:
                                print("\nZła odpowiedź! Przegrałeś\n")
                                break
                            else:
                                print("\nPoprawna odpowiedź!\n")

                                if i == len(groups) - 1:
                                    print("Gratulacje! Wygrałeś 1.000.000 zł!")
                        helper_50_50 = False
                        continue

                    elif helper == "lud" and helper_people:
                        people = [0, 0, 0, 0]
                        for c in range(1000 - people_true):
                            ran = random.randint(2, 5)
                            people[ran - 2] += 1 / 1000
                        for j in range(2, 6):
                            if groups[i][j] == groups[i][1]:
                                people[j - 2] += people_true / 1000

                        question_answers(i, groups, "lud", people)

                        answer = input("\nWpisz numer prawidwowej odpowiedzi: ")
                        helper_people = False

                    elif helper == "przy" and helper_friend:
                        friend = [2, 3, 4, 5]
                        for j in range(2, 6):
                            if groups[i][j] == groups[i][1]:
                                for k in range(friend_IQ):
                                    friend.append(j)
                                break

                        friend_choice = random.choice(friend)

                        question_answers(i, groups, "normal")

                        print(f"Wasz przyjaciów wybrał odpowiedz \"{friend_choice - 1}. {groups[i][friend_choice]}\"\n")
                        answer = input("\nWpisz numer prawidwowej odpowiedzi: ")
                        helper_friend = False

                    else:
                        print("\nBŁĄD! Zła wybrana opcja\n")

            if 0 < int(answer) < 5:
                if options[int(answer)] != groups[i][1]:
                    print("\nZła odpowiedź! Przegrałeś\n")
                    break
                else:
                    print("\nPoprawna odpowiedź!\n")
            else:
                print("\nBŁĄD! Zła wybrana opcja\n")
                break

            if i == len(groups) - 1:
                print("Gratulacje! Wygrałeś 1.000.000 zł!")

    elif game_option == '2':
        while True:
            with open("questions_answers.txt", 'a', encoding='utf-8') as f:
                question = input("\nWpisz pytanie, które chcesz dodać:\n")
                f.write('\n' + question + "\n")
                correct_answer = input("\nWpisz poprawną odpowiedź: ")
                f.write(correct_answer + "\n")

                answers = []

                for i in range(2, 5):
                    answer = input(f"\nWpisz {i} odpowiedź: ")
                    answers.append(answer)

                answers.append(correct_answer)

                for i in range(4):
                    random_answer = random.choice(answers)
                    f.write(random_answer + "\n")
                    answers.remove(random_answer)

                answer = input("\nChcesz dodać jeszcze jedno pytanie? Y/N\n")
                if answer == 'N':
                    break
                elif answer == 'Y':
                    continue
                else:
                    print("\nBŁĄD! Zła wybrana opcja\n")
                    break

        with open("questions_answers.txt", 'r', encoding='utf-8') as f:
            lines = f.read().split('\n\n')
            groups = [group.split('\n') for group in lines]

    elif game_option == '3':
        break

    else:
        print("Wpisałeś złą opcję!")
