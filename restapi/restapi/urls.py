"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

# from updates.views import (
#     json_example_view,
#     JsonCVB,
#     JsonCVB2,
#     SerializedListView,
#     SerializedDetaileView
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/updates/', include('updates.api.urls')),
    path('api/status/', include('status.api.urls')),
    path('api/auth/', include('accounts.api.urls')),
    path('api/user/', include('accounts.api.user.urls')),

    # path('', json_example_view),
    # path('json/cbv/', JsonCVB.as_view()),
    # path('json/cbv2/', JsonCVB2.as_view()),
    # path('json/serialized/list/', SerializedListView.as_view()),
    # path('json/serialized/detail/', SerializedDetaileView.as_view()),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
