from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, Regexp

class InputKtp(FlaskForm):
    nik = StringField("NIK", validators=[DataRequired(), Length(min=16, max=16), Regexp(regex='^[0-9]*$')])
    nama = StringField("Nama", validators=[DataRequired()])
    ttl = StringField("Tempat Tanggal Lahir", validators=[DataRequired()])
    choices = [("Laki-Laki", "Laki-Laki"), ("Perempuan", "Perempuan")]
    jk = RadioField("Jenis Kelamin", choices=choices, validators=[DataRequired()])
    alamat = TextAreaField("Alamat", validators=[DataRequired()])
    rt_choices = [("", "(pilih)"),("001", "001"), ("002", "002"), ("003", "003"), ("004", "004"), ("005", "005"), ("006", "006"), ("007", "007"), ("008", "008")
                  , ("009", "009"), ("010", "010"), ("011", "011"), ("012", "012"), ("013", "013"), ("014", "014"), ("015", "015"), ("016", "016")
                  , ("017", "017"), ("018", "018"), ("019", "019"), ("020", "020"), ("021", "021"), ("022", "022"), ("023", "023"), ("024", "024")
                  , ("025", "025"), ("026", "026"), ("027", "027"), ("028", "028"), ("029", "029"), ("030", "030")]
    rw_choices = [("", "(pilih)"),("001", "001"), ("002", "002"), ("003", "003"), ("004", "004"), ("005", "005"), ("006", "006"), ("007", "007"), ("008", "008")
                  , ("009", "009"), ("010", "010"), ("011", "011"), ("012", "012"), ("013", "013"), ("014", "014"), ("015", "015"), ("016", "016")
                  , ("017", "017"), ("018", "018"), ("019", "019"), ("020", "020"), ("021", "021"), ("022", "022"), ("023", "023"), ("024", "024")
                  , ("025", "025"), ("026", "026"), ("027", "027"), ("028", "028"), ("029", "029"), ("030", "030")]
    rt = SelectField("RT", choices=rt_choices,  validators=[DataRequired(), Length(min=3, max=3), Regexp(regex='^[0-9]*$')])
    rw = SelectField("RW", choices=rw_choices, validators=[DataRequired(), Length(min=3, max=3), Regexp(regex='^[0-9]*$')])
    choice_desa = [("", "(Pilih)"),("Sindangheula", "Sindangheula"), ("Blandongan", "Blandongan"), ("Kertasari", "Kertasari"),
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
    perkawinan_choice = [("", "(pilih)"),("Belum Kawin", "Belum Kawin"), ("Kawin", "Kawin"), ("Cerai Hidup", "Cerai Hidup"), ("Cerai Mati", "Cerai Mati")]
    status = SelectField("Status Perkawinan", choices=perkawinan_choice, validators=[DataRequired()])
    notelf = StringField("Nomer Telefon", validators=[DataRequired(), Length(min=12, max=12), Regexp(regex='^[0-9]*$')])
    surket_choice = [("", "(Pilih)"),("Sudah Membuat", "Sudah Membuat"), ("Belum Membuat", "Belum Membuat")]
    surat_keterangan = SelectField("Surat Pengantar Dari Desa", choices=surket_choice, validators=[DataRequired()])
    submit = SubmitField("Input Data", validators=[DataRequired()])

class InputLaporan(FlaskForm):
    nik = StringField("NIK", validators=[DataRequired(), Length(min=16, max=16), Regexp(regex='^[0-9]*$')])
    nama = StringField("Nama", validators=[DataRequired()])
    rt_choices = [("", "(pilih)"),("001", "001"), ("002", "002"), ("003", "003"), ("004", "004"), ("005", "005"), ("006", "006"),
                  ("007", "007"), ("008", "008")
        , ("009", "009"), ("010", "010"), ("011", "011"), ("012", "012"), ("013", "013"), ("014", "014"),
                  ("015", "015"), ("016", "016")
        , ("017", "017"), ("018", "018"), ("019", "019"), ("020", "020"), ("021", "021"), ("022", "022"),
                  ("023", "023"), ("024", "024")
        , ("025", "025"), ("026", "026"), ("027", "027"), ("028", "028"), ("029", "029"), ("030", "030")]
    rw_choices = [("", "(pilih)"),("001", "001"), ("002", "002"), ("003", "003"), ("004", "004"), ("005", "005"), ("006", "006"),
                  ("007", "007"), ("008", "008")
        , ("009", "009"), ("010", "010"), ("011", "011"), ("012", "012"), ("013", "013"), ("014", "014"),
                  ("015", "015"), ("016", "016")
        , ("017", "017"), ("018", "018"), ("019", "019"), ("020", "020"), ("021", "021"), ("022", "022"),
                  ("023", "023"), ("024", "024")
        , ("025", "025"), ("026", "026"), ("027", "027"), ("028", "028"), ("029", "029"), ("030", "030")]
    rt = SelectField("RT", choices=rt_choices, validators=[DataRequired(), Length(min=3, max=3), Regexp(regex='^[0-9]*$')])
    rw = SelectField("RW", choices=rw_choices, validators=[DataRequired(), Length(min=3, max=3), Regexp(regex='^[0-9]*$')])
    choice_desa = [("", "Pilih"),("Sindangheula", "Sindangheula"), ("Blandongan", "Blandongan"), ("Kertasari", "Kertasari"),
                   ("Bandungsari", "Bandungsari"), ("Cipajang", "Cipajang"), ("Penanggapan", "Penanggapan"),
                   ("Malahayu", "Malahayu"), ("Cikuya", "Cikuya"), ("Banjarharjo", "Banjarharjo"),
                   ("Parireja", "Parireja"), ("Cigadung", "Cigadung"), ("Tiwulandu", "Tiwulandu"),
                   ("Cikakak", "Cikakak"), ("Cibendung", "Cibendung"), ("Karangmaja", "Karangmaja"),
                   ("Dukuhjeruk", "Dukuhjeruk"), ("Pende", "Pende"), ("Sukareja", "Sukareja"),
                   ("KubangJero", "Kubangjero"), ("Cibuniwangi", "Cibuniwangi"), ("Cimunding", "Cimunding"),
                   ("Ciawi", "Ciawi"), ("Cihaur", "Cihaur"), ("Tegalreja", "Tegalreja"), ("Banjar Lor", "Banjar Lor")]
    desa = SelectField("Desa", choices=choice_desa, validators=[DataRequired()])
    kecamatan = StringField("Kecamatan")
    choices = [("Laki-Laki", "Laki-Laki"), ("Perempuan", "Perempuan")]
    jk = RadioField("Jenis Kelamin", choices = choices, validators=[DataRequired()])
    notelf = StringField("Nomer Telefon", validators=[DataRequired(), Length(min=12, max=12), Regexp(regex='^[0-9]*$')])
    categories = [("Dugaan Korupsi", "Dugaan Korupsi"), ("Pelecehan", "Pelecehan"), ("Kejahatan", "Kejahatan"), ("Jalan Rusak", "Jalan Rusak"), ("Lainnya", "Lainnya")]
    kategory = RadioField("Kategori Laporan", choices=categories)
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

class ValidasiKTP(FlaskForm):
    validasi = SubmitField("Validasi", validators=[DataRequired()])
    tolak = SubmitField("Tolak", validators=[DataRequired()])

class ValidasiLaporan(FlaskForm):
    validasi = SubmitField("Validasi", validators=[DataRequired()])
    tolak = SubmitField("Tolak", validators=[DataRequired()])
