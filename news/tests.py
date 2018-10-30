from django.test import TestCase
from .models import Editor, Article,Tags

class EditorTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.sly = Editor(first_name='sly', last_name='keller', email='muthonkel@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.sly, Editor))

    def test_save_method(self):
        self.sly.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
