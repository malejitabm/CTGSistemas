import os

from flask.globals import session
from flask.helpers import flash
from flask import render_template, redirect, url_for, session
from datetime import datetime

from controllers.emails import EmailController
from dao.propuesta_dao import PropuestaDao
from dao.propuesta_usuario_dao import Propuesta_UsuarioDao
from dao.usuario_dao import UsuarioDao
from dto.propuesta import Propuesta
from dto.usuario import Usuario
from dto.usuario_propuesta import UsuarioPropuesta
from werkzeug.utils import secure_filename


class EstudianteController:

    def __init__(self):
        pass

    def get_registro_propuesta(self):

        usuario_u = UsuarioDao().get_usuario_por_id(Usuario(id=session['usuario']
                                                          ['id']))
        return render_template("estudiante/registro_propuesta.html",
                               usuario_u=usuario_u)

    def get_registrar_propuesta(self):
        tipo = session['usuario']['tipo']
        usuario = Usuario(nombres=session['usuario']['nombres'],
                          tipo_usuario=tipo)
        propuesta = Propuesta_UsuarioDao().get_propuesta_usuario(
            UsuarioPropuesta(id_estudiante=session['usuario']['id']))
        if propuesta is None:
            return render_template("estudiante/home.html", usuario=usuario)

        pro = Propuesta_UsuarioDao().get_propuesta_codigo(UsuarioPropuesta(
                    id_propuesta=propuesta.getId_propuesta().getId()))

        return render_template("estudiante/home.html", propuesta=pro,
                               estudiante=propuesta, usuario=usuario)

    def registrar_propuesta(self, titulo, director, modalidad, file, id):
        from proyecto import UPLOAD_FOLDER
        filename = str(datetime.now().microsecond) + secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        fecha = datetime.now().date()
        propuesta = Propuesta(titulo=titulo, director_trabajo=director,
                              modalidad=modalidad, documentacion=filename,
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
        usuario_p = Propuesta_UsuarioDao().get_propuesta_usuario(
            UsuarioPropuesta(id_estudiante=usuario_e.getId()))
        if usuario_p is not None:
            flash("El estudiante ya esta asignado a una propuesta", "error")
            return redirect(url_for("estudiante.home"))

        usuario_pro = Propuesta_UsuarioDao().get_propuesta_usuario(
            UsuarioPropuesta(id_estudiante = session['usuario']['id']))
        print usuario_pro
        if Propuesta_UsuarioDao().crear_propuesta_usuario(usuario_pro.getId_propuesta(),
                                                          usuario_e.getId()):
            mensaje = "Ha sido asignado a una propuesta de trabajo." \
                      "Favor ingresar al sistema y verificar la informacion," \
                      " si no esta deacuerdo por favor diligenciar un retiro " \
                      "de la propuesta." \
                      ""
            flash("Se ha asignado correctamente al estudiante", "success")
            EmailController().enviar_email(
                usuario_e.getEmail(), mensaje,
                "Asignacion de Propuesta - CTG Sistemas")
            return redirect(url_for("estudiante.home"))


    def subir_entregable(self, file, id):
        from proyecto import UPLOAD_FOLDER
        filename = str(datetime.now().microsecond) + secure_filename(
            file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        propuesta_e = Propuesta_UsuarioDao().get_propuesta_usuario(
            UsuarioPropuesta(id_estudiante=id))
        if propuesta_e is None:
            flash("La propuesta no existe", "error")
            return redirect(url_for("estudiante.home"))
        pro = Propuesta_UsuarioDao().get_propuesta_codigo(UsuarioPropuesta(
            id_propuesta=propuesta_e.getId_propuesta().getId()))
        pro.getId_propuesta().setEntregables(filename)
        if PropuestaDao().subir_entregable(pro):
            flash("se subio correctamente el archivo", "success")
            return redirect(url_for("estudiante.home"))

    def get_subir_entregable(self):
        tipo = session['usuario']['tipo']
        usuario = Usuario(nombres=session['usuario']['nombres'],
                          tipo_usuario=tipo)
        return render_template("/estudiante/entregables.html", usuario=usuario)

    def subir_correcciones(self, file, id):
        from proyecto import UPLOAD_FOLDER
        filename = str(datetime.now().microsecond) + secure_filename(
            file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        propuesta_e = Propuesta_UsuarioDao().get_propuesta_usuario(
            UsuarioPropuesta(id_estudiante=id))
        if propuesta_e is None:
            flash("La propuesta no existe", "error")
            return redirect(url_for("estudiante.home"))
        pro = Propuesta_UsuarioDao().get_propuesta_codigo(UsuarioPropuesta(
            id_propuesta=propuesta_e.getId_propuesta().getId()))
        pro.getId_propuesta().setEntregables(filename)
        if PropuestaDao().subir_correcciones(pro):
            flash("se subio correctamente el archivo", "success")
            return redirect(url_for("estudiante.home"))

    def get_subir_correciones(self):
        tipo = session['usuario']['tipo']
        usuario = Usuario(nombres=session['usuario']['nombres'],
                          tipo_usuario=tipo)
        return render_template("/estudiante/entregables.html", usuario=usuario)









