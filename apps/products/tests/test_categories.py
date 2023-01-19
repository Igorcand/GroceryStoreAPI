import json
import pytest
from django.urls import reverse

from apps.products.models import Category

# set DJANGO_SETTINGS_MODULE=project.settings

categories_url = reverse("categories")
categories_detail_url = reverse("categories_detail", kwargs={'pk': 1})
# categories_detail_url = reverse("categories_detail")

pytestmark = pytest.mark.django_db
HEADERS = {'Content-Type': 'application/json'}

# --------------------- Test Get Categories -----------------------

def test_zero_categories_should_return_empty_list(client) -> None:
    response = client.get(categories_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []

def test_one_company_exists_should_succeed(client) -> None:
    test_cotegory = Category.objects.create(name="Test")
    response = client.get(categories_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("name") == test_cotegory.name

def test_get_one_company_by_pk_should_succeed(client) -> None:
    Category.objects.create(name="CategoryTest")
    response = client.get(path=categories_detail_url)
    assert response.status_code == 200
    assert json.loads(response.content).get("name") == "CategoryTest"

def test_get_one_company_by_pk_should_fail(client) -> None:
    response = client.get(path=categories_detail_url)
    assert response.status_code == 500
    assert json.loads(response.content) == {'detail': "This category doesn't exist"}

# --------------------- Test Post Categories -----------------------

def test_create_company_without_argumets_should_fail(client) -> None:
    response = client.post(path=categories_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {"detail": 
                                            "JSON parse error - Expecting value: line 1 column 1 (char 0)"
                                            }

def test_create_company_with_argumets_empty_should_fail(client) -> None:
    response = client.post(path=categories_url, data={"":""}, content_type='application/json')
    assert response.status_code == 400
    assert json.loads(response.content) == {"name": ["This field is required."]}

def test_create_existing_company_should_fail(client) -> None:
    Category.objects.create(name="CategoryTest")
    response = client.post(path=categories_url, data={"name": "CategoryTest"},  content_type='application/json')
    assert response.status_code == 400
    assert json.loads(response.content) == {"name": ["category with this name already exists."]}

def test_create_company_should_succeed(client) -> None:
    response = client.post(path=categories_url, data={"name": "CategoryTest"},  content_type='application/json')
    response_content = json.loads(response.content)
    assert response.status_code == 201
    assert response_content.get("name") == "CategoryTest"

# --------------------- Test Delete Categories -----------------------

def test_delete_company_nonexisted_should_fail(client) -> None:
    response = client.delete(path=categories_detail_url)
    assert response.status_code == 500
    assert json.loads(response.content) == {'detail': "This category doesn't exist"}

def test_delete_company_existed_should_succeed(client) -> None:
    Category.objects.create(name="CategoryTest")
    response = client.delete(path=categories_detail_url)
    assert response.status_code == 204