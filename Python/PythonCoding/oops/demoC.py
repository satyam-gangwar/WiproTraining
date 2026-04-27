from oops.demoA import A
from oops.demoB import B


class C(B, A):
    def __init__(self,n1, n2, msg):
        A.__init__(self, n1,  n2)
        super().__init__(msg)

    def final(self):
        print('Done')