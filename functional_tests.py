from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith hears about new to-do list and goes to visit
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail("Finish the test!")








		# She is invited to enter a to-do item right away

		# She types "Buy peacock feathers" into a text box

		# When she hits enter, the page updates.
		# "1: Buy peacock feathers" is added to the list

		# There is still a text box inviting another item

		# The page updates again to show two items on list

		# The site generates an unique url for her with some explaination

		# She visits the custom url and her list is there

		# The end

if __name__ == "__main__":
	unittest.main(warnings='ignore')