# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from djspikeval.models import Result

__all__ = ["ResultFranke"]


class ResultFranke(Result):
    """franke metric result entity"""

    # meta
    class Meta:
        app_label = "djspikeval_franke"
        verbose_name = "Result(Franke)"
        verbose_name_plural = "Results(Franke)"

    # fields
    unit_gt = models.CharField(max_length=255)
    unit_an = models.CharField(max_length=255)
    KS = models.IntegerField(default=0)
    KSO = models.IntegerField(default=0)
    FS = models.IntegerField(default=0)
    TP = models.IntegerField(default=0)
    TPO = models.IntegerField(default=0)
    FPA = models.IntegerField(default=0)
    FPAE = models.IntegerField(default=0)
    FPAO = models.IntegerField(default=0)
    FPAOE = models.IntegerField(default=0)
    FN = models.IntegerField(default=0)
    FNO = models.IntegerField(default=0)
    FP = models.IntegerField(default=0)

    # interface
    def display(self):
        """display list of numerical results"""

        return [self.unit_gt,
                self.unit_an,
                self.KS,
                self.KS - self.KSO,
                self.KSO,
                self.TP + self.TPO,
                self.TP,
                self.TPO,
                self.FPAE,
                self.FPAOE,
                self.FP,
                self.FPA,
                self.FPAO,
                self.FN,
                self.FNO]

    # interface
    def __unicode__(self):
        return unicode("{} gt={} an={}".format(super(ResultFranke, self).__unicode__(), self.unit_gt, self.unit_an))


if __name__ == "__main__":
    pass
