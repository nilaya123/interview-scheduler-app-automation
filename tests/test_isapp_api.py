'''
import requests as session

ses=session.post('http://localhost:6464/login',data={'username':'nilaya','password':'nilaya1234'})
cookie_value = ses.headers['Set-Cookie']
headers = {'Content-Type': 'application/x-www-form-urlencoded','Cookie': cookie_value}

ses=session.post('http://localhost:6464/jobs/add',data={'role':'just_new','interviewerlist':'["nilaya"]'},headers=headers)
print(ses.text)
print(ses.content)
print("For jobs added")

ses=session.post('http://localhost:6464/interviewers/add',data={'name':'ragi123','email':'ragini+1234@qxf2.com','designation':'QA Manager','timeObject':'{"starttime":["10:00"],"endtime":["19:00"]}'},headers=headers)
print(ses.text)
print(ses.content)
print("For interv added")

ses=session.post('http://localhost:6464/candidate/add',data={'candidateName':'test_more_new','candidateEmail':'test_more+1@gmail.com','jobApplied':'Senior QA','addedcomments':'N/A'},headers=headers)
print(ses.text)
print(ses.content)
print("For cand added")

'''
from conf import api_example_conf as conf
from endpoints.API_Player import API_Player
import os
import sys
import pytest
import requests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.mark.API
def test_isapi_example(api_url='http://localhost:6464/'):
    "Run api test"
    #try:
        # Create test object
    test_obj = API_Player(url=api_url)
    expected_pass = 0
    actual_pass = -1

# set authentication details
    username = conf.user_name
    password = conf.password
    job_data = conf.job_details
    candidate_data = conf.candidate_details
    interviewer_data = conf.interviewer_details

    auth_details = test_obj.set_login_details(username, password)

    result_flag = test_obj.login_app(auth_details)
    test_obj.log_result(result_flag,
                           positive='Successfully logged in app %s' % username,
                           negative='Could not login to app %s' % username)

    '''
    result_flag = test_obj.add_jobs(job_data)
    test_obj.log_result(result_flag,
                           positive='Successfully added new job with details %s' % job_data,
                           negative='Could not add new job with details %s' % job_data)


    result_flag = test_obj.get_jobs()
    test_obj.log_result(result_flag,
                           positive='Successfully got the list of jobs',
                           negative='Could not get the list of jobs')


    result_flag = test_obj.add_candidates(candidate_data)
    test_obj.log_result(result_flag,
                           positive='Successfully added a new candidate with all details %s' % candidate_data,
                           negative='Could not add the candidate %s' % candidate_data)


    result_flag = test_obj.get_candidates()
    test_obj.log_result(result_flag,
                           positive='Successfully got the list of candidates',
                           negative='Could not get the list of candidates')


    result_flag = test_obj.add_interviewers(interviewer_data)
    test_obj.log_result(result_flag,
                           positive='Successfully added a new interviewer with all details %s' % interviewer_data,
                           negative='Could not add the interviewer %s' % interviewer_data)


    result_flag = test_obj.get_interviewers()
    test_obj.log_result(result_flag,
                           positive='Successfully got the list of interviewers',
                           negative='Could not get the list of interviewers')

    '''
    result_flag = test_obj.delete_jobs()
    test_obj.log_result(result_flag,
                           positive='Successfully deleted the job',
                           negative='Could not delete the job')


    # write out test summary
    expected_pass = test_obj.total
    actual_pass = test_obj.passed
    test_obj.write_test_summary()


if __name__ == '__main__':
    test_isapi_example()