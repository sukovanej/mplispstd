import math
from typing import List
from mplisp import evaluator

def floor(args: List, _):
    """Evaluates expression (floor a) as {math.floor(a)}"""
    if len(args) != 1:
        evaluator.error("wrong number of arguments, got {}, 1 expected".format(
            str(len(args))))

    return math.floor(evaluator.evaluate_node(args[0]))
