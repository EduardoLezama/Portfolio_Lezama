import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# Funciones de voz

id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

# Convertir el audio captado a texto


def transformar_audio_a_texto():
    # Almacenar el reconocimiento en una variable
    r = sr.Recognizer()

    # Configuracion de microfono
    with sr.Microphone() as origen:
        # Tiempo de espera
        r.pause_threshold = 0.8

        # Dar la instruccion para hablar
        print("Ya puedes hablar")

        # Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # Conectar a google
            pedido = r.recognize_google(audio, language="es-mx")

            # Verifica la entrada de audio
            print("Instruccion: " + pedido)

            # Devolver la peticion
            return pedido

            # En caso de tener un error en la entrada de audio
        except sr.UnknownValueError:
            # Prueba de que no comprendio el error
            print("ups! Algo salío mal")

            # devolver el error
            return "Sigo esperando"

        # En caso de fallar la ejecucion
        except sr.RequestError:
            # Prueba de que no comprendio el error
            print("ups! Algo salío mal")

            # devolver el error
            return "Sigo esperando"

        # En caso de fallar la ejecucion
        except:
            # Prueba de que no comprendio el error
            print("ups! Algo salío mal")

            # devolver el error
            return "Sigo esperando"

# Funcion para escuchar al asistente


def hablar(mensaje):
    # Inicializar pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

# Informacion de fecha


def pedir_dia():
    # Crear variable con los datos de hoy
    dia = datetime.date.today()
    print(dia)

    # Crear la variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # Diccionario con dias
    calendario = {0: 'Lunes', 1: 'Martes', 2: 'Miércoles', 3: 'Jueves', 4: 'Viernes', 5: 'Sábado', 6: 'Domingo'}

    # Decir el dia de la semana
    hablar(f"Hoy es: {calendario[dia_semana]}")

# Informacion de hora


def pedir_hora():
    # Hacer una variable de hora
    hora = datetime.datetime.now()
    hora = f"Son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos"
    print(hora)

    # Decir la hora
    hablar(hora)

# Funcion de saludo


def saludo_inicial():

    # Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas nohces"
    elif hora.hour <= 6 or hora.hour < 13:
        momento = "Buenos días"
    else:
        momento = "Buenas tardes"

    # Saludo
    hablar(f'{momento} soy tu asistende de voz, ¿en que te puedo ayudar hoy?')

# Nucleo central


def nucleo_principal():
    # Activar saludo inicial
    saludo_inicial()

    # Variable de corte
    comenzar = True

    # Loop central
    while comenzar:
        # Activar el microfono y activar pedido
        pedido = transformar_audio_a_texto().lower()

        if 'abrir youtube' in pedido:
            hablar("Con gusto, estoy abriendo Youtube")
            webbrowser.open("https://www.youtube.com/")
            continue
        elif 'abrir navegador' in pedido:
            hablar("Con gusto, estoy abriendo Google")
            webbrowser.open("https://www.google.com/")
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Busca en wikipedia aguarda')
            pedido = pedido.replace('wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Encontre esto en wikipedia:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Buscando en internet')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que encontre en internet')
            continue
        elif 'reproduce' in pedido:
            hablar('Reproduciendo:')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL', 'amazon': 'AMZN', 'google': 'GOOGL'}

            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'Encontre la accion {accion}, el precio es de {precio_actual}')
                continue
            except:
                hablar('Perdón no la encontre')
                continue
        elif 'adiós' in pedido:
            hablar('Hasta pronto! Nos vemos después')
            break


nucleo_principal()






