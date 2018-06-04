import a
'''
def run():
    inp = input('shuru')
    if inp == 'login':
        a.login()
    if inp =='home':
        a.home()
    if inp =='logout':
        a.login()
'''
def run1():
    inp = input('shuru2')
    #modules,func = inp.split('/')    动态导入模块
    #obj = __import__("另一个文件夹名."+modules,fromlist=True)        等于from 另一个文件夹的模块(a.py)，（下面的a替换为obj）
    if hasattr(a,inp):           #判断模块a.py里面有没有跟inp同名的函数
        func = getattr(a,inp)    #在模块a.py里寻找跟inp同名的函数返回使用
        func()
    else:
        print('no',inp)
if __name__ == '__main__':
    run1()
