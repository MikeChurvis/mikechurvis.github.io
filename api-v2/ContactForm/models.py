from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models.functions import Length

from config_helper import validate_settings

validate_settings(settings, {
    'CONTACTFORM_NAME_MAX_LENGTH',
    'CONTACTFORM_ORGANIZATION_MAX_LENGTH',
    'CONTACTFORM_EMAIL_MAX_LENGTH',
    'CONTACTFORM_EMAIL_REGULAR_EXPRESSION',
    'CONTACTFORM_MESSAGE_MIN_LENGTH',
    'CONTACTFORM_MESSAGE_MAX_LENGTH',
})
models.CharField.register_lookup(Length)
models.TextField.register_lookup(Length)


class AdminNotificationStatus(models.TextChoices):
    PENDING = 'pending', 'Not yet forwarded, but queued to do so.'
    SUCCESS = 'success', 'Forwarded without error.'
    ERROR = 'error', 'ERROR! see detail field.'


class ContactFormEntry(models.Model):
    name = models.CharField(max_length=settings.CONTACTFORM_NAME_MAX_LENGTH)
    organization = models.CharField(max_length=settings.CONTACTFORM_ORGANIZATION_MAX_LENGTH, blank=True)
    email = models.EmailField(max_length=settings.CONTACTFORM_EMAIL_MAX_LENGTH)
    message = models.TextField(
        max_length=settings.CONTACTFORM_MESSAGE_MAX_LENGTH,
        validators=[MinLengthValidator(settings.CONTACTFORM_MESSAGE_MIN_LENGTH)]
    )
    datetime_received = models.DateTimeField(auto_now_add=True)
    admin_notification_status = models.CharField(
        choices=AdminNotificationStatus.choices,
        default=AdminNotificationStatus.PENDING,
        max_length=10
    )
    admin_notification_detail = models.TextField(null=True, blank=True)

    email_config_slug = 'contact-form'

    def __str__(self):
        return f'<{self.datetime_received}> {self.name} ({self.email}): "{self.message[:41]}"'

    class Meta:
        verbose_name = 'Contact Form Entry'
        verbose_name_plural = 'Contact Form Entries'

        constraints = [
            models.CheckConstraint(
                name=f'CHECK__ContactFormEntry__name__length_GT_0',
                check=models.Q(name__length__gt=0),
            ),
            models.CheckConstraint(
                name=f'CHECK__ContactFormEntry__name__length_LTE_{settings.CONTACTFORM_NAME_MAX_LENGTH}',
                check=models.Q(name__length__lte=settings.CONTACTFORM_NAME_MAX_LENGTH),
            ),
            models.CheckConstraint(
                name=f'CHECK__ContactFormEntry__organization__length_LTE_'
                     f'{settings.CONTACTFORM_ORGANIZATION_MAX_LENGTH}',
                check=models.Q(organization__length__lte=settings.CONTACTFORM_ORGANIZATION_MAX_LENGTH),
            ),
            models.CheckConstraint(
                name=f'CHECK__ContactFormEntry__email__length_GT_0',
                check=models.Q(email__length__gt=0),
            ),
            models.CheckConstraint(
                name=f'CHECK__ContactFormEntry__email__length_LTE_{settings.CONTACTFORM_EMAIL_MAX_LENGTH}',
                check=models.Q(email__length__lte=settings.CONTACTFORM_EMAIL_MAX_LENGTH),
            ),
            models.CheckConstraint(
                name=f'CHECK__ContactFormEntry__message__length_GTE_{settings.CONTACTFORM_MESSAGE_MIN_LENGTH}',
                check=models.Q(message__length__gte=settings.CONTACTFORM_MESSAGE_MIN_LENGTH),
            ),
            models.CheckConstraint(
                name=f'CHECK__ContactFormEntry__message__length_LTE_{settings.CONTACTFORM_MESSAGE_MAX_LENGTH}',
                check=models.Q(message__length__lte=settings.CONTACTFORM_MESSAGE_MAX_LENGTH),
            ),
        ]

        ordering = ['datetime_received']
