"""
This class models the form on the Selenium tutorial page
The form consists of some input fields, a dropdown, a checkbox and a button
"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Candidates_Object:
    "Page object for the Candidates"
    
    #locators
    add_candidates_button = locators.add_candidates_button
    name_candidates = locators.name_candidates
    email_candidates = locators.email_candidates
    job_applied = locators.job_applied
    comment_candidates = locators.comment_candidates
    submit_candidates_button = locators.submit_candidates_button   


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def add_candidates(self):
        "Click on Add Candidates button"
        result_flag = self.click_element(self.add_candidates_button)
        self.conditional_write(result_flag,
            positive='Clicked on the Add Candidates button',
            negative='Failed to click on Add Candidates button',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def add_name(self,name_candidates):
        "Set the name for candidate"
        result_flag = self.set_text(self.name_candidates,name_candidates)
        self.conditional_write(result_flag,
            positive='Set the  candidates name to: %s'% name_candidates,
            negative='Failed to set the name',
            level='debug')

        return result_flag 


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def add_email(self,email_candidates):
        "Set the email for the candidate"
        result_flag = self.set_text(self.email_candidates,email_candidates)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'%email_candidates,
            negative='Failed to set the email in the form',
            level='debug')

        return result_flag

    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def add_job_applied(self,job_applied):
        "Set the email on the form"
        result_flag = self.set_text(self.job_applied,job_applied)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'%job_applied,
            negative='Failed to set the email in the form',
            level='debug')

        return result_flag
    

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def add_comments(self,comment_candidates):
        "Set the email on the form"
        result_flag = self.set_text(self.comment_candidates,comment_candidates)
        self.conditional_write(result_flag,
            positive='Set the comments to: %s'%comment_candidates,
            negative='Failed to set comments',
            level='debug')

        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def submit(self):
        "Click on 'Submit' button"
        result_flag = self.click_element(self.submit_candidates_button)
        self.conditional_write(result_flag,
            positive='Clicked on the Submit button',
            negative='Failed to click on Submit button',
            level='debug')
        result_flag = self.alert_accept()

        return result_flag

    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def alert_accept(self):
        "Click on 'Ok' alert"
        result_flag = self.alert_window()
        return result_flag
        self.conditional_write(result_flag,
            positive='Clicked on the OK',
            negative='Failed to click on OK',
            level='debug')

        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def accept_terms(self):
        "Accept the terms and conditions"
        result_flag = self.select_checkbox(self.tac_checkbox)
        self.conditional_write(result_flag,
            positive='Accepted the terms and conditions',
            negative='Failed to accept the terms and conditions',
            level='debug')
            
        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_redirect(self):
        "Check if we have been redirected to the redirect page"
        result_flag = False
        if self.redirect_title in self.driver.title:
            result_flag = True
            self.switch_page("redirect")
        
        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def submit_form(self,username,password):
        "Submit the form"
        result_flag = self.set_user(username)
        result_flag &= self.set_password(password)
        result_flag &= self.accept_terms()
        result_flag &= self.login()
        result_flag &= self.check_redirect()

        return result_flag


