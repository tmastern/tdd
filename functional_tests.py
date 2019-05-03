from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# She is invited to enter a to-do item straght away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# She types her item into a text box
		inputbox.send_keys('Buy peacock feathers')

		# When she hits enter, the page updates with new item
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

		# There is still a box inviting enter next item
		self.fail('Finish the Test!')

		# The page updates again and shows both items 








		# The page updates again to show two items on list

		# The site generates an unique url for her with some explaination

		# She visits the custom url and her list is there

		# The end

if __name__ == "__main__":
	unittest.main(warnings='ignore')