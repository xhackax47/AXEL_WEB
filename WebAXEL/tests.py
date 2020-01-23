from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from WebAXEL.models import Document, DataSet, Robot


# Tests CRUD du model Document
class DocumentTestCase(TestCase):

    # Init données de tests
    def setUp(self):
        self.document = Document.objects.create(titre="DocumentTest", date_ajout=timezone.now(), auteur="AuteurTest",
                                                description="DescriptionTest", document=None, nb_vues=0)

    # Test de lecture objet Document
    def testRead(self):
        titre = self.document.titre
        self.assertEqual(titre, "DocumentTest")

    # Test de création objet Document
    def testCreate(self):
        self.assertIsInstance(self.document, Document)

    # Test de mise à jour objet Document
    def testUpdate(self):
        self.document.save()
        reponse = self.client.post(
            reverse('edit-document', kwargs={'pk': self.document.pk}),
            {'titre': 'TitreModifié', 'author': 'AuteurModifié'})
        self.assertEqual(reponse.status_code, 302)

    # Test de suppression objet Document
    def testDelete(self):
        self.document.save()
        reponse = self.client.post(reverse('delete-document', kwargs={'pk': self.document.pk}))
        self.assertEqual(reponse.status_code, 302)


# Tests CRUD du model Dataset
class DataSetTestCase(TestCase):

    # Init données de tests
    def setUp(self):
        self.dataset = DataSet.objects.create(nom="DatasetTest", date_ajout=timezone.now(),
                                              description="DescriptionTest", dataset=None, nb_vues=0)

    # Test de lecture objet Dataset
    def testRead(self):
        nom = self.dataset.nom
        self.assertEqual(nom, "DatasetTest")

    # Test de création objet Dataset
    def testCreate(self):
        self.assertIsInstance(self.dataset, DataSet)

    # Test de mise à jour objet Dataset
    def testUpdate(self):
        self.dataset.save()
        reponse = self.client.post(
            reverse('edit-dataset', kwargs={'pk': self.dataset.pk}),
            {'nom': 'NomModifié', 'description': 'DescriptionModifiée'})
        self.assertEqual(reponse.status_code, 302)

    # Test de suppression objet Dataset
    def testDelete(self):
        self.dataset.save()
        reponse = self.client.post(reverse('delete-dataset', kwargs={'pk': self.dataset.pk}))
        self.assertEqual(reponse.status_code, 302)


# Tests CRUD du model Robot
class RobotTestCase(TestCase):

    # Init données de tests
    def setUp(self):
        self.robot = Robot.objects.create(nom="RobotTest", date_ajout=timezone.now(),
                                          description="DescriptionTest", doc=None, nb_vues=0)

    # Test de lecture objet Robot
    def testRead(self):
        nom = self.robot.nom
        self.assertEqual(nom, "RobotTest")

    # Test de création objet Robot
    def testCreate(self):
        self.assertIsInstance(self.robot, Robot)

    # Test de mise à jour objet Robot
    def testUpdate(self):
        self.robot.save()
        reponse = self.client.post(
            reverse('edit-robot', kwargs={'pk': self.robot.pk}),
            {'nom': 'NomModifié', 'description': 'DescriptionModifiée'})
        self.assertEqual(reponse.status_code, 302)

    # Test de suppression objet Robot
    def testDelete(self):
        self.robot.save()
        reponse = self.client.post(reverse('delete-robot', kwargs={'pk': self.robot.pk}))
        self.assertEqual(reponse.status_code, 302)
