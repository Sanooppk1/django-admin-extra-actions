from django.contrib import admin
from django.utils.translation import ugettext as _
from django.db.models.fields import FieldDoesNotExist


def make_published(modeladmin, request, queryset):
    queryset.update(published=True)
make_published.short_description = _('Change the selected item(s) as published')


def make_unpublished(modeladmin, request, queryset):
    queryset.update(published=False)
make_unpublished.short_description = _('Change the selected item(s) as unpublished')


class ExtraOptionAdmin(admin.ModelAdmin):

    def __init__(self, model, admin_site):
        self.model = model
        self.opts = model._meta
        self.admin_site = admin_site
        super(ExtraOptionAdmin, self).__init__(model, admin_site)

    def get_actions(self, request):
        try:
            self.model._meta.get_field('published')
            self.actions.append(make_published)
            self.actions.append(make_unpublished)
        except FieldDoesNotExist:
            pass

        return super(ExtraOptionAdmin, self).get_actions(request)
