from random import randint
from time import sleep
import threading
from threading import Lock

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            j = randint(50, 500)
            self.balance += j
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {j}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for ii in range(100):
            jj = randint(50, 500)
            print(f'Запрос на {jj}')
            if jj <= self.balance:
                self.balance -= jj
                print(f'Снятие: {jj}. Баланс: {self.balance}')
            else jj > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
