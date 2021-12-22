from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class DataKtp(db.Model):
    __tablename__ = "data_ktp"
    nik = db.Column(db.String(30), primary_key=True)
    nama = db.Column(db.String(100), index=True, unique=False)
    ttl = db.Column(db.String(100), index=True, unique=False)
    jk = db.Column(db.String(100), index=True, unique=False)
    alamat = db.Column(db.String(100), index=True, unique=False)
    rt = db.Column(db.String(30), index=True, unique=False)
    rw = db.Column(db.String(30), index=True, unique=False)
    desa = db.Column(db.String(100), index=True, unique=False)
    kecamatan = db.Column(db.String(100), index=True, unique=False)
    kabupaten = db.Column(db.String(100), index=True, unique=False)
    kewarganegaraan = db.Column(db.String(100), index=True, unique=False)
    pekerjaan = db.Column(db.String(100), index=True, unique=False)
    status = db.Column(db.String(100), index=True, unique=False)
    notelf = db.Column(db.String(100), index=True, unique=False)
    surat_keterangan = db.Column(db.String(100), index=True, unique=False)
    status_validasi = db.Column(db.String(300), index=True, unique=False)

    def __repr__(self):
        return "{} - {}".format(self.nik, self.nama)

class DataLaporan(db.Model):
    __tablename__ = "data_laporan"
    nik = db.Column(db.String(30), primary_key=True)
    nama = db.Column(db.String(100), index=True, unique=False)
    rt = db.Column(db.String(30), index=True, unique=False)
    rw = db.Column(db.String(30), index=True, unique=False)
    desa = db.Column(db.String(100), index=True, unique=False)
    kecamatan = db.Column(db.String(100), index=True, unique=False)
    jk = db.Column(db.String(100), index=True, unique=False)
    notelf = db.Column(db.String(100), index=True, unique=False)
    kategory = db.Column(db.String(100), index=True, unique=False)
    tanggal = db.Column(db.String(100), index=True, unique=False)
    isilaporan = db.Column(db.String(700), index=True, unique=False)
    pernyataan = db.Column(db.String(200), index=True, unique=False)
    status_validasi = db.Column(db.String(300), index=True, unique=False)

    def __repr__(self):
        return "{} - {}".format(self.nik, self.nama)

class Admin(UserMixin, db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), index=True)
    name = db.Column(db.String(128), index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)