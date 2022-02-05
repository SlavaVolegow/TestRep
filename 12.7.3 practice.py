money = int(input ("Пожалуйста, введите сумму, которую Вы хотите положить на депозит:"))

percent: dict[str, float] = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

bank0 = percent['ТКБ']
bank1 = percent['СКБ']
bank2 = percent['ВТБ']
bank3 = percent['СБЕР']

percent0 = float(money + money/100*bank0)
percent1 = float(money + money/100*bank1)
percent2 = float(money + money/100*bank2)
percent3 = float(money + money/100*bank3)

result = percent0, percent1, percent2, percent3
print ("Внесённая сумма с процентами каждого из банков за год -", result)
print ("Максимальная сумма, которую вы можете заработать —", max(result))











