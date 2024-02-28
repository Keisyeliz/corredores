import os
os.system('cls')
corredor1Str = input('Nombre participante 1 -> ')
numeroP1Int = int(input('Número del participante 1 -> '))
corredor2Str = input('Nombre particante 2 -> ')
numeroP2Int = int(input('Número del particante 2 -> '))
var_kmrecorridos1Int = 0
var_kmrecorridos2Int = 0
controInt = True

while controInt == True:
    os.system('cls')
    print('<<<<< MENU DE OPCIONES >>>>\n\n')
    print('1.',corredor1Str,' No. ',numeroP1Int,' ',var_kmrecorridos1Int,'Km\n2.',corredor2Str,' No. ',numeroP2Int,' ',var_kmrecorridos2Int,'Km\n3. Finalizar')
    opcionInt = int(input('\nSeleccione una opción -> '))
    if opcionInt >=1 and opcionInt <= 2:
        var_recorridoEtapaInt = int(input('Ingrese los Km recorridos -> '))
        if opcionInt == 1:
            var_kmrecorridos1Int += var_recorridoEtapaInt
        if opcionInt == 2:
            var_kmrecorridos2Int += var_recorridoEtapaInt
    if opcionInt == 3:
        os.system('cls')
        print('<<<<< REPORTE DE COMPETENCIA >>>>>')
        print('Participante No. 1 ', corredor1Str, ' Recorrido: ', var_kmrecorridos1Int,'Km')
        print('Participante No. 2 ', corredor2Str, ' Recorrido: ', var_kmrecorridos2Int,'Km')
        enter = input('\n<ENTER> para continuar')
        controInt = False