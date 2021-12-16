from flask_wtf import FlaskForm
from wtforms import SubmitField, DateField, StringField, TextAreaField, RadioField
from wtforms.validators import DataRequired

class InputLaporan(FlaskForm):
    nik = StringField("NIK", validators=[DataRequired()])
    nama = StringField("Nama", validators=[DataRequired()])
    rt = StringField("RT", validators=[DataRequired()])
    rw = StringField("RW", validators=[DataRequired()])
    choices = [("Laki-Laki", "Laki-Laki"), ("Perempuan", "Perempuan")]
    jk = RadioField("Jenis Kelamin", choices = choices)
    notelf = StringField("Nomer Telefon", validators=[DataRequired()])
    categories = [("Pelecehan", "Pelecehan"), ("Kejahatan", "Kejahatan"), ("Jalan Rusak", "Jalan Rusak"), ("Lainnya", "Lainnya")]
    kategory = RadioField("Kategory Laporan", choices=categories)
    tanggal = DateField("Tanggal Laporan", validators=[DataRequired()])
    isilaporan = TextAreaField("Isi Laporan", validators=[DataRequired()])
    submit = SubmitField("Input Data", validators=[DataRequired()])
