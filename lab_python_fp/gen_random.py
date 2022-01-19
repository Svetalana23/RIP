import random
#gen_random(5, 1, 3) должен выдать выдать 5 случайных чисел
# в диапазоне от 1 до 3, например 2, 2, 3, 2, 1

def gen_random(num_count, begin, end):
    for i in range(num_count):
            yield random.randint(begin,end)

gen_random1=gen_random(5,1,9)
for i in gen_random1:
    print(i)