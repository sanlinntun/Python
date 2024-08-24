import secrets
secret_number = secrets.SystemRandom()

while True:
    print("Lottery Game:")
    print("Enter 1: to read the rules.")
    print("Enter 2: login to play game.")
    print("Enter 3: to exit the game.")

    g_num = int(input("\nChoose a number to play this game:>"))

    if g_num == 1:   
        print("Rule No.1 : User name must be more than two characters.")
        print("Rule No.2 : Age must be 18 or older.")
        print("Rule No.3 : Show Money must be at least 5000.")
        print("Rule No.4 : Bet Money must be 1000 or more.\n")

    elif g_num == 2:
        print("\nWelcome to Lottery Game.")
        user_name = str(input("Enter your name:>"))
        age = int(input("Enter your age:>"))

        if len(user_name) > 2 and age >= 18:
            print("\nWelcome to Lottery Game,",user_name)

            while True:
                show_money = int(input("Enter your show money:>"))
                if show_money >= 5000:
                    print("This is your Show Money is",show_money)
                    print("\nNow, you can play the game.")

                    while True:
                        bet_money = int(input("Enter your bet money:>"))

                        if bet_money >= 1000:
                            show_money -= bet_money
                            print("This is your remain show money:>", show_money)
                            bet_number = int(input("Enter your bet number:>"))
                            print("Your bet money is",bet_money)
                            print("Your bet number is", bet_number)

                            # check_number = secret_number.randint(0,10)
                            check_number = 2

                            if bet_number == check_number:
                                print("You are winner!")
                                bet_money = 2 * bet_money
                                show_money += bet_money
                                print("Here is your total show money:>",show_money)
                                play_again = str(input("Do you want to play again? (yes or no):>"))
                                if play_again == 'yes':
                                    print("You said yes")
                                    continue
                                else:
                                    print("Quit the game.")
                                    quit()

                            else:
                                print("You lose!")
                                print("This is your show money:>",show_money)
                                play_again = str(input("Do you want to play again? (yes or no):>"))
                                if play_again == 'yes':
                                    print("Checking remain show money...")
                                    if show_money < 1000:
                                        print("Now, you don't have enough money to play the game.")
                                        print("Show Money must have at least 1000")
                                        print("Now your show money is",show_money)
                                        print("Game Quited")
                                        quit()
                                    else:
                                        continue
                                else:
                                    print("Quit the game.")
                                    quit()

                        else:
                            print("Bet money must be at least 1000.")
                            continue


                else:
                    print("Not Enough Money. \nShow Money must be at least 5000.")
                    continue
        
        else:
            print("\nRead again the rules.")
            continue
        break
        
    elif g_num == 3:
        print("Exit the game.")
        exit(0)
    
    else:
        print("\nPlease Read Again Here.")


else:
    print("Something is wrong")