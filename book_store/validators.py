from django.core.validators import RegexValidator
from .messages import VALIDATION_ERROR_MESSAGES


# for alphabets + numeric + special characters (-, ., $, "",)
BookNameValidator = RegexValidator(
    regex='^[A-Za-z\s\-_,\.:;()''""]+$',
    message=VALIDATION_ERROR_MESSAGES['INVALID_BOOK_NAME'],
    code='INVALID_BOOK_NAME'
)

BookAuthorValidator = RegexValidator(
    regex='^[A-Za-z\s\-_,\.:;()''""]+$',
    message=VALIDATION_ERROR_MESSAGES['INVALID_AUTHOR_NAME'],
    code='INVALID_AUTHOR_NAME'
)

AddressNameValidator = RegexValidator(
    regex='^[\w*\s*\#\-\,\/\.\(\)\&]*$',
    message=VALIDATION_ERROR_MESSAGES['INVALID_ADDRESS'],
    code='INVALID_ADDRESS'
)

MobileNumberValidator = RegexValidator(
    regex='^[6-9]\d{9}$',
    message=VALIDATION_ERROR_MESSAGES['INVALID_MOBILE_NUMBER'],
    code='INVALID_MOBILE_NUMBER'
)

PinCodeValidator = RegexValidator(
    regex='^[1-9][0-9]{5}$',
    message=VALIDATION_ERROR_MESSAGES['INVALID_PINCODE'],
    code='INVALID_PINCODE'
)

NameValidator = RegexValidator(
    regex='^[a-zA-Z\s]{2,255}$',
    message=VALIDATION_ERROR_MESSAGES['INVALID_NAME'],
    code='INVALID_NAME'
)