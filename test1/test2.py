from multiprocessing import Process
# def fun():
#     print("hello")
#
# if __name__=="__main__":
#     p=Process(target=fun,args=())
#     p.start()

class my_process(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print("the name id %s"%self.name)

if __name__=="__main__":
    p=my_process("线程1")
    p.start()

    print("jjjjjjjjjjjjjj")