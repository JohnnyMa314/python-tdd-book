from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def test_start_list_retrieve_later(self):
        # Angela visits my new to-do list site:
        self.browser.get('http://localhost:8000')
        
        # Angela is invited to enter in a to-do list
        self.assertIn('To-Do', self.browser.title)
        self.fail("failed")

        # Angela types in "buy milk" as her to-do

        # Angela hits enter, and "1: buy milk" is displayed

        # A check box is also displayed next to the text

        # The text box remains, and asks her to add another item

        # After Angela enters another item, the page updates to show both this and the previous TO DO:

        # The site generates a unique URL when each item is entered

        # The unique site maintains the to-do list entered in

        # Angela is done with the site and leaves it.

if __name__=='__main__':
    unittest.main()
