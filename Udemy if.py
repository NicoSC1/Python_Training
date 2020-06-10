number = 4
user_input = input("Jesli chesz zagrac w gre wcisnij T:").lower()

if user_input == "t":
    user_number = int(input("zgadnij numer od 1 do 10: "))
    if user_number == number:
        print("farciaz, zgadles, wygrales!")
    elif abs(number - user_number) == 1:
        print("pomyliles sie o jeden")
    else:
        print("ooo grubo sie pomyliles")