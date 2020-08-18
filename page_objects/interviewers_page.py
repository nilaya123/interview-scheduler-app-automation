"""
This class models the main Selenium tutorial page.
URL: selenium-tutorial-main
The page consists of a header, footer, form and table objects
"""

from page_objects.Base_Page import Base_Page
from page_objects.form_object import Form_Object
from page_objects.index_object import Index_Object
from page_objects.candidates_object import Candidates_Object
from page_objects.interviewers_object import Interviewers_Object
from utils.Wrapit import Wrapit


class Interviewers_Page(Base_Page,Interviewers_Object):
    "Page Object for the tutorial's main page"
    
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = '/interviewers'
        self.open(url)