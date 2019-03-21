def generarArrayInt(n):
    datos = []
    import random
    if n>0:
        for i in range(n):
            datos.append(random.randint(1,10000000))
        return datos
    return None