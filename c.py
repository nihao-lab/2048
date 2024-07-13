"""
Up
下：Down
左：Left
右：Right
"""

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
    def left(self):
        for itme in self.map:
            self.new=itme
            self.__merge()
    def right(self):
        for itme in self.map:
            self.new=itme[::-1]
            self.__merge()
            itme[::-1]=self.new
    def matrix_transpose(self):
        new=[list(itme)for itme in zip(*self.map)]
        self.map[:]=new
    def up(self):
        self.matrix_transpose()
        self.left()
        self.matrix_transpose()
    def down(self):
        self.matrix_transpose()
        self.right()
        self.matrix_transpose()







