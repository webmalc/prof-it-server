"""
profit URL Configuration
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

# from two_factor.admin import AdminSiteOTPRequired

# admin.site.__class__ = AdminSiteOTPRequired

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('two_factor.urls', 'two_factor')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
