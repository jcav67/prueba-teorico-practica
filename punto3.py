import datetime
import calendar
import locale

locale.setlocale(locale.LC_ALL, 'esp') 

def conteo_de_dias(inicio, final) -> list:
  """
    mediante las librerias datetime y calendar se calcula la repeticion de dias 
    de la semana entre 2 fechas suministradas por el usuario
    args:
      incio->String
      Final->String
    return
      semana-> list
  """
  dia_inicial  = datetime.datetime.strptime(inicio, '%d/%m/%Y')
  dia_final    = datetime.datetime.strptime(final, '%d/%m/%Y')
  semana        = {}
  for i in range((dia_final - dia_inicial).days + 1):
    dia       = calendar.day_name[(dia_inicial + datetime.timedelta(days=i)).weekday()]
    semana[dia] = semana[dia] + 1 if dia in semana else 1
  return semana

def horas_laboradas(inicio, final) -> int:
  """
    haciendo uso de la funcion conteo_de_dias creada anteriormente
    se hace el conteo de dias nuevamente y se calculan las horas trabajadas
    teniendo encuenta que todos los dias laborales se trabajaron completos
    args:
      incio->String
      Final->String
    return
      horas_totales-> int
  """
  dias_laborados = conteo_de_dias(inicio,final)
  dias_laborales = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']
  horas_totales = 0

  for dia in dias_laborales:
    horas_totales += int(dias_laborados[dia]) * 8

  return horas_totales
  
def diferencia_horas(inicio, final) -> dict:
  """
    mediante las librerias datetime y calendar se calcula la repeticion de dias 
    de la semana entre 2 fechas suministradas por el usuario
    args:
      incio->String
      Final->String
    return
      semana-> list
  """
  dia_inicial  = datetime.datetime.strptime(inicio, '%d/%m/%Y %H:%M:%S')
  dia_final    = datetime.datetime.strptime(final, '%d/%m/%Y %H:%M:%S')
  diferencia_dias = dia_final - dia_inicial

  return {"segundos":diferencia_dias.seconds, "Horas":round(diferencia_dias.seconds/3600), "Días": diferencia_dias.days }


fecha_1 ='10/10/2022 10:22:20 +5000'
fecha_2 ='30/05/2023 19:42:20 +5000'
lst_fecha_1 = fecha_1.split(' ')
lst_fecha_2 = fecha_2.split(' ')
print(conteo_de_dias(lst_fecha_1[0], lst_fecha_2[0]))
print("horas laboradas",horas_laboradas(lst_fecha_1[0], lst_fecha_2[0]))
print(diferencia_horas(fecha_1[0:19], fecha_2[0:19]))


