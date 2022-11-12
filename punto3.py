import datetime
import calendar
import locale

locale.setlocale(locale.LC_ALL, 'esp') 

def conteo_de_dias(inicio, final):
  """
    
  """
  dia_inicial  = datetime.datetime.strptime(inicio, '%d/%m/%Y')
  dia_final    = datetime.datetime.strptime(final, '%d/%m/%Y')
  semana        = {}
  for i in range((dia_final - dia_inicial).days + 1):
    dia       = calendar.day_name[(dia_inicial + datetime.timedelta(days=i)).weekday()]
    semana[dia] = semana[dia] + 1 if dia in semana else 1
  return semana

def horas_laboradas(inicio, final):
  dias_laborados = conteo_de_dias(inicio,final)
  dias_laborales = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']
  horas_totales = 0

  for dia in dias_laborales:
    horas_totales += int(dias_laborados[dia]) * 8

  return horas_totales
  
def diferencia_horas(inicio, final):
  dia_inicial  = datetime.datetime.strptime(inicio, '%d/%m/%Y %H:%M:%S')
  dia_final    = datetime.datetime.strptime(final, '%d/%m/%Y %H:%M:%S')
  diferencia_dias = dia_final - dia_inicial
  print(diferencia_dias.days/30)
  print("seconds",diferencia_dias.seconds/3600)
  return ''


fecha_1 ='10/10/2022 10:22:20 +5000'
fecha_2 ='30/05/2023 19:42:20 +5000'
lst_fecha_1 = fecha_1.split(' ')
lst_fecha_2 = fecha_2.split(' ')
print(conteo_de_dias(lst_fecha_1[0], lst_fecha_2[0]))
print(horas_laboradas(lst_fecha_1[0], lst_fecha_2[0]))
print(diferencia_horas(fecha_1[0:19], fecha_2[0:19]))

#DD/MM/YYYY hh:mm:ss +xxxx


