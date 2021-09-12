import unittest
from app.models import Articles

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('realnews','real-news','John Doe','Man Bites Dog','Unsuspecting dog bitten by rabid man', 'news.com', 'newsimage.com', '2020-08-01')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))