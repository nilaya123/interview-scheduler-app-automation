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
#from utils.__init__ import get_dict_item
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
        table_rows
        for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text for i in td]
        self.new_job_id = row[0]
        result_flag = True if response['response'] == 200 else False
        self.write(msg="Fetched jobs list:\n %s"%str(row))
        self.conditional_write(result_flag,
                               positive="Successfully fetched jobs",
                               negative="Could not fetch jobs")

        return response


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
        table_rows
        for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text for i in td]
            print(row)
        print (row)
        print (row[0])
        print (row[1])
        print (row[2])
        print (row[3])
        print (row[4])
        print (row[5])

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
        table_rows
        for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text for i in td]

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

    '''
    def get_car(self, car_name, brand, auth_details=None):
        "gets a given car details"
        url_params = {'car_name': car_name, 'brand': brand}
        url_params_encoded = urllib.parse.urlencode(url_params)
        headers = self.set_header_details(auth_details)
        json_response = self.api_obj.get_car(url_params=url_params_encoded,
                                             headers=headers)
        response = json_response['response']
        result_flag = True if response['successful'] == True else False
        self.write(msg='Fetched car details of :%s %s' % (car_name, response))

        return result_flag


    def add_car(self, car_details, auth_details=None):
        "adds a new car"
        data = car_details
        headers = self.set_header_details(auth_details)
        json_response = self.api_obj.add_car(data=data,
                headers=headers)
        result_flag = True if json_response['response']['successful'] == True else False

        return result_flag


    def register_car(self, car_name, brand, auth_details=None):
        "register car"
        url_params = {'car_name': car_name, 'brand': brand}
        url_params_encoded = urllib.parse.urlencode(url_params)
        customer_details = conf.customer_details
        data = customer_details
        headers = self.set_header_details(auth_details)
        json_response = self.api_obj.register_car(url_params=url_params_encoded,
                                                  json=data,
                                                  headers=headers)
        response = (json_response['response'])
        result_flag = True if response['registered_car']['successful'] == True else False

        return result_flag


    def update_car(self, car_details, car_name='figo', auth_details=None):
        "updates a car"
        data = {'name': car_details['name'],
                'brand': car_details['brand'],
                'price_range': car_details['price_range'],
                'car_type': car_details['car_type']}

        headers = self.set_header_details(auth_details)
        json_response = self.api_obj.update_car(car_name,
                                                json=data,
                                                headers=headers)
        json_response = json_response['response']
        result_flag = True if json_response['response']['successful'] == True else False

        return result_flag


    def remove_car(self, car_name, auth_details=None):
        "deletes a car entry"
        headers = self.set_header_details(auth_details)
        json_response = self.api_obj.remove_car(car_name,
                                                headers=headers)
        result_flag = True if json_response['response']['successful'] == True else False

        return result_flag


    def get_registered_cars(self, auth_details=None):
        "gets registered cars"
        headers = self.set_header_details(auth_details)
        json_response = self.api_obj.get_registered_cars(headers=headers)
        response = json_response['response']
        result_flag = True if response['successful'] == True else False
        self.write(msg="Fetched registered cars list:\n %s"%str(json_response))
        self.conditional_write(result_flag,
                               positive='Successfully fetched registered cars list',
                               negative='Could not fetch registered cars list')

        return response



    def get_car_count(self,auth_details=None):
        "Verify car count at the start"
        self.write('\n*****Verifying car count******')
        car_count = self.get_cars(auth_details)
        car_count = len(car_count['cars_list'])

        return car_count


    def get_regi_car_count(self,auth_details=None):
        "Verify registered car count"
        car_count_registered = self.get_registered_cars(auth_details)
        car_count_registered = len(car_count_registered['registered'])

        return car_count_registered


    def verify_car_count(self, expected_count, auth_details=None):
        "Verify car count"
        self.write('\n*****Verifying car count******')
        car_count = self.get_cars(auth_details)
        car_count = len(car_count['cars_list'])
        result_flag = True if car_count == expected_count else False

        return result_flag


    def verify_registration_count(self, expected_count, auth_details=None):
        "Verify registered car count"
        self.write('\n******Verifying registered car count********')
        car_count = self.get_registered_cars(auth_details)
        car_count = len(car_count['registered'])
        result_flag = True if car_count == expected_count else False

        return result_flag


    def get_user_list(self, auth_details=None):
        "get user list"
        headers = self.set_header_details(auth_details)
        result = self.api_obj.get_user_list(headers=headers)
        self.write("Request & Response:\n%s\n" % str(result))
        user_list = {}
        response_code = None

        """if userlist result is none then return http error code"""
        try:
            response = result
            if response is not None:
                user_list = result['user_list']
                error = result['response']
            if error is not None:
                response_code = error
        except (TypeError, AttributeError) as e:
            raise e

        return {'user_list': result['user_list'], 'response_code': result['response']}

    def check_validation_error(self, auth_details=None):
        "verify validatin error 403"
        result = self.get_user_list(auth_details)
        user_list = result['user_list']
        response_code = result['response_code']
        result_flag = False
        msg = ''

        "verify result based on user list and response code"
        if  response_code == 403:
            msg = "403 FORBIDDEN: Authentication successful but no access for non admin users"

        elif response_code == 200:
            result_flag = True
            msg = "successful authentication and access permission"

        elif response_code == 401:
            msg = "401 UNAUTHORIZED: Authenticate with proper credentials OR Require Basic Authentication"

        elif response_code == 404:
            msg = "404 NOT FOUND: URL not found"

        else:
            msg = "unknown reason"

        return {'result_flag': result_flag, 'msg': msg}
    '''