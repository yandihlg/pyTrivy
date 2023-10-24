import subprocess
import json
import os
import time
from pyResult import Result

def encontrar_etiqueta_segura(imagen, vulnerabilidades_prohibidas):
    tmp_json = "tmp.json"
    lista_etiquetas = []
    # Obtener la lista de todas las etiquetas de la imagen
    comando = ["trivy", "-f", "json", "-o", tmp_json, "image", imagen]
    subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    file= open('tmp.json', 'r')
    # Cargar el contenido del archivo JSON en un diccionario
    data = json.loads(file.read())
    file.close()
    # Obtener la lista de vulnerabilidades de la imagen
    vulnerability_image = data["Results"][0]["Vulnerabilities"]
    resultado = []
    result=Result(imagen.split(":")[0],imagen.split(":")[1], [])
    for vulnerability in vulnerabilidades_prohibidas:
        for vul_image in vulnerability_image:
            if vul_image["VulnerabilityID"]==vulnerability:
                result.add_vulnerabilidad(vulnerability)
                break
    # Intentar borrar el archivo
    try:
        os.remove('tmp.json')
        print("El archivo tmp.json ha sido borrado exitosamente.")
    except OSError as e:
        print(f"No se pudo borrar el archivo: {e}")
    return result

# Ejemplo de uso:
# imagen = "library/ubuntu"
# vulnerabilidades_prohibidas = ["CVE-2021-12345", "CVE-2021-67890"]
# tag = "latest"
# imagenTag = imagen + ":" + tag
# etiqueta_segura = encontrar_etiqueta_segura(imagenTag, vulnerabilidades_prohibidas)
# if etiqueta_segura:
#     print(f"Se encontró una etiqueta segura: {etiqueta_segura}")
# else:
#     print("No se encontraron etiquetas seguras.")
