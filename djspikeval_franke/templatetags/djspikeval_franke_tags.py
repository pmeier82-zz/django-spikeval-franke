# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import template
from django.db.models.aggregates import Sum
from ..models import ResultFranke

__author__ = "pmeier82"

register = template.Library()
res_tbl_nam = ResultFranke.__name__.lower()


# FILTERS
@register.filter
def sort(query_set):
    """return the sorted queryset"""

    return query_set.order_by("{}__unit_gt".format(res_tbl_nam))


@register.filter
def summary(query_set):
    """summary from result queryset"""

    # early exit
    if not query_set:
        return None

    # aggregate
    return query_set.aggregate(
        KS=Sum("{}__KS".format(res_tbl_nam)),
        KSO=Sum("{}__KSO".format(res_tbl_nam)),

        FS=Sum("{}__FS".format(res_tbl_nam)),

        TP=Sum("{}__TP".format(res_tbl_nam)),
        TPO=Sum("{}__TPO".format(res_tbl_nam)),

        FPAE=Sum("{}__FPAE".format(res_tbl_nam)),
        FPAOE=Sum("{}__FPAOE".format(res_tbl_nam)),
        FP=Sum("{}__FP".format(res_tbl_nam)),

        FPA=Sum("{}__FPA".format(res_tbl_nam)),
        FPAO=Sum("{}__FPAO".format(res_tbl_nam)),

        FN=Sum("{}__FN".format(res_tbl_nam)),
        FNO=Sum("{}__FNO".format(res_tbl_nam)))


@register.filter
def summary_table(query_set):
    """summary table from result queryset"""

    # early exit
    if not query_set:
        return None
    qs_sum = summary(query_set)
    if not qs_sum:
        return None

    # return dict
    return {"FP": qs_sum["FP"],

            "FN": qs_sum["FN"] + qs_sum["FNO"],
            'FNno': qs_sum["FN"],
            "FNo": qs_sum["FNO"],

            "FPAE": qs_sum["FPAE"] + qs_sum["FPAOE"],
            "FPAEno": qs_sum["FPAE"],
            "FPAEo": qs_sum["FPAOE"],

            "error_sum": qs_sum["FP"] + qs_sum["FN"] + qs_sum["FPAE"]}


@register.filter
def summary_short(query_set):
    """short summary from result queryset"""

    # early exit
    if not query_set:
        return None
    qs_sum = summary(query_set)
    if not qs_sum:
        return None

    # result dict
    return {
        "TP": (qs_sum["TP"] + qs_sum["TPO"]) / float(qs_sum["KS"]) * 100,
        "FP": (qs_sum["FS"] - qs_sum["TP"] - qs_sum["TPO"]) / float(qs_sum["KS"]) * 100}


if __name__ == "__main__":
    pass
