from flask import Blueprint, request, render_template, redirect, url_for, flash
from service.stok_service import StokService

stok_bp = Blueprint("stok", __name__, url_prefix="/stok")
service = StokService()


@stok_bp.route("/", methods=["GET"])
def index():
    data = service.get_all()
    barang_list = service.get_all_barang()
    return render_template(
        "stok/index.html",
        data=data,
        edit_item=None,
        barang_list=barang_list,
    )


@stok_bp.route("/create", methods=["POST"])
def create():
    idbarang = int(request.form.get("idbarang", 0))
    jumlah = int(request.form.get("jumlah", 0))
    success, message, _ = service.create(idbarang, jumlah)
    flash(message, "success" if success else "error")
    return redirect(url_for("stok.index"))


@stok_bp.route("/edit/<int:id>", methods=["GET"])
def edit(id: int):
    data = service.get_all()
    edit_item = service.get_by_id(id)
    barang_list = service.get_all_barang()
    return render_template(
        "stok/index.html",
        data=data,
        edit_item=edit_item,
        barang_list=barang_list,
    )


@stok_bp.route("/update/<int:id>", methods=["POST"])
def update(id: int):
    idbarang = int(request.form.get("idbarang", 0))
    jumlah = int(request.form.get("jumlah", 0))
    success, message = service.update(id, idbarang, jumlah)
    flash(message, "success" if success else "error")
    return redirect(url_for("stok.index"))


@stok_bp.route("/delete/<int:id>", methods=["POST"])
def delete(id: int):
    success, message = service.delete(id)
    flash(message, "success" if success else "error")
    return redirect(url_for("stok.index"))
