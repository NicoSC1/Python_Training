# -- Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
## if (numbers % 2) == 0:

# musze strorzyc 'numer'ktory bedzie mial tylko numery pazyste a evens.append(number) wypeli liste

evens = []
for number in numbers:
    if (number % 2) == 0:
        evens.append(number)
print(evens)