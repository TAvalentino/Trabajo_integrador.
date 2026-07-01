def validar_rango(numero, minimo, maximo):
    """
    La funcion encuentra un numero dentro de un rango dado
    Recibe tres parametros tipo enteros
    Retorna los boolenos
    """
    if minimo > maximo:
        return False
    elif numero == minimo:
        return True
    elif numero < minimo:
        return False
    else:
        return validar_rango(numero, minimo + 1, maximo)
    
def es_par(numero):
    """
    La funcion determina si el numero es par
    Recibe como parametro un numero tipo entero
    Retorna el valor en booleano
    """
    if numero < 0:
        return es_par(-numero)
    elif numero == 0:
        return True
    elif numero == 1:
        return False
    else:
        return es_par(numero - 2)
    
def es_primo(numero, divisor = 2):

    """
    La funcion determina si es primo
    Recibe dos parametros tipo entero
    Retorna el valor en booleano
    """
    if numero < 2:
        return False
    elif divisor * divisor > numero:
        return True
    elif numero % divisor == 0:
        return False
    else:
        return es_primo(numero, divisor + 1)
    
def es_multiplo(numero, base):

    """
    La funcion determina si es multiplo de otro
    Recibe dos parametros tipo entero
    Retorna el valor en booleano
    """
    if base == 0:
        return False
    elif numero < 0:
        return es_multiplo(-numero, base)
    elif numero == 0:
        return True
    elif numero < base:
        return False
    else:
        return es_multiplo(numero - base, base)