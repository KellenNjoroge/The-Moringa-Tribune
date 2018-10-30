from django.test import TestCase
from .models import Editors, Article,Tags

class EditorsTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.james = Editors(first_name='Sly', last_name='keller', email='muthonkel@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.james, Editors))
