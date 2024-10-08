import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = int(0)
        self.lock = threading.Lock()
        self.random_num = randint(50, 500)

    def deposit(self):
        replenishment_trans = 100
        for i in range(replenishment_trans):
            replenishment = int(randint(50, 500))
            self.balance += replenishment
            print(f'Пополнение: {replenishment}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        withdrawal_trans = 100
        for i in range(withdrawal_trans):
            withdrawal = int(randint(50, 500))
            print(f'Запрос на {withdrawal}')
            if withdrawal <= self.balance:
                self.balance -= withdrawal
                print(f'Снятие: {withdrawal}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств.')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
