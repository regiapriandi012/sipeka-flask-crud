from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, Regexp

class InputKtp(FlaskForm):
    nik = StringField("NIK", validators=[DataRequired(), Length(min=16, max=16), Regexp(regex='^[0-9]*$')])
    nama = StringField("Nama", validators=[DataRequired()])
    ttl = StringField("Tempat Tanggal Lahir", validators=[DataRequired()])
    choices = [("Laki-Laki", "Laki-Laki (Jenis Kelamin)"), ("Perempuan", "Perempuan (Jenis Kelamin)")]
    jk = RadioField("Jenis Kelamin", choices=choices, validators=[DataRequired()])
    alamat = TextAreaField("Alamat", validators=[DataRequired()])
    rt = StringField("RT", validators=[DataRequired(), Length(min=3, max=3), Regexp(regex='^[0-9]*$')])
    rw = StringField("RW", validators=[DataRequired(), Length(min=3, max=3), Regexp(regex='^[0-9]*$')])
    choice_desa = [("Sindangheula", "Sindangheula"), ("Blandongan", "Blandongan"), ("Kertasari", "Kertasari"),
                   ("Bandungsari", "Bandungsari"), ("Cipajang", "Cipajang"), ("Penanggapan", "Penanggapan"),
                   ("Malahayu", "Malahayu"), ("Cikuya", "Cikuya"), ("Banjarharjo", "Banjarharjo"),
                   ("Parireja", "Parireja"), ("Cigadung", "Cigadung"), ("Tiwulandu", "Tiwulandu"),
                   ("Cikakak", "Cikakak"), ("Cibendung", "Cibendung"), ("Karangmaja", "Karangmaja"),
                   ("Dukuhjeruk", "Dukuhjeruk"), ("Pende", "Pende"), ("Sukareja", "Sukareja"),
                   ("KubangJero", "Kubangjero"), ("Cibuniwangi", "Cibuniwangi"), ("Cimunding", "Cimunding"),
                   ("Ciawi", "Ciawi"), ("Cihaur", "Cihaur"), ("Tegalreja", "Tegalreja"), ("Banjar Lor", "Banjar Lor")]
    desa = SelectField("Desa", choices=choice_desa, validators=[DataRequired()])
    kecamatan = StringField("Kecamatan")
    kabupaten = StringField("Kabupaten")
    kewarganegaraan = StringField("Kewarganegaraan")
    pekerjaan = StringField("Pekerjaan", validators=[DataRequired()])
    status = StringField("Status", validators=[DataRequired()])
    notelf = StringField("Nomer Telefon", validators=[DataRequired(), Length(min=12, max=12), Regexp(regex='^[0-9]*$')])
    submit = SubmitField("Input Data", validators=[DataRequired()])

class InputLaporan(FlaskForm):
    nik = StringField("NIK", validators=[DataRequired(), Length(min=16, max=16), Regexp(regex='^[0-9]*$')])
    nama = StringField("Nama", validators=[DataRequired()])
    rt = StringField("RT", validators=[DataRequired(), Length(min=3, max=3), Regexp(regex='^[0-9]*$')])
    rw = StringField("RW", validators=[DataRequired(), Length(min=3, max=3), Regexp(regex='^[0-9]*$')])
    choice_desa = [("Sindangheula", "Sindangheula"), ("Blandongan", "Blandongan"), ("Kertasari", "Kertasari"),
                   ("Bandungsari", "Bandungsari"), ("Cipajang", "Cipajang"), ("Penanggapan", "Penanggapan"),
                   ("Malahayu", "Malahayu"), ("Cikuya", "Cikuya"), ("Banjarharjo", "Banjarharjo"),
                   ("Parireja", "Parireja"), ("Cigadung", "Cigadung"), ("Tiwulandu", "Tiwulandu"),
                   ("Cikakak", "Cikakak"), ("Cibendung", "Cibendung"), ("Karangmaja", "Karangmaja"),
                   ("Dukuhjeruk", "Dukuhjeruk"), ("Pende", "Pende"), ("Sukareja", "Sukareja"),
                   ("KubangJero", "Kubangjero"), ("Cibuniwangi", "Cibuniwangi"), ("Cimunding", "Cimunding"),
                   ("Ciawi", "Ciawi"), ("Cihaur", "Cihaur"), ("Tegalreja", "Tegalreja"), ("Banjar Lor", "Banjar Lor")]
    desa = SelectField("Desa", choices=choice_desa, validators=[DataRequired()])
    kecamatan = StringField("Kecamatan")
    choices = [("Laki-Laki", "Laki-Laki (Jenis Kelamin)"), ("Perempuan", "Perempuan (Jenis Kelamin)")]
    jk = RadioField("Jenis Kelamin", choices = choices, validators=[DataRequired()])
    notelf = StringField("Nomer Telefon", validators=[DataRequired(), Length(min=12, max=12), Regexp(regex='^[0-9]*$')])
    categories = [("Dugaan Korupsi", "Dugaan Korupsi (Jenis Laporan)"), ("Pelecehan", "Pelecehan (Jenis Laporan)"), ("Kejahatan", "Kejahatan (Jenis Laporan)"), ("Jalan Rusak", "Jalan Rusak (Jenis Laporan)"), ("Lainnya", "Lainnya (Jenis Laporan)")]
    kategory = RadioField("Kategory Laporan", choices=categories)
    tanggal = StringField("Tanggal Laporan (hari, tanggal/bulan/tahun)", validators=[DataRequired()])
    isilaporan = TextAreaField("Isi Laporan", validators=[DataRequired()])
    pernyataan = TextAreaField("Pernyataan Kebenaran Data", validators=[DataRequired()])
    submit = SubmitField("Input Data", validators=[DataRequired()])

class CekKtp(FlaskForm):
    nik = StringField("NIK", validators=[DataRequired(), Length(min=16, max=16), Regexp(regex='^[0-9]*$')])
    submit = SubmitField("Cek Data", validators=[DataRequired()])

class CekLaporan(FlaskForm):
    nik = StringField("NIK", validators=[DataRequired(), Length(min=16, max=16), Regexp(regex='^[0-9]*$')])
    submit = SubmitField("Cek Data", validators=[DataRequired()])