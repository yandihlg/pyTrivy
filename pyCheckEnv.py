import shutil

color_azul = "\033[94m"
color_rojo = "\033[91m"
reset_color = "\033[0m"

def check_env_tools():
    trivy_path = shutil.which("trivy")
    if trivy_path is None:
        print("Trivy no está instalado o no se puede encontrar en el sistema.")
    else:
        print(f"Ruta de Trivy: {trivy_path}")

    docker_path = shutil.which("docker")
    if docker_path is None:
        print("Docker no está instalado o no se puede encontrar en el sistema.")
    else:
        print(f"Ruta de Docker: {docker_path}")

    python_path = shutil.which("python")
    if python_path is None:
        print("Python no está instalado o no se puede encontrar en el sistema.")
    else:
        print(f"Ruta de Python: {python_path}")
    return trivy_path is not None and docker_path is not None and python_path is not None



if __name__ == "__main__":
    print(check_env_tools())