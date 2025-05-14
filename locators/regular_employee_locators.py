from selenium.webdriver.common.by import By

class Regular_EmployeeFormLocators:
    ADD_EMPLOYEE_BUTTON=(By.XPATH, "//span[text()='Add Employee']")
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
    DOB_FIELD = (By.XPATH, "//input[@placeholder='DD-MM-YYYY']")
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

    EMERGENCY_NAME=(By.XPATH,"//input[@placeholder='Enter Contact name']")
    EMERGENCY_CONTACT=(By.XPATH,"//input[@placeholder='Enter Contact no']")

    RELEIVING_DOCUMENT_UPLOAD=(By.XPATH,"//div[contains(text(),'Relieving Document')]//following-sibling::button/input[@type='file']")
    PAYSLIPS_UPLOAD=(By.XPATH,"//div[contains(text(),'Payslips')]//following-sibling::button/input[@type='file']")
    EDUCATIONAL_CERTIFICATE_UPLOAD=(By.XPATH,"//div[contains(text(),'Educational Certificate')]//following-sibling::button/input[@type='file']")
    EXPERIENCE_CERTIFICATE_UPLOAD=(By.XPATH,"//div[contains(text(),'Experience Certificate')]//following-sibling::button/input[@type='file']")

    INSURANCE_YES=(By.XPATH,"(//input[@name='user.insurance_status'])[1]")
    INSURANCE_NO=(By.XPATH,"(//input[@name='user.insurance_status'])[2]")
    ADD_DEPENDENT_BUTTON=(By.XPATH,"//button[text()='Add New Dependent']")
    DEPENDENT_NAME=(By.XPATH,"//input[@placeholder='Enter Dependent's Name']")
    DEPENDENT_RELATIONSHIP_DROPDOWN=(By.XPATH,"//div[@data-qa-automation='relationship']")
    DEPENDENT_RELATIONSHIP_DROPDOWN_OPTIONS=(By.XPATH,"//div[@id='menu-dependents.0.relationship']//ul/li")
    DEPENDENT_DOB=(By.XPATH,"//input[@placeholder='DD-MM-YYYY']")




