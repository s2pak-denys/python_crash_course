#print("Python")

#щоб додати одинарну табуляцію до тексту \t
#print("\tPython")

#щоб додати до тексту новий рядок, напиши \n
#print("languages:\nPython\nc\nJavaScript")

#комбінувати таб та символи в одному значенні типу string. 
#приклад "\n\t"
#print("languages:\n\tPython\n\tc\n\tJavaScript")

#щоб забезпечити відсутність пробільних символів з правого боку рядка метод rstrip()

>>> favorite_language = 'python '
>>> favorite_language
'python '
>>> favorite_language.rstrip()
'python'
>>> favorite_language
'python '

#щоб остаточно прогалину з рядка треба привязати нове значення зміної до імені
>>> favorite_language
'python '
>>> favorite_language = 'python '
>>> favorite_language = favorite_language.rstrip()
>>> favorite_language
'python'




