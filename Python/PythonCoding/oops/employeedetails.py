class EmployeeDetails:
    def __init__(self,empno,ename,basicpay):
        self.empno = empno
        self.ename = ename
        self.basic_pay = basicpay
        self.da = 20.0
        self.hra = 10.0
        self.pf = 5.5

    def calc_allowance(self):
        allowance = (self.basic_pay * self.da / 100) + (self.basic_pay * self.hra/100)
        return allowance

    def calc_deduction(self):
        deduction = (self.basic_pay * self.pf / 100)
        return deduction

    def calc_netsal(self):
        netsal = self.basic_pay + self.calc_allowance() - self.calc_deduction()
        return netsal