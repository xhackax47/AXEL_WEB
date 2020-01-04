from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from WebAXEL.models import Document, DataSet


class DocumentTestCase(TestCase):

    def setUp(self):
        self.document = Document.objects.create(titre="DocumentTest", date_ajout=timezone.now(), auteur="AuteurTest",
                                                description="DescriptionTest", document=None)

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


class DataSetTestCase(TestCase):

    def setUp(self):
        self.dataset = DataSet.objects.create(nom="DatasetTest", date_ajout=timezone.now(),
                                              description="DescriptionTest", dataset=None)

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
