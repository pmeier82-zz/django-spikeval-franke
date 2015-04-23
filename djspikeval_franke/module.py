# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from spikeval.module import ModMetricFranke, ModuleExecutionError
from .models.result import ResultFranke

__author__ = "pmeier82"
__all__ = ["ModuleFranke"]


def toint(val):
    # if type(val) == type(""):
    res = int(float(val))
    return res


class ModuleFranke(ModMetricFranke):
    """spikeval module for the franke metric"""

    # RESULT_TYPES
    # MRTable,  # res_table - this is what we will save!
    # MRTable,  # similarity_matrix
    # MRTable,  # shift_matrix
    # MRTable,  # sp.atleast_2d(delta_shift)
    # MRDict,   # alignment
    # MRDict,   # O
    # MRTable,  # spike_no_assignment_matrix
    # MRDict,   # EL
    # MRDict,   # GL
    # MRTable,  # sp.atleast_2d(TP)
    # MRTable,  # sp.atleast_2d(TPO)
    # MRTable,  # sp.atleast_2d(FPA)
    # MRTable,  # sp.atleast_2d(FPAO)
    # MRTable,  # sp.atleast_2d(FN)
    # MRTable,  # sp.atleast_2d(FNO)
    # MRTable,  # sp.atleast_2d(FP)
    # MRTable,  # sp.atleast_2d(u_k2f)
    # MRTable,  # sp.atleast_2d(u_f2k)

    def save(self, mod, ana):
        """save django result entities"""

        # check for results
        if self._stage != 3:
            raise ModuleExecutionError("save initiated when module was not finalised!")

        # result saving
        for row in self.result[0].value:
            res_entity = ResultFranke(analysis=ana, module=mod)
            res_entity.unit_gt = row[0]
            res_entity.unit_an = row[1]
            res_entity.KS = toint(row[2])
            res_entity.KSO = toint(row[3])
            res_entity.FS = toint(row[4])
            res_entity.TP = toint(row[5])
            res_entity.TPO = toint(row[6])
            res_entity.FPA = toint(row[7])
            res_entity.FPAE = toint(row[8])
            res_entity.FPAO = toint(row[9])
            res_entity.FPAOE = toint(row[10])
            res_entity.FN = toint(row[11])
            res_entity.FNO = toint(row[12])
            res_entity.FP = toint(row[13])
            res_entity.save()


if __name__ == "__main__":
    pass
