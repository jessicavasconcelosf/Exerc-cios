import random
import datetime

num_inteiro = random.randint(1,1000)

print ("NUMERO ALEATORIO: ",num_inteiro)


data_atual = datetime.date.today().day
print ("DATA ATUAL: ",data_atual) 

sub = num_inteiro - data_atual

print ("SUBTRAÇÃO: ",sub)

horas = datetime.datetime.now().hour
print ("HORÁRIO ATUAL:",horas,"H")

div = num_inteiro / 3 
print (f"DIVISÃO :  {div:.2f}")

ac_dia = datetime.timedelta(hours=div)


dia_atual = datetime.datetime.now()



data_futura = dia_atual + ac_dia
print ("DATA E HORÁRIO FUTURO: ", data_futura)
des_horas = data_futura.hour



semana = data_futura.weekday()




if semana == 0:
    print ("Segunda feita")
elif semana == 1:
    print ("Terça Feira")
elif semana == 2:
    print ("Quarta Feira")
elif semana ==3:
    print ("Quinta Feira")
elif semana ==4:
    print ("Sexta Feira")
elif semana ==5:
    print ("Sabado")
elif semana ==6:
    print ("Domingo")
else: 
    print ("erro")


if semana in (0,1,2,3,4) and (des_horas > 8 or des_horas < 18) :
        print ("HORÁRIO COMERCIAL")
else:
    print ("HORÁRIO NÃO COMERCIAL")