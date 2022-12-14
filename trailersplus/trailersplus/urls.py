from django.conf import settings
from django.conf.urls import url
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
from home.views import search_redirect
from checkout import views

urlpatterns = [
    url(r"^django-admin/", admin.site.urls),
    url(r"^admin/", include(wagtailadmin_urls)),
    url(r"^documents/", include(wagtaildocs_urls)),
    url(r"^i18n/", include("django.conf.urls.i18n")),
    url(r"^search/$", search_views.search, name="search"),
    url(r"^api/", include("api.urls")),
    url(r"^en/api/", include("api.urls")),
    url(r"^es/api/", include("api.urls")),
    url(r"^submit/$", search_redirect, name="Search Trailers Form Redirect"),
    url(r"^en/submit/$", search_redirect, name="Search Trailers Form Redirect"),
    url(r"^es/submit/$", search_redirect, name="Search Trailers Form Redirect"),
    url(r"^checkout-submit/$", views.submit, name="Checkout submit"),
    url(r"^en/checkout-submit/$", views.submit, name="Checkout submit"),
    url(r"^es/checkout-submit/$", views.submit, name="Checkout submit"),
    path("invoice/<str:invoice_id>/", views.InvoiceView.as_view(), name="Invoice"),
]

# Multilang patterns
urlpatterns += i18n_patterns(url(r"", include(wagtail_urls)),)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    # Serve static and media files from development server

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r"", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r"^pages/", include(wagtail_urls)),
]

handler404 = 'home.views.error_404_view'
