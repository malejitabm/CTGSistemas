from dto.trabajoGrado import TrabajoGrado


class TrabajoGradoDao:
    def __init__(self):
        from proyecto import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()

    def get_trabajo_titulo(self, trabajoG):
        try:
            query = "SELECT * FROM 'trabajo de grado'  WHERE titulo = %s"
            param = (trabajoG.getTitulo(),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            return TrabajoGrado(codigo=data[0], titulo=data[1],fecha_sustentacion=data[12],lugar_sustentacion=data[13],
                                   hora_sustentacion=data[17],nota=data[16],fecha=data[15])
        except Exception as e:
            print e.message
            return None

    def consultar_trabajos(self, trabaj):
        if (trabaj.getTitulo() == "" and trabaj.getCodigo() != ""):
            try:
                query = "SELECT * FROM `trabajo de grado` WHERE codigo LIKE %s or codigo LIKE %s or codigo LIKE %s"
                param = (trabaj.getCodigo() + "%", "%" + trabaj.getCodigo() + "%", "%" + trabaj.getCodigo())
                self.__cur.execute(query, param)
                data = self.__cur.fetchall()
                resultado = list()
                if data is None:
                    return []
                for trabajo in data:
                    tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1],fecha_sustentacion=trabajo[12],lugar_sustentacion=trabajo[13],
                                   hora_sustentacion=trabajo[17],nota=trabajo[16],fecha=trabajo[15])
                    resultado.append(tra)
                return resultado
            except Exception as e:
                print e.message
                return []

        if (trabaj.getTitulo() != "" and trabaj.getCodigo() == ""):
            try:
                query = "SELECT * FROM `trabajo de grado` WHERE titulo LIKE %s or titulo LIKE %s or titulo LIKE %s"
                param = (trabaj.getTitulo() + "%", "%" + trabaj.getTitulo() + "%", "%" + trabaj.getTitulo())
                self.__cur.execute(query, param)
                data = self.__cur.fetchall()
                resultado = list()
                if data is None:
                    return []
                for trabajo in data:
                    tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1],fecha_sustentacion=trabajo[12],lugar_sustentacion=trabajo[13],
                                   hora_sustentacion=trabajo[17],nota=trabajo[16],fecha=trabajo[15])
                    resultado.append(tra)
                return resultado
            except Exception as e:
                print e.message
                return []

        if (trabaj.getTitulo() != "" and trabaj.getCodigo() != ""):
            try:
                print "entro"
                query = "SELECT * FROM `trabajo de grado` WHERE titulo LIKE %s or titulo LIKE %s " \
                        "or titulo LIKE %s AND codigo LIKE %s or `codigo` LIKE %s or `codigo` LIKE %s"
                param = (trabaj.getTitulo() + "%", "%" + trabaj.getTitulo() + "%", "%" + trabaj.getTitulo(),
                         trabaj.getCodigo() + "%", "%" + trabaj.getCodigo() + "%", "%" + trabaj.getCodigo())
                self.__cur.execute(query, param)
                data = self.__cur.fetchall()
                resultado = list()
                if data is None:
                    return []
                for trabajo in data:
                    tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1],fecha_sustentacion=trabajo[12],lugar_sustentacion=trabajo[13],
                                   hora_sustentacion=trabajo[17],nota=trabajo[16],fecha=trabajo[15])
                    resultado.append(tra)
                return resultado
            except Exception as e:
                print e.message
                return []

    def get_trabajo_codigo(self, codigo):
        try:
            query = "SELECT * FROM `trabajo de grado`  WHERE codigo = %s"
            param = (codigo,)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            return TrabajoGrado(codigo=data[0], titulo=data[1],fecha_sustentacion=data[12],lugar_sustentacion=data[13],
                                   hora_sustentacion=data[17],nota=data[16],fecha=data[15])
        except Exception as e:
            print e.message
            return None


    def registrar_nota(self,trabajo):
        try:
            query = "UPDATE `trabajo de grado` SET nota= %s WHERE codigo=%s "

            param = (trabajo.getNota(), trabajo.getCodigo())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False

    def agregar_fechas_correcciones(self,trabajo):
        try:
            query = "UPDATE `trabajo de grado` SET fecha_correcciones= %s WHERE codigo=%s "

            param = (trabajo.getFecha_Correcciones(), trabajo.getCodigo())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False


    def get_trabajos_sin_sustentacion(self):
        try:
            print "entra a dao"
            query = "SELECT * FROM  `trabajo de grado` WHERE  fecha_sustentacion ='' AND  lugar_sustentacion ='' " \
                    "AND  hora_sustentacion =''"
            param = ()
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for trabajo in data:
                tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1],fecha_sustentacion=trabajo[12],lugar_sustentacion=trabajo[13],
                                   hora_sustentacion=trabajo[17],nota=trabajo[16],fecha=trabajo[15])
                resultado.append(tra)
            return resultado
        except Exception as e:
            print e.message
            return []


    def agregar_datos_sustentacion(self,trabajo):
        try:
            query = "UPDATE `trabajo de grado` SET fecha_sustentacion= %s, lugar_sustentacion= %s, hora_sustentacion= %s" \
                    "WHERE codigo=%s"

            param = (trabajo.getFecha_Sustentacion(),trabajo.getLugar_Sustentacion(),trabajo.getHora_Sustentacion(),
                     trabajo.getCodigo())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False


    def get_trabajos_sin_jurados(self):
        try:
            query = "SELECT * FROM  `trabajo de grado` WHERE cod_jurado1 =  '' AND cod_jurado2 =  '' AND cod_jurado3 =  '' "
            param = ()
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for trabajo in data:
                tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1],fecha_sustentacion=trabajo[12],lugar_sustentacion=trabajo[13],
                                   hora_sustentacion=trabajo[17],nota=trabajo[16],fecha=trabajo[15])
                resultado.append(tra)
            return resultado
        except Exception as e:
            print e.message
            return []

    def asignar_jurados_trabajo(self, trabajo, jurado1, jurado2, jurado3):
        try:
            query = "UPDATE `trabajo de grado` SET cod_jurado1= %s, cod_jurado2= %s, cod_jurado3= %s WHERE titulo=%s "

            param = (jurado1, jurado2, jurado3, trabajo)
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False


    def get_trabajo_consulta_jurado(self,jurado):
        try:
            query = "SELECT * FROM `trabajo de grado`  WHERE cod_jurado1 = %s or cod_jurado2 =%s or cod_jurado3 =%s"
            param = (jurado.getCodigo(),jurado.getCodigo(),jurado.getCodigo())
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for trabajoG in data:
                pro = TrabajoGrado(codigo=trabajoG[0], titulo=trabajoG[1], cod_estudiante1=trabajoG[3],
                                   cod_estudiante2=trabajoG[4],cod_estudiante3=trabajoG[5], cod_estudiante4=trabajoG[6],
                                   cod_jurado1=trabajoG[7], cod_jurado2=trabajoG[8], cod_jurado3=trabajoG[9],
                                   modalidad=[10], correciones=trabajoG[11],documentacion=trabajoG[12],
                                   estado=trabajoG[13], protocolo=trabajoG[14],fecha_sustentacion=trabajoG[15],
                                   lugar_sustentacion=trabajoG[16],fecha_correcciones=trabajoG[17],
                                   fecha=trabajoG[18],nota=trabajoG[19],hora_sustentacion=trabajoG[20])
                resultado.append(pro)
            return resultado
        except Exception as e:
            print e.message
            return []
