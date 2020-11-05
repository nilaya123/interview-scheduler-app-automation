"""
API endpoints for Cars
"""
#!/usr/bin/python -tt
from .Base_API import Base_API

class Jobs_API_Endpoints(Base_API):
    "Class for Jobs endpoints"

    def login_url(self,suffix=''):
        """Append API end point to base URL"""
        return self.base_url+'login'


    def jobs_url(self,suffix=''):
        """Append API end point to base URL"""
        return self.base_url+'jobs'+suffix


    def login_app_is(self,data):
        """Login to App"""
        url = self.login_url()
        print(data)
        response = self.post(url,data=data)
        #print(response)
        #cookie_value = response.headers['Set-Cookie']
        #print(response.headers)
        #print(response)
        return response


    def add_jobs_is(self,data):
        "Adds a new job"
        url = self.jobs_url('/add')
        response = self.post(url,data=data)
        return {
            'url':url,
            'response':response['response']
        }


    def get_jobs_is(self):
        "gets list of jobs"
        url = self.jobs_url()
        response = self.get(url)
        return {
            'url':url,
            'response': response['response'],
            'response_content': response['json_response']
        }


    def delete_jobs_is(self,data):
        "Adds a new job"
        url = self.jobs_url('/delete')
        response = self.post(url,data=data)
        return {
            'url':url,
            'response':response['response']
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