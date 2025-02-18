from sympy import symbols, pretty_print,solve,expand, simplify, factor # pretty_printpara imprimir bien las expreciones,#solve de solucion, expand expandir


#expr = "2x + 5"   # como cadena con sympy se crea como una expresion, un objeto real que no es una cadena sino una expresion para luego poder evaluar esto, sustituir valores en el factorizarlo, simplificarlo, todo tipo de cosas diferentes que podemos hacer con el ,simplify simplificada su version completa de la expresion

#creacion de simbolos, symbols significa una incognita
x, y, z = symbols("x y z ")
print("Creación de una expresión básica")
#creacion de una expresion basica ->expr / expresion
expr1 = 2*x + 5 # no podemos poner 2x + 5 porque no le toma como expresion sino usart el asterisco * lo que muestra lo mismo es el doble de x por eso 2 por x es igual a 2*x
expr2 = x**2 - x - 6     # doble asterisco quiere decir es potenciado en este caso 2
expr3 = x**2 + y**2
expr4 = (x - 6) / (y + 5)
expr5 = (x+1)*(x+5)*(x-6)
expr6= x**3 - 31*x - 30
expr7 = x*(y +5)
expr8= x*y +5*x


print(expr1)
print(solve(expr1))

print("*"*40)

print(expr2)
print(solve(expr2))

print("*"*40)

#para que se vea mejor y bien la expresion
#print(expr3)  // expresion tal cual como se escribe el doble asterisco(**) actua omo potencia
pretty_print(expr3)
#sustituir resultado
print(expr3.subs([(x,2),(y,3)]))
print(expr3.subs({x:2,y:3}))

print("*"*40)

#print(expr4)
pretty_print(expr4)
print(solve(expr4))

print("*"*40)
print(expr5)
print(expr5)
#expandir-> funcion expand , simplificar y factorizar
print(expand(expr5)) # mostrara la version completa de la expresion matematica  en este caso x**3 - 31*x - 30

print("*"*40)

print(expr6)
#inverso de una expresion completa a su version mas simplificada    # factor, factorizar con simplificar no es lo mismo factor recrea valores
print(factor(expr6))  # = a la expresion 5


print("*"*40)
print(expr7)
print(expand(expr7))


print("*"*40)

print(expr8)
print(simplify(expr8))
