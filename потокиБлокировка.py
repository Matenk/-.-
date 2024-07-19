from threading import Thread, Lock

lock1 = Lock()
lock2 = Lock()
class BankAccount():

    def info_balance(self):
        self.balance = 10000
        print(f'Баланас счета: {self.balance}.')


    def deposit_task(self, amount):
        lock1.acquire()
        for i in range(5):
            self.amount = amount
            self.balance += self.amount
            print(f'Пополнение: {self.amount}, на счету: {self.balance}')
        lock1.release()

    def withdraw_task(self, amount):
        lock2.acquire()
        for i in range(5):
            self.amount = amount
            self.balance -= self.amount
            print(f'Снятие: {self.amount}, на счету: {self.balance}')
        lock2.release()

account = BankAccount()

def deposit(account, amount):
    account.deposit_task(amount)

def withdraw(account, amount):
    account.withdraw_task(amount)




account.info_balance()

deposit_thread = Thread(target=deposit, args=(account, 100))
withdraw_thread = Thread(target=withdraw, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

