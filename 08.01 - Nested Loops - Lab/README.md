# Nested Loops - Lab
Programming Basics with Python SoftUni July 2022


########################################

01. Часовник
Напишете програма, която отпечатва часовете в денонощието от 0:0 до 23:59, всеки на отделен ред. Часовете трябва да се изписват във формат "{час}:{минути}".

Вход
- няма

Изход
- "{час}:{минути}"

########################################
   
02. Таблица за умножение
Отпечатайте на конзолата таблицата за умножение за числата от 1 до 10 във формат: 
"{първи множител} * {втори множител} = {резултат}". 

Вход
- няма
	
Изход
- "{първи множител} * {втори множител} = {резултат}"

########################################

03. Комбинации
Напишете програма, която изчислява колко решения в естествените числа (включително и нулата) има уравнението: x1 + x2 + x3 = n
Числото n е цяло число и се въвежда от конзолата. 

Вход
- Числото n е цяло число и се въвежда от конзолата. 
	
Изход
- резултат от формулата x1 + x2 + x3 = n

########################################

04. Сума от две числа
Напишете програма която проверява всички възможни комбинации от двойка числа в интервала от две дадени числа. На изхода се отпечатва, коя поред е комбинацията чиито сбор от числата е равен на дадено магическо число. Ако няма нито една комбинация отговаряща на условието се отпечатва съобщение, че не е намерено.

Вход
Входът се чете от конзолата и се състои от три реда:
- Първи ред – начало на интервала – цяло число в интервала [1...999]
- Втори ред – край на интервала – цяло число в интервала [по-голямо от първото число...1000]
- Трети ред – магическото число – цяло число в интервала [1...10000]
	
Изход
На конзолата трябва да се отпечата един ред, според резултата:
- Ако е намерена комбинация чиито сбор на числата е равен на магическото число
	- "Combination N:{пореден номер} ({първото число} + {второ число} = {магическото число})"
- Ако не е намерена комбинация отговаряща на условието
	- "{броят на всички комбинации} combinations - neither equals {магическото число}"

########################################

05. Пътуване
Ани обича да пътува и иска тази година да посети няколко различни дестинации. Като си избере дестинация, ще прецени колко пари ще й трябват, за да отиде до там, и ще започне да спестява. Когато е спестила достатъчно, ще може да пътува.
От конзолата всеки път ще се четат първо дестинацията и минималния бюджет (десетично число), който ще е нужен за пътуването. 
След това ще се четат няколко суми (десетични числа), които Ани спестява като работи и когато успее да събере достатъчно за пътуването, ще заминава, като на конзолата трябва да се изпише: "Going to {дестинацията}!" 
Когато е посетила всички дестинации, които иска, вместо дестинация ще въведе "End" и програмата ще приключи.

Вход
- От конзолата всеки път ще се четат първо дестинацията и минималния бюджет (десетично число), който ще е нужен за пътуването. 
	- След това ще се четат няколко суми (десетични числа)
	
Изход
Да се отпечата:
- Kогато успее да събере достатъчно за пътуването, ще заминава, като на конзолата трябва да се изпише: "Going to {дестинацията}!"

########################################

06.	Сграда
Напишете програма, която извежда на конзолата номерата на стаите в една сграда (в низходящ ред), като са изпълнени следните условия:
	- На всеки четен етаж има само офиси;
	- На всеки нечетен етаж има само апартаменти;
	- Всеки апартамент се означава по следния начин : А{номер на етажа}{номер на апартамента}, номерата на апартаментите започват от 0;
	- Всеки офис се означава по следния начин : О{номер на етажа}{номер на офиса}, номерата на офисите също започват от 0;
	- На последният етаж винаги има апартаменти и те са по-големи от останалите, затова пред номера им пише 'L', вместо 'А'. Ако има само един етаж, то има само големи апартаменти!
От конзолата се прочитат две цели числа - броят на етажите и броят на стаите за един етаж.

Вход
- От конзолата се прочитат две цели числа - броят на етажите и броят на стаите за един етаж.

Изход
- А{номер на етажа}{номер на апартамента}, номерата на апартаментите започват от 0;

########################################