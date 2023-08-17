def caballo(posicion, movimientos):
    if posicion == 1:
        if movimientos > 1:
            return caballo(6, movimientos-1) + caballo(8,movimientos-1)
        else:
            return 2

    elif posicion == 2:
        if movimientos > 1:
            return caballo(7, movimientos-1) + caballo(9,movimientos-1)
        else:
            return 2
        
    elif posicion == 3:
        if movimientos > 1:
            return caballo(4, movimientos-1) + caballo(8,movimientos-1)
        else:
            return 2
        
    elif posicion == 4:
        if movimientos > 1:
            return caballo(3, movimientos-1) + caballo(9,movimientos-1) + caballo(0,movimientos-1)
        else:
            return 3
    
    elif posicion == 5:
        return 0
    
    elif posicion == 6:
        if movimientos > 1:
            return caballo(1, movimientos-1) + caballo(7,movimientos-1) + caballo(0,movimientos-1)
        else:
            return 3
        
    elif posicion == 7:
        if movimientos > 1:
            return caballo(2, movimientos-1) + caballo(6,movimientos-1)
        else:
            return 2
        
    elif posicion == 8:
        if movimientos > 1:
            return caballo(1, movimientos-1) + caballo(3,movimientos-1)
        else:
            return 2
        
    elif posicion == 9:
        if movimientos > 1:
            return caballo(2, movimientos-1) + caballo(4,movimientos-1)
        else:
            return 2
    
    elif posicion == 0:
        if movimientos > 1:
            return caballo(4, movimientos-1) + caballo(6,movimientos-1)
        else:
            return 2
        
def caballo2(posicion, movimientos):
    if posicion == 1: posibilidades = (6,8)
    elif posicion == 2: posibilidades = (9,7)
    elif posicion == 3: posibilidades = (4,8)
    elif posicion == 4: posibilidades = (3,9,0)
    elif posicion == 5: posibilidades = ()
    elif posicion == 6: posibilidades = (1,7,0)
    elif posicion == 7: posibilidades = (2,6)
    elif posicion == 8: posibilidades = (1,3)
    elif posicion == 9: posibilidades = (2,4)
    elif posicion == 0: posibilidades = (4,6)

    if movimientos > 1:
        return sum(list(map(lambda posibilidad: caballo2(posibilidad, movimientos-1), posibilidades)))
        '''
        total = 0
        for elemento in posibilidades:
            total += caballo2(elemento, movimientos - 1)    
        return total
        '''
    else:
        return len(posibilidades)

total_movimientos = 0
movimientos = int(input("Cuantos movimientos realiza el caballo? "))
for i in range (10):
    print(f"Desde la posición {i} con {movimientos} movimientos el caballo se puede mover {caballo2(i,movimientos)} veces.")
    total_movimientos += caballo2(i,movimientos)
print(f"\nEn total son {total_movimientos} movimientos.")