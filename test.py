import unittest
import QuadraticEqation


class MyTestCase(unittest.TestCase):
    def test_0_0_0(self):
        experror = "R"
        expresult = []
        a = 0
        b = 0
        c = 0
        answer, acterror = QuadraticEqation.Equation.Equl(a, b, c)
        self.assertEqual(experror, acterror)
        self.assertEqual(expresult, answer)

    def test_0_0_3(self):
        experror = "Нет корней"
        expresult = []
        a = 0
        b = 0
        c = 3
        answer, acterror = QuadraticEqation.Equation.Equl(a, b, c)
        self.assertEqual(experror, acterror)
        self.assertEqual(expresult, answer)

    def test_0_5_1(self):
        experror = ""
        a = 0
        b = 5
        c = 1
        expresult = [-5]
        answer, acterror = QuadraticEqation.Equation.Equl(a, b, c)
        self.assertEqual(experror, acterror)
        self.assertEqual(expresult, answer)

    def test_2_6_9(self):
        experror = ""
        a = 2
        b = 6
        c = 9
        expresult = []
        answer, acterror = QuadraticEqation.Equation.Equl(a, b, c)
        self.assertEqual(experror, acterror)
        self.assertEqual(expresult, answer)

    def test_1_m3_2(self):
        experror = ""
        a = 1
        b = -3
        c = 2
        expresult = [2, 1]
        answer, acterror = QuadraticEqation.Equation.Equl(a, b, c)
        self.assertEqual(experror, acterror)
        self.assertEqual(expresult, answer)

    def test_1_2_1(self):
        experror = ""
        a = 1
        b = -3
        c = 2
        expresult = [-1]
        answer, acterror = QuadraticEqation.Equation.Equl(a, b, c)
        self.assertEqual(experror, acterror)
        self.assertEqual(expresult, answer)


if __name__ == '__main__':
    unittest.main()
