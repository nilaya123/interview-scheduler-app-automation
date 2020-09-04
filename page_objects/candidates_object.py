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
import conf.login_conf as login
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime, timedelta


#Fetching conf details from the conf file
imap_host = conf_file.imaphost
username = conf_file.username
password = conf_file.app_password
email = login.email_candidates
date_picker = login.date_picker
date_check = login.date_check
free_slot = login.free_slot


class Candidates_Object:
    "Page object for the Candidates"

    #locators
    add_candidates_button = locators.add_candidates_button
    name_candidates = locators.name_candidates
    email_candidates = locators.email_candidates
    job_applied = locators.job_applied
    job_applied_select = locators.job_applied_select
    comment_candidates = locators.comment_candidates
    submit_candidates_button = locators.submit_candidates_button
    delete_candidates_button = locators.delete_candidates_button
    remove_candidates_button = locators.remove_candidates_button
    select_candidate_button = locators.select_candidate_button
    search_option_candidate = locators.search_option
    thumbs_up_button = locators.thumbs_up_button
    thumbs_down_button = locators.thumbs_down_button
    select_round_level_scroll = locators.select_round_level_scroll
    send_email_button = locators.send_email_button
    select_url = locators.select_url
    select_unique_code = locators.select_unique_code
    select_candidate_email = locators.select_candidate_email
    go_for_schedule = locators.go_for_schedule
    date_picker = locators.date_picker
    confirm_interview_date = locators.confirm_interview_date
    select_free_slot = locators.select_free_slot
    schedule_my_interview = locators.schedule_my_interview
    date_on_calendar = locators.date_on_calendar


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
    def add_job_applied(self,job_applied_select,wait_seconds=1):
        "Set the email on the form"
        result_flag = self.click_element(self.job_applied)
        self.wait(wait_seconds)
        result_flag = self.click_element(self.job_applied_select%job_applied_select)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'%job_applied_select,
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
    def search_candidate(self,search_option_candidate):
        "Click on 'Search' button"
        result_flag = self.set_text(self.search_option_candidate,search_option_candidate)
        self.conditional_write(result_flag,
            positive='Search for Candidate name: %s'%search_option_candidate,
            negative='Failed to Search for Candidate name',
            level='debug')

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
    def fetch_email_invite(self):
        "Get email contents and fetch URL and unique code"
        imap_host = conf_file.imaphost
        username = conf_file.username
        password = conf_file.app_password

        time_elapsed = 0
        unique_code = 0
        email_obj = Email_Util()

        #Connect to the IMAP host
        email_obj.connect(imap_host)
        result_flag = email_obj.login(username, password)
        self.conditional_write(result_flag,
                               positive='Logged into %s' % imap_host,
                               negative='Could not log into %s to fetch the activation email' % imap_host)
        if result_flag is True:
            result_flag = email_obj.select_folder('Inbox')
            self.conditional_write(result_flag,
                                   positive='Selected the folder Inbox',
                                   negative='Could not select the folder Inbox')
        uid = email_obj.get_latest_email_uid(
                    subject="Invitation to schedule an Interview with Qxf2 Services!", sender='test@qxf2.com',wait_time=10)
        email_body = email_obj.fetch_email_body(uid)
        soup = BeautifulSoup(''.join(email_body), 'html.parser')
        unique_code = soup.b.text
        url = soup.a.get('href')


        result_flag = self.open_url_new_tab(url,wait_time=1)
        self.conditional_write(result_flag,
            positive='Opened the new tab with link',
            negative='Failed to open the new tab with link',
            level='debug')


        result_flag = self.set_text(self.select_unique_code,unique_code)
        self.conditional_write(result_flag,
            positive='Set unique code  to: %s'% unique_code,
            negative='Failed to set the unique code',
            level='debug')


        result_flag = self.set_text(self.select_candidate_email,email)
        self.conditional_write(result_flag,
            positive='Set candidate email to: %s'% email,
            negative='Failed to set the email',
            level='debug')


        result_flag = self.click_element(self.go_for_schedule)
        self.conditional_write(result_flag,
            positive='Clicked on Scheduling interview button',
            negative='Failed to click on Scheduling interview button',
            level='debug')


        result_flag = self.click_element(self.date_picker)
        self.conditional_write(result_flag,
            positive='Get the date',
            negative='Failed to get the date',
            level='debug')
        '''
        now = datetime.datetime.now()
        date = now.day
        date = date + 7
        '''
        N_DAYS_After = 7

        date = datetime.now()
        date = date + timedelta(days=N_DAYS_After)
        date = date.day
        print(date)

        result_flag = self.click_element(self.date_on_calendar%date)
        self.conditional_write(result_flag,
                positive='Set the date',
                negative='Failed to set the date',
                level='debug')


        result_flag = self.click_element(self.confirm_interview_date)
        self.conditional_write(result_flag,
            positive='Clicked on confirming interview date',
            negative='Failed to click on confirming interview date',
            level='debug')

        #time_slot = self.get_dom_text
        result_flag = self.click_element(self.select_free_slot)
        self.conditional_write(result_flag,
            positive='Selected free interview slot',
            negative='Failed to select free interview slot',
            level='debug')

        self.wait(10)
        result_flag = self.click_element(self.schedule_my_interview)
        self.conditional_write(result_flag,
            positive='Clicked on schedule my interview',
            negative='Failed to click on schedule my interview',
            level='debug')


        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_on_invite(self):
        "Copy URL"
        url = "60/1/eyJhbGciOiJIUzUxMiIsImlhdCI6MTU5NTQ4NjcwOCwiZXhwIjoxNTk2MDkxNTA4fQ.eyJjYW5kaWRhdGVfaWQiOiI2MCIsImpvYl9pZCI6IjEifQ.lpfFAZhZygidrssijed3qWRRJAuVIiU9Pqpa2h0ZI3BRXmn529rKE8tvpCdxcEpXoe2pkySYU1GNzgrviHsriQ/welcome"
        result_flag = self.open(url,wait_time=1)
        self.conditional_write(result_flag,
            positive='OPened the new tab with link',
            negative='Failed to open the new tab with link',
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
