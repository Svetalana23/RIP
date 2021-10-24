# используется для сортировки
from operator import itemgetter
 
class Lang:
    
    def __init__(self, id, namee, year, lang_id):
        self.id = id
        self.namee = namee
        self.year = year
        self.lang_id = lang_id
 
class Env:
    
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Env_Lang:
    """
    'Сотрудники отдела' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, lang_id, env_id):
        self.lang_id = lang_id
        self.env_id = env_id
 
# Отделы
langs = [
    Lang(1, 'JavaScript', 1995, 1),
    Lang(2, 'Assembly language', 1949, 2),
    Lang(3, 'Pascal', 1968, 3),
    Lang(4, 'Python', 1991, 4),

 ]
 
envs = [
    Env(1, 'Visual Studio Code'),
    Env(2, 'Atom'),
    Env(3, 'Notepad++'),
    Env(4, 'Eclipse'),
]
 
langs_envs = [
    Env_Lang(1,1),
    Env_Lang(2,2),
    Env_Lang(3,3),
    Env_Lang(4,4),
 ]
 
def main():
    """Основная функция"""
 
    # Соединение данных один-ко-многим 
    one_to_many = [(e.namee, e.year, d.name) 
        for d in envs 
        for e in langs
        if e.lang_id==d.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, ed.lang_id, ed.env_id) 
        for d in envs
        for ed in langs_envs
        if d.id==ed.lang_id]
    
    many_to_many = [(e.namee, e.year, env_name) 
        for env_name, lang_id, env_id in many_to_many_temp
        for e in langs if e.id==env_id]
 
    print('Задание B1')
    a1 = list(filter(lambda x : (str)(x[2]).startswith('A'), one_to_many))
    a1 = [(el[2], el[1]) for el in a1]
    print(a1)

    print('Задание B2')
    res_2 = []
    for d in envs:
        d_vods = list(filter(lambda i: i[2] == d.name, one_to_many))
        if len(d_vods) > 0:
           res_2.append(min(d_vods, key = lambda i: i[1] ))

        res_2 = sorted(res_2, key = lambda i: i[1])
    print(res_2)
 
    print('Задание B3')
    res_3 = sorted(many_to_many, key = itemgetter(2))
    print(res_3)

if __name__ == '__main__':
    main()
 

