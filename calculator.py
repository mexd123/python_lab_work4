print("Внимание!"
	"\nПри написании слова 'выход' программа завершится")
while True:
	action = (input("Дейсвие над числами: +,-,*,/ ?: "))
	if action == "выход":
		break
	if action in('+', '-', '*', '/'):
		numb1 = float(input("Введите первое число :"))
		numb2 = float(input("Введите второе число :"))
		
		variable = 14 
		if (variable > 10 and  variable != 12 and variable <=15) or variable == 18:
			print(True) 
						

		if action == "+":
			print("Результат вычисления над числами :",numb1 + numb2)
		elif action == "-":
			print("Результат вычисления над числами :",numb1 - numb2)
		elif action == "*":
			print("Результат вычисления над числами :",numb1 * numb2)
		elif action == "/":
			if numb2 != 0:
				print("Результат вычисления над числами :",numb1/numb2)
			else:
				print("Вы делите на ноль")
	else:
		print("Неправильный знак действия"
			"\nЛибо введите 'выход'")








