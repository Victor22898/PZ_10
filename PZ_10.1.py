# В магазинах имеются следующие. Магнит - молоко, соль, сахар. Пятерочка - мясо, молоко, сыр. Перекресток - молоко, творог, сыр, сахар. Определить:
# 1.в каких магазинах нельзя приобрести сыр. 2 в каких магазинах приобрести одновременно молоко и сахар. 3. в каких магазинах можно пиобрести соль.
magnit = {'молоко', 'соль', 'сахар'}
pyterochka = {'мясо', 'молоко', 'сыр'}
perekrestok = {'молоко', 'творог', 'сыр', 'сахар'}

stpres_without_cheese = []

if 'сыр' not in magnit:
    stpres_without_cheese.append('Магнит')
    if 'сыр' not in pyterochka:

        stpres_without_cheese.append('Пятерочка')
        if 'сыр'not in perekrestok:
            stores_without_cheese.append('Перекресток')
            print("В магазинах нельзя приобрести сыр:", stpres_without_cheese)

milk_and_sugar_stores = []

if 'молоко' in magnit and 'сахар' in magnit:
  milk_and_sugar_stores.append('Магнит')
if 'молоко' in pyterochka and 'сахар' in pyterochka:
    milk_and_sugar_stores.append('Пятерочка')
if 'молоко' in perekrestok and 'сахар' in perekrestok:
 milk_and_sugar_stores.append('Перекресток')

print("В магазинах можно приобрести молоко и сахар:", milk_and_sugar_stores)

stores_with_salt = []

if 'соль' in magnit:
    stores_with_salt.append('Магнит')
if 'соль' in pyterochka:
    stores_with_salt.append('Пятерочка')
if 'соль' in perekrestok:
    stores_with_salt.append('Перекресток')

print("В магазинах можно приобрести соль:", stores_with_salt)