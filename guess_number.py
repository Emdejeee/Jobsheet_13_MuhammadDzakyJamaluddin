def guess_number():
    number = []
    secret_number = 16
    guess_count = 0
    guess_limit = 3

    while(guess_count < guess_limit):
        number = int(input("Masukkan tebakan anda dari 10 - 20: "))
        if (number == secret_number):
            print(f"{number}")
            print("Mantap Bujang!")
            break
        else:
            print("Yahahaha salah")
            
        guess_count = guess_count + 1
    else:
        print("Kesempatan habis bujang")