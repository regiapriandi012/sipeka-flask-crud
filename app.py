from flask import Flask, render_template, redirect, url_for, request, flash
from form import InputLaporan, InputKtp, CekKtp, CekLaporan, ValidasiLaporan, ValidasiKTP, LoginAdmin, RegistrationAdmin, InputKtpUpdate, InputLaporanUpdate
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, DataKtp, DataLaporan, Admin
from flask_login import LoginManager, login_required, login_user, current_user, logout_user

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://doadmin:L8nQyZGwO5UiwcfG@sipekaid-do-user-8822551-0.b.db.ondigitalocean.com:25060/data_sipeka'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

#halaman untuk User
#----------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/inputktp", methods=['GET', 'POST'])
def ktp():
    ktp_form = InputKtp(csrf_enabled=False)
    if ktp_form.validate_on_submit():
        nik = ktp_form.nik.data
        nama = ktp_form.nama.data
        ttl = ktp_form.ttl.data
        jk = ktp_form.jk.data
        alamat = ktp_form.alamat.data
        rt = ktp_form.rt.data
        rw = ktp_form.rw.data
        desa = ktp_form.desa.data
        kecamatan = "Banjarharjo"
        kabupaten = "Brebes"
        kewarganegaraan = "Indonesia"
        pekerjaan = ktp_form.pekerjaan.data
        status = ktp_form.status.data
        notelf = ktp_form.notelf.data
        surat_keterangan = ktp_form.surat_keterangan.data
        status_validasi = "Data Belum Divalidasi"
        data_ktp = DataKtp(nik=nik, nama=nama, ttl=ttl, jk=jk, alamat=alamat, rt=rt, rw=rw,
                           desa=desa, kecamatan=kecamatan, kabupaten=kabupaten,
                           kewarganegaraan=kewarganegaraan, pekerjaan=pekerjaan,
                           status=status, notelf=notelf, surat_keterangan=surat_keterangan,
                           status_validasi=status_validasi)
        try:
            db.session.add(data_ktp)
            db.session.commit()
        except:
            return redirect(url_for("input_ktp_gagal"))
        return redirect(url_for("input_ktp_success", nik=nik, nama=nama, _external=True))
    return render_template("inputKTP.html", ktp_form=ktp_form)

@app.before_first_request
def create_table():
    db.create_all()

@app.route("/inputlaporan", methods=['GET', 'POST'])
def laporan():
    laporan_form = InputLaporan(csrf_enabled=False)
    if laporan_form.validate_on_submit():
        nik = laporan_form.nik.data
        nama = laporan_form.nama.data
        rt = laporan_form.rt.data
        rw = laporan_form.rw.data
        desa = laporan_form.desa.data
        kecamatan = "Banjarharjo"
        jk = laporan_form.jk.data
        notelf = laporan_form.notelf.data
        kategory = laporan_form.kategory.data
        tanggal = laporan_form.tanggal.data
        isilaporan = laporan_form.isilaporan.data
        pernyataan = laporan_form.pernyataan.data
        status_validasi = "Data Belum DiValidasi"
        data_laporan = DataLaporan(nik=nik, nama=nama, rt=rt, rw=rw, desa=desa,
                                   kecamatan=kecamatan, jk=jk, notelf=notelf,
                                   kategory=kategory, tanggal=tanggal, isilaporan=isilaporan,
                                   pernyataan=pernyataan, status_validasi=status_validasi)
        try:
            db.session.add(data_laporan)
            db.session.commit()
        except:
            return redirect(url_for("input_laporan_gagal"))
        return redirect(url_for("input_lap_success", nik=nik, nama=nama, _external=True))
    return render_template("inputLaporan.html", laporan_form=laporan_form)

@app.route("/inputktp/reportsubmit/<nik>/<nama>", methods=['GET', 'POST'])
def input_ktp_success(nik, nama):
    return render_template("inputKTP_success.html", nama_form=nama, nik_form=nik)

@app.route("/inputlaporan/reportsubmit/<nik>/<nama>", methods=['GET', 'POST'])
def input_lap_success(nik, nama):
    return render_template("inputLaporan_success.html", nama_form=nama, nik_form=nik)

@app.route("/inputktp/gagal")
def input_ktp_gagal():
    return render_template("inputKTP_failed.html")

@app.route("/inputlaporan/gagal")
def input_laporan_gagal():
    return render_template("inputLaporan_failed.html")

@app.route("/inputktp/cekvalidasi", methods=['GET', 'POST'])
def cek_ktp():
    cek_ktp = CekKtp()
    if cek_ktp.validate_on_submit():
        try:
            nik = cek_ktp.nik.data
            nama = DataKtp.query.get(nik).nama
            status = DataKtp.query.get(nik).status_validasi
            return redirect(url_for("cek_status_ktp_sukses", nik=nik, nama=nama, status=status, _external=True))
        except:
            return redirect(url_for("cek_status_ktp_gagal"))
    return render_template("cek_KTP.html", cekKTP_form=cek_ktp)

@app.route("/inputlaporan/cekvalidasi", methods=['GET', 'POST'])
def cek_laporan():
    cek_laporan = CekLaporan()
    if cek_laporan.validate_on_submit():
        try:
            nik = cek_laporan.nik.data
            nama = DataLaporan.query.get(nik).nama
            status = DataLaporan.query.get(nik).status_validasi
            return redirect(url_for("cek_status_laporan_sukses", nik=nik, nama=nama, status=status, _external=True))
        except:
            return redirect(url_for("cek_status_laporan_gagal"))
    return render_template("cek_Laporan.html", cekLaporan_form=cek_laporan)

@app.route("/inputktp/cekvalidasi/<nik>/<nama>/<status>", methods=['GET', 'POST'])
def cek_status_ktp_sukses(nik, nama, status):
    return render_template("cekKTP_success.html", nama_form=nama, nik_form=nik, status_form=status)

@app.route("/inputlaporan/cekvalidasi/<nik>/<nama>/<status>", methods=['GET', 'POST'])
def cek_status_laporan_sukses(nik, nama, status):
    return render_template("cekLaporan_success.html", nama_form=nama, nik_form=nik, status_form=status)

@app.route("/inputktp/cekvalidasi/<nik>/<nama>/update", methods=['GET', 'POST'])
def update_data_ktp_ditolak(nik, nama):
    data_ktp = DataKtp.query.get(nik)
    ktp_form = InputKtpUpdate(csrf_enabled=False)
    if ktp_form.validate_on_submit():
        ttl = ktp_form.ttl.data
        jk = ktp_form.jk.data
        alamat = ktp_form.alamat.data
        rt = ktp_form.rt.data
        rw = ktp_form.rw.data
        desa = ktp_form.desa.data
        kecamatan = "Banjarharjo"
        kabupaten = "Brebes"
        kewarganegaraan = "Indonesia"
        pekerjaan = ktp_form.pekerjaan.data
        status = ktp_form.status.data
        notelf = ktp_form.notelf.data
        surat_keterangan = ktp_form.surat_keterangan.data
        status_validasi = "Data Belum Divalidasi"
        #--------------------------------------------------
        data_ktp = DataKtp.query.get(nik)
        data_ktp.ttl = ttl
        data_ktp.jk = jk
        data_ktp.alamat = alamat
        data_ktp.rt = rt
        data_ktp.rw = rw
        data_ktp.desa = desa
        data_ktp.kecamatan = kecamatan
        data_ktp.kabupaten = kabupaten
        data_ktp.kewarganegaraan = kewarganegaraan
        data_ktp.pekerjaan = pekerjaan
        data_ktp.status = status
        data_ktp.notelf = notelf
        data_ktp.surat_keterangan = surat_keterangan
        data_ktp.status_validasi = status_validasi
        try:
            db.session.commit()
            return redirect(url_for("update_data_ktp_ditolak_success", nik=nik, nama=nama, _external=True))
        except:
            db.session.rollback()
    return render_template("inputKTP_update.html", data_ktp=data_ktp, ktp_form=ktp_form)

@app.route("/inputlaporan/cekvalidasi/<nik>/<nama>/update", methods=['GET', 'POST'])
def update_data_laporan_ditolak(nik, nama):
    data_laporan = DataLaporan.query.get(nik)
    laporan_form = InputLaporanUpdate(csrf_enabled=False)
    if laporan_form.validate_on_submit():
        rt = laporan_form.rt.data
        rw = laporan_form.rw.data
        desa = laporan_form.desa.data
        kecamatan = "Banjarharjo"
        jk = laporan_form.jk.data
        notelf = laporan_form.notelf.data
        kategory = laporan_form.kategory.data
        tanggal = laporan_form.tanggal.data
        isilaporan = laporan_form.isilaporan.data
        pernyataan = laporan_form.pernyataan.data
        status_validasi = "Data Belum DiValidasi"
        #-----------------------------------------------------------
        data_laporan = DataLaporan.query.get(nik)
        data_laporan.rt = rt
        data_laporan.rw = rw
        data_laporan.desa = desa
        data_laporan.kecamatan = kecamatan
        data_laporan.jk = jk
        data_laporan.notelf = notelf
        data_laporan.kategory = kategory
        data_laporan.tanggal = tanggal
        data_laporan.isilaporan = isilaporan
        data_laporan.pertanyaan = pernyataan
        data_laporan.status_validasi = status_validasi
        try:
            db.session.commit()
            return redirect(url_for("update_data_laporan_ditolak_success", nik=nik, nama=nama, _external=True))
        except:
            db.session.rollback()
    return render_template("inputLaporan_update.html", data_laporan=data_laporan, laporan_form=laporan_form)

@app.route("/inputktp/cekvalidasi/<nik>/<nama>/update/success", methods=['GET', 'POST'])
def update_data_ktp_ditolak_success(nik, nama):
    return render_template("inputKTP_update_success.html", nama_form=nama, nik_form=nik)

@app.route("/inputlaporan/cekvalidasi/<nik>/<nama>/update/success", methods=['GET', 'POST'])
def update_data_laporan_ditolak_success(nik, nama):
    return render_template("inputLaporan_update_success.html", nama_form=nama, nik_form=nik)

@app.route("/inputktp/cekvalidasi/gagal", methods=['GET', 'POST'])
def cek_status_ktp_gagal():
    return render_template("cekKTP_failed.html")

@app.route("/inputlaporan/cekvalidasi/gagal", methods=['GET', 'POST'])
def cek_status_laporan_gagal():
    return render_template("cekLaporan_failed.html")

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

@app.route("/admin/login", methods=['GET', 'POST'])
def login_admin():
    form_login = LoginAdmin(csrf_enabled=False)
    if form_login.validate_on_submit():
        username = form_login.username.data
        remember = form_login.remember.data
        password = form_login.password.data
        user = Admin.query.filter(Admin.username == username).first()
        if not user:
            flash('Please check login details and try again', 'danger')
            return redirect(url_for('login_admin', _external=True))
        if user.check_password(password):
            flash('Successfully logged in', 'success')
            login_user(user, remember=remember)
            next = request.args.get('next')
            return redirect(next) if next else redirect(url_for("admin", _external=True))
        else:
            return redirect(url_for('login_admin', _external=True))
    return render_template("loginAdmin.html", form_login=form_login)

#--------------------------------------------
#halaman untuk Admin

@app.route("/admin", methods=['GET', 'POST'])
@login_required
def admin():
    return render_template("indexAdmin.html")

@app.route("/admin/validasi/ktp", methods=['GET', 'POST'])
@login_required
def validasi_ktp():
    data_ktp = DataKtp.query.filter(DataKtp.status_validasi == 'Data Belum Divalidasi').all()
    return render_template("validasiKTP.html", data_ktp=data_ktp)

@app.route("/admin/validasi/laporan", methods=['GET', 'POST'])
@login_required
def validasi_laporan():
    data_laporan = DataLaporan.query.filter(DataLaporan.status_validasi == 'Data Belum Divalidasi').all()
    return render_template("validasiLaporan.html", data_laporan=data_laporan)

@app.route("/admin/validasi/ktp/<nik>", methods=['GET', 'POST'])
@login_required
def validasi_ktp_data(nik):
    data_ktp = DataKtp.query.get(nik)
    validasi_ktp = ValidasiKTP()
    if validasi_ktp.is_submitted():
        if validasi_ktp.validasi.data:
            try:
                data_ktp = DataKtp.query.get(nik)
                data_ktp.status_validasi = "Data Berhasil Divalidasi, selanjutnya silahkan datang ke kantor kecamatan banjarharjo mulai pukul 08:00 sampai pukul 16:00"
                db.session.commit()
                return redirect(url_for("accept_data_ktp", nik=nik, _external=True))
            except:
                db.session.rollback()
        elif validasi_ktp.tolak.data:
            try:
                data_ktp = DataKtp.query.get(nik)
                data_ktp.status_validasi = "Data Ditolak, silahkan untuk Update Data dan Input Data dengan benar"
                db.session.commit()
                return redirect(url_for("decline_data_ktp", nik=nik, _external=True))
            except:
                db.session.rollback()
    return render_template("validasiKTP_data.html", data_ktp=data_ktp, validasi_ktp=validasi_ktp)

@app.route("/admin/validasi/laporan/<nik>", methods=['GET', 'POST'])
@login_required
def validasi_laporan_data(nik):
    data_laporan = DataLaporan.query.get(nik)
    validasi_laporan = ValidasiLaporan()
    if validasi_laporan.is_submitted():
        if validasi_laporan.validasi.data:
            try:
                data_laporan = DataLaporan.query.get(nik)
                data_laporan.status_validasi = "Data Berhasil Divalidasi, Laporan telah kami terima, untuk selanjutnya akan pami proses lebih lanjut"
                db.session.commit()
                return redirect(url_for("accept_data_laporan", nik=nik, _external=True))
            except:
                db.session.rollback()
        elif validasi_laporan.tolak.data:
            try:
                data_laporan = DataLaporan.query.get(nik)
                data_laporan.status_validasi = "Data Ditolak, Laporan tidak diterima, silahkan untuk Update Data dan Input Data dengan benar"
                db.session.commit()
                return redirect(url_for("decline_data_laporan", nik=nik, _external=True))
            except:
                db.session.rollback()
    return render_template("validasiLaporan_data.html", data_laporan=data_laporan, validasi_laporan=validasi_laporan)


#-------------------------------------
#validasi data dan tolak validasi data

@app.route("/admin/validasi/ktp/<nik>/accept", methods=['GET', 'POST'])
@login_required
def accept_data_ktp(nik):
    data_ktp = DataKtp.query.get(nik)
    return render_template("validasiKTP_accept.html", data_ktp=data_ktp)

@app.route("/admin/validasi/ktp/<nik>/decline", methods=['GET', 'POST'])
@login_required
def decline_data_ktp(nik):
    data_ktp = DataKtp.query.get(nik)
    return render_template("validasiKTP_decline.html", data_ktp=data_ktp)

@app.route("/admin/validasi/laporan/<nik>/accept", methods=['GET', 'POST'])
@login_required
def accept_data_laporan(nik):
    data_laporan = DataLaporan.query.get(nik)
    return render_template("validasiLaporan_accept.html", data_laporan=data_laporan)

@app.route("/admin/validasi/laporan/<nik>/decline", methods=['GET', 'POST'])
@login_required
def decline_data_laporan(nik):
    data_laporan = DataLaporan.query.get(nik)
    return render_template("validasiLaporan_decline.html", data_laporan=data_laporan)

#----------------------------------
#data divalidasi
@app.route("/admin/validasi/ktp/divalidasi", methods=['GET', 'POST'])
@login_required
def ktp_divalidasi():
    data_ktp = DataKtp.query.filter(DataKtp.status_validasi == 'Data Berhasil Divalidasi, selanjutnya silahkan datang ke kantor kecamatan banjarharjo mulai pukul 08:00 sampai pukul 16:00').all()
    return render_template("dataKTP_divalidasi.html", data_ktp=data_ktp)

@app.route("/admin/validasi/laporan/divalidasi", methods=['GET', 'POST'])
@login_required
def laporan_divalidasi():
    data_laporan = DataLaporan.query.filter(DataLaporan.status_validasi == 'Data Berhasil Divalidasi, Laporan telah kami terima, untuk selanjutnya akan pami proses lebih lanjut').all()
    return render_template("dataLaporan_divalidasi.html", data_laporan=data_laporan)

@app.route("/admin/validasi/ktp/<nik>/divalidasi", methods=['GET', 'POST'])
@login_required
def ktp_divalidasi_data(nik):
    data_ktp = DataKtp.query.get(nik)
    return render_template("dataKTP_divalidasi_data.html", data_ktp=data_ktp)

@app.route("/admin/validasi/laporan/<nik>/divalidasi", methods=['GET', 'POST'])
@login_required
def laporan_divalidasi_data(nik):
    data_laporan = DataLaporan.query.get(nik)
    return render_template("dataLaporan_divalidasi_data.html", data_laporan=data_laporan)

#-----------------------------------
#Secret Register
@app.route("/admin/register", methods=['GET', 'POST'])
@login_required
def secret_register():
    form_register = RegistrationAdmin(csrf_enabled=False)
    if form_register.validate_on_submit():
        try:
            username = form_register.username.data
            name = form_register.name.data
            email = form_register.email.data
            password = form_register.password.data
            user = Admin(username=username, name=name, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("secret_register_accept", _external=True))
        except:
            db.session.rollback()
            return redirect(url_for("secret_register_decline", _external=True))
    return render_template("secret_register.html", form_register=form_register)

@app.route("/admin/register/accept", methods=['GET', 'POST'])
@login_required
def secret_register_accept():
    return render_template("register_accept.html")

@app.route("/admin/register/decline", methods=['GET', 'POST'])
@login_required
def secret_register_decline():
    return render_template("register_decline.html")

#--------------------
#logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)