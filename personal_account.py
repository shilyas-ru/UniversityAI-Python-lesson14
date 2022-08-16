"""
По сравнению с версией из урока 10 добавлена
возможность посмотреть состояние счёта


Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. история движения по счёту
5. остаток на счёте
6. выход


1. пополнение счета
при выборе этого пункта пользователю предлагается ввести
сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
Снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что
денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
Выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
Возвращаемся в основное меню

4. история движения по счёту
выводим историю движения по счёту пользователя.
        Поступления на счёт отражаются: ++10
        Списания со счёта отражаются: --3
        Остаток по счёту: 7
где 10, 3, 7 - сумма поступления/списания со счёта и остаток по счёту.
Возвращаемся в основное меню.
        print('  5. остаток на счёте')
        print('  6. выход')

5. остаток на счёте
выводим остаток на счёте пользователя.

6. выход
выход из программы
"""

def personal_account(account = 0, account_lst = [], history_lst = []):
    # account = 0         # Исходное состояние счёта
    # account_lst = []    # Список хранит историю поступлений и списаний со счёта.
    # history_lst = []    # Список хранит историю покупок.
                          # Будет храниться в виде кортежей (название покупки, сумма покупки).
                          # То есть, итоговый список с историей будет примерно такой:
                          # [('Наименование1', 100), ('Наименование2', 200)]
    # print('\n\nВнимание!!!\nВводить цифры требуется только целые,\n' +
    #       'проверка корректности ввода не производится!\n')
    while True:
        print('  1. пополнение счета')
        print('  2. покупка')
        print('  3. история покупок')
        print('  4. история движения по счёту')
        print('  5. остаток на счёте')
        print('  6. выход')

        choice = input('  Выберите пункт меню: ')
        if choice == '1':
            # пополнение счета
            purchase_sum = int(input('введите сумму на сколько пополнить счет (целое число): '))
            account += purchase_sum
            account_lst.append(purchase_sum)
        elif choice == '2':
            # покупка
            purchase_sum = int(input('введите сумму покупки (целое число): '))
            if (purchase_sum > account):
                print(f'денег не хватает. Всего на счёте {account}, сумма покупки {purchase_sum}')
                continue
            history_lst.append((purchase_sum,
                            input('введите наименование покупки: ')))
            account_lst.append(-purchase_sum)
            account -= purchase_sum
        elif choice == '3':
            # история покупок
            if len(history_lst) == 0:
                print('Покупок ещё не было.')
                continue
            i = 0
            for purchase_sum, purchase_name in history_lst:
                i += 1
                print(f'Покупка номер {i}.')
                print(f'    Наименование покупки: {purchase_name}.')
                print(f'    Сумма покупки: {purchase_sum}.')
        elif choice == '4':
            # история движения по счёту
            if len(account_lst) == 0:
                print('Движения по счёту ещё не было.')
                continue
            i = 0
            print('Движение по счёту.')
            for purchase_sum in account_lst:
                i += 1
                operation_type_str = ('++Поступление' if purchase_sum > 0
                                                    else '--Списание')
                print(f'   {i}.  {operation_type_str}: {abs(purchase_sum)}.')
            print(f'Остаток по счёту: {account}')

        elif choice == '5':
            # остаток на счёте
            print(f'Остаток по счёту: {account}')

        elif choice == '6':
            # выход
            break
        else:
            print('Неверный пункт меню')

    return account, account_lst, history_lst

if __name__ == '__main__':
    account, account_lst, history_lst = personal_account()
    print(f'Баланс = {account}')
    print(f'Движение по счёту = {account_lst}')
    print(f'История покупок = {history_lst}')