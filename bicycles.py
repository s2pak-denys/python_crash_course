#bycycles = ['trek', 'cannondale', 'redline', 'specialized']
#print(bycycles)
#print(bycycles[0])
#print(bycycles[0]. title())

#print(bycycles[1]. title())
#print(bycycles[3]. title())


#щоб отримати останній елемент, запит -1 (print(bycycles[-1])) 
#print(bycycles[-1])
#print(bycycles[-2]. title())

#message = f"My first bycycle was a {bycycles[0].title()}."
#print(message)

               #1motorcycles: ЗАМІНА ЕЛЕМЕНТА У СПИСКУ
#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)
#motorcycles[0] = 'ducati'
#print(motorcycles)
#motorcycles[-1] = 'planeta'
#print(motorcycles)

				#додавання елементів до списку .append()


#motorcycles = ['honda', 'yamaha', 'suzuki']
#motorcycles.append('ducati')
#print(motorcycles)

#moto = []
#moto.append('izh')
#moto.append('planeta')
#moto.append('mt')
#print(moto)
 
			
				#вставляти елементи у список .insert()

#motorcycles.insert(0, 'ducati')
#print(motorcycles)

				#вилучення елементів зі списку інструукції del
#del motorcycles[0]
#print(motorcycles)

				#вилучення елементів метод pop()

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
#popped_motorccycle = motorcycles.pop()
#last_ownet = motorcycles.pop()
#first_ownet = motorcycles.pop(0)

				
#print(motorcycles)
#print(popped_motorccycle)
#print(f"the last motorcycles i ownet was a {last_ownet.title()}")
#print(f"The first motorcycles i ownet was a {first_ownet.title()}")

#				remove()
#motorcycles.remove('ducati')
too_expensive = 'ducati'
motorcycles.remove(too_expensive)

#print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")






