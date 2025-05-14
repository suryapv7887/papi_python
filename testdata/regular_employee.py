from testdata.files import FilePaths

class PeopleData:
    ADD_EMPLOYEE_DATA = {
        "first_name": "Melina",
        "last_name": "QA",
        "email": "QA123@mail.com",
        "mobile": "9876543210",
        "linkedin": "https://linkedin.com/in/abcd",
        "dob": "01-01-1995",
        "age": "30",
        "blood_group": "A+",
        "gender": "Female",
        "marital_status": "Single",
        "present_address": {
            "house": "123",
            "locality": "Green Street, Chennai",
            "state": "Tamilnadu",
            "country": "India",
            "pincode": "400001"
        },
        "same_as_present": False,
        "Permanent_address": {
            "house": "321",
            "locality": "Yellow Street, Ernakulam",
            "state": "Kerala",
            "country": "India",
            "pincode": "500001"
        },
        "aadhar": "444455556666",
        "aadhar_file": FilePaths.AADHAR,
        "pan": "ABCDE1234F",
        "pan_file": FilePaths.PAN,
        "bank": "RBIB",
        "account_number": "222233334444",
        "ifsc": "SBIN0012345",
        "passport_file": FilePaths.PASSPORT,

        "emergency_name": "Joe",
        "emergency_contact": "9876543210",

        "releiving_letter_file": FilePaths.RELIEVING_LETTER,
        "payslips_file": FilePaths.PAYSLIPS,
        "experience_certificate_file": FilePaths.EXPERIENCE_CERTIFICATE,
        "educational_certificate_file": FilePaths.EDUCATION_CERTIFICATE,
        "insurance_required": False,
        "dependent_data": {
            "name": "Joe",
            "relationship": "Spouse",
            "dob": "1990-05-10"
        }
    }
