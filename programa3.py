opc = int(input('Seleccione una opcion:\n'
                '1. EURO a LIBRA\n'
                '2. LIBRA a EURO\n'
                '3. DOLAR a EURO\n'
                '4. EURO a DOLAR\n'))
money = float(input('Ingrese la cantidad que desea convertir\n'))
if opc == 1:
    exe = money * 0.87
    print('EL monto de {} EUROS equivale a {} LIBRAS'.format(money, exe))
elif opc == 2:
    exe = money * 1.15
    print('EL monto de {} LIBRAS equivale a {} EUROS'.format(money, exe))
elif opc == 3:
    exe = money * 0.94
    print('EL monto de {} DOLARES equivale a {} EUROS'.format(money, exe))
elif opc == 4:
    exe = money * 1.06
    print('EL monto de {} EUROS equivale a {} DOLAR'.format(money, exe))
else:
    print('No eligio un opcion valida')
