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
        "blood_group": "B+",
        "gender": "Female",
        "marital_status": "Married",
        "present_address": {
            "house": "123",
            "locality": "Green Street, Chennai",
            "state": "Tamilnadu",
            "country": "India",
            "pincode": "400001"
        },
        "same_as_present": True,
        "permanent_address": {
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
            "dep_dob": "01-01-1994"
        },
        "PF_required": True,
        "PF_data":{
            "uan": "123456789012",
            "pf_nominee": "Joe"
        },
        "Gratuity_data":{
            "gratuity_nominee_name": "Joe",
            "gratuity_nominee_relationship":"Spouse",
            "gratuity_nominee_age": "30",
            "gratuity_nominee_distribution": "100"
        },
        "skill_category": "Programming Language",
        "skill": "Python",
        "experience_years": "3",
        "experience_months": "6",
        "proficiency": 3,

        "department": "Delivery Team",
        "title": "Senior Quality Analyst",
        "L2_manager": "Alice QA",
        "L3_manager": "Admin",
        "official_email": "abc@work.com",
        "total_experience": "4",
        "location": "Chennai",
        "work_mode": "Remote",

        "institution":"ABC College",
        "degree":"B.E",
        "field":"C.S",
        "year": "2016"

    }
