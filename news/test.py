from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

class EditorTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.james=Editor(first_name ='James', last_name ='Muriuki', email ='james@muriuki.com')
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))
        #self.james.save_editor()


    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)


    def test_delete_method(self):
        self.james.save_editor()
        self.james.delete_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)


    def test_display_method(self):
        self.james.save_editor()
        editors = Editor.objects.filter(first_name ='James')
        self.assertTrue(len(editors)>0)

    def test_update_method(self):
        self.james.save_editor()
        Editor.objects.filter( id = 1 ).update(first_name ='James Smart')
        self.assertTrue(self.james.first_name,'James Smart')

    
# Creating a new tag and saving it
class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()


    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
