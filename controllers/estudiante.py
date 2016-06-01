from flask.globals import session
from flask.helpers import flash
from flask import render_template, redirect, url_for, session
from datetime import datetime
from dao.propuesta_dao import PropuestaDao
from dao.propuesta_usuario_dao import Propuesta_UsuarioDao
from dao.usuario_dao import UsuarioDao
from dto.propuesta import Propuesta
from dto.usuario import Usuario
from dto.usuario_propuesta import UsuarioPropuesta


class EstudianteController:

    def __init__(self):
        pass

    def get_registro_propuesta(self):

        usuario_u = UsuarioDao().get_usuario_por_id(Usuario(id=session['usuario']
                                                          ['id']))
        return render_template("estudiante/registro_propuesta.html",
                               usuario_u=usuario_u)

    def get_registrar_propuesta(self):

        propuesta = Propuesta_UsuarioDao().get_propuesta_usuario(
            UsuarioPropuesta(id_estudiante=session['usuario']['id']))
        if propuesta is None:

            return render_template("estudiante/home.html")

        pro = Propuesta_UsuarioDao().get_propuesta_codigo(UsuarioPropuesta(
                    id_propuesta=propuesta.getId_propuesta().getId()))


        return render_template("estudiante/home.html", propuesta=pro,
                               estudiante=propuesta)

    def registrar_propuesta(self, titulo, director, modalidad, documentos, id):
        fecha = datetime.now().date()
        propuesta = Propuesta(titulo=titulo, director_trabajo=director,
                              modalidad=modalidad, documentacion=documentos,
                              fecha=fecha)

        propuest = PropuestaDao().get_propuesta_titulo(propuesta)
        if propuest is not None:
            flash("Ya existe una propuesta con ese titulo", "error")
            return self.get_registro_propuesta()

        if PropuestaDao().crear_propuesta(propuesta):
            pro = PropuestaDao().get_propuesta_titulo(propuesta)
            if Propuesta_UsuarioDao().crear_propuesta_usuario(pro, id):
                flash("se creo la propuesta exitosamente.", "success")
                return self.get_registrar_propuesta()
        else:
                flash("error al crear la propuesta", "error")
        return self.get_registro_propuesta()

    def asignar_propuesta(self, codigo):
        usuario = Usuario(codigo=codigo)
        usuario_e = UsuarioDao().get_usuario_por_codigo(usuario)
        if usuario_e is None:
            flash("El codigo del estudiante no existe", "error")
            return redirect(url_for("estudiante.home"))
        usuario_p = Propuesta_UsuarioDao().get_propuesta_codigo(
            UsuarioPropuesta(id_estudiante=usuario_e.getId()))
        if usuario_p is not None:
            flash("El estudiante ya esta asignado a una propuesta", "error")
            return redirect(url_for("estudiante.home"))











