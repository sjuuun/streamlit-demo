from math import sqrt
from typing import Dict
from scipy import stats


def calculate_z_test(n_c: int, conversion_c: int, n_v: int, conversion_v: int) -> Dict:
    if n_c < conversion_c or n_v < conversion_v:
        return {}

    cvr_c = conversion_c / n_c
    cvr_v = conversion_v / n_v

    z = (cvr_v - cvr_c) / sqrt(cvr_v * (1 - cvr_v) / n_v + cvr_c * (1 - cvr_c) / n_c)

    stat_sig = stats.norm.cdf(abs(z))
    p_value = 1 - stat_sig

    return {
        "cvr_c": cvr_c,
        "cvr_v": cvr_v,
        "cvr_change": cvr_v - cvr_c,
        "cvr_relative_change": (cvr_v - cvr_c) / cvr_c,
        "z_score": z,
        "p_value": p_value,
        "stat_sig": stat_sig,
        "is_statistically_significant": stat_sig >= 0.95,
        "is_increase": (cvr_v - cvr_c) > 0
    }


def calculate_t_test(n_c: int, mean_c: float, variance_c: float, n_v: int, mean_v: float, variance_v: float) -> Dict:
    vmr_c = variance_c / n_c
    vmr_v = variance_v / n_v

    t = (mean_v - mean_c) / sqrt(vmr_v + vmr_c)
    dof = pow(vmr_v + vmr_c, 2) / ((pow(vmr_v, 2) / (n_v - 1)) + (pow(vmr_c, 2) / (n_c - 1)))

    p_value = stats.t.cdf(-abs(t), dof) * 2
    stat_sig = 1 - p_value

    return {
        "mean_change": mean_v - mean_c,
        "mean_relative_change": (mean_v - mean_c) / mean_c,
        "t_score": t,
        "degrees_of_freedom": dof,
        "p_value": p_value,
        "stat_sig": stat_sig,
        "is_statistically_significant": stat_sig >= 0.95,
        "is_increase": (mean_v - mean_c) > 0
    }
