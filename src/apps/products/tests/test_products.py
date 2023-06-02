import json

import pytest
from django.urls import reverse

from src.apps.products.models import Category, Product

products_url = reverse('products')
products_detail_url = reverse('products_detail', kwargs={'pk': 1})

pytestmark = pytest.mark.django_db

# --------------------- Test Get Products -----------------------


def test_zero_products_should_return_empty_list(client) -> None:
    response = client.get(products_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


def test_one_product_exists_should_succeed(client) -> None:
    category = Category.objects.create(name='CategoryTest')
    test_product = Product.objects.create(
        name='ProductTest',
        description='description',
        stock=2,
        price=12.20,
        category=category,
    )
    response = client.get(products_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get('name') == test_product.name
    assert response_content.get('description') == test_product.description
    assert float(response_content.get('stock')) == test_product.stock
    assert float(response_content.get('price')) == test_product.price


def test_get_one_product_by_pk_should_succeed(client) -> None:
    category = Category.objects.create(name='CategoryTest')
    Product.objects.create(
        name='ProductTest',
        description='description',
        stock=2,
        price=12.20,
        category=category,
    )
    response = client.get(path=products_detail_url)
    assert response.status_code == 200
    assert json.loads(response.content).get('name') == 'ProductTest'


def test_get_one_product_by_pk_should_fail(client) -> None:
    response = client.get(path=products_detail_url)
    assert response.status_code == 500
    assert json.loads(response.content) == {
        'detail': "This product doesn't exist"
    }


# --------------------- Test Post Categories -----------------------


def test_create_products_without_argumets_should_fail(client) -> None:
    response = client.post(path=products_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {
        'detail': 'JSON parse error - Expecting value: line 1 column 1 (char 0)'
    }


def test_create_products_with_argumets_empty_should_fail(client) -> None:
    response = client.post(
        path=products_url, data={'': ''}, content_type='application/json'
    )
    assert response.status_code == 400
    assert json.loads(response.content) == {
        'name': ['This field is required.'],
        'description': ['This field is required.'],
        'stock': ['This field is required.'],
        'price': ['This field is required.'],
    }


def test_create_existing_product_should_fail(client) -> None:
    category = Category.objects.create(name='CategoryTest')
    Product.objects.create(
        name='ProductTest',
        description='description',
        stock=2,
        price=12.20,
        category=category,
    )
    response = client.post(
        path=products_url,
        data={
            'name': 'ProductTest',
            'description': 'description',
            'stock': 2,
            'price': 12.20,
            'category': '1',
        },
        content_type='application/json',
    )

    assert response.status_code == 400
    assert json.loads(response.content) == {
        'name': ['product with this name already exists.']
    }


def test_create_product_should_succeed(client) -> None:
    Category.objects.create(name='CategoryTest')
    response = client.post(
        path=products_url,
        data={
            'name': 'ProductTest',
            'description': 'description',
            'stock': 2,
            'price': 12.20,
            'category': '1',
        },
        content_type='application/json',
    )
    response_content = json.loads(response.content)
    assert response.status_code == 201
    assert response_content.get('name') == 'ProductTest'
    assert response_content.get('description') == 'description'
    assert float(response_content.get('stock')) == 2
    assert float(response_content.get('price')) == 12.20
    assert response_content.get('category') == 1


# --------------------- Test Put Categories -----------------------
def test_update_existing_product_should_succeed(client) -> None:
    category = Category.objects.create(name='CategoryTest')
    Product.objects.create(
        name='ProductTest',
        description='description',
        stock=2,
        price=12.20,
        category=category,
    )
    response = client.put(
        path=products_detail_url,
        data={
            'name': 'ProductTest',
            'description': 'description_changed',
            'stock': 10,
            'price': 15.20,
            'category': '1',
        },
        content_type='application/json',
    )
    response_content = json.loads(response.content)
    assert response.status_code == 200
    assert response_content.get('name') == 'ProductTest'
    assert response_content.get('description') == 'description_changed'
    assert float(response_content.get('stock')) == 10
    assert float(response_content.get('price')) == 15.20
    assert response_content.get('category') == 1


def test_update_existing_product_with_negative_stock_should_fail(
    client,
) -> None:
    category = Category.objects.create(name='CategoryTest')
    Product.objects.create(
        name='ProductTest',
        description='description',
        stock=2,
        price=12.20,
        category=category,
    )
    response = client.put(
        path=products_detail_url,
        data={
            'name': 'ProductTest',
            'description': 'description_changed',
            'stock': -4,
            'price': 15.20,
            'category': '1',
        },
        content_type='application/json',
    )
    assert response.status_code == 400
    assert json.loads(response.content) == {
        'message': 'Cannot update a negative stock.'
    }


def test_update_existing_product_with_nonexisted_category_should_fail(
    client,
) -> None:
    category = Category.objects.create(name='CategoryTest')
    Product.objects.create(
        name='ProductTest',
        description='description',
        stock=2,
        price=12.20,
        category=category,
    )
    response = client.put(
        path=products_detail_url,
        data={
            'name': 'ProductTest',
            'description': 'description_changed',
            'stock': 10,
            'price': 15.20,
            'category': '2',
        },
        content_type='application/json',
    )
    assert response.status_code == 400
    assert json.loads(response.content) == {
        'category': ['Invalid pk "2" - object does not exist.']
    }


def test_update_nonexisted_product_should_fail(client) -> None:

    response = client.put(
        path=products_detail_url,
        data={
            'name': 'ProductTest',
            'description': 'description_changed',
            'stock': 10,
            'price': 15.20,
            'category': '2',
        },
        content_type='application/json',
    )
    assert response.status_code == 500
    assert json.loads(response.content) == {
        'detail': "This product doesn't exist"
    }


# --------------------- Test Delete Categories -----------------------


def test_delete_product_nonexisted_should_fail(client) -> None:
    response = client.delete(path=products_detail_url)
    assert response.status_code == 500
    assert json.loads(response.content) == {
        'detail': "This product doesn't exist"
    }


def test_delete_product_existed_should_succeed(client) -> None:
    category = Category.objects.create(name='CategoryTest')
    Product.objects.create(
        name='ProductTest',
        description='description',
        stock=2,
        price=12.20,
        category=category,
    )
    response = client.delete(path=products_detail_url)
    assert response.status_code == 204
