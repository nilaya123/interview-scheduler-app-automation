"""
Test steps to automate Signup email confirmation feature
    #Navigate to the Login Page
    #Click on the SignUp button
    #Populate the fields Username, Email address, Password and Confirm Password
    #Click on the Submit button

"""
import os
import sys
import string
import random
import pytest
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.login_conf as conf
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



@pytest.mark.GUI
def test_add_delete(test_obj):

    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1

        #1. Create a test object and fill the login form.
        test_obj = PageFactory.get_page_object("login page")


        # Turn on the highlighting feature
        test_obj.turn_on_highlight()
      

      #3. Get the test details from the conf file
        username = conf.user_name
        password = conf.password
        #email = "kavya.suryaprakash+" + ''.join(random.choices(string.digits, k=3)) + ('@qxf2.com')
        email = "kavya.suryaprakash+427" + ''.join('@qxf2.com')

       
        #4. Navigate to Signup page
        result_flag = test_obj.signup()
        test_obj.log_result(result_flag,
                            positive="Successfully navigated to the Signup form\n",
                            negative="Failed to navigate to the Signup form \nOn url: %s" \
                                % test_obj.get_current_url(),
                            level="debug")

        #5. Populate the fields in Signup Form
        result_flag = test_obj.submit_signup_form(username, email, password)
        test_obj.log_result(result_flag,
                            positive="Successfully clicked on the Signup button\n",
                            negative="Failed to click the Submit button \nOn url: %s"\
                                 % test_obj.get_current_url(),
                            level="debug")

        
        #6. Populate the Username and Password and click on Login button on the Login page
        result_flag = test_obj.login_page(username, password)
        test_obj.log_result(result_flag,
                            positive="Successfully Logged In to the application\n",
                            negative="Failed to Login In to the application \nOn url: %s"\
                                 % test_obj.get_current_url(),
                            level="debug")
        

        #6.Turn off the highlighting feature
        test_obj.turn_off_highlight()

        #7. Print out the result
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
        test_obj.register_driver(options.remote_flag, options.os_name, options.os_version,\
             options.browser, options.browser_version, options.remote_project_name,\
                  options.remote_build_name)

        #teardowm
        test_obj.wait(3)
        test_obj.teardown()
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(options_obj.print_usage())
