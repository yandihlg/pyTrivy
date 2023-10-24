import pyReadExcel
import pyDockerHubTags
import pyCheckEnv
import pyCveSearch

def main():
    if pyCheckEnv.check_env_tools() == False:
        print("No se cumplen los requisitos mínimos para ejecutar el script.")
        exit(1)
    else:
        print("Los requisitos mínimos se cumplen.")
        cve_map=pyReadExcel.read_cve(pyReadExcel.archivo)
        imagenes_filtradas={}
        for key in cve_map:
            image_tag=None
            if r"docker.io/" in key:
                image_tag=key.replace("docker.io/","")
            image=image_tag.split(":")[0]
            tag=image_tag.split(":")[1]
            all_tags=pyDockerHubTags.get_dockerhub_tags(image)
            
            date_pushed=all_tags[tag]
            imagenes_filtradas = {nombre: fecha for nombre, fecha in all_tags.items() if date_pushed!=None and fecha >= date_pushed}
            resultado_final={}
            for imagen in imagenes_filtradas:
                etiqueta_segura = pyCveSearch.encontrar_etiqueta_segura(image_tag, cve_map[key])
            resultado_final[imagen].append(etiqueta_segura)
        print(resultado_final)

if __name__ == "__main__":
    main()