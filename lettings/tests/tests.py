import pytest
from django.urls import reverse, resolve
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

from lettings.models import Letting, Address

# INDEX
# VERIFIER PATH URL AVEC REVERSE + ELEMENT DE TITRE AVEC HTML
@pytest.mark.django_db
def test_lettings_index_url():
    path = reverse("lettings_index")

    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings_index"


@pytest.mark.django_db
def test_lettings_index_view():
    client = Client()
    path = reverse("lettings_index")
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Lettings</title>"

    assert expected_content in content
    assert response.status_code == 200
    path = reverse("lettings_index")
    assertTemplateUsed(response, "lettings/index.html")  # CHANGER NOM DE TEMPLATE


def test_lettings_detail_url():
    path = reverse("letting", kwargs={"letting_id": 1})

    assert path == "/lettings/1/"
    assert resolve(path).view_name == "letting"


@pytest.mark.django_db
def test_lettings_detail_view():
    client = Client()
    Address.objects.create(
        id=1,
        number=1,
        street="place Colbert",
        city="Lyon",
        state="France",
        zip_code=111,
        country_iso_code=222,
    )
    address = Address.objects.get(id=1)
    Letting.objects.create(title="title", address=address)
    path = reverse("letting", kwargs={"letting_id": 1})
    cur_letting = Letting.objects.get(id=1)
    response = client.get(path)
    content = response.content.decode()
    expected_content = f"<h1>{cur_letting.title}</h1>"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")  # CHANGER NOM DE TEMPLATE
