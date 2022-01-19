# Итератор для удаления дубликатов
class Unique:
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = False, Aбв и АБВ - разные строки
        #           ignore_case = True, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        self.used_elements = set() # тут мы будем хранить значения, которые уже занесли для вывода как уникальные
        self.data = items
        self.index = 0
        if 'ignore_case' not in kwargs: # ignore_case-ключевое значение
            self.ignore_case=False
        else:
            self.ignore_case=kwargs['ignore_case']

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]
                self.index = self.index + 1
                if self.ignore_case: # если False
                    if current.lower() not in self.used_elements:
                      self.used_elements.add(current.lower())
                      return current
                else:
                    if current not in self.used_elements:
                    # Добавление в множество производится
                    # с помощью метода add
                      self.used_elements.add(current)
                      return current

    def __iter__(self):
        return self

lst2 = [1,3,2,3,2,1,4,7,3,3]
for i in Unique(lst2):
    print(i)
print("-------------")
data=['a','A','c','C','C','B','b','b']
for a in Unique(data,ignore_case=False):
    print(a)
print("-------------")
for a in Unique(data,ignore_case=True):
    print(a)








