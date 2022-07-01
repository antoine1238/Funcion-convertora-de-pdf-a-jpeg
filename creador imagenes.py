from pdf2image import convert_from_path
import os

# este link es estatico, descarga poopler  ---> https://www.youtube.com/watch?v=SmWDy_Jr8fw&t=283s&ab_channel=Koolac
poopler_path = r"C:/Users/antoi.DESKTOP-26ARF9V/Downloads/Lucrex Youtube/poppler-22.04.0/Library\bin"

# Datos
pdf_input = str(input("Ruta del pdf: "))        # Aquí pones el link del pdf a convertir
carpeta_name = str(input("Ruta de guardado: ")) # Carpeta donde vas a guardar las imagenes
desde = int(input("Desde que página: "))        # Desde que página 
hasta = int(input("Hasta que página: "))        # Hasta que página

# modificacion de caracter especial 
pdf_input.replace("""
\
""", "/")
carpeta_name.replace("""
\
""", "/")

# Aqui empieza la magia
c = 1
while True:
    # uso de libreria: (pdf , poopler, desde, hasta)
    paginas = convert_from_path(
        pdf_path = pdf_input, 
        poppler_path = poopler_path, 
        first_page = desde, 
        last_page = hasta
    )   
    for pagina in paginas:
        img_name = f"img-{c}.jpeg"
        pagina.save(os.path.join(carpeta_name,img_name), "JPEG")
        c+=1

    desde = c + 2
    hasta+= hasta
    print(c)
    continuar = input("continuar: ")
    if continuar == "si":
        continue
    else:
        break

