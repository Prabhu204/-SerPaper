from django.contrib import admin
from . models import Article, Researchpaper, Subscription,Contact


# Register the Article Model in the Admin Pannel
class ArticleAdmin(admin.ModelAdmin):
    fields = ['title','preview','content']

admin.site.register(Article, ArticleAdmin)


class ResearchpaperAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'pub_date', 'abstract', 'pdf_url', 'subject']

admin.site.register(Researchpaper, ResearchpaperAdmin)


class SubscriptionAdmin(admin.ModelAdmin):
    fields = ['email']
    list_display = ('email', 'created_at')

admin.site.register(Subscription, SubscriptionAdmin)

class ContactAdmin(admin.ModelAdmin):
    fields = ['email', 'subject','message']
    readonly_fields = ('contacted_at',)
    list_display = ('email', 'contacted_at')
admin.site.register(Contact, ContactAdmin)

