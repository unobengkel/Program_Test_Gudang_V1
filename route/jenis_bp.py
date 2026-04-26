from flask import Blueprint, request, render_template, redirect, url_for, flash
from service.jenis_service import JenisService

jenis_bp = Blueprint("jenis", __name__, url_prefix="/jenis")
service = JenisService()


@jenis_bp.route("/", methods=["GET"])
def index():
    data = service.get_all()
    return render_template("jenis/index.html", data=data, edit_item=None)


@jenis_bp.route("/create", methods=["POST"])
def create():
    nama = request.form.get("nama", "")
    success, message, _ = service.create(nama)
    flash(message, "success" if success else "error")
    return redirect(url_for("jenis.index"))


@jenis_bp.route("/edit/<int:id>", methods=["GET"])
def edit(id: int):
    data = service.get_all()
    edit_item = service.get_by_id(id)
    return render_template("jenis/index.html", data=data, edit_item=edit_item)


@jenis_bp.route("/update/<int:id>", methods=["POST"])
def update(id: int):
    nama = request.form.get("nama", "")
    success, message = service.update(id, nama)
    flash(message, "success" if success else "error")
    return redirect(url_for("jenis.index"))


@jenis_bp.route("/delete/<int:id>", methods=["POST"])
def delete(id: int):
    success, message = service.delete(id)
    flash(message, "success" if success else "error")
    return redirect(url_for("jenis.index"))
