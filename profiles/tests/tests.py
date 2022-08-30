import pytest
from django.urls import reverse, resolve
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profiles_index_url():
    path = reverse("profiles_index")

    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles_index"


@pytest.mark.django_db
def test_profiles_index_view():
    client = Client()
    path = reverse("profiles_index")
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Profiles</title>"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profiles_detail_view():
    client = Client()
    user = User.objects.create(username="User", password="Passwordpassword")
    Profile.objects.create(user=user, favorite_city="Paris")
    path = reverse("profile", kwargs={"username": f"{user.username}"})
    response = client.get(path)
    content = response.content.decode()
    expected_content = f"<h1>{user.username}</h1>"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")
