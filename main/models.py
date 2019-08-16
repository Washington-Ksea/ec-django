from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator, RegexValidator
from django.utils.translation import gettext_lazy as _ #翻訳機能など国際化のため


class User(AbstractUser):
    """Custom user to perform authentication by email """
    username_validator = UnicodeUsernameValidator()
    username_regex = RegexValidator(regex=r'^[a-zA-Z0-9][a-zA-Z0-9\-]+', message="ユーザネームに使用できない文字が指定されています。")
    username = models.CharField(_('username'), max_length=150, unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator, username_regex, MinLengthValidator(5)],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField('emial address', unique=True)

    
        