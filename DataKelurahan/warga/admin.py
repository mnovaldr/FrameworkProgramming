from django.contrib import admin
from .models import Warga, Pengaduan
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin


admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

class WargaAdmin(ModelAdmin):
    list_display = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']
    search_fields = ['nik', 'nama_lengkap']

class PengaduanAdmin(ModelAdmin):
    list_display = ['judul', 'deskripsi', 'status', 'tanggal_lapor', 'pelapor']
    search_fields = ['judul', 'status', 'pelapor']

admin.site.register(Warga, WargaAdmin)
admin.site.register(Pengaduan, PengaduanAdmin)
