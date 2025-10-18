## 💡 Challenge P3 — Form Tambah Data Warga & Pengaduan

### 🎯 Tujuan
Membuat form input data menggunakan Django `ModelForm` dan `CreateView`.

---

### 🧩 Langkah-langkah

#### 1️⃣ Buat forms.py
```python
class WargaForm(forms.ModelForm):
    class Meta:
        model = Warga
        fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']

class PengaduanForm(forms.ModelForm):
    class Meta:
        model = Pengaduan
        fields = ['judul', 'deskripsi', 'status', 'pelapor']
````

#### 2️⃣ Tambahkan `CreateView`

```python
class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')
```

#### 3️⃣ Tambahkan URL

```python
path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
```

#### 4️⃣ Template

```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Simpan</button>
</form>
```

---

### ✅ Hasil

* `/warga/tambah/` menambahkan warga baru
* `/warga/pengaduan/tambah/` menambahkan pengaduan baru

Setelah klik **Simpan**, data langsung tersimpan dan diarahkan ke halaman daftar.

---

