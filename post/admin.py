from django.contrib import admin
from . models import Article, Researchpaper, SubscribeModel


# Register the Article Model in the Admin Pannel
class ArticleAdmin(admin.ModelAdmin):
    fields = ['title','preview','content']

admin.site.register(Article, ArticleAdmin)


class ResearchpaperAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'pub_date', 'abstract', 'pdf_url', 'subject']

admin.site.register(Researchpaper, ResearchpaperAdmin)


class SubscribeModelAdmin(admin.ModelAdmin):
    fields = ['email', 'sys_id','status','created_date','updated_date']

admin.site.register(SubscribeModel, SubscribeModelAdmin)

