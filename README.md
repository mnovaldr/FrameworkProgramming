# 📘 **P2 — Relasi Model & QuerySet Lanjutan**

```markdown
# 🔗 Pertemuan 2 — Relasi Model & QuerySet Lanjutan

## 🎯 Tujuan Pembelajaran
- Memahami relasi One-to-Many menggunakan `ForeignKey`
- Membuat model `Pengaduan` yang terhubung ke `Warga`
- Menampilkan daftar pengaduan per warga
- Menggunakan QuerySet untuk memfilter data

---

## 🧩 Studi Kasus
Setiap warga dapat memiliki banyak pengaduan.

---

## ⚙️ Langkah Praktikum

### 1️⃣ Tambahkan Model Pengaduan
`warga/models.py`
```python
class Pengaduan(models.Model):
    STATUS_CHOICES = [
        ('BARU', 'Baru'),
        ('DIPROSES', 'Diproses'),
        ('SELESAI', 'Selesai'),
    ]
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='BARU')
    tanggal_lapor = models.DateTimeField(auto_now_add=True)
    pelapor = models.ForeignKey(Warga, on_delete=models.CASCADE, related_name='pengaduan')

    def __str__(self):
        return self.judul
````

---

### 2️⃣ Migrasi Database

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 3️⃣ Daftarkan Model di Admin

`warga/admin.py`

```python
from django.contrib import admin
from .models import Warga, Pengaduan

admin.site.register(Warga)
admin.site.register(Pengaduan)
```

Tambahkan beberapa data pengaduan melalui admin.

---

### 4️⃣ Tampilkan Pengaduan di Halaman Detail Warga

`warga/templates/warga/warga_detail.html`

```html
<h1>{{ object.nama_lengkap }}</h1>
<p>NIK: {{ object.nik }}</p>
<p>Alamat: {{ object.alamat }}</p>

<h2>Daftar Pengaduan:</h2>
<ul>
{% for aduan in object.pengaduan.all %}
    <li><strong>{{ aduan.judul }}</strong> ({{ aduan.get_status_display }})</li>
{% empty %}
    <li>Belum ada pengaduan</li>
{% endfor %}
</ul>
```

---

## ✅ Hasil

Halaman detail warga kini menampilkan daftar pengaduan yang dilaporkan warga tersebut.
<img width="2880" height="1615" alt="image" src="https://github.com/user-attachments/assets/1c555693-770b-4e4c-ac52-65c84e4d8afb" />


---

## 💡 Challenge

Buat halaman `/warga/pengaduan/` untuk menampilkan **semua pengaduan** dengan `ListView`.
Tambahkan nama pelapor (`aduan.pelapor.nama_lengkap`) pada tiap item.

<img width="2880" height="1636" alt="image" src="https://github.com/user-attachments/assets/3f5e58a6-a498-4ec2-9a32-bd002913e749" />

---
