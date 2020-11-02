"""
API endpoints for Candidates
"""
#!/usr/bin/python -tt
from .Base_API import Base_API

class Interviewer_API_Endpoints(Base_API):
    "Class for Interviewer endpoints"

    def login_url(self,suffix=''):
        """Append API end point to base URL"""
        return self.base_url+'login'



    def interviewer_url(self,suffix=''):
        """Append API end point to base URL"""
        return self.base_url+'interviewers'+suffix



    def add_interviewer_is(self,data):
        "Adds a new job"
        url = self.interviewer_url('/add')
        response = self.post(url,data=data)
        return {
            'url':url,
            'response':response['response']
        }


    def get_interviewer_is(self):
        "gets list of jobs"
        url = self.interviewer_url()
        response = self.get(url)
        return {
            'url':url,
            'response': response['response'],
            'response_content': response['json_response']
        }

    '''
    def get_car(self,url_params,headers):
        "gets given car details"
        url = self.cars_url('/find?')+url_params
        json_response = self.get(url,headers=headers)
        return {
            'url':url,
            'response':json_response['json_response']
        }


    def update_job(self,job_name,json,headers):
        "updates a given job"
        url = self.cars_url('/update/%s'%job_name)
        json_response =self.put(url,json=json,headers=headers)
        return {
            'url':url,
            'response':json_response['json_response']
        }


    def remove_job(self,job_name,headers):
        "deletes a car entry"
        url =self.jobs_url('/remove/%s'%car_name)
        json_response = self.delete(url,headers=headers)
        return{
            'url':url,
            'response':json_response['json_response']
        }
    '''