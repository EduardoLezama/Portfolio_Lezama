import cv2
import face_recognition as fr

# Cargar imagenes
foto_control = fr.load_image_file('FotoA.jpg')
foto_prueba = fr.load_image_file('FotoB.jpg')

# Pasar imagenes a RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Localizar cara control
lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

# Localizar cara prueba
lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]

# Mostrar rectangulos
cv2.rectangle(foto_control,
              (lugar_cara_A[3], lugar_cara_A[0]),
              (lugar_cara_A[1], lugar_cara_A[2]),
              (0, 255, 0),
              2)

cv2.rectangle(foto_prueba,
              (lugar_cara_B[3], lugar_cara_B[0]),
              (lugar_cara_B[1], lugar_cara_B[2]),
              (0, 255, 0),
              2)

# Comparar caras
resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B)

# Medir distancia
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B)

# Mostrar resultado
cv2.putText(foto_prueba,
            f'{resultado} {distancia.round(2)}',
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0, 255, 0),
            2
            )

# Establecer un tamaño máximo para la ventana
max_width = 1000
max_height = 1000

# Obtener dimensiones originales de las imágenes
height, width, _ = foto_control.shape

# Verificar si el ancho o el alto son mayores que el máximo permitido
if width > max_width or height > max_height:
    # Calcular el factor de escala para ajustar el tamaño
    scale = min(max_width / width, max_height / height)

    # Redimensionar las imágenes
    foto_control = cv2.resize(foto_control, (int(width * scale), int(height * scale)))
    foto_prueba = cv2.resize(foto_prueba, (int(width * scale), int(height * scale)))

# Mostrar imagenes
cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)

# Mantener programa abierto
cv2.waitKey(0)
