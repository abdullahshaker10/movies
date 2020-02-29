from django.contrib import admin
from movies.models import Genre,Movie
# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id','name')
admin.site.register(Movie)
admin.site.register(Genre,GenreAdmin)
