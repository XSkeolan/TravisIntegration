import QuadraticEqation;


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
answer, error = QuadraticEqation.Equation.Equl(a, b, c)
print(answer)
print(error)