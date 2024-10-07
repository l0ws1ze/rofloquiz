from django.contrib import admin
from .models import*

admin.site.register(User)
admin.site.register(Quiz)
admin.site.register(QuizAnswer)
admin.site.register(QuizMeta)
# Register your models here.
