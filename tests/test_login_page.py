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
    #Go to Candidates/JObs/Rounds and ddelete the same.

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
        #Set start_time with current time
        start_time = int(time.time())

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

        job_role = conf.job_role
        job_interviewers = conf.job_interviewers

        name_candidates = conf.name_candidates
        email_candidates = conf.email_candidates
        job_applied_select = conf.job_applied_select
        comment_candidates = conf.comment_candidates
        search_option = conf.search_option

        round_name = conf.round_name
        round_duration_select = conf.round_duration_select
        round_description = conf.round_description
        round_requirements = conf.round_requirements

        #3. Set name in form
        result_flag = test_obj.set_user(username)
        test_obj.log_result(result_flag,
                            positive="Name was successfully set to: %s\n" % username,
                            negative="Failed to set name: %s \nOn url: %s\n" % (username, test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #4. Set Password in form
        result_flag = test_obj.set_password(password)
        test_obj.log_result(result_flag,
                            positive="Password was successfully set to: %s\n" % password,
                            negative="Failed to set password: %s \nOn url: %s\n" % (password, test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #5. Set and submit the form in one go
        result_flag = test_obj.login()
        test_obj.log_result(result_flag,
                            positive="Successfully logged in the page\n",
                            negative="Failed to login the page \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        if result_flag is True:
            result_flag = test_obj.check_heading()
        test_obj.log_result(result_flag,
                            positive="Heading on the redirect page checks out!\n",
                            negative="Fail: Heading on the redirect page is incorrect!")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #6. Click on Interviewers Page
        result_flag = test_obj.click_on_link()
        test_obj.log_result(result_flag,
                            positive="Successfully Opened Interviewers page\n",
                            negative="Failed to Open Interviewers page \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #7. Click on  add Interviewers Page
        result_flag = test_obj.add_inter()
        test_obj.log_result(result_flag,
                            positive="Successfully Opened Add Interviewers page\n",
                            negative="Failed to Open Add Interviewers page \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #8. Add interviewer name
        result_flag = test_obj.set_name(interviewers_name)
        test_obj.log_result(result_flag,
                            positive="Successfully added Interviewers name\n",
                            negative="Failed to add Interviewers name \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #9. Add interviewer email
        result_flag = test_obj.set_email(interviewers_email)
        test_obj.log_result(result_flag,
                            positive="Successfully added Interviewers email\n",
                            negative="Failed to add Interviewers email \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #10. Add interviewers designatiom
        result_flag = test_obj.set_designation(interviewers_designation)
        test_obj.log_result(result_flag,
                            positive="Successfully added Interviewers designation\n",
                            negative="Failed to add Interviewers designation \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #11. Add interviewers starttime
        result_flag = test_obj.set_starttime(interviewers_starttime_drop)
        test_obj.log_result(result_flag,
                            positive="Successfully added Interviewers start time\n",
                            negative="Failed to add Interviewers start time \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #12. Add interviewers endime
        result_flag = test_obj.set_endtime(interviewers_endtime_drop)
        test_obj.log_result(result_flag,
                            positive="Successfully added Interviewers end time\n",
                            negative="Failed to add Interviewers end time \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #13. Save Interviewers details
        result_flag = test_obj.save()
        test_obj.log_result(result_flag,
                            positive="Successfully Saved Interviewer details\n",
                            negative="Failed to save Interviewer details \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #14. Click on Ok
        result_flag = test_obj.close_inter()
        test_obj.log_result(result_flag,
                            positive="Successfully Clicked on OK\n",
                            negative="Failed to Click on OK \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        test_obj = PageFactory.get_page_object("jobs page")

        #19. Add JObs
        result_flag = test_obj.add_jobs()
        test_obj.log_result(result_flag,
                            positive="Successfully opened add jobs page\n",
                            negative="Failed to open jobs page \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #20. Set Job Role
        result_flag = test_obj.set_job_role(job_role)
        test_obj.log_result(result_flag,
                            positive="Successfully added job role\n",
                            negative="Failed to add job role \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #16. Add interviewers endime
        result_flag = test_obj.set_job_interviewer(job_interviewers)
        test_obj.log_result(result_flag,
                            positive="Successfully added Interviewers end time\n",
                            negative="Failed to add Interviewers end time \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #17. Save Interviewers details
        result_flag = test_obj.submit_job()
        test_obj.log_result(result_flag,
                            positive="Successfully Saved job details\n",
                            negative="Failed to save Job details \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        test_obj = PageFactory.get_page_object("candidates page")


        result_flag = test_obj.add_candidates()
        test_obj.log_result(result_flag,
                            positive="Successfully opened add candidates page\n",
                            negative="Failed to open candidates page \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #19. Add interviewers starttime
        result_flag = test_obj.add_name(name_candidates)
        test_obj.log_result(result_flag,
                            positive="Successfully added name of candidate\n",
                            negative="Failed to add name of candidate \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #16. Add interviewers endime
        result_flag = test_obj.add_email(email_candidates)
        test_obj.log_result(result_flag,
                            positive="Successfully added Candidates email\n",
                            negative="Failed to add Candidates email \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #16. Add interviewers endime
        result_flag = test_obj.add_job_applied(job_applied_select)
        test_obj.log_result(result_flag,
                            positive="Successfully added Job appliedl\n",
                            negative="Failed to add Job applied \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #16. Add interviewers endime
        result_flag = test_obj.add_comments(comment_candidates)
        test_obj.log_result(result_flag,
                            positive="Successfully added Candidates comments\n",
                            negative="Failed to add Candidates comments \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #17. Save Interviewers details
        result_flag = test_obj.submit()
        test_obj.log_result(result_flag,
                            positive="Successfully Saved Candidate details\n",
                            negative="Failed to save Candidate details \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        test_obj = PageFactory.get_page_object("jobs page")


        #18. Open jobs page to add rounds
        result_flag = test_obj.round_to_job()
        test_obj.log_result(result_flag,
                            positive="Successfully opened jobs page to add rounds\n",
                            negative="Failed to open jobs page \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #19. Click Add rounds
        result_flag = test_obj.add_rounds()
        test_obj.log_result(result_flag,
                            positive="Successfully opened add rounds\n",
                            negative="Failed to open add rounds \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #20. Add Round name
        result_flag = test_obj.add_name(round_name)
        test_obj.log_result(result_flag,
                            positive="Successfully added round name\n",
                            negative="Failed to add round name \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #21. Add Round duration
        result_flag = test_obj.add_duration(round_duration_select)
        test_obj.log_result(result_flag,
                            positive="Successfully added Round duration\n",
                            negative="Failed to add Round duration \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #22. Add Round description
        result_flag = test_obj.add_description(round_description)
        test_obj.log_result(result_flag,
                            positive="Successfully added Round description\n",
                            negative="Failed to add Round description \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #22. Add Round requirements
        result_flag = test_obj.add_requirements(round_requirements)
        test_obj.log_result(result_flag,
                            positive="Successfully added Round requirements\n",
                            negative="Failed to add Round requirements \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #23. Click Add
        result_flag = test_obj.add()
        test_obj.log_result(result_flag,
                            positive="Successfully clicked on add \n",
                            negative="Failed to open add  \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        test_obj = PageFactory.get_page_object("candidates page")


        result_flag = test_obj.search_candidate(search_option)
        test_obj.log_result(result_flag,
                            positive="Successfully searched candidates name\n",
                            negative="Failed to search candidates name \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        result_flag = test_obj.delete_candidates()
        test_obj.log_result(result_flag,
                            positive="Successfully opened delete candidates page\n",
                            negative="Failed to open delete candidates page \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        result_flag = test_obj.remove_candidates()
        test_obj.log_result(result_flag,
                            positive="Successfully deleted candidate\n",
                            negative="Failed to delete candidate \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        test_obj = PageFactory.get_page_object("interviewers page")


        result_flag = test_obj.delete_interviewers()
        test_obj.log_result(result_flag,
                            positive="Successfully opened delete interviewers page\n",
                            negative="Failed to open delete interviewers page \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        result_flag = test_obj.remove_interviewers()
        test_obj.log_result(result_flag,
                            positive="Successfully deleted interviewer\n",
                            negative="Failed to delete interviewer \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        test_obj = PageFactory.get_page_object("jobs page")


        result_flag = test_obj.delete_job()
        test_obj.log_result(result_flag,
                            positive="Successfully opened delete jobs page\n",
                            negative="Failed to open delete jobs page \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        result_flag = test_obj.remove_job()
        test_obj.log_result(result_flag,
                            positive="Successfully deleted job\n",
                            negative="Failed to delete job \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))


        #Turn off the highlighting feature
        #test_obj.turn_off_highlight()

        #13. Print out the result
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
