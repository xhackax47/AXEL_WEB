from rest_framework import serializers

from WebAXEL.models import Document, DataSet, Robot


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        exclude = ('categories_document',)


class DataSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataSet
        exclude = ('categories_dataset',)


class RobotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Robot
        exclude = ('categories_robot',)
