"""
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?

Return YES, if Vasya can sell a ticket to each person and give the change with the bills he has at hand at that moment. Otherwise return NO.

###Examples:

### Python ###

tickets([25, 25, 50]) # => YES
tickets([25, 100])
         # => NO. Vasya will not have enough money to give change to 100 dollars
"""


def tickets(people):
    aven = {
        100.0: 0,
        50.0: 0,
        25.0: 0,
    }
    for i in people:
        aven[i] += 1
        change = i - 25

        for j in (50, 25):
            while(j <= change and aven[j] > 0):
                aven[j] -= 1
                change -= j

        if change != 0:
            return "NO"
    return "YES"


print(tickets([25, 25, 25, 25, 25, 25, 25, 50, 50, 50, 100, 100, 100, 100]))
