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

email_on_link = login.email_on_link
password_link = login.password_link

class Interview_Schedule_Object:
    "Page Object for Scheduling an interview"

    #locators
    select_url = locators.select_url
    select_unique_code = locators.select_unique_code
    select_candidate_email = locators.select_candidate_email
    go_for_schedule = locators.go_for_schedule
    date_picker = locators.date_picker
    confirm_interview_date = locators.confirm_interview_date
    select_free_slot = locators.select_free_slot
    schedule_my_interview = locators.schedule_my_interview
    date_on_calendar = locators.date_on_calendar
    calendar_link = locators.calendar_link
    google_meet_link = locators.google_meet_link
    email_on_link = locators.email_on_link
    next_button = locators.next_button
    next_button_after_password = locators.next_button_after_password
    password_link = locators.password_link

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
        self.wait(30)
        if result_flag is True:
            result_flag = email_obj.select_folder('Inbox')
            self.conditional_write(result_flag,
                                   positive='Selected the folder Inbox',
                                   negative='Could not select the folder Inbox')
        uid = email_obj.get_latest_email_uid(
                    subject="Invitation to schedule an Interview with Qxf2 Services!", sender='careers@qxf2.com',wait_time=20)
        email_body = email_obj.fetch_email_body(uid)
        soup = BeautifulSoup(''.join(email_body), 'html.parser')
        unique_code = soup.b.text
        url = soup.a.get('href')


        result_flag = self.open_url_new_tab(url)
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

        N_DAYS_After = 7

        date = datetime.now()
        date = date + timedelta(days=N_DAYS_After)
        date = date.day

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

        self.wait(5)

        result_flag = self.scroll_down(self.confirm_interview_date)
        self.conditional_write(result_flag,
            positive='Scrolling down the page till Schedule my interview option',
            negative='Failed to scroll down the page till schedule my interview option',
            level='debug')

        result_flag = self.click_element(self.select_free_slot)
        self.conditional_write(result_flag,
            positive='Selected free interview slot',
            negative='Failed to select free interview slot',
            level='debug')

        result_flag = self.click_element(self.schedule_my_interview)
        self.conditional_write(result_flag,
            positive='Clicked on schedule my interview',
            negative='Failed to click on schedule my interview',
            level='debug')

        self.wait(5)

        result_flag = self.click_element(self.calendar_link)
        self.conditional_write(result_flag,
            positive='Clicked on calendar link',
            negative='Failed to click on calendar link',
            level='debug')

        self.wait(2)

        self.switch_window()

        result_flag = self.set_text(self.email_on_link,email_on_link)
        self.conditional_write(result_flag,
            positive='Set email to: %s'% email_on_link,
            negative='Failed to set the email',
            level='debug')

        result_flag = self.click_element(self.next_button)
        self.conditional_write(result_flag,
            positive='Clicked on Next',
            negative='Failed to click on Next',
            level='debug')

        self.wait(5)
        result_flag = self.set_text(self.password_link,password_link)
        self.conditional_write(result_flag,
            positive='Set password to: %s'% password_link,
            negative='Failed to set the password',
            level='debug')

        result_flag = self.click_element(self.next_button_after_password)
        self.conditional_write(result_flag,
            positive='Clicked on Next',
            negative='Failed to click on Next',
            level='debug')

        result_flag = self.click_element(self.google_meet_link)
        self.conditional_write(result_flag,
            positive='Clicked on Google meet link',
            negative='Failed to click on Google meet link',
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
