# While Loop - Lab
Programming Basics with Python SoftUni July 2022


########################################

01. Четене на думи
Напишете програма, която чете текст от конзолата(стринг) и го принтира, докато не получи командата "Stop".

Вход
- на всеки нов ред текст, до въвежданети на "Stop"

Изход
- текстът въведен от конзолата

########################################
   
02. Парола
Напишете програма, която първоначално прочита име и парола на потребителски профил. След това чете парола за вход. 
- при въвеждане на грешна парола: потребителя да се подкани да въведе нова парола.
- при въвеждане на правилна парола: отпечатваме "Welcome {username}!".

Вход
От конзолата се чете 1 ред
- името на потребителя
	На всеки следващ ред
	- паролата, до въвеждане на правилната
	
Изход
- при правилна парола "Welcome {username}!"

########################################

03. Сума от числа
Напишете програма, която чете цяло число от конзолата и на всеки следващ ред цели числа, докато тяхната сума стане по-голяма или равна на първоначалното число. След приключване на четенето да се отпечата сумата на въведените числа.

Вход
От конзолата се чете:
- На първия ред – първоначално число
	- На всеки следващ ред число
	
Изход
- сумата от въведените числа

########################################

04. Редица числа 2k + 1
Напишете програма, която чете число n, въведено от потребителя, и отпечатва всички числа  ≤  n от редицата: 1, 3, 7, 15, 31, …. Всяко следващо число се изчислява като умножим предишното с 2 и добавим 1.

Вход
 - цяло число
 
Изход
- поредица от числа, всяко на отделен ред

########################################

05. Баланс по сметка
Напишете програма, която пресмята колко общо пари има в сметката, след като направите определен брой вноски. На всеки ред ще получавате сумата, която трябва да внесете в сметката, до получаване на команда  "NoMoreMoney". При всяка получена сума на конзолата трябва да се извежда "Increase: " + сумата и тя да се прибавя в сметката. Ако получите число по-малко от 0 на конзолата трябва да се изведе "Invalid operation!"  и програмата да приключи. Когато програмата приключи трябва да се принтира "Total: " + общата сума в сметката форматирана до втория знак след десетичната запетая. 

Вход
Входът се чете от конзолата:
- поредица от реални числа, всяко на отделен рен, до получаване на "NoMoreMoney"
	
Изход
- на всеки ред "Increase: {sum}"
- при число по-малко от 0 - "Invalid operation!"  
- на последния ред "Total: {total_sum}" 

########################################

06. Най-голямо число
Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя,  намира най-голямото измежду тях и го принтира. Въвежда се по едно число на ред.

Вход
Входът се чете от конзолата:
- поредица цели числа, всяко на отделен ред, до командата "Stop"
	
Изход
- най-голямото от числата

########################################

07.	Най-малко число
Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя, намира най-малкото измежду тях и го принтира. Въвежда се по едно число на ред. 

Вход
Входът се чете от конзолата:
- поредица цели числа, всяко на отделен ред, до командата "Stop"
	
Изход
- най-малкото от числата

########################################

08. Завършване
Напишете програма, която изчислява средната оценка на ученик от цялото му обучение. На първия ред ще получите името на ученика, а на всеки следващ ред неговите годишни оценки. Ученикът преминава в следващия клас, ако годишната му оценка е по-голяма или равна на 4.00. Ако ученикът бъде скъсан повече от един път, то той бива изключен и програмата приключва, като се отпечатва името на ученика и в кой клас бива изключен.
 
Вход
От конзолата се четат:
- на първи ред - името на ученика
- на всеки следващ ред - оценките на ученика, реално число

Изход
- При успешно завършване на 12-ти клас да се отпечата: 
	- "{име на ученика} graduated. Average grade: {средната оценка от цялото обучение}"
- В случай, че ученикът е изключен от училище, да се отпечата:
	- "{име на ученика} has been excluded at {класа, в който е бил изключен} grade"
Стойността трябва да бъде форматирана до втория знак след десетичната запетая.  

########################################