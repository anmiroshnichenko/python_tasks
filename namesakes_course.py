#     Условие задачи:
# В этом задании вы должны для каждого курса в отдельности подсчитать, сколько на нём встречается преподавателей-тёзок — людей с одинаковыми именами 
# и разными фамилиями.
# После того как все тёзки обнаружены, вы должны вывести название курса и список преподавателей-тёзок (с именем и фамилией в алфавитном порядке), 
# которые обучают студентов в рамках этого курса.
# Как назвать переменные, решайте сами (советуем выбирать максимально осмысленные имена). Вы можете придумать свой алгоритм, отличный от предложенного.
# Важно соблюдать следующий формат вывода:
# 1 На курсе Java-разработчик с нуля есть тёзки: Иван Бочаров, Иван Маркитан, ...
# 2 На курсе Fullstack-разработчик на Python есть тёзки: Александр Бардин, Александр Иванов, ...
# 3 На курсе Python-разработчик с нуля есть тёзки: Александр Бардин, Александр Ульянцев, ...
# 4 На курсе Frontend-разработчик с нуля есть тёзки: Александр Фитискин, Александр Шлейко, ...
# Это задание поможет вам систематизировать знания по словарям, множествам и спискам, 
# а также потренироваться в создании сложных алгоритмов, поэтому вы увидите только общую структуру-намёк, каким может быть алгоритм.

# Это вы мне? Подсчитываем тёзок на каждом курсе

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]
courses_list = []
for course, mentor, duration in zip(courses, mentors, durations):
	course_dict = {"title":course, "mentors":mentor, "duration":duration}
	courses_list.append(course_dict)
# С этого момента начинается выполнение задания 4.
# На входе у вас есть только список курсов courses_list. Об исходных данных, на базе которых он был сделан, вы ничего не знаете

# На каждом курсе в отдельности вам необходимо: 1) найти имена, которые встречаются более 1 раза;
# 2) отобрать людей (Имя + Фамилия), для которых совпало Имя. Это и будут наши тёзки
for course in courses_list:
	all_mentors = []
	all_mentors += course['mentors']	
	all_names = []		
	for m in all_mentors:		
		name = m.split()[0]	
		all_names.append(name)
	# Самостоятельно напишите код, который создаёт множество уникальных имён без фамилий
	# Подсказка: вам нужно вспомнить и повторить код из задания 1 по множествам
	# Результат (уникальные имена без фамилий) запишите в переменную под названием unique_names, преобразуйте в список и отсортируйте по возрастанию
	# Это необходимо, чтобы ваша программа всегда давала один и тот же результат и тренажёр смог его сверить
	unique_names = set(all_names)
	# Напишите алгоритм, который подсчитывает частоту встречаемости каждого имени из names_set в исходном списке преподавателей
	# Подсказка: при работе со строками воспользуйтесь конструкцией in
	# Внимание: в список same_name_list вы будете сохранять найденных тёзок-преподавателей
	same_name_list = []
	# Организуйте цикл по всем именам на курсе из множества:
	for name in unique_names:		
		# Подсчитайте частоту встречаемости имени (должно быть более 1 раза):
		if all_names.count(name) > 1:			
			# Сделайте цикл по исходному списку преподавателей (с Именем и Фамилией)
			for mentor in all_mentors:				
				# Найдите тех преподавателей, у кого совпало имя (для них if вернёт True)
				if name in mentor:					
					# Добавьте преподавателя с этим именем в список тёзок
					same_name_list.append(mentor)
	# Если список тёзок не пустой, выведите всех преподавателей из него
	if len(same_name_list) > 0:
		# Дополните конструкцию ниже, чтобы выводилось сообщение такого вида: На курсе Название есть тёзки: тёзки через запятую
		# Подсказка: для соединения преподавателей через запятую используйте string.join()
		print(f'На курсе {course["title"]} есть тёзки: {", ".join(sorted(same_name_list))}')
print('-------------------------------------------------------------------------------------------------------------------------')
	
# Решение эксперта
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Это вы мне? Подсчитываем тёзок на каждом курсе
# 4) продолжаем заниматься статистикой. Считаем, сколько тёзок на каждом курсе
# После того как нашли тёзок, выведите преподавателей-тёзок с Именем и Фамилией )

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]

courses_list = []
for course, mentor, duration in zip(courses, mentors, durations):
	course_dict = {"title":course, "mentors":mentor, "duration":duration}
	courses_list.append(course_dict)

# Решение без list comprehension с lambda:
# Работаем с каждым курсом отдельно: 1) отделяем имена, считаем, какие из них встречаются больше 1 раза;
# 2) для имени с встречаемостью больше 1 раза проходимся циклом по списку Имя + Фамилия, и если имя там встречается,
# добавляем его в конечный список same_name_list
for course in courses_list:
	names_list = []
	for mentor in course["mentors"]:
		names_list.append(mentor.split(" ")[0].strip())
	# Чтобы результат был всегда одинаков для тренажёра, сделаем уникальные имена списком и отсортируем по возрастанию
	unique_names = sorted(list(set(names_list)))
	same_name_list = []
	for name in unique_names:
		if names_list.count(name) > 1:
			for name_and_last in course["mentors"]:
				if name in name_and_last:
					same_name_list.append(name_and_last)
	if len(same_name_list) > 0:
		print(f'На курсе {course["title"]} есть тёзки: {", ".join(sorted(same_name_list))}')
