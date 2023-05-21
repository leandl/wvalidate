import pytest

from wvalidate import Validator, ValidatorReturn, ValidatorError
from wvalidate.validators.email_validator import EmailValidator

VALID_EMAILS = [
	r"example@example.com",
	r"test.email@example.com",
	r"john.doe@example.com",
	r"jane_doe@example.com",
	r"email123@example.com",
	r"e-mail@example.com",
	r"email@example-domain.com",
	r"email@example.co.uk",
	r"email@example.io",
	r"email@example.org",
	r"email@example123.com",
	r"email.123@example.com",
	r"email-123@example.com",
	r"email_123@example.com",
	r"email.abc.def@example.com",
	r"email@example.aero",
	r"email@example.museum",
	r"email@example.travel",
	r"email@example.info",
	r"email@example.biz",
	r"email@example.name",
	r"email@example.pro",
	r"email@example.me",
	r"email@example.us",
	r"email@example.eu",
	r"email@example.de",
	r"email@example.es",
	r"email@example.fr",
	r"email@example.jp"
]

INVALID_EMAILS = [
	r"example@domain",
	r"test.email@com",
	r"invalid.email@domain.",
	r"@domain.com",
	r"email@domain@com",
	r"email.domain.com",
	r"email@domain_com",
	r"email@domain..com",
	r"email@domain_com",
	r"email@.domain.com",
	r"email@domain..com",
	r"email@domain_com",
	r"email@domain,com",
	r"email@domain;com",
	r"email@domain com",
	r"email@domain#com",
	r"email@domain[com",
	r"email@domain]com",
	r"email@domain{com",
	r"email@domain}com",
	r"email@domain(com",
	r"email@domain)com",
	r"email@domain<com",
	r"email@domain>com",
	r"email@domain|com",
	r"email@domain\com"
]


def test_email_validator_is_instance_validator():
	assert issubclass(EmailValidator, Validator) == True

@pytest.mark.parametrize("email_valid", VALID_EMAILS)
def test_email_validator_validate_email_valid(email_valid):
	assert EmailValidator().is_valid(email_valid) == ValidatorReturn(True) 


@pytest.mark.parametrize("email_invalid", INVALID_EMAILS)
def test_email_validator_validate_email_invalid(email_invalid):
	assert EmailValidator().is_valid(email_invalid) == ValidatorReturn(False, ValidatorError("Invalid email format.")) 
