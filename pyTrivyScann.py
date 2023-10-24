import subprocess
import sys

def escanear_vulnerabilidades(imagen, tag):
    try:
        # Ejecutar el comando de Trivy para escanear la imagen y capturar la salida
        resultado_bytes = subprocess.check_output(["trivy", "image", imageTag], stderr=subprocess.STDOUT)
        resultado = resultado_bytes.decode("utf-8")

        # Devolver la salida del escaneo
        return resultado
    except subprocess.CalledProcessError as e:
        # En caso de error, capturar la excepción y devolver el mensaje de error
        return f"Error al escanear la imagen {imagen+ ":" + tag}: {e.output}"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <nombre_de_la_imagen> <tag>")
    else:
        imagen = sys.argv[1]
        tag = sys.argv[2]
        imageTag = imagen + ":" + tag

        resultado = escanear_vulnerabilidades(imagen, tag)
        print(f"Vulnerabilidades en la imagen {imageTag}:")
        print(resultado)
        
