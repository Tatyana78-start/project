"""
Дана произвольная строка. Написать программу, которая с использованием регулярных выражений находит
 все даты в строке. Допускаются следующие форматы записи даты:
●	00.00.0000
●	00/00/0000
●	00-00-0000
На месте 0 может стоять любая цифра. Программа должна вернуть список всех найденных дат.
Проверка на корректность количества дней в месяце или месяцев в году не требуется.

"""
import re


str = "The First Version was released on 12-07-2008." \
	"Next Release will might come on 12 July 2009. " \
	"The due date for payment is 2023-09-1." \
	"India gained its freedom on 15 August 1947 which was a Friday." \
	"Republic Day is a public holiday in India where the country marks and celebrates " \
	"the date on which the Constitution of India came into effect on 26-1-1950."


str_pattern = [
	"\\d{2}-\\d{2}-\\d{4}",
	"[0-9]{2}/{1}[0-9]{2}/{1}[0-9]{4}",
	"\\d{1,2}-(January|February|March|April|May|June|July|August|September|October|November|December)-\\d{4}",
	"\\d{4}-\\d{1,2}-\\d{1,2}",
	"[0-9]{1,2}\\s(January|February|March|April|May|June|July|August|September|October|November|December)\\s\\d{4}",
	"\\d{1,2}-\\d{1,2}-\\d{4}"
]

