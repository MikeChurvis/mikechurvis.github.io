import os

from django.db import IntegrityError
from django.test import TestCase, override_settings
from ContactForm.models import Message

@override_settings(
    DEBUG=True,
    SECRET_KEY='test-key-12345',
    CONTACT_FORM_NAME_MAXLENGTH=120,
    CONTACT_FORM_COMPANY_MAXLENGTH=180,
    CONTACT_FORM_EMAIL_MAXLENGTH=320,
    CONTACT_FORM_EMAIL_REGEX="^([a-zA-Z0-9_+-]+\.)*[a-zA-Z0-9_+-]+@([a-zA-Z0-9-]+\.)+[a-zA-Z]+$",
    CONTACT_FORM_MESSAGE_CONTENT_MAXLENGTH=1000,
    CONTACT_FORM_MESSAGE_CONTENT_MINLENGTH=20,
)    
class MessageTestCase(TestCase):
    
    def test_create_valid_message(self):
        message = Message.objects.create(
            name="Joe Smith",
            company="JoeCorp",
            email="joe.smith@joecorp.com",
            content="Hi! Joe Smith here, CEO and founder of JoeCorp..."
        )
        self.assertIn(message, Message.objects.all())
    
    def test_create_message_no_name_fails(self):
        def create_message():
            message = Message.objects.create(
                name="",
                company="JoeCorp",
                email="joe.smith@joecorp.com",
                content="Hi! Joe Smith here, CEO and founder of JoeCorp..."
            )
        self.assertRaises(IntegrityError, create_message)
                    
