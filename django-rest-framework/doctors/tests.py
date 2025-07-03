from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from patients.models import Patient
from doctors.models import Doctor

class DoctorViewSetTests(TestCase):

    def setUp(self) -> None:
        self.patient = Patient.objects.create(
            first_name='Karina',
            last_name='Samaniego',
            date_of_birth='1998-11-06',
            contact_number='6984-2398',
            email='karina.samaniego@gmail.com',
            address='Los Santos',
            medical_history='Alergias',
        )
        self.doctor = Doctor.objects.create(
            first_name='Julian',
            last_name='Zurita',
            qualification='Especialista en Pediatria',
            contact_number='6245-3856',
            email='julian.zurita@saludfuturo.gmail.com',
            address='Veraguas',
            biography='Cuenta con más de 15 años de experiencia',
            is_on_vacation=False,
        )   
        self.client = APIClient()

    def test_list_should_return_200(self):
        url = reverse(
            'doctor-appointments', 
            kwargs={"pk": self.doctor.id},
        ) 
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
