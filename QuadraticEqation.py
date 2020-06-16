import math


class Equation:
    def __init__(self):
        pass

    @staticmethod
    def Equl(a, b, c):
        error = ""
        if a == 0:
            if b == 0:
                if c == 0:
                    error = "R"
                    return [], error
                else:
                    error = "Нет корней"
                    return [], error
            else:
                return [-b / c], error
        else:
            D = b * b - 4 * a * c
            if D > 0:
                return [(-b + math.sqrt(D)) / (2 * a), (-b - math.sqrt(D)) / (2 * a)], error
            elif D == 0:
                return [-b / (2 * a)], error
            else:
                return [], error
