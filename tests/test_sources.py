import unittest
from app.models import Sources

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('technews','tech-news','tech-news.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))