import pytest
from cel_in_py import Runtime

def test_visitor_interp():
    runtime = Runtime("1 + 2")
    assert runtime.evaluate({}) == 3

def test_subtraction():
    runtime = Runtime("5 - 3")
    assert runtime.evaluate({}) == 2

def test_multiplication():
    runtime = Runtime("4 * 2")
    assert runtime.evaluate({}) == 8

def test_division():
    runtime = Runtime("8 / 2")
    assert runtime.evaluate({}) == 4.0

def test_modulo():
    runtime = Runtime("10 % 3")
    assert runtime.evaluate({}) == 1

def test_arithmetic_precedence():
    runtime = Runtime("2 + 3 * 4")
    assert runtime.evaluate({}) == 14

def test_parentheses_precedence():
    runtime = Runtime("(2 + 3) * 4")
    assert runtime.evaluate({}) == 20

def test_logical_and():
    runtime = Runtime("true && false")
    assert runtime.evaluate({}) is False

def test_logical_or():
    runtime = Runtime("true || false")
    assert runtime.evaluate({}) is True

def test_logical_not():
    runtime = Runtime("!true")
    assert runtime.evaluate({}) is False

def test_comparison_equal():
    runtime = Runtime("5 == 5")
    assert runtime.evaluate({}) is True

def test_comparison_not_equal():
    runtime = Runtime("5 != 4")
    assert runtime.evaluate({}) is True

def test_comparison_greater():
    runtime = Runtime("6 > 4")
    assert runtime.evaluate({}) is True

def test_comparison_less():
    runtime = Runtime("3 < 4")
    assert runtime.evaluate({}) is True

def test_comparison_greater_equal():
    runtime = Runtime("5 >= 5")
    assert runtime.evaluate({}) is True

def test_comparison_less_equal():
    runtime = Runtime("3 <= 4")
    assert runtime.evaluate({}) is True

def test_conditional_operator():
    runtime = Runtime("5 > 3 ? 10 : 20")
    assert runtime.evaluate({}) == 10

def test_string_concatenation():
    runtime = Runtime('"Hello" + " " + "World"')
    assert runtime.evaluate({}) == "Hello World"

def test_function_call_min():
    runtime = Runtime("min(3, 5)")
    assert runtime.evaluate({}) == 3

def test_function_call_max():
    runtime = Runtime("max(3, 5)")
    assert runtime.evaluate({}) == 5

def test_function_call_length():
    runtime = Runtime('length("Hello")')
    assert runtime.evaluate({}) == 5

def test_nested_function_calls():
    runtime = Runtime('upper(replace("hello world", "world", "CEL"))')
    assert runtime.evaluate({}) == "HELLO CEL"

def test_list_creation():
    runtime = Runtime("[1, 2, 3]")
    assert runtime.evaluate({}) == [1, 2, 3]

def test_map_creation():
    runtime = Runtime('{"key1": "value1", "key2": "value2"}')
    assert runtime.evaluate({}) == {"key1": "value1", "key2": "value2"}

def test_list_indexing():
    runtime = Runtime("[1, 2, 3][1]")
    assert runtime.evaluate({}) == 2

def test_map_access():
    runtime = Runtime('{"key1": "value1", "key2": "value2"}["key2"]')
    assert runtime.evaluate({}) == "value2"

def test_bool_true():
    runtime = Runtime("true")
    assert runtime.evaluate({}) is True

def test_bool_false():
    runtime = Runtime("false")
    assert runtime.evaluate({}) is False

def test_null():
    runtime = Runtime("null")
    assert runtime.evaluate({}) is None

def test_complex_expression():
    runtime = Runtime('(5 + 2) * 3 - min(4, 2) / 2 > 10')
    assert runtime.evaluate({}) is True
