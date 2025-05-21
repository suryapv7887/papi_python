from selenium.webdriver.common.by import By

class Regular_EmployeeFormLocators:
    ADD_EMPLOYEE_BUTTON=(By.XPATH, "//button[@data-qa-automation='zohoSyncButton']")
    ADD_EMPLOYEE_FORM=(By.XPATH,"//span[text()='Add Regular Employee']")
    FIRST_NAME = (By.XPATH, "//input[@placeholder='First Name']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='Last Name']")
    EMAIL = (By.XPATH, "//input[@placeholder='Email ID']")
    MOBILE = (By.XPATH, "//input[@placeholder='Mobile Number']")
    LINKEDIN=(By.XPATH,"//input[@placeholder='URL']")

    # DATE_PICKER_BTN = (By.XPATH, "//button[@aria-label='Choose date']")
    # MONTH_YEAR = (By.XPATH, "//div[@role='presentation']/child::div[1]/div")
    # PREV_MONTH_BTN = (By.XPATH, "//button[@title='Previous month']")
    # NEXT_MONTH_BTN= (By.XPATH, "//button[@title='Next month']")
    # DATE_CELLS = (By.XPATH, "//div[@role='presentation']//button[@role='gridcell']")
    DOB_FIELD = (By.XPATH, "(//input[@placeholder='DD-MM-YYYY'])[1]")
    AGE_FIELD = (By.XPATH, "//input[@placeholder='Age']")

    BLOOD_GROUP_DROPDOWN = (By.XPATH, "//div[@data-qa-automation='bloodGroup']")
    BLOOD_GROUP_OPTIONS = (By.XPATH, "//div[@id='menu-user.blood_group']//ul/li")

    GENDER_DROPDOWN=(By.XPATH,"//div[@data-qa-automation='gender']")
    GENDER_OPTIONS=(By.XPATH,"//div[@id='menu-user.gender']//ul/li")

    MARITAL_STATUS_DROPDOWN = (By.XPATH, "//div[@data-qa-automation='maritalStatus']")
    MARITAL_STATUS_OPTIONS=(By.XPATH,"//div[@id='menu-user.marital_status']//ul/li")

    SAME_AS_PRESENT_CHECKBOX = (By.XPATH, "//input[@id='address_same_as_present']")

    PRESENT_HOUSENO = (By.XPATH, "(//input[@placeholder='House Name/No'])[1]")
    PRESENT_LOCALITY = (By.XPATH, "(//input[@placeholder='Locality'])[1]")
    PRESENT_STATE = (By.XPATH, "(//input[@placeholder='State'][1])")
    PRESENT_COUNTRY = (By.XPATH, "(//input[@placeholder='Country'])[1]")
    PRESENT_PINCODE = (By.XPATH, "(//input[@placeholder='Pincode'])[1]")

    PERMANENT_HOUSENO = (By.XPATH, "(//input[@placeholder='House Name/No'])[2]")
    PERMANENT_LOCALITY = (By.XPATH, "(//input[@placeholder='Locality'])[2]")
    PERMANENT_STATE = (By.XPATH, "(//input[@placeholder='State'])[2]")
    PERMANENT_COUNTRY = (By.XPATH, "(//input[@placeholder='Country'])[2]")
    PERMANENT_PINCODE = (By.XPATH, "(//input[@placeholder='Pincode'])[2]")

    AADHAR_NUMBER_BOX=(By.XPATH, "//input[@placeholder='Enter Aadhaar No.']")
    PAN_NUMBER_BOX=(By.XPATH, "//input[@placeholder='Enter Pancard No.']")
    AADHAR_FILE_UPLOAD=(By.XPATH,"(//input[@type='file'])[1]")
    PAN_FILE_UPLOAD=(By.XPATH,"//input[@placeholder='Enter Pancard No.']//following::button[1]/input[@type='file']")

    BANK_NAME=(By.XPATH,"//input[@placeholder='Enter Bank Name']")
    BANK_ACCOUNT_NUMBER=(By.XPATH,"//input[@placeholder='Enter Account Number']")
    IFSC_CODE=(By.XPATH,"//input[@placeholder='Enter IFSC Code']")

    PASSPORT_UPLOAD=(By.XPATH,"//div[contains(text(),'Attach Passport')]/following-sibling::button/input[@type='file']")

    EMERGENCY_NAME=(By.XPATH,"//label[@for='emergencyContact.contact_name']/following-sibling::div/div/input")
    EMERGENCY_CONTACT=(By.XPATH,"//label[@for='emergencyContact.contact_number']/following-sibling::div/div/input")

    RELEIVING_DOCUMENT_UPLOAD=(By.XPATH,"//div[contains(text(),'Relieving Document')]//following-sibling::button/input[@type='file']")
    PAYSLIPS_UPLOAD=(By.XPATH,"//div[contains(text(),'Payslips')]//following-sibling::button/input[@type='file']")
    EDUCATIONAL_CERTIFICATE_UPLOAD=(By.XPATH,"//div[contains(text(),'Educational Certificate')]//following-sibling::button/input[@type='file']")
    EXPERIENCE_CERTIFICATE_UPLOAD=(By.XPATH,"//div[contains(text(),'Experience Certificate')]//following-sibling::button/input[@type='file']")

    INSURANCE_YES=(By.XPATH,"//div[text()='Company Insurance']/following-sibling::div/label[1]/span[1]")
    INSURANCE_NO=(By.XPATH,"(//input[@name='user.insurance_status'])[2]")
    ADD_DEPENDENT_BUTTON=(By.XPATH,"//button[text()='Add New Dependent']/img")
    DEPENDENT_NAME=(By.XPATH,"//label[@for='dependents.0.name']/following-sibling::div/div/input")
    DEPENDENT_RELATIONSHIP_DROPDOWN=(By.XPATH,"//div[@id='mui-component-select-dependents.0.relationship']")
    DEPENDENT_RELATIONSHIP_DROPDOWN_OPTIONS=(By.XPATH,"//div[@id='menu-dependents.0.relationship']//ul/li")
    DEPENDENT_DOB=(By.XPATH,"(//input[@placeholder='DD-MM-YYYY'])[2]")

    PROVIDENT_FUND_YES=(By.XPATH,"//div[text()='Provident Fund']/following-sibling::div/label[1]/span[1]")
    PROVIDENT_FUND_NO=(By.XPATH,"(//input[@name='user.PROVIDENT_FUND_status'])[2]")
    UAN_NUMBER=(By.XPATH,"//label[@for='user.uan_number']/following-sibling::div/div/input")
    PF_NOMINEE_NAME=(By.XPATH,"//label[@for='user.nominee_name']/following-sibling::div/div/input")
    Gratuity_NOMINEE_NAME=(By.XPATH,"//label[@for='nominees.0.name']/following-sibling::div/div/input")
    Gratuity_NOMINEE_RELATIONSHIP_DROPDOWN=(By.XPATH,"//div[@id='mui-component-select-nominees.0.relationship']")
    Gratuity_NOMINEE_RELATIONSHIP_DROPDOWN_OPTIONS=(By.XPATH,"//div[@id='menu-nominees.0.relationship']//ul/li")
    Gratuity_NOMINEE_AGE=(By.XPATH,"//label[@for='nominees.0.age']/following-sibling::div/div/input")
    Gratuity_NOMINEE_DISTRRIBUTION=(By.XPATH,"//label[@for='nominees.0.proportion']/following-sibling::div/div/input")


    SKILL_CATEGORY_DROPDOWN=(By.XPATH,"//div[@id='mui-component-select-user_skill[0].category']")
    SKILL_CATEGORY_OPTIONS=(By.XPATH,"//div[@id='menu-user_skill[0].category']//ul/li")
    SKILLS_DROPDOWN=(By.XPATH,"//div[@id='mui-component-select-user_skill[0].skill']")
    SKILLS_OPTIONS =(By.XPATH,"//div[@id='menu-user_skill[0].skill']//ul/li")
    EXPERIENCE_YEARS=(By.XPATH,"(//input[@placeholder='Experience'])[1]")
    EXPERIENCE_MONTHS=(By.XPATH,"(//input[@placeholder='Experience'])[2]")
    SKILL_RATINGS=(By.XPATH,"//input[@name='user_skill[0].rating']/../label")

    DEPARTMENT_DROPDOWN=(By.XPATH,"//div[@id='mui-component-select-user.department']")
    DEPARTMENT_DROPDOWN_OPTIONS=(By.XPATH,"//div[@id='menu-user.department']//ul/li")
    TITLE_DROPDOWN=(By.XPATH,"//div[@id='mui-component-select-user.designation']")
    TITLE_DROPDOWN_OPTIONS=(By.XPATH,"//div[@id='menu-user.designation']//ul/li")
    L2_MANAGER_DROPDOWN=(By.XPATH,"//div[@id='mui-component-select-user.reporting_manager']")
    L2_MANAGER_DROPDOWN_OPTIONS=(By.XPATH,"//div[@id='menu-user.reporting_manager']//ul/li")
    L3_MANAGER_DROPDOWN=(By.XPATH,"//div[@id='mui-component-select-user.l3_manager']")
    L3_MANAGER_DROPDOWN_OPTIONS=(By.XPATH,"//div[@id='menu-user.l3_manager']//ul/li")
    OFFICIAL_EMAIL_ID=(By.XPATH,"//label[@for='user.email']/following-sibling::div/div/input")
    TOTAL_EXPERIENCE=(By.XPATH,"//label[@for='user.experience']/following-sibling::div/div/input")
    LOCATIONS_DROPDOWN=(By.XPATH,"//div[@id='mui-component-select-user.location']")
    LOCATIONS_DROPDOWN_OPTIONS=(By.XPATH,"//div[@id='menu-user.location']//ul/li")
    WORK_MODE_BUTTON=(By.XPATH,"//div[text()='Work Mode']/following-sibling::div/div/label/span[2]")

    INSTITUTION = (By.XPATH,"//label[@for='qualification[0].school']/following-sibling::div/div/input")
    DEGREE = (By.XPATH,"//label[@for='qualification[0].qualification']/following-sibling::div/div/input")
    FIELD = (By.XPATH,"//label[@for='qualification[0].domain']/following-sibling::div/div/input")
    YEAR = (By.XPATH,"//label[@for='qualification[0].year_of_completion']/following-sibling::div/div/input")


    SUBMIT=(By.XPATH,"//button[@data-testid='submit-button-id']")
    CONFIRMATION_MESSAGE=(By.XPATH,"//div[@role='alert']/div[1]")