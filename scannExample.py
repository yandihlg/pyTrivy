import docker
import subprocess

def escanear_vulnerabilidades(imagen, tag):
    cliente_docker = docker.from_env()
    nombre_imagen = f"{imagen}:{tag}"

    # Descargar la imagen si no está presente localmente
    try:
        cliente_docker.images.get(nombre_imagen)
    except docker.errors.ImageNotFound:
        print(f"La imagen {nombre_imagen} no está presente localmente. Descargando...")
        cliente_docker.images.pull(imagen, tag)

    # Iniciar un contenedor con Trivy y escanear la imagen
    contenedor = cliente_docker.containers.run("aquasec/trivy", f"{nombre_imagen}", detach=True)
    #trivy --severity CRITICAL,HIGH --format template --template "{{ .Target }} ({{ .Severity }}): {{ .VulnerabilityID }} - {{ .Title }}" <nombre_de_la_imagen>

    contenedor_id = contenedor.id

    # Esperar a que el contenedor de Trivy termine de escanear
    contenedor.wait()

    # Obtener las vulnerabilidades escaneadas por Trivy
    salida_trivy = subprocess.check_output(["docker", "logs", contenedor_id])
    vulnerabilidades = salida_trivy.decode("utf-8").strip()

    # Eliminar el contenedor después del escaneo
    contenedor.remove(force=True)

    return vulnerabilidades

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Uso: python script.py <nombre_de_la_imagen> <tag>")
    else:
        imagen = sys.argv[1]
        tag = sys.argv[2]
        vulnerabilidades = escanear_vulnerabilidades(imagen, tag)
        print(f"Vulnerabilidades en la imagen {imagen}:{tag}:")
        print(vulnerabilidades)
