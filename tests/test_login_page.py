"""
This is an example automated test to help you test interview scheduler application
Our automated test will do the following:
    #Open Login Page of Scheduler App.
    #Enter Login details.
    #Login to app.
    #Go to interviewers page.
    #Add the details of interviewers add the same.
    #Go to the Jobs Page
    #Add the job details, add the same.
    #Go to the candidates page.
    #add the candidate details, add the same.
    #Go to the Jobs page, add rounds.
    #Go to Candidates/JObs/Rounds and delete the same.

"""
import os
import sys
import time
import pytest
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.login_conf as conf
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.mark.GUI
def test_login_page(test_obj):

    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1

        #1. Create a test object and fill the login form.
        test_obj = PageFactory.get_page_object("login page")


        # Turn on the highlighting feature
        test_obj.turn_on_highlight()

        #2. Get the test details from the conf file
        username = conf.user_name
        password = conf.password

        interviewers_name = conf.interviewers_name
        interviewers_email = conf.interviewers_email
        interviewers_designation = conf.interviewers_designation
        interviewers_starttime_drop = conf.interviewers_starttime_drop
        interviewers_endtime_drop = conf.interviewers_endtime_drop
        search_option_interviewer = conf.search_option_interviewer

        job_role = conf.job_role
        job_interviewers = conf.job_interviewers
        search_option_job = conf.search_option_job

        name_candidates = conf.name_candidates
        email_candidates = conf.email_candidates
        job_applied_select = conf.job_applied_select
        comment_candidates = conf.comment_candidates
        search_option_candidate = conf.search_option_candidate

        round_name = conf.round_name
        round_duration_select = conf.round_duration_select
        round_description = conf.round_description
        round_requirements = conf.round_requirements

        #3. Enter Username and Password and login to page
        result_flag = test_obj.login_page(username,password)
        test_obj.log_result(result_flag,
                            positive="Successfully logged in the page\n",
                            negative="Failed to login the page \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")


        if result_flag is True:
            result_flag = test_obj.check_heading()
        test_obj.log_result(result_flag,
                            positive="Heading on the redirect page checks out!\n",
                            negative="Fail: Heading on the redirect page is incorrect!")


        #4. Click on Interviewers Page
        result_flag = test_obj.click_on_link()
        test_obj.log_result(result_flag,
                            positive="Successfully Opened Interviewers page\n",
                            negative="Failed to Open Interviewers page \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")


        #5. Click on add Interviewers Page
        result_flag = test_obj.add_interviewer()
        test_obj.log_result(result_flag,
                            positive="Successfully Opened Add Interviewers page\n",
                            negative="Failed to Open Add Interviewers page \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")


        #6. Add interviewer
        result_flag = test_obj.interviewers_details(interviewers_name,interviewers_email,interviewers_designation,interviewers_starttime_drop,interviewers_endtime_drop)
        test_obj.log_result(result_flag,
                            positive="Successfully added interviewer with all details\n",
                            negative="Failed to add interviewer with all details \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")


        test_obj = PageFactory.get_page_object("jobs page")


        #7. Add JObs
        result_flag = test_obj.add_jobs()
        test_obj.log_result(result_flag,
                            positive="Successfully opened add jobs page\n",
                            negative="Failed to open jobs page \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")


        #8. Add Job details
        result_flag = test_obj.job_details(job_role,job_interviewers)
        test_obj.log_result(result_flag,
                            positive="Successfully added job details\n",
                            negative="Failed to add Job details \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")


        test_obj = PageFactory.get_page_object("candidates page")

        #9. Add Candidate
        result_flag = test_obj.add_candidates()
        test_obj.log_result(result_flag,
                            positive="Successfully opened add candidates page\n",
                            negative="Failed to open candidates page \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")

        #10. Add Candidate details
        result_flag = test_obj.candidate_details(name_candidates,email_candidates,job_applied_select,comment_candidates)
        test_obj.log_result(result_flag,
                            positive="Successfully added Candidates details and saved the same\n",
                            negative="Failed to add Candidates details and save \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")


        test_obj = PageFactory.get_page_object("jobs page")


        #11. Search job
        result_flag = test_obj.search_job(search_option_job)
        test_obj.log_result(result_flag,
                            positive="Successfully searched interviewer name\n",
                            negative="Failed to search interviewer name \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")


        #12. Open jobs page to add rounds
        result_flag = test_obj.round_to_job()
        test_obj.log_result(result_flag,
                            positive="Successfully opened jobs page to add rounds\n",
                            negative="Failed to open jobs page \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")


        #13. Click Add rounds
        result_flag = test_obj.add_rounds()
        test_obj.log_result(result_flag,
                            positive="Successfully opened add rounds\n",
                            negative="Failed to open add rounds \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")


        #14. Add job round details
        result_flag = test_obj.round_details(round_name,round_duration_select,round_description,round_requirements)
        test_obj.log_result(result_flag,
                            positive="Successfully added round details \n",
                            negative="Failed to add round details \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")


        test_obj = PageFactory.get_page_object("candidates page")

        #15. Delete Candidate
        result_flag = test_obj.remove_candidates(search_option_candidate)
        test_obj.log_result(result_flag,
                            positive="Successfully deleted candidate\n",
                            negative="Failed to delete candidate \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")


        test_obj = PageFactory.get_page_object("interviewers page")

        #16. Delete interviewer
        result_flag = test_obj.remove_interviewers(search_option_interviewer)
        test_obj.log_result(result_flag,
                            positive="Successfully deleted interviewer\n",
                            negative="Failed to delete interviewer \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")


        test_obj = PageFactory.get_page_object("jobs page")

        #17. Delete Job
        result_flag = test_obj.remove_job(search_option_job)
        test_obj.log_result(result_flag,
                            positive="Successfully deleted job\n",
                            negative="Failed to delete job \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")


        #Turn off the highlighting feature
        test_obj.turn_off_highlight()

        #18. Print out the result
        test_obj.write_test_summary()
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter

    except Exception as e:
        print("Exception when trying to run test: %s"%__file__)
        print("Python says:%s"%str(e))

    assert expected_pass == actual_pass, "Test failed: %s"%__file__


#---START OF SCRIPT
if __name__ == '__main__':
    print("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()

    #Run the test only if the options provided are valid
    if options_obj.check_options(options):
        test_obj = PageFactory.get_page_object("Zero", base_url=options.url)

        #Setup and register a driver
        test_obj.register_driver(options.remote_flag, options.os_name, options.os_version, options.browser, options.browser_version, options.remote_project_name, options.remote_build_name)

        test_login_page(test_obj)

        #teardowm
        test_obj.wait(3)
        test_obj.teardown()
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(options_obj.print_usage())
