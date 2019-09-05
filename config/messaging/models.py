# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from fcm.models import AbstractDevice

class MyDevice(AbstractDevice):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)

