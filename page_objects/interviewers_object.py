"""
This class models the form on the Selenium tutorial page
The form consists of some input fields, a dropdown, a checkbox and a button
"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Interviewers_Object:
    "Page object for the Form"
    
    #locators
    add_interviewers_button = locators.add_interviewers_button
    interviewers_name = locators.interviewers_name
    interviewers_email = locators.interviewers_email
    interviewers_designation = locators.interviewers_designation
    interviewers_starttime = locators.interviewers_starttime
    interviewers_endtime = locators.interviewers_endtime
    add_time_button = locators.add_time_button
    save_interviewers_button = locators.save_interviewers_button
    cancel_interviewers_button = locators.cancel_interviewers_button


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def add_inter(self):
        "Click on 'Add Interviewers' button"
        result_flag = self.click_element(self.add_interviewers_button)
        self.conditional_write(result_flag,
            positive='Clicked on the "Add Interviewers" button',
            negative='Failed to click on "Add Interviewers" button',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_name(self,interviewers_name):
        "Set the name on the form"
        result_flag = self.set_text(self.interviewers_name,interviewers_name)
        self.conditional_write(result_flag,
            positive='Set the name to: %s'% interviewers_name,
            negative='Failed to set the name in the form',
            level='debug')

        return result_flag 

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_email(self,interviewers_email):
        "Set the name on the form"
        result_flag = self.set_text(self.interviewers_email,interviewers_email)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'% interviewers_email,
            negative='Failed to set the email in the form',
            level='debug')

        return result_flag 

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_designation(self,interviewers_designation):
        "Set the name on the form"
        result_flag = self.set_text(self.interviewers_designation,interviewers_designation)
        self.conditional_write(result_flag,
            positive='Set the designation to: %s'% interviewers_designation,
            negative='Failed to set the designation in the form',
            level='debug')

        return result_flag 

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_starttime(self,interviewers_starttime):
        "Set the name on the form"
        result_flag = self.set_text(self.interviewers_starttime,interviewers_starttime)
        self.conditional_write(result_flag,
            positive='Set the start time to: %s'% interviewers_starttime,
            negative='Failed to set the start time in the form',
            level='debug')

        return result_flag 

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_endtime(self,interviewers_endtime):
        "Set the name on the form"
        result_flag = self.set_text(self.interviewers_endtime,interviewers_endtime)
        self.conditional_write(result_flag,
            positive='Set the end time to: %s'% interviewers_endtime,
            negative='Failed to set the end time in the form',
            level='debug')

        return result_flag 

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def add_time(self):
        "Click on 'Add Interviewers' button"
        result_flag = self.click_element(self.add_time_button)
        self.conditional_write(result_flag,
            positive='Clicked on the "Add time" button',
            negative='Failed to click on "Add time" button',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def save(self):
        "Click on 'Add Interviewers' button"
        result_flag = self.click_element(self.save_interviewers_button)
        self.conditional_write(result_flag,
            positive='Clicked on the "Save Interviewers" button',
            negative='Failed to click on "Save Interviewers" button',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def cancel(self):
        "Click on 'Add Interviewers' button"
        result_flag = self.click_element(self.cancel_interviewers_button)
        self.conditional_write(result_flag,
            positive='Clicked on the "Cancel Interviewers" button',
            negative='Failed to click on "Cancel Interviewers" button',
            level='debug')

        return result_flag

    
    '''
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_user(self,username):
        "Set the name on the form"
        result_flag = self.set_text(self.username_field,username)
        self.conditional_write(result_flag,
            positive='Set the name to: %s'% username,
            negative='Failed to set the name in the form',
            level='debug')

        return result_flag 


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_password(self,password):
        "Set the email on the form"
        result_flag = self.set_text(self.password_field,password)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'%password,
            negative='Failed to set the email in the form',
            level='debug')

        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def login(self):
        "Click on 'Login' button"
        result_flag = self.click_element(self.login_button)
        self.conditional_write(result_flag,
            positive='Clicked on the "Login" button',
            negative='Failed to click on "Login" button',
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
    '''