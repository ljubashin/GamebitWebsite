from django.contrib import admin

from gamebit.models import Game, Category, gameStudio, Review

# Register your models here.

admin.site.register(Game)
admin.site.register(Category)
admin.site.register(gameStudio)
admin.site.register(Review)