"""
This class models the form on the Selenium tutorial page
The form consists of some input fields, a dropdown, a checkbox and a button
"""
import os,sys,time,imaplib,email,datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
from utils.email_util import Email_Util
import conf.email_conf as conf_file
import re

#Fetching conf details from the conf file
imap_host = conf_file.imaphost
username = conf_file.username
password = conf_file.app_password


class Candidates_Object:
    "Page object for the Candidates"
    
    #locators
    add_candidates_button = locators.add_candidates_button
    name_candidates = locators.name_candidates
    email_candidates = locators.email_candidates
    job_applied = locators.job_applied
    comment_candidates = locators.comment_candidates
    submit_candidates_button = locators.submit_candidates_button   
    delete_candidates_button = locators.delete_candidates_button
    remove_candidates_button = locators.remove_candidates_button
    select_candidate_button = locators.select_candidate_button
    thumbs_up_button = locators.thumbs_up_button
    thumbs_down_button = locators.thumbs_down_button
    select_round_level_scroll = locators.select_round_level_scroll
    send_email_button = locators.send_email_button
    select_url = locators.select_url

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
    def delete_candidates(self):
        "Click on Delete Candidates button"
        result_flag = self.click_element(self.delete_candidates_button)
        self.conditional_write(result_flag,
            positive='Clicked on the Delete Candidates button',
            negative='Failed to click on Delete Candidates button',
            level='debug')

        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def remove_candidates(self):
        "Click on Remove Candidates button"
        result_flag = self.click_element(self.remove_candidates_button)
        self.conditional_write(result_flag,
            positive='Clicked on the Delete Candidates button',
            negative='Failed to click on Delete Candidates button',
            level='debug')

        return result_flag

    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def select_candidates(self):
        "Click on Select Candidates button"
        result_flag = self.click_element(self.select_candidate_button)
        self.conditional_write(result_flag,
            positive='Clicked on the Select Candidates button',
            negative='Failed to click on Select Candidates button',
            level='debug')

        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def thumbs_up(self):
        "Click on thumbs up button"
        result_flag = self.click_element(self.thumbs_up_button)
        self.conditional_write(result_flag,
            positive='Clicked on the thumbs up button',
            negative='Failed to click on thumbs up button',
            level='debug')

        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def thumbs_down(self):
        "Click on thumbs up button"
        result_flag = self.click_element(self.thumbs_down_button)
        self.conditional_write(result_flag,
            positive='Clicked on the thumbs down button',
            negative='Failed to click on thumbs down button',
            level='debug')

        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def select_round(self,select_round_level):
        "Set the name for round"
        result_flag = self.set_text(self.select_round_level_scroll,select_round_level)
        self.conditional_write(result_flag,
            positive='Set the round to: %s'% select_round_level,
            negative='Failed to set the round',
            level='debug')

        return result_flag 

    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def send_email(self):
        "Click on send email button"
        result_flag = self.click_element(self.send_email_button)
        self.conditional_write(result_flag,
            positive='Clicked on the send eail button',
            negative='Failed to click on send email button',
            level='debug')

        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def copy_url(self):
        "Copy URL"
        result_flag = self.get_text(self.select_url)
        self.conditional_write(result_flag,
            positive='Copied the URL',
            negative='Failed to copy the URL',
            level='debug')

        return result_flag

   
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def get_url(self):
        #Fetching conf details from the conf file
        imap_host = conf_file.imaphost
        username = conf_file.username
        password = conf_file.app_password
        "Get email contents and fetch URL and unique code"
        email_obj = Email_Util()

        #Connect to the IMAP host
        email_obj.connect(imap_host)
    
        #Login
        if email_obj.login(username,password):
            print("PASS: Successfully logged in.")
        else:
            print("FAIL: Failed to login")
        '''
        #Get a list of folder
        folders = email_obj.get_folders() 
        if folders != None or []:
            print("PASS: Email folders:", email_obj.get_folders()) 

        else:
            print("FAIL: Didn't get folder details")
        '''
        #Select a folder
        if email_obj.select_folder('Inbox'):
            print("PASS: Successfully selected the folder: Inbox")
        else:
            print("FAIL: Failed to select the folder: Inbox")

        #Get the latest email's unique id
        uid = email_obj.get_latest_email_uid(subject = "Invitation to schedule an Interview with Qxf2 Services!",wait_time=300)
        if uid != None:
            print("PASS: Unique id of the latest email is: ",uid)
        else:
            print("FAIL: Didn't get unique id of latest email")
        '''
        #A. Look for an Email from provided sender, print uid and check it's contents
        uid = email_obj.get_latest_email_uid(sender="Qxf2 Services",wait_time=300)
        '''
        if uid != None:
            print("PASS: Unique id of the latest email with given sender is: ",uid)

            #Check the text of the latest email id
            email_body = email_obj.fetch_email_body(uid)
            
            print("nilaya")
            print(type(email_body))
            print(email_body)
            print(raw_email)
            link_pattern = re.compile('<a[^>]+href=\'(.*?)\'[^>]*>(.*)?</a>')
            unique_code = re.compile('<b>[a-z0-9]{8}')
            print("nilaya_waiting _for")
            link = link_pattern.findall(raw_email)
            u_code = unique_code.findall(raw_email)
            print(u_code)
            print(link)
            
            
            data_flag = False
            print("  - Automation checking mail contents")
            for line in email_body:
                line = line.replace('=','')
                line = line.replace('<','')
                line = line.replace('>','')

                if "Hi Email_Util" and "This email was sent to you" in line:
                    data_flag = True
                    break
            if data_flag == True:
                print("PASS: Automation provided correct Email details. Email contents matched with provided data.")
            else:
                print("FAIL: Provided data not matched with Email contents. Looks like automation provided incorrect Email details")

        else:
            print("FAIL: After wait of 5 mins, looks like there is no email present with given sender")

               
        result_flag = self.get_url(self.select_url)
        self.conditional_write(result_flag,
            positive='Copied the URL',
            negative='Failed to copy the URL',
            level='debug')

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


   


