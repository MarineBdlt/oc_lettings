from django.contrib import admin
from django.urls import path
from . import views
from lettings import views as l_views
from profiles import views as p_views

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", l_views.index, name="lettings_index"),  # ANCHOR change name ?
    path("lettings/<int:letting_id>/", l_views.letting, name="letting"),
    path("profiles/", p_views.index, name="profiles_index"),
    path("profiles/<str:username>/", p_views.profile, name="profile"),
    path("admin/", admin.site.urls),
]
