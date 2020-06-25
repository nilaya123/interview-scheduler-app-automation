"""
This class models the form on the Selenium tutorial page
The form consists of some input fields, a dropdown, a checkbox and a button
"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Jobs_Object:
    "Page object for the Form"
    
    #locators
    add_jobs_button = locators.add_jobs_button
    job_role = locators.job_role
    job_interviewers = locators.job_interviewers
    submit_job_button = locators.submit_job_button


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def add_jobs(self):
        "Click on 'Add Jobs' button"
        result_flag = self.click_element(self.add_jobs_button)
        self.conditional_write(result_flag,
            positive='Clicked on the "Add Jobs" button',
            negative='Failed to click on "Add Jobs" button',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_job_role(self,job_role):
        "Set the name on the form"
        result_flag = self.set_text(self.job_role,job_role)
        self.conditional_write(result_flag,
            positive='Set the job role to: %s'% job_role,
            negative='Failed to set the job role',
            level='debug')

        return result_flag 

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_job_interviewer(self,job_interviewers):
        "Set the name on the form"
        result_flag = self.set_text(self.job_interviewers,job_interviewers)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'% job_interviewers,
            negative='Failed to set the interviewers',
            level='debug')

        return result_flag 

    

    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def submit_job(self):
        "Click on Submit button"
        result_flag = self.click_element(self.submit_job_button)
        self.conditional_write(result_flag,
            positive='Clicked on the "Submit Job" button',
            negative='Failed to click on "Submit Job" button',
            level='debug')
        result_flag = self.alert_accept()

        return result_flag

   