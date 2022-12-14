# Programming Basics Online Exam - 6 and 7 July 2019
Programming Basics with Python SoftUni July 2022

########################################

01. Басейн
Преподавателският екип на СофтУни организира работен ден на басейн по случай настъпването на лятото. Вашата задача е да напишете програма, която да изчислява каква сума трябва да се заплати. За всеки един човек от екипа трябва да се заплати такса вход. Трябва да имате предвид, че един чадър стига за двама души. Знае се, че само 75% от екипа искат шезлонги. При изчислението на броя на чадърите и шезлонгите, техният брой да се закръгли до по-голямото цяло число.

Вход
От конзолата се четат 4 числа:
- Първи ред – брой на хората. Цяло число в интервала [1…100]
- Втори ред – такса вход. Реално число в интервала [0.00…50.00]
- Трети ред – цена един за шезлонг. Реално число в интервала [0.00…50.00]
- Четвърти ред – цена за един чадър. Реално число в интервала [0.00...50.00] 

Изход
- "{сумата за покриване на разходите} lv." 
Резултатът да се форматира до втората цифра след десетичния знак.

########################################
   
02. Семейна почивка
Семейство Иванови планират семейната си почивка. Вашата задача е да напишете програма, която да изчислява дали предвидения от тях бюджет ще им стигне, като знаете колко нощувки са планирали, каква е цената за нощувка и колко процента от бюджета са предвидили за допълнителни разходи. Трябва да се има предвид, че ако броят на нощувките е по-голям от 7, цената за нощувка се намаля с 5%.

Вход
От конзолата се четат 4 реда:
- Бюджетът, с който разполагат – реално число в интервала [1.00 … 10000.00]
- Брой нощувки – цяло число в интервала [0 … 1000]
- Цена за нощувка – реално число в интервала [1.00 … 500.00]
- Процент за допълнителни разходи – цяло число в интервала [0 … 100]

Изход
Отпечатването на конзолата зависи от резултата:
- Ако сумата е достатъчна:
	- "Ivanovi will be left with {останали пари след почивката} leva after vacation."
- Ако НЕ е достигната сумата:
	- "{парите нужни до достигане на целта} leva needed."
Сума трябва да се форматира до втората цифра след десетичния знак.

########################################

03. 3. Кафемашина
Напишете софтуер, който да пресмята сметката на клиент, закупил определен брой от дадена напитка от кафемашина.

			Без захар		Нормално		Допълнително захар
Еспресо		0.90 лв./бр.	1 лв. /бр.		1.20 лв. /бр.
Капучино	1.00 лв. /бр.	1.20 лв. /бр.	1.60 лв. /бр.
Чай			0.50 лв. /бр.	0.60 лв. /бр.	0.70 лв. /бр.

Трябва да имате предвид следните отстъпки:
- При избрана напитка без захар има 35% отстъпка.
- При избрана напитка "Espresso" и закупени поне 5 броя, има 25% отстъпка.
- При сума надвишава 15 лева, 20% отстъпка от крайната цена,  
Отстъпките се прилагат в реда на тяхното описване.

Вход
Входът се чете от конзолата и се състои от три реда:
- Първи ред - напитка - текст с възможности"Espresso", "Cappuccino" или "Tea"
- Втори ред - захар - текст  с възможности "Without", "Normal" или "Extra"
- Трети ред - брой напитки - цяло число в интервала [1… 50]

Изход
На конзолата трябва да се отпечата един ред:
- "You bought {брой напитки} cups of {напитка} for {крайна цена} lv."
Цената да бъде форматирана до втората цифра след десетичния знак.

########################################

03. Туристическа агенция
Туристическа агенция има нужда от система за изчисляване на дължимата сума при резервация. В зависимост от различните дестинации и различните пакети, цената е различна.
Цените за ден са следните:

Цена за ден				Банско/Боровец						Варна/Бургас
				с екипировка	без екипировка			със закуска		без закуска
					100лв.			80лв					130лв.			100лв.
VIP отстъпка		10%				5%						12%				7%

Ако клиентът е заявил престой повече от 7 дни, получава единия ден безплатно.

Вход
От конзолата се четат 4 реда:
- Име на града - текст с възможности ("Bansko",  "Borovets", "Varna" или "Burgas")
- Вид на пакета - текст с възможности ("noEquipment",  "withEquipment", "noBreakfast" или "withBreakfast")
- Притежание на VIP отстъпка - текст с възможности  "yes" или "no"
- Дни за престой - цяло число в интервала [1 … 10000]

Изход
На конзолата се отпечатва 1 ред:
- Когато потребителят е въвел всички данни правилно, отпечатваме: 
	- "The price is {цената, форматирана до втория знак}lv! Have a nice time!"
- Ако потребителят е въвел по-малко от 1 ден за престой, отпечатваме: 
	- "Days must be positive number!"
- Когато при въвеждането на града или вида на пакета се въведат невалидни данни, отпечатваме:
	- "Invalid input!"

########################################

04. Клуб
Времето се затопля и клубовете пускат обещаващи промоции. Напише програма, която да изчислява приходите на един клуб за вечерта и дали е достигната желаната печалба, като знаете следните условия: цената на един коктейл е дължината неговото име. Ако цената на една поръчка е нечетно число, има 25% отстъпка от цената на поръчката. 

Вход
От конзолата се четат:
- На първия ред – желаната печалба на клуба - реално число в интервала [1.00... 15000.00]
Поредица от два реда до получаване на командата "Party!" или до достигане на желаната печалба:
	- Име на коктейла – текст
	- Брой на коктейлите за поръчката – цяло число в интервала [1… 50]
	
Изход
На конзолата първо да се отпечата един ред:
- При получена команда "Party!":
	- "We need {недостигаща сума} leva more."
- При достигане на желаната печалба:
	- "Target acquired."
След това да се отпечата:
	- "Club income - {приходи от клуба} leva."
Парите да бъдат форматирани до втората цифра след десетичния знак.

########################################

04.	Ремонт
Пешо решава, че иска да направи ремонт вкъщи. Неговата задача е да боядиса стените в хола, като знаете височината и ширината на една стена. Холът на Пешо има 4 стени с еднакви размери, определен процент от които се заемат от прозорци и врати, които няма да бъдат боядисвани. Той не е сигурен дали ще успее наведнъж, затова моли Вас да му помогнете да изчисли дали ще му остава още работа за следващия ден и, ако да, колко кв. м. има да довърши, а в случай, че успее да боядиса хола, колко боя му е останала (трябва да се има предвид, че с един литър боя се боядисва един квадратен метър от стената). 

Вход
От конзолата се четат следните редове:
- Височина на стената - цяло число [0… 100]
- Ширина на стената - цяло число [0… 100]
- Процент от общата площ на стените, който няма да бъде боядисан - цяло число [5… 95]
На следващите редове до получаване на командата "Tired!" или докато не бъдат боядисани всички стени, се чете по едно число:
	- Литри боя – цяло число [0…100]:
Забележка: Площта за боядисване да бъде закръглена нагоре до най-близкото цяло число.

Изход
Да се отпечата на конзолата един от следните редове:
- При получаване на командата "Tired!":
	- "{квадратни метри} quadratic m left." 
	- {квадратни метри} е повърхнината, която му остава да боядисана.
- Aко е останала боя в излишък:
	- "All walls are painted and you have {литри боя} l paint left!" 
- Aко след боядисването на всички стени, не е останала боя:
	- "All walls are painted! Great job, Pesho!" 

########################################

05.	Магазин за компютърни игри	
Магазин за компютърни игри ви наема за да направите статистика на процента продажби на игрите от последния месец, като изчислите по колко процента от общите продажби са за някоя от игрите.
Процентите трябва да бъдат разделени на четири части, три заглавия на игри и всички останали:
	- Hearthstone
	- Fornite
	- Overwatch
	- Others
	
Вход
От конзолата се четат:
- Брой продадени игри- n - цяло положително число в интервала [1… 100]
За следващите n реда се чете по един ред:
	- Име на игра - текст
	
Изход
На конзолата да се изпишат четири реда:
	- "Hearthstone - {процент продажби на Hearthstone}%"
	- "Fornite - {процент продажби на Fornite}%"
	- "Overwatch - {процент продажби на Overwatch}%"
	- "Others - {процент продажби на всички останали игри}%"
Резултатът да бъде закръглен до втората цифра след десетичния знак.

########################################

05. Футболно състезание
Задачата ви е да напишете програма, която приема името на отбор и прави статистика за него. През един сезон всеки отбор изиграва определен брой футболни срещи, като за всяка среща на отбора се дават точки в зависимост от изхода от срещата. Има три възможни изхода от една среща:
	- W - Отборът е победител и получава 3 точки
	- D - Срещата е завършила без победител и отборът получава 1 точка
	- L - Отборът е загубил срещата и не получава точки
Напишете програма, която приема името на футболен отбор и извежда неговата статистика, на база на изиграните срещи през този сезон. Неговата статистика трябва да включва общия брой спечелени точки през настоящия сезон, подробна статистика за изхода на изиграните игри и процент победи през сезона. Ако отборът по някаква причина не е играл мачове през настоящия сезон се извежда специално съобщение.

Вход
От конзолата се четат два реда:
	- Името на футболния отбор, за който водим статистика - текст
	- Броя изиграни срещи през настоящия сезон - цяло число в интервала [0… 100]
 За всяка изиграна среща се прочита отделен ред:
	- Резултатът от изиграната среща в един от горепосочените формати – символ с възможности 'W', 'D' и 'L'
	
Изход
В зависимост от това дали отборът е играл мачове през настоящия сезон се извеждат два вида изход.
- Ако отборът не е изиграл нито един мач през настоящия сезон се извежда точно един ред в следния формат:
	- "{името на отбора} hasn't played any games during this season."
- Ако отборът е изиграл един мач или повече се извеждат шест реда в следния формат:
	- "{името на отбора} has won {брой спечелени точки} points during this season"
	- "Total stats:"
	- "## W: {брой спечелени игри}"
	- "## D: {брой игри, завършили наравно}" 
	- "## L: {брой загубени игри}" 
	- "Win rate: {процент спечелени игри}%"
Процентът спечелени игри трябва да бъде форматиран до втората цифра след десетичния знак.

########################################

06. Игра на имена
Иван е измислил нова игра в която да се състезава със своите приятели. Вашата задача е да напишете програма за играта. Всеки играч написва името си, след това за всяка една буква от името си написва по едно цяло число, ако числото съвпада с ASCII стойността на съответната буква, играчът получава 10 точки, в противен случай, получава само 2 точки. Победител е играчът с най-много точки в края на играта. В случай, че двама играчи имат равен брой точки, печели този, който втори е достигнал резултата.

Вход
До получаване на командата "Stop" се чете по един ред:
- Име на играча с дължина n - текст
За всеки играч се четат n на брой реда:
	- число – цяло число в интервала[0…127] 
	
Изход
Да се отпечата един ред в следния формат:
- "The winner is {името на победителя} with {точките на победителя} points!"

########################################

06. Най-силната дума
 За Лора думите притежават голяма сила. Тя те моли да измислиш алгоритъм, с който да откриеш коя е "най-силната" дума. До получаване на команда "End of words" ще се четат от конзолата думи. За да се открие силата на всяка една, трябва да се намери сборът от ASCII стойностите на символите, от които се състои думата. Ако започва с гласна буква - 'a', 'e', 'i', 'o', 'u', 'y' (или техните еквивалентни главни букви), полученият сбор трябва да се умножи по дължината на думата, в противен случай, да се раздели на дължината и да се закръгли до най-близкото цяло число надолу.
 
Вход
До получаване на команда "End of words" се чете по един ред от конзолата:
	- дума – текст
	
Изход
След приключване на програмата се печата на един ред думата с "най-голяма сила":
	- "The most powerful word is {думата с най-голяма сила} - {силата на думата}" 

########################################
