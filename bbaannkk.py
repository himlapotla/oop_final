class Bank:
    usersss = []
    admins = []
    accuntnumbers = []
    loan_feature = 1
    def __init__(self, name, amount) -> None:
        self.name = name
        self.amount = amount
        self.loan_amount = 0

class Customer:
    def __init__(self, name, email, address, ac_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.ac_type = ac_type
        self.ac_number = len(Bank.usersss)+100
        Bank.accuntnumbers.append(self.ac_number)
        self.balance = 0
        self.loan = 0

        Bank.usersss.append(self)
        self.transaction_his = []

    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            bank.amount += amount
            print(f'{amount} taka has been added to {self.name}s account')
        self.transaction_his.append(f'{amount} taka has added to {self.name}s account')

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'{amount} taka has been withdrawed')
            self.transaction_his.append(f'{amount} taka has been withdrawed')
        else:
            print('Withdrawal amount exceeded')

    def transfer(self, amount, ac_num):
        for a_n in Bank.usersss:
            if a_n.ac_number == ac_num:
                a_n.balance += amount
                self.balance -= amount
                print(f'{amount} taka has been transfered to {ac_num}s account')
        self.transaction_his.append(f'{amount} has transfered to account {ac_num} by {self.name}')

    def history(self):
        for t in self.transaction_his:
            print(t)

    def check_balance(self):
        print(f' this is your current balance {self.balance}')

    def take_loan(self, amont):
        if bank.loan_feature == 1:
            if self.loan < 2:
                self.balance += amont
                bank.amount -= amont
                self.loan += 1
                print(f'loan successfully added to {self.name}s account')
                bank.loan_amount += amont
            else:
                print('your loan limit is finish')
        else:
            print('loan feature is off')
            

class Admin:
    def __init__(self, name, email, type) -> None:
        self.name = name
        self.email = email
        self.type = type
        self.ac_number = len(Bank.admins)+1
        Bank.admins.append(self)

    def see_all_accounts(self):
        print('this are the all bank accounts -- ')
        for accounts in bank.usersss:
            print(f'account name -- {accounts.name} account number -- {accounts.ac_number} account type -- {accounts.ac_type}')

    def delete_account(self, acc_n):
        for acc in bank.usersss:
            if acc.ac_number == acc_n:
                bank.usersss.remove(acc)
                print(f"Account {acc_n} has been deleted.")

    def total_balance_of_bank(self):
        print(f'total bank amount -- {bank.amount}')

    def total_loan_amount(self):
        print(f'total loan amount -- {bank.loan_amount}')

    def control_loan_feature(self):
        op = int(input('if you want to loan off press 2 : '))
        print()
        if op == 2:
            bank.loan_feature = 2
            print('loan feature has been turned off')
            print()
        
bank = Bank('Sonali Bank', 10000)
himla = Customer('himla', 'him@gmail.cm', 'chapai', 'savings') 
mimla = Customer('mimla', 'mim@gmail.cm', 'rajshahi', 'current')
Shah = Admin('s', 'ss', 'ADMIN')

while(True):
    print()
    print()
    print('1. login as an admin ')
    print('2. login as user ')
    print('3. exit')

    m_op = int(input('enter an option : '))
    print()
    if m_op == 1:
            admin_nm = input('enter admin name : ')
            admin_email = input('enter admin email : ')
            admin_acc_type = input('enter account type : ')
            print()

            for ad in Bank.admins:
                if ad.name == admin_nm and ad.email == admin_email and ad.type == admin_acc_type:
                    print('you have logged in as an admin.')
                    print()

                    while True:
                        # print('1. sing in as an user')
                        print('2. delete user account')
                        print('3. see all users account')
                        print('4. total balance of bank')
                        print('5. total loan amount of bank')
                        print('6. on or off loan feature')
                        print('7. exit')
                        print()

                        a_op = int(input('enter an option : '))
                        print()
                        # 
                       

                        if a_op == 2:
                            ac_num = int(input('enter your admin account num : '))
                            print()
                            for usr in bank.admins:
                                if usr.ac_number == ac_num:
                                    acc_n = int(input('enter the account number you want to deleted : '))
                                    usr.delete_account(acc_n)
                                    print()
                                    break
                                else:
                                    print('invalid admin account number')
                                    print()
                                    print('invalid input, you can not sign in as an admin')
                        
                        if a_op == 3:
                            ac_num = int(input('enter your admin account num : '))
                            print()
                            for usr in bank.admins:
                                if usr.ac_number == ac_num:
                                    usr.see_all_accounts()
                                    break
                                else:
                                    print('invalid admin account number')
                                    print()

                        if a_op == 4:
                            ac_num = int(input('enter your admin account num : '))
                            print()
                            for usr in bank.admins:
                                if usr.ac_number == ac_num:
                                    usr.total_balance_of_bank()
                                    break
                                else:
                                    print('invalid admin account number')
                                    print()

                        if a_op == 5:
                            ac_num = int(input('enter your admin account num : '))
                            print()
                            for usr in bank.admins:
                                if usr.ac_number == ac_num:
                                    usr.total_loan_amount()
                                    break
                                else:
                                    print('invalid admin account number')
                                    print()

                        if a_op == 6:
                            ac_num = int(input('enter your admin account num : '))
                            print()
                            for usr in bank.admins:
                                if usr.ac_number == ac_num:
                                    usr.control_loan_feature()
                                    break
                                else:
                                    print('invalid admin account number')
                                    print()

                        if a_op == 7:
                            break
                    break
            else:
                print('invalid admin input. ')

    elif m_op == 2:
        ac_num = int(input('enter your bank account number : '))
        print()
        for an in Bank.accuntnumbers:
            if an == ac_num:
                print('you have signed in as an user. what do you want to do ?')
                print()
                while True:
                        print('1. deposit money')
                        print('2. withdraw money')
                        print('3. check available balance')
                        print('4. check transaction history')
                        print('5. take a loan')
                        print('6. transfer money')
                        print('7. exit')
                        print()
                        u_op = int(input('enter an option : '))
                        print()
                        if u_op == 1:
                            ac_num = int(input('enter your account num : '))
                            print()
                            for usr in bank.usersss:
                                if usr.ac_number == ac_num:
                                    amt = int(input('enter your deposit amount : '))
                                    print()
                                    usr.deposit(amt)
                                    break
                                else:
                                    print('invalid account number')
                                    print()

                        elif u_op == 2:
                            ac_num = int(input('enter your account num : '))
                            for usr in bank.usersss:
                                if usr.ac_number == ac_num:
                                    amt = int(input('enter your withdrw amount : '))
                                    print()
                                    usr.withdraw(amt)
                                    break
                                else:
                                    print('invalid account number')
                                    print()

                        if u_op == 3:
                            ac_num = int(input('enter your account num : '))
                            print()
                            for usr in bank.usersss:
                                if usr.ac_number == ac_num:
                                    usr.check_balance()
                                    break
                            else:
                                print('invalid account number')
                                print()

                        if u_op == 4:
                            ac_num = int(input('enter your account num : '))
                            print()
                            print(f'all the tramsaction history of {usr.name}s account -- ')
                            for usr in bank.usersss:
                                if usr.ac_number == ac_num:
                                    for th in usr.transaction_his:
                                        print(th)
                                    break
                            else:
                                print('invalid account number')
                                print()

                        if u_op == 5:
                            ac_num = int(input('enter your account num : '))
                            print()
                            for usr in bank.usersss:
                                if usr.ac_number == ac_num:
                                    if bank.loan_feature == 1:
                                        amt = int(input('enter your loan amount : '))
                                        print()
                                        usr.take_loan(amt)
                                    else:
                                        print('loan feature is off')
                                    break
                            else:
                                print('invalid account number')
                                print()    

                        if u_op == 6:
                            ac_num = int(input('enter your account num : '))       
                            print()
                            for usr in bank.usersss:
                                if usr.ac_number == ac_num:
                                    amt = int(input('enter your transfer amount : '))
                                    acnt = int(input('enter the account you want ta transfer : '))
                                    usr.transfer(amt, acnt)
                                    break
                            else:
                                print('invalid account number')
                                print()

                        if u_op == 7:
                            break
    elif m_op == 3:
        break
        



