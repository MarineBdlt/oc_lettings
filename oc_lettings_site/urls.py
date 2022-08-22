from django.contrib import admin
from django.urls import path
from lettings import views as l_views
from profiles import views as p_views

# from lettings.views import index, letting
# from profiles.views import profiles_index, profile

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", l_views.index, name="lettings_index"),
    path("lettings/<int:letting_id>/", l_views.letting, name="letting"),
    path("profiles/", p_views.index, name="profiles_index"),
    path("profiles/<str:username>/", p_views.profile, name="profile"),
    path("admin/", admin.site.urls),
]

# from django.contrib import admin
# from django.urls import path, include
# from rest_framework import routers
# from contracts.views import ContractViewSet
# from events.views import EventViewSet
# from clients.views import ClientViewSet
# from auth_app.views import UserViewSet

# admin.site.site_header = 'Epic Event CER'

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'clients', ClientViewSet)
# router.register(r'contracts', ContractViewSet)
# router.register(r'events', EventViewSet)


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('rest_framework.urls')),
#     path("api/account/", include(router.urls)),
# ]
