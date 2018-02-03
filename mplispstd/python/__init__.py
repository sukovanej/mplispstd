from typing import List
from mplisp import evaluator


def python_apply(args: List, _):
    """Call python function from mplisp"""
    if len(args) < 1:
        evaluator.error("at least 1 parameters expected, {} given".format(len(args)))

    func_name = args[0].value

    params = evaluator.evaluate_parallel_args(args[1:])

    if func_name not in globals():
        evaluator.error("callable {} not found".format(func_name))

    func_object = globals()[func_name]

    if callable(func_object):
        evaluator.error("{} is not callable".format(func_name))

    return func_object(*params)
