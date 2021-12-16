from flask import Flask, render_template, redirect, url_for
from ktp_form import InputKtp
from laporan_form import InputLaporan

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

@app.route("/ktp", methods=['GET', 'POST'])
def ktp():
    ktp_form = InputKtp()
    #return redirect(url_for("input_ktp_success", _external=True, _scheme='https'))
    return render_template("inputKTP.html", ktp_form=ktp_form)

@app.route("/laporan", methods=['GET', 'POST'])
def laporan():
    laporan_form = InputLaporan()
    #return redirect(url_for("input_lap_success", _external=True, _scheme='https'))
    return render_template("inputLaporan.html", laporan_form=laporan_form)

@app.route("/laporan/ktpsuccess/<nik>", methods=['GET', 'POST'])
def input_ktp_success(nik):
    ktp_form = InputKtp()
    return render_template("inputKTP_success.html")

@app.route("/laporan/lapsuccess/<nik>", methods=['GET', 'POST'])
def input_lap_success(nik):
    laporan_form = InputLaporan()
    return render_template("inputLaporan_success.html")

if __name__ == "__main__":
    app.run(debug=True)