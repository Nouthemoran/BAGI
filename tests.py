from django.test import TestCase
from .models import sekolah
from django.core.exceptions import ObjectDoesNotExist
class SekolahTestCase(TestCase):
    def setUp(self):
        sekolah.objects.create(npsn="2026822X", nama="SMKN 1 Cimahi", status="Negeri")
    
    def test_sekolah_cek_nama(self):
        """ Cek nama sekolah """
        smkn1 = sekolah.objects.get(nama="SMKN 1 Cimahi")
        self.assertEqual(smkn1.nama, "SMKN 1 Cimahi")

    def test_update(self):
        # create an instance of the model
        instance = sekolah(nama='SMKN 1 Cimahi', status='negeri')
        instance.save()

        # update the instance
        instance.nama = 'SMKN 2 Cimahi'
        instance.save()

        # get the updated instance from the database
        updated_instance = sekolah.objects.get(id=instance.id)

        # assert that the values have been updated
        self.assertEqual(updated_instance.nama, 'SMKN 2 Cimahi')

    def test_read(self):
        # create an instance of the model
        instance = sekolah(nama='SMKN 1 Cimahi',)
        instance.save()

        # get the instance from the database
        retrieved_instance = sekolah.objects.get(id=instance.id)

        # assert that the values match
        self.assertEqual(retrieved_instance.nama, 'SMKN 1 Cimahi')

    def test_delete(self):
        # create an instance of the model
        instance = sekolah(nama='SMKN 1 Cimahi',)
        instance.save()

        # delete the instance
        instance.delete()

        # try to get the deleted instance from the database
        with self.assertRaises(ObjectDoesNotExist):
            sekolah.objects.get(id=instance.id)

    

    

        