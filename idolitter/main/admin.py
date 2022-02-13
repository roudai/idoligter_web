from django.contrib import admin
from import_export import resources
from import_export.admin import ImportMixin
from .models import Group, Idol

class groupModelAdmin(ImportMixin, admin.ModelAdmin):
  class groupResource(resources.ModelResource):
    class Meta:
      model = Group
      fields = ('id', 'name', 'twitterUsername', 'twitterId', 'twitterName', 'twitterDescription')
  resource_class = groupResource

  list_display = ('name', 'twitterUsername', 'twitterId', 'twitterName', 'twitterDescription')
  fields = ('name', 'twitterUsername')

class idolModelAdmin(ImportMixin, admin.ModelAdmin):
  list_display = ('name', 'twitterUsername', 'twitterId', 'twitterName', 'twitterDescription')
  fields = ('group', 'name', 'twitterUsername')
  filter_horizontal = ('group',)

admin.site.register(Group, groupModelAdmin)
admin.site.register(Idol, idolModelAdmin)