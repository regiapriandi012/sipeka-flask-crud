from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, DateField, RadioField
from wtforms.validators import DataRequired

class InputKtp(FlaskForm):
    nik = StringField("NIK", validators=[DataRequired()])
    nama = StringField("Nama", validators=[DataRequired()])
    ttl = DateField("Tempat Tanggal Lahir", validators=[DataRequired()])
    choices = [("Laki-Laki", "Laki-Laki"), ("Perempuan", "Perempuan")]
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