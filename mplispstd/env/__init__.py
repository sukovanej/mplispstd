"""
Environment library
5. 2. 2018, Milan Suk
"""
from typing import List
from mplisp import evaluator


def local_env(args: List, node):
    """get local environment"""
    return node.parent.local_env.symbols

