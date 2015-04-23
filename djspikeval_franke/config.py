# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

__author__ = "pmeier82"


class DjSpikevalFrankeAppConfig(AppConfig):
    label = "djspikeval_franke"
    name = "djspikeval_franke"
    verbose_name = _("Django Spikeval - Metric by F. Franke")

    def ready(self):
        # import all parts of the application that need to be exposed
        pass


if __name__ == "__main__":
    pass
