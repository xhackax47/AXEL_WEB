from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from WebAXEL.models import Robot, Document, DataSet
from api.serializers import RobotSerializer, DocumentSerializer, DataSetSerializer


# DOCUMENTS

# Vue DocumentListView qui renvoi la liste des documents en JSON
class DocumentListView(ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


# Vue DocumentListViewSet qui renvoi la liste des documents en JSON dans un viewset
class DocumentListViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


# Vue DocumentDetailViewSet qui renvoi le détail d'un document en JSON
class DocumentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


# DATASETS

# Vue DataSetListView qui renvoi la liste des datasets en JSON
class DataSetListView(ListCreateAPIView):
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer


# Vue DataSetListViewSet qui renvoi la liste des datasets en JSON dans un viewset
class DataSetListViewSet(ModelViewSet):
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer


# Vue DataSetDetailViewSet qui renvoi le détail d'un dataset en JSON
class DataSetDetailView(RetrieveUpdateDestroyAPIView):
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer


# ROBOTS

# Vue RobotListView qui renvoi la liste des robots en JSON
class RobotListView(ListCreateAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


# Vue RobotListViewSet qui renvoi la liste des robots en JSON dans un viewset
class RobotListViewSet(ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


# Vue RobotDetailViewSet qui renvoi le détail d'un robot en JSON
class RobotDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
