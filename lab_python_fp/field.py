goods = [
 {'title': 'Кресло', 'price': 5700, 'color': 'pink'},
 {'title': 'Диван раскладной', 'price': 26700, 'color': 'cream'}] #создание списка с аргументами в виде словарей

def field(items, *args): # генератор field  качестве первого аргумента генератор принимает список словарей,
 # дальше через *args генератор принимает неограниченное количествово аргументов
  assert len(args) > 0 # если данное утвержение верно
  for i in items: # перебираем весь список
   if(len(args)==1): # если передан только один аргумент,то генератор выводит только значение поля
    if(i.get(args[0])): #метод get() возвращает значение для данного ключа
      yield i [args[0]]
   else: #если передано несколько аргументов
    res={} # пустой словарь
    for a in args:
      if(i.get(a)):
       res[a]=i[a]
    if(len(res.items())!=0):
     yield res

field_gen=field(goods, 'title')
field_gen1=field(goods, 'title', 'price')
for i in field_gen:
   print(i)
for i in field_gen1:
   print(i)

