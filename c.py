"""
Up
下：Down
左：Left
右：Right
"""
import time
#
class C:
    def __init__(self):
        self.map=[
            [1,2,1,2],
            [1,2,1,2],
            [1,2,1,2],
            [1,2,1,2],
        ]
        self.new=None

    @staticmethod
    def __time(func):
        def warp(*args, **kwargs):
            dict_={'left':'左移',"right":'右移',"up":'上移','down':'下移'}
            star_time = time.time()
            func(*args)
            end_time = time.time()
            values=dict_[func.__name__]
            print(f'{values}动作的运行时间是{end_time - star_time:.5f}秒')
            return func
        return warp
    def __zero(self):
        for i in range(len(self.new)-1,-1,-1):
            if self.new[i]==0:
                del self.new[i]
                self.new.append(0)
    def __merge(self):
        self.__zero()
        for i in range(len(self.new)-1):
            if self.new[i]==self.new[i+1]:
                self.new[i]*=2
                del self.new[i+1]
                self.new.append(0)
    @__time
    def left(self):
        for itme in self.map:
            self.new=itme
            self.__merge()
    @__time
    def right(self):
        for itme in self.map:
            self.new=itme[::-1]
            self.__merge()
            itme[::-1]=self.new
    def matrix_transpose(self):
        new=[list(itme)for itme in zip(*self.map)]
        self.map[:]=new
    @__time
    def up(self):
        self.matrix_transpose()
        self.left()
        self.matrix_transpose()
    @__time
    def down(self):
        self.matrix_transpose()
        self.right()
        self.matrix_transpose()







