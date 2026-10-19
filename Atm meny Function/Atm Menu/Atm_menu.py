# ========== ATM MENU ==========
# 1. Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# 4. Exit
# ==============================
# Enter your choice:
                        #      Project 1: ATM Menu


                                # Log in system!!!

def login():
        user_mobile_number=int(input('Enter your mobile number: '))
        user_pin=int(input('Enter your PIN number: '))

        if user_mobile_number == 9702617797 and user_pin == 123:
                Atm_menu()
        else:
             print('invalid Nikal beta!!')

def Atm_menu():
    Balance=100000
    while True:
        menu_driven=input('''
                Hi! How Can I Help You!!
                1. check balance
                2. Deposite Balance
                3. Withdraw Balance
                4. Exit
                Enter a number: ''')
        match menu_driven:
                case '1':
                        print(f'Your current balance: Rs{Balance}')
                case '2':
                        user_deposite=int(input('Enter your deposite Amount:Rs'))
                        Balance+=user_deposite
                        print(f'Deposite SuccessFully!! {Balance}: Rs your current Balance')

                case '3':
                        user_withdraw=int(input('Enter your Withdraw amount:Rs'))
                        if user_withdraw <= Balance:
                           user_withdraw-=Balance
                           print(f'Withdrawl Successful!! {Balance}: Rs Your Current Balance')
                        else:
                            print('Tu garib Chi vai!!!')
                case '4':
                    print('Exit successful!!')
                    break
                case _:
                    print('Invalid Menu Try')

login()