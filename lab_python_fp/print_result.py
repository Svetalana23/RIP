# Здесь должна быть реализация декоратора
def print_result(func_to_decorate):
    def decorate_func(*args):
        print(func_to_decorate.__name__)
        f=func_to_decorate(*args)
        if isinstance(f,list):
         for v in f:
            print(v)
         return f
        elif isinstance(f,dict):
          for key,value in f.items():
             print ("{} = {}".format(key,value))
          return f
        else:
            print(f)
            return f
    return decorate_func

@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4():
    return [1, 2]

print('!!!!!!!!')
test_1()
test_2()
test_3()
test_4()
