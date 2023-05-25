from rest_framework import serializers

from apps.reports import models


class ReportsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Reports
        fields = '__all__'
