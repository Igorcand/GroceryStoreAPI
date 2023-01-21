import json
import pytest
from django.urls import reverse

from apps.reports.models import Reports
from apps.sales.models import Sale
from apps.products.models import Product, Category


# set DJANGO_SETTINGS_MODULE=project.settings

reports_url = reverse("reports")
# sales_url = reverse("sales_url")


pytestmark = pytest.mark.django_db

# --------------------- Test Get Reports -----------------------


def test_zero_report_should_return_empty_list(client) -> None:
    response = client.get(reports_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


def test_one_report_exists_should_succeed(client) -> None:
    report = Reports(
        product="Product",
        category="Category",
        quantity_itens=2,
        stock=45,
        sale=45.70,
        payment="Money",
        data="2023-01-18",
    )
    report.save()
    response = client.get(reports_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert report.data in response_content.get("data")
    assert response_content.get("category") == report.category
    assert int(response_content.get("quantity_itens")) == report.quantity_itens
    assert response_content.get("payment") == report.payment
    assert float(response_content.get("stock")) == report.stock
    assert float(response_content.get("sale")) == report.sale


# --------------------- Test Post Reports -----------------------


def test_create_reports_without_argumets_should_fail(client) -> None:
    response = client.post(path=reports_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "detail": "JSON parse error - Expecting value: line 1 column 1 (char 0)"
    }


def test_create_reports_with_argumets_empty_should_fail(client) -> None:
    response = client.post(path=reports_url, data={}, content_type="application/json")
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "message": "You need to pass even 'data' value to do a filter on database"
    }


def test_filtring_report_should_succeed(client) -> None:
    report1 = Reports(
        product="Product1",
        category="Category1",
        quantity_itens=2,
        stock=45,
        sale=45.70,
        payment="Money",
        data="2023-01-18",
    )
    report1.save()
    report2 = Reports(
        product="Product2",
        category="Category2",
        quantity_itens=3,
        stock=45,
        sale=45.70,
        payment="Credit Card",
        data="2023-01-18",
    )
    report2.save()
    response = client.post(
        path=reports_url, data={"data": "2023-01-18"}, content_type="application/json"
    )
    response_content = json.loads(response.content)
    data = response_content["data"]
    assert response.status_code == 201
    assert data["total_items"] == report1.quantity_itens + report2.quantity_itens
    assert data["total_value"] == report1.sale + report2.sale
    assert len(response_content["description"]) == 2
