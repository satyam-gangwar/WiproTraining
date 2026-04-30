from src.calculations import Calculations


class TestCalc:
    calc = Calculations()

    def test_area_square(self):
        res = self.calc.area_square(10)
        assert res == 100, 'Area is wrong'

    def test_peri_rectangle(self):
        res = self.calc.peri_rectangle(10,5)
        assert res == 30, 'Perimeter is wrong'