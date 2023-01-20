import json
import pytest
from django.urls import reverse

from apps.sales.models import Sale
from apps.products.models import  Product, Category


# set DJANGO_SETTINGS_MODULE=project.settings

sales_url = reverse("sales")

pytestmark = pytest.mark.django_db

# --------------------- Test Get Products -----------------------

def test_zero_sales_should_return_empty_list(client) -> None:
    response = client.get(sales_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []

def test_one_sale_exists_should_succeed(client) -> None:
    category = Category.objects.create(name="CategoryTest")
    test_product = Product.objects.create(name="ProductTest", description='description', stock=2, price=12.20, category = category)
    test_sale = Sale(data='2023-01-18', product=test_product, quantity=1.0,)
    test_sale.save()

    response = client.get(sales_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("data") == test_sale.data
    assert float(response_content.get("quantity")) == test_sale.quantity
    assert response_content.get("payment") == 'Credit Card'
    assert response_content.get("product") == test_sale.product.id

# --------------------- Test Post Categories -----------------------
def test_create_sale_without_argumets_should_fail(client) -> None:
    response = client.post(path=sales_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {"detail": 
                                            "JSON parse error - Expecting value: line 1 column 1 (char 0)"}

def test_create_sale_with_argumets_empty_should_fail(client) -> None:
    category = Category.objects.create(name="CategoryTest")
    test_product = Product.objects.create(name="ProductTest", description='description', stock=2, price=12.20, category = category)
    test_product.save()
    test_sale = Sale(data='2023-01-18', product=test_product, quantity=1.0,)
    test_sale.save()
    response = client.post(path=sales_url, data={}, content_type='application/json')
    assert response.status_code == 500
    assert json.loads(response.content) ==  {'detail': 'You need to pass the fields'}

def test_add_sale_with_arguments_should_succeed(client) -> None:
    category = Category.objects.create(name="CategoryTest")
    test_product = Product.objects.create(name="ProductTest", description='description', stock=2, price=12.20, category = category)
    test_product.save()
    response = client.post(path=sales_url, data={
                                                    "data": "2023-01-18",
                                                    "quantity": "1.00",
                                                    "payment": "Debit Card",
                                                    "product": 1,
                                                    },  content_type='application/json')
    response_content = json.loads(response.content)
    assert response.status_code == 201
    assert response_content.get("data") ==  "2023-01-18"
    assert response_content.get("payment") == "Debit Card"
    assert float(response_content.get("quantity")) == 1

def test_add_sale_without_stock_should_fail(client) -> None:
    category = Category.objects.create(name="CategoryTest")
    test_product = Product.objects.create(name="ProductTest", description='description', stock=2, price=12.20, category = category)
    test_product.save()
    response = client.post(path=sales_url, data={
                                                    "data": "2023-01-18",
                                                    "quantity": "3.00",
                                                    "payment": "Debit Card",
                                                    "product": 1,
                                                    },  content_type='application/json')
    response_content = json.loads(response.content)
    assert response.status_code == 400
    assert json.loads(response.content) == {'message': "Cannot buy '3.00'  of 'ProductTest' because we just have 2 on stock"}