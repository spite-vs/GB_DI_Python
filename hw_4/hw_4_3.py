# 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


MULTIPLICITY = 50
PERCENT = 0.015
PERCENT_BONUS = 0.03
COUNT_PERC = 3
MIN_LIMIT = 30
MAX_LIMIT = 600
PERCENT_RICHNESS = 0.1
RICHNESS_AMOUNT = 5_000_000
CMD_DEPOSIT = "1"
CMD_WITHDRAW = "2"
LOG = "3"
CMD_EXIT = "4"

operations = 0
balance = 0
logs = []


def write_log(oper: str):
    """Функция записи операций в список"""
    logs.append(oper)


def read_log():
    """Функция вывода операций"""
    print('Список операций: ')
    for item in logs:
        print(item)


def cash_in():
    """Функция пополнения баланса"""
    amount = int(input(f"Введите сумму кратную {MULTIPLICITY}: "))
    while amount % MULTIPLICITY != 0 or amount <= 0:
        amount = int(input(f"Введите сумму кратную {MULTIPLICITY}: "))
    global balance
    balance += amount
    global operations
    operations += 1
    print(f"Внесли сумму {amount}. Баланс {balance:.2f}.")
    write_log(f"Внесли сумму {amount}. Баланс {balance:.2f}.")
    bonus()
    ricnhess()
    


def cash_out():
    """Функция снятия с баланса"""
    global balance
    amount = int(input(f"Введите сумму кратную {MULTIPLICITY}: "))
    while amount % MULTIPLICITY != 0 or amount <= 0:
        amount = int(input(f"Введите сумму кратную {MULTIPLICITY}: "))
    comission = amount * PERCENT
    if comission < MIN_LIMIT:
        comission = MIN_LIMIT
    if comission > MAX_LIMIT:
        comission = MAX_LIMIT
    if comission + amount > balance:
        print(f"На балансе недостаточно средств")
    else:
        balance -= (amount + comission)
        global operations
        operations += 1
        print(f"Сумма снятия {amount}, комиссия {comission}. Баланс {balance:.2f}.")
        write_log(f"Сумма снятия {amount}, комиссия {comission}. Баланс {balance:.2f}.")
        bonus()
        ricnhess()


def bonus():
    """Функция начисления бонуса"""
    global balance
    if operations % COUNT_PERC == 0:
        bonus = balance * PERCENT_BONUS
        balance += bonus
        print(f"Начислен бонус {bonus:.2f}. Баланс {balance:.2f}.")
        write_log(f"Начислен бонус {bonus:.2f}. Баланс {balance:.2f}.")


def ricnhess():
    """Функция вычета налога на богатство"""
    global balance
    if balance > RICHNESS_AMOUNT:
        tax = balance*PERCENT_RICHNESS        
        balance -= tax
        print(f"Вычтен налог на богатство в размере {tax}. Баланс {balance:.2f} ")
        write_log(f"Вычтен налог на богатство в размере {tax}. Баланс {balance:.2f} ")


def err():
    """Функция уведомления об ошибке"""
    print('\n Открой глаза шире и нажимай на клавиши с умом')
    
    
def end():
    """Функция уведомления о выходе"""
    print('\n -- Возвращайся, я буду ждать --')

    
def choise():
    """Функция выбора операций"""
    command = ''
    operation = {CMD_DEPOSIT: cash_in, CMD_WITHDRAW: cash_out, LOG: read_log,
                 CMD_EXIT: end}
    while command != CMD_EXIT:
        print(f'\nТвой дружелюбный банкомат, чего делаем?\n{CMD_DEPOSIT}. Пополняем\n{CMD_WITHDRAW}. Снимаем\n{LOG}. Смотрим операции\n{CMD_EXIT}. Убегаем, пока не разорились')
        command = input("Введите номер операции: ")
        operation.get(command, err)()
        
        
choise()