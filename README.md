# 📘 **P1 — Fondasi Django & Class-Based Views (ListView)**

````markdown
# 🧱 Pertemuan 1 — Fondasi Django & Migrasi ke Class-Based Views (CBV)

## 🎯 Tujuan Pembelajaran
- Memahami arsitektur MVT (Model–View–Template)
- Membuat proyek Django dan aplikasi pertama
- Membuat model `Warga` dan melakukan migrasi
- Mengimplementasikan tampilan daftar warga dengan `ListView`

---

## 🧩 Studi Kasus: Aplikasi Warga Kelurahan
Aplikasi sederhana untuk mengelola data warga dan pengumuman di lingkungan kelurahan.  
Pada tahap ini kita akan menampilkan daftar warga.

---

## ⚙️ Langkah Praktikum

### 1️⃣ Setup Awal
```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install django
django-admin startproject DataKelurahan
cd DataKelurahan
python manage.py startapp warga
````

Tambahkan `'warga'` di `data_kelurahan/settings.py` → `INSTALLED_APPS`.

---

### 2️⃣ Membuat Model Warga (`warga/models.py`)

```python
from django.db import models

class Warga(models.Model):
    nik = models.CharField(max_length=16, unique=True)
    nama_lengkap = models.CharField(max_length=100)
    alamat = models.TextField()
    no_telepon = models.CharField(max_length=15, blank=True)
    tanggal_registrasi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama_lengkap
```

---

### 3️⃣ Migrasi Database

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 4️⃣ Tambah Model di Admin

`warga/admin.py`

```python
from django.contrib import admin
from .models import Warga

admin.site.register(Warga)
```

Kemudian:

```bash
python manage.py createsuperuser
python manage.py runserver
```

Login ke `/admin/` dan tambahkan 3 data warga.

---

### 5️⃣ Implementasi ListView

`warga/views.py`

```python
from django.views.generic import ListView
from .models import Warga

class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'
```

`warga/urls.py`

```python
from django.urls import path
from .views import WargaListView

urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
]
```

`data_kelurahan/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('warga/', include('warga.urls')),
]
```

`warga/templates/warga/warga_list.html`

```html
<h1>Daftar Warga</h1>
<ul>
{% for warga in object_list %}
    <li>{{ warga.nama_lengkap }} - NIK: {{ warga.nik }}</li>
{% empty %}
    <li>Belum ada data warga</li>
{% endfor %}
</ul>
```

---

## ✅ Hasil

Akses: [http://127.0.0.1:8000/warga/](http://127.0.0.1:8000/warga/)
Menampilkan daftar warga dari database.

<img width="2865" height="1627" alt="image" src="https://github.com/user-attachments/assets/f7e4c793-3d54-489a-ad93-369d40b4c15b" />

---

## 💡 Challenge

Buat halaman **Detail Warga** menggunakan `DetailView` dan tambahkan tautan dari daftar.

<img width="2876" height="1633" alt="image" src="https://github.com/user-attachments/assets/266532ee-89a2-442c-87d2-59c7c0caf1e2" />
<img width="2870" height="1621" alt="image" src="https://github.com/user-attachments/assets/9f3c4743-8d2e-4525-b001-0b32d583dae8" />


---

