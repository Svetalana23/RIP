import json
from gen_random import gen_random
import sys
from lab_python_fp.cm_timer import Cm_timer_1
from lab_python_fp.print_result import print_result
# Сделаем другие необходимые импорты

path ="data_light.json"

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path) as f:
    data = json.load(f) # метод считывает файл в формате JSON и возвращает объекты Python

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return sorted(set([p.lower() for p in arg]),key=str.lower)

@print_result
def f2(arg):
    return list(filter(lambda x: str.startswith(x,'программист'),arg))


@print_result
def f3(arg):
    return list(map(lambda x:x +' с опытом Python',arg))

@print_result
def f4(arg):
    t=list(zip(arg,[" зарплата " + str(el)+ " руб." for el in list(gen_random(len(arg),100000,200000))]))
    return [e[0]+e[1] for e in t]

if __name__=='__main__':
 before_ms = "Сообщение при входе в контекстный менеджер на основе классса"
 after_ms = "Сообщение при выходе из контекстного менеджера на основе классса"
 with Cm_timer_1(before_ms,after_ms) as cm_object:
    f4(f3(f2(f1([el['job-name'] for el in data]))))
