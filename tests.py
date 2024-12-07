# real_estate/tests.py
from django.test import TestCase
from .models import Property, Solicitor

class PropertyTestCase(TestCase):
    def setUp(self):
        Property.objects.create(
            title="Luxury Villa",
            description="Beautiful beachfront property",
            price=1000000.00,
            location="Malibu",
            category="Platinum"
        )

    def test_property_creation(self):
        property = Property.objects.get(title="Luxury Villa")
        self.assertEqual(property.location, "Malibu")
        self.assertEqual(property.category, "Platinum")

class SolicitorTestCase(TestCase):
    def setUp(self):
        Solicitor.objects.create(
            name="John Doe",
            state="California",
            years_of_experience=10,
            verified=True
        )

    def test_solicitor_creation(self):
        solicitor = Solicitor.objects.get(name="John Doe")
        self.assertTrue(solicitor.verified)
        self.assertEqual(solicitor.state, "California")
