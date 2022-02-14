from pytube import YouTube
from math import ceil
from moviepy.editor import AudioFileClip
from string import punctuation
from os import remove

def main():
    interfaz()


def iniciar_descarga(archivo_links):
    lista_mp4 = []

    try:
        txt_archivo = open(archivo_links,'r')
        #leyendo
        links = txt_archivo.readlines()
        #lo cierro
        txt_archivo.close()

        print('\nIniciando descargas')
        print('─'*len('Iniciando descargas\n'))
    

        for i in links:

            try:

                yt = YouTube(i)

                nombre = yt.title.translate(str.maketrans('', '', punctuation))
                lista_mp4.append(nombre)
            
                stream = yt.streams.get_by_itag(140)

                print('_'*ceil(len('Descarga de ' + yt.title + ' finalizada')))
                print('Descargando '+yt.title)
                
                stream.download(output_path='YMD descargas',filename=nombre +'.mp4')

                print('Descarga de ' + yt.title + ' finalizada')
                print('_'*ceil(len('Descarga de ' + yt.title + ' finalizada')))
                print('\n')

            except:
                print('\n')
                print('El video con el enlace ' + i + ' no está disponible, se pasará al siguiente')
                print('\n')
        

    except FileNotFoundError:
        print('\n')
        print('El archivo seleccionado no existe')
        print('\n')
    
    return lista_mp4

def interfaz():
    #YMD You Music Download
    print("""
 __     __           __  __           _        _____                      _                 _ 
 \ \   / /          |  \/  |         (_)      |  __ \                    | |               | |
  \ \_/ /__  _   _  | \  / |_   _ ___ _  ___  | |  | | _____      ___ __ | | ___   __ _  __| |
   \   / _ \| | | | | |\/| | | | / __| |/ __| | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |
    | | (_) | |_| | | |  | | |_| \__ \ | (__  | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |
    |_|\___/ \__,_| |_|  |_|\__,_|___/_|\___| |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|
                                                                                              
                                                                                              
""")

    titulo = 'Descarga musica de youtube en formato mp4'
    espaciadores_1 = '─'*len(titulo)

    instrucciones = 'Escribe el nombre del archivo txt donde guardaste los url'
    instrucciones_2 = 'O escribe "salir" para finalizar'
    espaciadores_2 = '═'*len(instrucciones)

    direccion = ''

    error = 'El archivo debe tener una extension ".txt"'
    espaciadores_3 = '⚠ '*(len(error)//2)

    print(espaciadores_1)
    print(titulo)
    print(espaciadores_1)

    print('\n')
    
    while direccion.lower() != 'salir':
        print(instrucciones)
        print(instrucciones_2)
        print(espaciadores_2)
        direccion = input('direccion: ')

        extension_cadena = direccion[len(direccion)-4:len(direccion)]

        if extension_cadena.lower() == '.txt':
            #devuelve una lista con los nombres de las canciones
            lista_mp4 = iniciar_descarga(direccion)
            convertir_mp3(lista_mp4)

        elif direccion.lower() == 'salir':
            print('─'*len('saliendo'))
            print('Saliendo')
            print('─'*len('saliendo'))

        else:
            print('\n')
            print(espaciadores_3)
            print(error)
            print(espaciadores_3)
            print('\n')

def convertir_mp3(lista_mp4):
    print('─'*len('Comenzando conversión a formato "mp3"'))
    print('Comenzando conversión a formato "mp3"')
    print('─'*len('Comenzando conversión a formato "mp3"'))
    print('\n')

    for i in lista_mp4:
        direccion_mp4 = 'YMD descargas/' + i

        try:

            print('_'*ceil(len('Conversión de ' + i + ' a formato "mp3" finalizada')))
            print('Convirtiendo ' + i + ' a formato "mp3"')

            #tomando el archivo mp4 y creando un mp3
            mp4_to_mp3(direccion_mp4+'.mp4', direccion_mp4+'.mp3')

            #eliminando archivo .mp4
            remove(direccion_mp4+'.mp4')

            print('Conversión de ' + i + ' a formato "mp3" finalizada')
            print('_'*ceil(len('Conversión de ' + i + ' a formato "mp3" finalizada')))
            print('\n')
        except:
            print('Ha ocurrido un error durante la conversión del archivo llamado '+ i +' a mp3')
            print('Se conservará el archivo en formato mp4')
    
    print('─'*len('Música descargada correctamente en la carpeta llamada "YMD descargas"'))
    print('Música descargada correctamente en la carpeta llamada "YMD descargas"')
    print('─'*len('Música descargada correctamente en la carpeta llamada "YMD descargas"'))
    print('\n')


def mp4_to_mp3(mp4, mp3):
    mp4_without_frames = AudioFileClip(mp4)
    mp4_without_frames.write_audiofile(mp3)
    mp4_without_frames.close() 
    # function call mp4_to_mp3("my_mp4_path.mp4", "audio.mp3")


if __name__ == '__main__':
    main()
