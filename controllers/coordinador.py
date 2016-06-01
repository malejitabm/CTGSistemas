from flask import render_template
from flask.helpers import flash

from dao.acta_dao import ActaDao
from dao.propuesta_dao import PropuestaDao
from dao.tipo_usuario_dao import TipoUsuarioDao
from dao.trabajoDeGrado_dao import TrabajoGradoDao
from dto.propuesta import Propuesta
from dto.acta import Acta
from dto.tipo_usuario import TipoUsuario
from dto.trabajoGrado import TrabajoGrado
import hashlib

from flask import session, render_template, redirect, url_for


from dao.trabajoDeGrado_dao import TrabajoGradoDao
from dao.usuario_dao import UsuarioDao
from dto.usuario import Usuario



class CoordinadorController:
    def __init__(self):
        pass



    def get_view_nombreT(self):
        tipoU = session['usuario']['tipo']
        usuario_tipo = Usuario(tipo_usuario=tipoU)
        usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
        return render_template("/coordinador/nombreT.html",  usuario=usuario_u, usuario_u=usuario_u, tipoU=tipoU)


    def consulta_nombreT(self, nombre):
        trabajoG = TrabajoGrado (titulo=nombre)
        if (TrabajoGradoDao().get_trabajo_titulo(trabajoG) is not None):
         trabajos = TrabajoGradoDao().get_trabajo_titulo(trabajoG)
         tipoU = session['usuario']['tipo']
         usuario_tipo = Usuario(tipo_usuario=tipoU)
         usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
         return render_template("/coordinador/nombreT.html", trabajos=trabajos,usuario=usuario_u,
                                 usuario_u=usuario_u, tipoU=tipoU)
        else:
         flash("No existen Trabajos con esos parametros.", "error")
         tipoU = session['usuario']['tipo']
         usuario_tipo = Usuario(tipo_usuario=tipoU)
         usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
         return render_template("/coordinador/nombreT.html", usuario=usuario_u,
                                usuario_u=usuario_u, tipoU=tipoU)

    def get_view_nombreP(self):
        tipoU = session['usuario']['tipo']
        usuario_tipo = Usuario(tipo_usuario=tipoU)
        usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
        return render_template("/coordinador/nombreP.html", usuario=usuario_u,
                               usuario_u=usuario_u, tipoU=tipoU)

    def consulta_nombreP(self, nombre):
        propuesta = Propuesta(titulo=nombre)
        if (PropuestaDao().get_propuesta_consultaN):
            propuestas = PropuestaDao().get_propuesta_consultaN(propuesta)
            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            return render_template("/coordinador/nombreP.html", propuestas=propuestas, usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)
        else:
            flash("No existen Propuestas con esos parametros.", "error")
            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            return render_template("/coordinador/nombreP.html",  usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)

    def get_view_cancelarP(self):
        tipoU = session['usuario']['tipo']
        usuario_tipo = Usuario(tipo_usuario=tipoU)
        usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
        return render_template("/coordinador/cancelarP.html", usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)

    def consulta_cancelarP(self, nombre, estado):
        propuesta = Propuesta(titulo=nombre, estado=estado)

        if (PropuestaDao().get_propuesta_titulo(propuesta)is not None):
            PropuestaDao().get_propuesta_cancelar(propuesta, estado)
            flash("Actualiacion Exitosa", "success")
            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            return render_template("/coordinador/cancelarP.html",usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)
        else:
            flash("No existen Propuesta con esos parametros.", "error")
            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            return render_template("/coordinador/cancelarP.html", usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)

    def get_view_estadoP(self):
            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            return render_template("/coordinador/estadoP.html",usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)

    def consulta_estadoP(self, estado):

        propuesta = Propuesta(estado=estado)
        if (PropuestaDao().get_propuesta_estado(propuesta)):
            propuestas = PropuestaDao().get_propuesta_estado(propuesta)
            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            return render_template("/coordinador/estadoP.html", propuestas=propuestas,usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)
        else:
            flash("No existen Propuestas con esos parametros.", "error")
            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            return render_template("/coordinador/estadoP.html",usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)

    def get_view_juradoEstudiante(self):
        tipoU = session['usuario']['tipo']
        usuario_tipo = Usuario(tipo_usuario=tipoU)
        usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
        return render_template("/coordinador/juradoEstudiante.html",usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)

    def consulta_jurado(self, cod_jurado1):
        trabajoG= TrabajoGrado (cod_jurado1=cod_jurado1)
        if (TrabajoGradoDao().get_trabajo_Jurado(trabajoG) ):
            trabajos = TrabajoGradoDao().get_trabajo_Jurado(trabajoG)
            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            return render_template("/coordinador/juradoEstudiante.html", trabajos = trabajos,usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)
        else:
            flash("No existen Trabajos con esos parametros.", "error")
            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            return render_template("/coordinador/juradoEstudiante.html",usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)

    def consulta_estudiante(self, cod_jurado1):
        trabajoG = TrabajoGrado(cod_jurado1=cod_jurado1)
        if (TrabajoGradoDao().get_trabajo_Estudiante(trabajoG)):
            trabajos = TrabajoGradoDao().get_trabajo_Estudiante(trabajoG)
            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            return render_template("/coordinador/juradoEstudiante.html", trabajos=trabajos,usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)
        else:
            flash("No existen Trabajos con esos parametros.", "error")
            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            return render_template("/coordinador/juradoEstudiante.html",usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)

    def get_view_modalidadT(self):
            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            return render_template("/coordinador/modalidadT.html",usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)

    def consulta_modalidadT(self, tipo_modalidad, trabajo_a):

        trabajoG = TrabajoGrado(modalidad=tipo_modalidad)
        if (TrabajoGradoDao().get_trabajo_modalidadT(trabajoG , trabajo_a)):
            trabajos = TrabajoGradoDao().get_trabajo_modalidadT(trabajoG, trabajo_a)
            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            return render_template("/coordinador/modalidadT.html", trabajos=trabajos,usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)
        else:
            flash("No existen Trabajos con esos parametros.", "error")

            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            return render_template("/coordinador/modalidadT.html",usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)

    def get_view_consultarA(self):
            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            return render_template("/coordinador/consultarA.html",usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)

    def consulta_actaC(self, fecha):

        acta = Acta(fecha=fecha)
        if (ActaDao().get_acta_fecha(acta)):
            actas = ActaDao().get_acta_fecha(acta)
            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            return render_template("/coordinador/consultarA.html", actas=actas,usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)
        else:
            flash("No existen Actas con esos parametros.", "error")
            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            return render_template("/coordinador/consultarA.html",usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)

    def get_view_estadoT(self):
            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            return render_template("/coordinador/estadoT.html",usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)

    def consulta_estadoT(self, estado, trabajo_a):

        trabajoG = TrabajoGrado(estado=estado)
        if (TrabajoGradoDao().get_trabajo_estadoT(trabajoG, trabajo_a)):
            trabajos = TrabajoGradoDao().get_trabajo_estadoT(trabajoG, trabajo_a)
            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            return render_template("/coordinador/estadoT.html", trabajos=trabajos,usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)
        else:
            flash("No existen Trabajos con esos parametros.", "error")
            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario_u = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            return render_template("/coordinador/estadoT.html",usuario=usuario_u,
                                   usuario_u=usuario_u, tipoU=tipoU)
