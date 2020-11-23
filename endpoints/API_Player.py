"""
API_Player class does the following:
a) serves as an interface between the test and API_Interface
b) contains several useful wrappers around commonly used combination of actions
c) maintains the test context/state
"""
import json
from base64 import b64encode
from .API_Interface import API_Interface
from utils.results import Results
import urllib.parse
import logging
from bs4 import BeautifulSoup
from conf import api_example_conf as conf


class API_Player(Results):
    "The class that maintains the test context/state"

    def __init__(self, url, log_file_path=None, session_flag=True):
        "Constructor"
        super(API_Player, self).__init__(
            level=logging.DEBUG, log_file_path=log_file_path)
        self.api_obj = API_Interface(url=url, session_flag=session_flag)


    def set_login_details(self, username, password):
        "encode auth details"
        user = username
        password = password
        login_data={'username': user,'password':password}
        return login_data


    def login_app(self,login_data):
        "login to app"
        response = self.api_obj.login_app_is(data=login_data)
        result_flag = True if response['response'] == 200 else False

        return result_flag


    def get_jobs(self):
        "get available jobs"
        response = self.api_obj.get_jobs_is()
        result_flag = True if response['response'] == 200 else False
        ses = response['response_content']
        soup = BeautifulSoup(ses)
        My_table = soup.find('table',{'class':'table table-striped'})
        table_rows = My_table.find_all('tr')
        list_1=[]
        for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text for i in td]
            list_1.append(row)
        list_1.pop(0)
        list_2 = []
        for val in list_1:
            list_2.append(val[1])
        list_2 = [x.replace("\n","") for x in list_2]
        self.new_job_id = row[0]

        result_flag = True if response['response'] == 200 else False
        self.write(msg="Fetched jobs list:\n %s"%list_2)
        self.conditional_write(result_flag,
                               positive="Successfully fetched jobs",
                               negative="Could not fetch jobs")

        return result_flag


    def add_jobs(self,job_data):
        "add new job"
        response = self.api_obj.add_jobs_is(data=job_data)
        result_flag = True if response['response'] == 200 else False

        return result_flag


    def add_candidates(self,candidate_data):
        "add new candidate"
        response = self.api_obj.add_candidates_is(data=candidate_data)
        result_flag = True if response['response'] == 200 else False

        return result_flag


    def get_candidates(self):
        "get available candidates"
        response = self.api_obj.get_candidates_is()
        result_flag = True if response['response'] == 200 else False
        ses = response['response_content']
        soup = BeautifulSoup(ses)
        My_table = soup.find('table',{'class':'table table-striped'})
        table_rows = My_table.find_all('tr')
        list_1=[]
        for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text for i in td]
            list_1.append(row)
        list_1.pop(0)
        list_2 = []
        for val in list_1:
            list_2.append(val[1])
        list_2 = [x.replace("\n","") for x in list_2]
        result_flag = True if response['response'] == 200 else False
        self.write(msg="Fetched candidates list:\n %s"%list_2)
        self.conditional_write(result_flag,
                               positive="Successfully fetched candidates",
                               negative="Could not fetch candidates")

        return result_flag

    def add_interviewers(self,interviewer_data):
        "add new interviewer"
        response = self.api_obj.add_interviewer_is(data=interviewer_data)
        result_flag = True if response['response'] == 200 else False

        return result_flag


    def get_interviewers(self):
        "get available interviewers"
        response = self.api_obj.get_interviewer_is()
        result_flag = True if response['response'] == 200 else False
        ses = response['response_content']
        soup = BeautifulSoup(ses)
        My_table = soup.find('table',{'class':'table table-striped'})
        table_rows = My_table.find_all('tr')
        list_1=[]
        for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text for i in td]
            list_1.append(row)
        list_1.pop(0)
        list_2 = []
        for val in list_1:
            list_2.append(val[1])
        list_2 = [x.replace("\n","") for x in list_2]
        result_flag = True if response['response'] == 200 else False
        self.write(msg="Fetched interviewers list:\n %s"%list_2)
        self.conditional_write(result_flag,
                               positive="Successfully fetched interviewers",
                               negative="Could not fetch interviewers")

        return result_flag


    def delete_jobs(self):
        "delete job"
        response = self.api_obj.get_jobs_is()
        result_flag = True if response['response'] == 200 else False
        ses = response['response_content']
        soup = BeautifulSoup(ses)
        My_table = soup.find('table',{'class':'table table-striped'})
        table_rows = My_table.find_all('tr')
        for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text for i in td]
        self.new_job_id = row[0]
        response = self.api_obj.delete_jobs_is(data={'job-id': self.new_job_id})
        result_flag = True if response['response'] == 200 else False

        return result_flag


    def delete_candidates(self):
        "delete candidate"
        response = self.api_obj.get_candidates_is()
        result_flag = True if response['response'] == 200 else False
        ses = response['response_content']
        soup = BeautifulSoup(ses)
        My_table = soup.find('table',{'class':'table table-striped'})
        table_rows = My_table.find_all('tr')
        for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text for i in td]
        self.new_job_id
        self.new_candidate_id =row[0]
        response = self.api_obj.delete_candidates_is(candidate_id = self.new_candidate_id,data = {'candidateId':self.new_candidate_id,'jobId':self.new_job_id})
        result_flag = True if response['response'] == 200 else False

        return result_flag


    def delete_interviewers(self):
        "delete interviewers"
        response = self.api_obj.get_interviewer_is()
        result_flag = True if response['response'] == 200 else False
        ses = response['response_content']
        soup = BeautifulSoup(ses)
        My_table = soup.find('table',{'class':'table table-striped'})
        table_rows = My_table.find_all('tr')
        for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text for i in td]
        self.new_interviewer_id = row[0]
        data = {'interviewer-id':self.new_interviewer_id}
        response = self.api_obj.delete_interviewers_is(interviewer_id = self.new_interviewer_id,data = {'interviewer-id':self.new_interviewer_id})
        result_flag = True if response['response'] == 200 else False

        return result_flag
