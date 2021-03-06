from dto.propuesta import Propuesta


class TrabajoGrado:

    def __init__(self, codigo="", titulo="", id_propuesta=0,
                 cod_jurado1="", cod_jurado2="", cod_jurado3="", correciones="",
                 estado="", documentacion="", fecha_correcciones="",
                 fecha_sustentacion="", lugar_sustentacion="", fecha="",nota="",
                 hora_sustentacion=""):

        self.__codigo = codigo
        self.__titulo = titulo
        self.__id_propuesta = Propuesta(id=id_propuesta)
        self.__cod_jurado1 = cod_jurado1
        self.__cod_jurado2 = cod_jurado2
        self.__cod_jurado3 = cod_jurado3
        self.__correciones = correciones
        self.__estado = estado
        self.__documentacion = documentacion
        self.__fecha_correcciones = fecha_correcciones
        self.__fecha_sustentacion = fecha_sustentacion
        self.__lugar_sustentacion = lugar_sustentacion
        self.__fecha = fecha
        self.__nota = nota
        self.__hora_sustentacion= hora_sustentacion

    def getCodigo(self):
        return self.__codigo

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getTitulo(self):
        return self.__titulo

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def getDirector_proyecto(self):
        return self.__director_proyecto

    def setDirector_proyecto(self, director_proyecto):
        self.__director_proyecto = director_proyecto

    def getId_propuesta(self):
        return self.__id_propuesta

    def setId_propuesta(self, id_propuesta):
        self.__id_propuesta = id_propuesta

    def getCod_jurado1(self):
        return self.__cod_jurado1

    def setCod_jurado1(self, cod_jurado1):
        self.__cod_jurado1 = cod_jurado1

    def getCod_jurado2(self):
        return self.__cod_jurado2

    def setCod_jurado2(self, cod_jurado2):
        self.__cod_jurado2 = cod_jurado2

    def getCod_jurado3(self):
        return self.__cod_jurado3

    def setCod_jurado3(self, cod_jurado3):
        self.__cod_jurado3 = cod_jurado3

    def getModalidad(self):
        return self.__modalidad

    def setModalidad(self, modalidad):
        self.__modalidad = modalidad

    def getCorreciones(self):
        return self.__correciones

    def setCorreciones(self, correciones):
        self.__correciones = correciones

    def getDocumentacion(self):
        return self.__documentacion

    def setDocumentacion(self, documentacion):
        self.__documentacion = documentacion

    def getEstado(self):
        return self.__estado

    def setEstado(self, estado):
        self.__estado = estado

    def getFecha_Correcciones(self):
        return self.__fecha_correcciones

    def setFecha_Correcciones(self, fechaC):
        self.__fecha_correcciones = fechaC

    def getFecha_Sustentacion(self):
        return self.__fecha_sustentacion

    def setFecha_Sustentacion(self, fecha_sustentacion):
        self.__fecha_sustentacion = fecha_sustentacion

    def getLugar_Sustentacion(self):
        return self.__lugar_sustentacion

    def setLugar_Sustentacion(self,lugar_sustentacion):
        self.__lugar_sustentacion=lugar_sustentacion

    def getFecha(self):
        return self.__fecha

    def setFecha(self, fecha):
        self.__fecha = fecha

    def getNota(self):
        return self.__nota

    def setNota(self,nota):
        self.__nota = nota

    def getHora_Sustentacion(self):
        return self.__hora_sustentacion

    def setHora_Sustentacion(self,hora_sustentacion):
        self.__hora_sustentacion=hora_sustentacion
