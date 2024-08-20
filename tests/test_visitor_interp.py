import pytest
from cel_in_py import Runtime

def test_simple_arithmetic_expression():
    runtime = Runtime("2 + 3")
    assert runtime.evaluate({}) == 5

def test_expression_with_variables():
    runtime = Runtime("a + b")
    context = {'a': 2, 'b': 3}
    assert runtime.evaluate(context) == 5

def test_comparison_expression():
    runtime = Runtime("a == b")
    context = {'a': 2, 'b': 2}
    assert runtime.evaluate(context) is True

def test_arithmetic_and_comparison():
    runtime = Runtime("a + b > c")
    context = {'a': 2, 'b': 3, 'c': 4}
    assert runtime.evaluate(context) is True

def test_undefined_variable():
    runtime = Runtime("x")
    with pytest.raises(Exception, match="Variable 'x' is not defined"):
        runtime.evaluate({})

def test_nested_arithmetic_expressions():
    runtime = Runtime("(2 + 3) * (4 - 1)")
    assert runtime.evaluate({}) == 15

def test_logical_and_or():
    runtime = Runtime("a > b && b < c || a == c")
    context = {'a': 5, 'b': 3, 'c': 5}
    assert runtime.evaluate(context) is True

def test_ternary_conditional_expression():
    runtime = Runtime("a > b ? 'greater' : 'lesser'")
    context = {'a': 5, 'b': 3}
    assert runtime.evaluate(context) == 'greater'

def test_string_concatenation():
    runtime = Runtime("'Hello ' + 'World'")
    assert runtime.evaluate({}) == "Hello World"

def test_nested_parentheses():
    runtime = Runtime("2 * (3 + (4 - 1))")
    assert runtime.evaluate({}) == 12

def test_logical_negation():
    runtime = Runtime("!true")
    assert runtime.evaluate({}) is False

def test_nested_logical_operations():
    runtime = Runtime("!(a > b) || (c < d && e >= f)")
    context = {'a': 3, 'b': 5, 'c': 2, 'd': 4, 'e': 5, 'f': 5}
    assert runtime.evaluate(context) is True

def test_complex_numerical_expressions():
    runtime = Runtime("2 * (3 + 4) - (10 / 2) + 7")
    assert runtime.evaluate({}) == 16

def test_string_concatenation_multiple_parts():
    runtime = Runtime('"hello" + " " + "world"')
    assert runtime.evaluate({}) == "hello world"

def test_ternary_operator():
    runtime = Runtime('true ? "yes" : "no"')
    assert runtime.evaluate({}) == "yes"
