class Result:

    def __init__(self, imagen_original, tag_escaneada, vulnerabilidad_escaneada):
        self.imagen_original = imagen_original
        self.tag_escaneada = tag_escaneada
        self.vulnerabilidad_escaneada = vulnerabilidad_escaneada

    def add_vulnerabilidad(self, vulnerabilidad):
        self.vulnerabilidad_escaneada.append(vulnerabilidad)