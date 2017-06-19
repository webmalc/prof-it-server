"""
profit URL Configuration
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from pages.views import PagesViewSet

# from two_factor.admin import AdminSiteOTPRequired

# admin.site.__class__ = AdminSiteOTPRequired

router = DefaultRouter()
router.register(r'pages', PagesViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('two_factor.urls', 'two_factor')),
]
urlpatterns += i18n_patterns(url(r'^', include(router.urls)))

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
