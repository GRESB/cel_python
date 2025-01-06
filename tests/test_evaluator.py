# tests/test_evaluator.py

import pytest
from typing import ContextManager

from datetime import datetime, date, timezone
from cel_python.runtime import Runtime

@pytest.mark.parametrize("expression, context, expected", [
    # Basic Arithmetic
    ("2 + 3", {}, 5),
    ("a + b", {'a': 2, 'b': 3}, 5),
    ("a + b > c", {'a': 2, 'b': 3, 'c': 4}, True),
    ("(2 + 3) * (4 - 1)", {}, 15),
    ("2 * (3 + (4 - 1))", {}, 12),
    ("2 * (3 + 4) - (10 / 2) + 7", {}, 16),

    # Comparison
    ("a == b", {'a': 2, 'b': 2}, True),
    ("a > b && b < c || a == c", {'a': 5, 'b': 3, 'c': 5}, True),

    # Logical Operations
    ("!true", {}, False),
    ("!(a > b) || (c < d && e >= f)", {'a': 3, 'b': 5, 'c': 2, 'd': 4, 'e': 5, 'f': 5}, True),

    # String Operations
    ("'Hello ' + 'World'", {}, "Hello World"),
    ("\"hello\" + \" \" + \"world\"", {}, "hello world"),

    # Ternary Operator
    # ("a > b ? 'greater' : 'lesser'", {'a': 5, 'b': 3}, 'greater'),

    # Error Cases
    ("x", {}, pytest.raises(Exception, match="Variable 'x' is not defined")),
    ("undefinedVar + 1", {}, pytest.raises(Exception, match="Variable 'undefinedVar' is not defined")),
    #("a > b && b < c || a == c", {'a': 5, 'b': 3.3, 'c': 5}, pytest.raises(Exception, match="Mismatching types: Cannot compare 'int' and 'float' with '>'")),
    ("1 || 2.3 == 4.0", {}, pytest.raises(Exception, match="Logical '||' requires boolean operands, but got 'int' and 'bool'")),
    #("1 <= 2.3", {}, pytest.raises(Exception, match="Mismatching types: Cannot compare 'int' and 'float' with '<='")),
    #("2 * (3 + 4.0)", {}, pytest.raises(Exception, match="Operator '+' requires matching types, but got 'int' and 'float'")),
    ("true && 1", {}, pytest.raises(Exception, match="Logical '&&' requires boolean operands, but got 'bool' and 'int'")),
    ("'string' + 123", {}, pytest.raises(Exception, match="Operator '\+' requires matching types, but got 'string' and 'int'")),
    ("true == 'false'", {}, pytest.raises(Exception, match="Mismatching types: Cannot compare 'bool' and 'string' with '=='")),
])
def test_evaluator(expression, context, expected):
    runtime = Runtime(expression)
    if isinstance(expected, ContextManager):
        with expected:
            runtime.evaluate(context)
    else:
        result = runtime.evaluate(context)
        assert result == expected
