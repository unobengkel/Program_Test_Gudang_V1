from flask import Blueprint, request, render_template, redirect, url_for, flash
from service.barang_service import BarangService

barang_bp = Blueprint("barang", __name__, url_prefix="/barang")
service = BarangService()


@barang_bp.route("/", methods=["GET"])
def index():
    data = service.get_all()
    jenis_list = service.get_all_jenis()
    satuan_list = service.get_all_satuan()
    merek_list = service.get_all_merek()
    return render_template(
        "barang/index.html",
        data=data,
        edit_item=None,
        jenis_list=jenis_list,
        satuan_list=satuan_list,
        merek_list=merek_list,
    )


@barang_bp.route("/create", methods=["POST"])
def create():
    idjenis = int(request.form.get("idjenis", 0))
    idsatuan = int(request.form.get("idsatuan", 0))
    idmerek = int(request.form.get("idmerek", 0))
    success, message, _ = service.create(idjenis, idsatuan, idmerek)
    flash(message, "success" if success else "error")
    return redirect(url_for("barang.index"))


@barang_bp.route("/edit/<int:id>", methods=["GET"])
def edit(id: int):
    data = service.get_all()
    edit_item = service.get_by_id(id)
    jenis_list = service.get_all_jenis()
    satuan_list = service.get_all_satuan()
    merek_list = service.get_all_merek()
    return render_template(
        "barang/index.html",
        data=data,
        edit_item=edit_item,
        jenis_list=jenis_list,
        satuan_list=satuan_list,
        merek_list=merek_list,
    )


@barang_bp.route("/update/<int:id>", methods=["POST"])
def update(id: int):
    idjenis = int(request.form.get("idjenis", 0))
    idsatuan = int(request.form.get("idsatuan", 0))
    idmerek = int(request.form.get("idmerek", 0))
    success, message = service.update(id, idjenis, idsatuan, idmerek)
    flash(message, "success" if success else "error")
    return redirect(url_for("barang.index"))


@barang_bp.route("/delete/<int:id>", methods=["POST"])
def delete(id: int):
    success, message = service.delete(id)
    flash(message, "success" if success else "error")
    return redirect(url_for("barang.index"))
