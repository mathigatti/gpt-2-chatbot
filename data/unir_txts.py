import os
import sys

def unir_txts(carpeta_con_los_txts):
	lista_de_txts = os.listdir(carpeta_con_los_txts) # Esto arma la lista de todos los archivos que estan en ese directorio/carpeta

	texto_final = "" # Variable donde voy a ir juntando el texto de todos los txts

	for nombre_del_txt in lista_de_txts: # recorro los archivos uno por una
	 # uno el nombre de la carpeta con el nombre del archivo para armar la ruta exacta donde el txt se ubica
	 ruta_al_archivo = carpeta_con_los_txts + "/" + nombre_del_txt 

	 # leo el archivo y agrego su texto a "texto_final"
	 with open(ruta_al_archivo,'r') as f:
	  texto_del_proximo_txt = f.read()
	  texto_final = texto_final + texto_del_proximo_txt.strip() + "\n"

	# Escribo todo el texto en un archivo llamado "archivo_final.txt"
	with open("merge.txt",'w') as f:
	 f.write(texto_final.strip())


if __name__ == '__main__':
	carpeta_con_los_txts = sys.argv[1]
	unir_txts(carpeta_con_los_txts)