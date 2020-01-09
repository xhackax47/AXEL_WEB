from rest_framework.serializers import HyperlinkedRelatedField, ModelSerializer

from WebAXEL.models import Document, DataSet, Robot


class DocumentSerializer(ModelSerializer):

    class Meta:
        model = Document
        exclude = ('categories_document',)


class DataSetSerializer(ModelSerializer):

    class Meta:
        model = DataSet
        exclude = ('categories_dataset',)


class RobotSerializer(ModelSerializer):

    class Meta:
        model = Robot
        exclude = ('categories_robot',)
