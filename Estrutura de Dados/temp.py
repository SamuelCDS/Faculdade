import datetime
data1 = input().split()
data2 = input().split()

data11 = data1[1].split(':')
data22 = data2[1].split(':')
dia = datetime.timedelta(days=int(data2[0]), hours=int(data22[0]), minutes=int(data22[1]), seconds=int(data22[2])) - datetime.timedelta(days=int(data1[0]), hours=int(data11[0]), minutes=int(data11[1]), seconds=int(data11[2]))
try:
    if ((int(data2[0])-int(data1[0])) >= 0) and (data1 != data2):
        dia = str(dia)
        dia = dia.split()
        if len(dia) > 1:
            horas = dia[2].split(':')
            print(f'{int(dia[0])} dia(s)\n{int(horas[0])} hora(s)\n{int(horas[1])} minuto(s)\n{int(horas[2])} segundo(s)')
        else:
            horas = dia[0].split(':')
            print(f'0 dia(s)\n{int(horas[0])} hora(s)\n{int(horas[1])} minuto(s)\n{int(horas[2])} segundo(s)')
    else:
        print('Data inválida!')
except:
    print('Data inválida!')