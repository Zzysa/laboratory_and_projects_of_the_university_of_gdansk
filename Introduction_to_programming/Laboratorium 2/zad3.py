print("If you press x, the display stops, where x is a number or a letter")
symbol = input("Write symbol: ")
counter = 0
symbolToFind = 't'
limitToCounter = 10

while True:
    if symbol == symbolToFind or counter > limitToCounter:
        print("Program is over")
        break
    else:
        print("If you press x, the display stops, where x is a number or a letter")
        symbol = input("Write symbol: ")
        print("counter = ", counter)
        counter += 1





