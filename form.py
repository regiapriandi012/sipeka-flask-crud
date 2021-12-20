from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, RadioField
from wtforms.validators import DataRequired

class InputKtp(FlaskForm):
    nik = StringField("NIK", validators=[DataRequired()])
    nama = StringField("Nama", validators=[DataRequired()])
    ttl = StringField("Tempat Tanggal Lahir", validators=[DataRequired()])
    choices = [("Laki-Laki", "Laki-Laki (Jenis Kelamin)"), ("Perempuan", "Perempuan (Jenis Kelamin)")]
    jk = RadioField("Jenis Kelamin", choices=choices)
    alamat = TextAreaField("Alamat", validators=[DataRequired()])
    rt = StringField("RT", validators=[DataRequired()])
    rw = StringField("RW", validators=[DataRequired()])
    desa = StringField("Desa", validators=[DataRequired()])
    kecamatan = StringField("Kecamatan", validators=[DataRequired()])
    kabupaten = StringField("Kabupaten", validators=[DataRequired()])
    kewarganegaraan = StringField("Kewarganegaraan", validators=[DataRequired()])
    pekerjaan = StringField("Pekerjaan", validators=[DataRequired()])
    status = StringField("Status", validators=[DataRequired()])
    notelf = StringField("Nomer Telefon", validators=[DataRequired()])
    submit = SubmitField("Input Data", validators=[DataRequired()])

class InputLaporan(FlaskForm):
    nik = StringField("NIK", validators=[DataRequired()])
    nama = StringField("Nama", validators=[DataRequired()])
    rt = StringField("RT", validators=[DataRequired()])
    rw = StringField("RW", validators=[DataRequired()])
    desa = StringField("Desa", validators=[DataRequired()])
    kecamatan = StringField("Kecamatan", validators=[DataRequired()])
    choices = [("Laki-Laki", "Laki-Laki (Jenis Kelamin)"), ("Perempuan", "Perempuan (Jenis Kelamin)")]
    jk = RadioField("Jenis Kelamin", choices = choices)
    notelf = StringField("Nomer Telefon", validators=[DataRequired()])
    categories = [("Dugaan Korupsi", "Dugaan Korupsi (Jenis Laporan)"), ("Pelecehan", "Pelecehan (Jenis Laporan)"), ("Kejahatan", "Kejahatan (Jenis Laporan)"), ("Jalan Rusak", "Jalan Rusak (Jenis Laporan)"), ("Lainnya", "Lainnya (Jenis Laporan)")]
    kategory = RadioField("Kategory Laporan", choices=categories)
    tanggal = StringField("Tanggal Laporan (hari, tanggal/bulan/tahun)", validators=[DataRequired()])
    isilaporan = TextAreaField("Isi Laporan", validators=[DataRequired()])
    pernyataan = TextAreaField("Pernyataan Kebenaran Data", validators=[DataRequired()])
    submit = SubmitField("Input Data", validators=[DataRequired()])

class CekKtp(FlaskForm):
    nik = StringField("NIK", validators=[DataRequired()])
    submit = SubmitField("Cek Data", validators=[DataRequired()])

class CekLaporan(FlaskForm):
    nik = StringField("NIK", validators=[DataRequired()])
    submit = SubmitField("Cek Data", validators=[DataRequired()])