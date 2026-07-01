from validaciones.funciones import validar_rango, es_par, es_primo, es_multiplo

print(validar_rango(4, 12, 20))
print(validar_rango(15, 1,10))

print(es_par(9))
print(es_par(8))

print(es_primo(14))
print(es_primo(15))

print(es_multiplo(14, 7))
print(es_multiplo(8, 16))