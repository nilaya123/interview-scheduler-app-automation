#Common locator file for all locators
#Locators are ordered alphabetically

############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################
'''
#Locators for the footer object(footer_object.py)

footer_menu = "xpath,//ul[contains(@class,'nav-justified')]/descendant::a[text()='%s']"
copyright_text = "xpath,//p[contains(@class,'qxf2_copyright')]"
#----
'''
#Locators for the login object(form_object.py)
username_field = "xpath,//input[@id = 'username']"
password_field = "xpath,//input[@id='userpassword']"
login_button = "xpath,//*[@id='loginButton']"
signup_button = "xpath,//*[@id='signupButton']"

#Locators for the index object(index_object.py)
interviewers_page = "xpath,//a[contains(.,'List the interviewers')]"
jobs_page = "xpath,//a[contains(.,'List the jobs')]"
candidates_page = "xpath,//a[contains(.,'List the candidates')]"

#Heading for index page
heading = "xpath,//h2[contains(.,'Why Interview Scheduler Application?')]"

#Locators for Candidates Page
search_option = "xpath,//input[contains(@type,'search')]"
add_candidates_button = "xpath,//input[@id='add']"
delete_candidate = "xpath,//button[contains(@data-candidateid,'')]"
edit_candidate = "xpath,//input[@onclick='editCandidates()']"
name_candidates = "xpath,//input[@id='fname']"
email_candidates = "xpath,//input[@id='email']"
job_applied = "xpath,//select[contains(@id,'select1')]"
comment_candidates = "xpath,//textarea[@id='comments']"
submit_candidates_button = "xpath,//button[@id='addSubmit']"
delete_candidates_button = "xpath,//button[contains(@data-candidatename,'Mayara')]"
remove_candidates_button = "xpath,//button[@id='remove-button']"
select_candidate_button = "xpath,//a[contains(.,'Mayara')]"
thumbs_up_button = "xpath,//input[@value='Thumbs up']"
thumbs_down_button = "xpath,//input[@value='Thumbs down']"
select_round_level_scroll = "xpath,//select[@id='select1']"
send_email_button = "xpath,//button[contains(.,'Send Email')]"
select_url = "xpath,//label[@class='col-md-8'][contains(.,'http://localhost:6464/')]"
select_unique_code = "xpath,//input[contains(@id,'candidate-name')]"
select_candidate_email = "xpath,//input[contains(@id,'candidate-email')]"
go_for_schedule = "xpath,//input[contains(@id,'submit')]"
date_picker = "xpath,//input[contains(@id,'datepicker')]"
#date_on_calendar = "xpath,//table[@class='ui-datepicker-calendar']//td"
#date_on_calendar = "xpath,//td[not(contains(@class,'ui-datepicker-other-month'))]"
#date_on_calendar = "xpath,//a[contains(text(),%s)]"
#date_on_calendar = "xpath,//a[contains(.,%s)]"
date_on_calendar = "xpath,//td[not(contains(@class,'ui-datepicker-other-month'))]/a[text()=%s]"
confirm_interview_date = "xpath,//input[contains(@id,'submit')]"
select_free_slot = "xpath,//input[@value='%s']"
schedule_my_interview = "xpath,//input[contains(@value,'Schedule my interview')]"

#Locators for Interviewers Page
add_interviewers_button = "xpath,//input[contains(@onclick,'addinterviewer()')]"
interviewers_name = "xpath,//input[contains(@id,'fname')]"
interviewers_email = "xpath,//input[@id='email']"
interviewers_designation = "xpath,//input[contains(@id,'designation')]"
interviewers_starttime = "xpath,//input[contains(@id,'starttime0')]"
interviewers_endtime = "xpath,//input[contains(@id,'endtime0')] "
add_time_button = "xpath,//input[contains(@value,'Add time')]"
save_interviewers_button = "xpath,//input[@id='submit']"
cancel_interviewers_button = "xpath,//button[@id='clear']"
close_interviewers_button = "xpath,//button[@id='close']"
delete_interviewers_button = "xpath,//a[text()='avinash']/parent::td/following-sibling::td/button[@data-toggle='modal']"
remove_interviewers_button = "xpath,//button[contains(@id,'remove-button')]"

#Locators for Jobs Page
add_jobs_button = "xpath,//input[contains(@onclick,'addJob()')]"
job_role = "xpath,//input[contains(@id,'role')]"
job_interviewers = "xpath,//input[contains(@id,'interviewers')]"
submit_job_button = "xpath,//button[contains(@id,'submit')]"
delete_job_button = "xpath,//a[text()='Junior QA']/parent::td/following-sibling::td/button[@data-jobrole='Junior QA']"
remove_job_button = "xpath,//button[@id='remove-button']"

#Locators for Rounds
specific_round_add = "xpath,//a[text()='Junior QA']/parent::td/following-sibling::td/input[@value='Rounds']"
add_rounds_button = "xpath,//input[@value='Add Rounds']"
round_name = "xpath,//input[@id='rname']"
round_duration = "xpath,//select[@name='Duration']"
round_description = "xpath,//textarea[@name='rdesc']"
round_requirements = "xpath,//input[@name='rreq']"
add_button = "xpath,//button[@id='addRound']"
cancel_rounds_button = "xpath,//button[@id='cancelRound']"

'''
#Locators for the form object(form_object.py)
name_field = "id,name"
email_field = "name,email"
phone_no_field = "css selector,#phone"
click_me_button = "xpath,//button[text()='Click me!']"
gender_dropdown = "xpath,//button[@data-toggle='dropdown']"
gender_option = "xpath,//a[text()='%s']"
tac_checkbox = "xpath,//input[@type='checkbox']"
#----

#Locators for hamburger menu object(hamburg_menu_object.py)
menu_icon = "xpath,//img[@alt='Menu']"
menu_link = "xpath,//ul[contains(@class,'dropdown-menu')]/descendant::a[text()='%s']"
menu_item = "xpath,//ul[contains(@class,'dropdown-menu')]/descendant::a[@data-toggle='dropdown' and text()='%s']"
#----

#Locators for header object(header_object.py)
qxf2_logo = "xpath,//img[contains(@src,'qxf2_logo.png')]"
qxf2_tagline_part1 = "xpath,//h1[contains(@class,'banner-brown') and text()='SOFTWARE TESTING SERVICES']"
qxf2_tagline_part2 = "xpath,//h1[contains(@class,'banner-grey') and text()='for startups']"
#----

#Locators for table object(table_object.py)
table_xpath = "xpath,//table[@name='Example Table']"
rows_xpath = "xpath,//table[@name='Example Table']//tbody/descendant::tr"
cols_xpath = "xpath,//table[@name='Example Table']//tbody/descendant::td"
cols_relative_xpath = "xpath,//table[@name='Example Table']//tbody/descendant::tr[%d]/descendant::td"
cols_header = "xpath,//table[@name='Example Table']//thead/descendant::th"
#----

#Locators for tutorial redirect page(tutorial_redirect_page.py)
heading = "xpath,//h2[contains(@class,'grey_text') and text()='Selenium for beginners: Practice page 2']"

#Locators for Contact Object(contact_object.py)
contact_name_field = "id,name"

#Locators for mobile application - Bitcoin Info(bitcoin_price_page.py)
bitcoin_real_time_price_button = "xpath,//android.widget.TextView[@resource-id='com.dudam.rohan.bitcoininfo:id/current_price']"
bitcoin_price_page_heading = "xpath,//android.widget.TextView[@text='Real Time Price of Bitcoin']"
bitcoin_price_in_usd = "xpath,//android.widget.TextView[@resource-id='com.dudam.rohan.bitcoininfo:id/doller_value']"
'''
