.. |...| unicode:: U+2026   .. ellipsis

===================
django-admin-extra-actions
===================

Added publish and unpublish actions by default, If a field named 'published' exists in your model.


Install
=======

- add 'extra_action_options' to your INSTALLED_APPS

Example Usage
=======

.. code:: python

    # models.py
    # ============

    class Vehicle(models.Model):

        name = models.CharField('Name', max_length=50)
        color = models.CharField()
        owner_name = models.CharField()
        cost = models.DecimalField()
        published = models.BooleanField(default=True)

        def __unicode__(self):
            return '%s' %self.name
    
    # admin.py
    # =======
		
    from extra_action_options.options import ExtraOptionAdmin
    from .models import Vehicle

    class VehicleAdmin(ExtraOptionAdmin):
        list_display = ['name', 'published']
        search_fields = ('name', )

    admin.site.register(Vehicle, VehicleAdmin)

.. image:: https://raw.githubusercontent.com/sayonetech/django-admin-multioption-filters/master/screehshots/multifilter.png



