
palabras_distintivas = []
num_ocurrencias_por_palabra=[]
contador = 0
# 2,2,3,4,5,6,6,6,7,9
palabras = open('file.txt','r').readlines()
# Se eliminan los saltos de linea del archivo leido
palabras_limpias = [l.strip('\n\r') for l in palabras]
num_palabras = palabras_limpias.pop(0)

for palabra in palabras_limpias:
    if not palabra in palabras_distintivas:
        palabras_distintivas.append(palabra)
        for comparar_palbras in palabras_limpias:
            if palabra == comparar_palbras:
                contador +=1
        num_ocurrencias_por_palabra.append(contador)
        contador = 0

num_palabras_distintivas= len(palabras_distintivas)

nuevo_archivo = open("archivo_punto1.txt", "w")
nuevo_archivo.write(str(num_palabras_distintivas))
nuevo_archivo.write('\n')
for occurrencia in num_ocurrencias_por_palabra:
    nuevo_archivo.write(str(occurrencia))
nuevo_archivo.close()
