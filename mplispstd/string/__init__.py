"""
String library
5. 2. 2018, Milan Suk
"""
from typing import List
from mplisp import evaluator


def substr(args: List, _):
    """python str[x:y] equiv"""
    if not args:
        evaluator.error("max 3 arguments expected, {} given".format(len(args)))

    params = evaluator.evaluate_parallel_args(args)

    if not isinstance(params[0], str):
        evaluator.error("first param must be of type str, {} given".format(type(params[0])))

    if len(params) == 1:
        return params[0]
    if len(params) == 2:
        if not isinstance(params[1], int):
            evaluator.error("second param must be of type int")

        return params[0][params[1]:]
    elif len(params) == 3:
        if not isinstance(params[2], int):
            evaluator.error("third param must be of type int")

        return params[0][params[1]:params[2]]

