def newtons_binomial(n, k):
    if k == 0 or k == n:
        return 1
    elif k == 1:
        return n
    elif k > n:
        return 0
    else:
        return newtons_binomial(n - 1, k - 1) + newtons_binomial(n - 1, k)


def probability_of_ejection(heads, throws):
    probability = input("The probability of getting heads and tails is the same? (Y/N) ")
    if probability == 'Y':
        return newtons_binomial(throws, heads) / (2 ** throws) * 100
    elif probability == 'N':
        probability_of_heads = int(input("What is probability of getting heads from 0% to 100%: ")) / 100
        if 0 <= probability_of_heads <= 1:
            return newtons_binomial(throws, heads) * (probability_of_heads ** heads) * ((1 - probability_of_heads) ** (throws - heads)) * 100
        else:
            return "You chose wrong probability!"
    else:
        return "You chose wrong option!"


throws_number = int(input("Number of throws: "))
heads_number = int(input("Number of heads dropped: "))
print(f"Probability is {probability_of_ejection(heads_number, throws_number)}%")
