from django.contrib import admin

from .models import Instrument
from django.utils.html import format_html
# Register your models here.

@admin.register(Instrument)
class InstrumentAd(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html(f'<img src="{obj.thumbnail.url}" style="width:70px; height:80px; object-fit:cover" />')
    
    def sound_tag(self, obj):
        return format_html(f'<hr> <audio controls> <source src="{ obj.sound.url }" type="audio/mp3"> </audio><hr>')

    list_display = ['image_tag', 'title', 'sound_tag']


