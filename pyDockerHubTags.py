import requests
import sys
import docker
import subprocess

def get_dockerhub_tags(image_name):
    url = f"https://hub.docker.com/v2/repositories/{image_name}/tags"
    tags_info = {}  # Diccionario para almacenar los tags y sus fechas de última actualización
    while True:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            for tag in data['results']:
                tag_name = tag['name']
                last_pushed = tag['tag_last_pushed']
                tags_info[tag_name] = last_pushed
        else:
            print(f"Error al obtener los tags para la imagen '{image_name}': {response.status_code}")
            return tags_info
        if data['next'] is None:
            break
        else:
            url = data['next']

    return tags_info

if __name__ == "__main__":
    tags_info = get_dockerhub_tags("jenkins/jenkins")
    print(tags_info)
    print("si")
