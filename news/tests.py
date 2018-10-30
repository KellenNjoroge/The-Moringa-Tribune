from django.test import TestCase

from .models import Editor, Article, Tags
import datetime as dt


class EditorTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.sly = Editor(first_name='sly', last_name='keller', email='muthonkel@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.sly, Editor))

    def test_save_method(self):
        self.sly.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)


class ArticleTestClass(TestCase):
    def setUp(self):

        self.sly = Editor(first_name='sly', last_name='keller', email='muthonkel@gmail.com')
        self.sly.save_editor()

        # creating new tags and saving it
        self.new_tag = Tags(name= 'testing')
        self.new_tag.save()

        self.new_article = Article( title= "Test Artcle", post= 'random post', editor=self.sly )
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        Tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        test_date = '2018-10-30'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)

        self.assertTrue(len(news_by_date)>0)
