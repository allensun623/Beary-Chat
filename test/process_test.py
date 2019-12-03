import pysnooper

@pysnooper.snoop()
def func_a(func_a_arg_a, func, **kwargs):
    print(func_a_arg_a)
    func(**kwargs)

@pysnooper.snoop()
def func_b(arg_a, arg_a2):
    print(arg_a)

@pysnooper.snoop()
def func_c():
    print('Hello World')

if __name__ == '__main__':
    func_a(func_a_arg_a='temp', arg_a='Hello Python',arg_a2='Hello Python2', func=func_b)
    func_a(func_a_arg_a='temp', func=func_c)