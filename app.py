import os
from flask import Flask, render_template
from model.database import init_database
from route.jenis_bp import jenis_bp
from route.satuan_bp import satuan_bp
from route.merek_bp import merek_bp
from route.barang_bp import barang_bp
from route.stok_bp import stok_bp

app = Flask(__name__)
app.secret_key = "gudang-secret-key-2024"

# Register blueprints
app.register_blueprint(jenis_bp)
app.register_blueprint(satuan_bp)
app.register_blueprint(merek_bp)
app.register_blueprint(barang_bp)
app.register_blueprint(stok_bp)


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    init_database()
    # Gunakan environment variable PORT jika ada, default 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
