from flask import Flask, request, render_template

app = Flask(__name__)

# Data mata pelajaran
senin = "=== Mata Pelajaran ===\n1: IPA\n2:B. Korea\n3:B. Arab\n4:B. Indonesia"
selasa = "=== Mata Pelajaran ===\n1: MTK\n2: Akidah Akhlak\n3:B. Indonesia\n4: IPS"
rabu = "=== Mata Pelajaran ===\n1:B. Inggris\n2: Al-Quran Hadist\n3: MTK\n4: IPA"
kamis = "=== Mata Pelajaran ===\n1: Fiqih\n2: PPKn\n3:B. Inggris\n4:Seni Budaya"
jumat = "=== Mata Pelajaran ===\n1: Penjas\n2: BTQ"
sabtu = "=== Mata Pelajaran ===\n1:B. Indonesia\n2: IPS\n3: Informatika\n4: SKI"

# Fungsi untuk mengambil jadwal berdasarkan hari
def get_jadwal(hari):
    jadwal = {
        'senin': senin,
        'selasa': selasa,
        'rabu': rabu,
        'kamis': kamis,
        'jumat': jumat,
        'sabtu': sabtu
    }
    return jadwal.get(hari.lower(), "Mohon masukkan nama hari yang valid.")

# Rute untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Rute untuk menampilkan jadwal
@app.route('/jadwal', methods=['POST'])
def jadwal():
    hari = request.form['hari']
    jadwal_hari = get_jadwal(hari)
    return render_template('jadwal.html', hari=hari, jadwal_hari=jadwal_hari)

if __name__ == '__main__':
    app.run(debug=True)