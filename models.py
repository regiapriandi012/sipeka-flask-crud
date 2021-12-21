from flask_sqlalchemy import SQLAlchemy

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
