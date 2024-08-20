import pytest
from cel_in_py import Runtime
from datetime import datetime

@pytest.mark.parametrize("expression, context, expected", [
    # Arithmetic Functions
    ("min(a, b)", {'a': 10, 'b': 20}, 10),
    ("max(a, b)", {'a': 10, 'b': 20}, 20),
    ("abs(a)", {'a': -10}, 10),
    ("ceil(a)", {'a': 10.1}, 11),
    ("floor(a)", {'a': 10.9}, 10),
    ("round(a)", {'a': 10.7}, 11),

    # String Functions
    ("contains(s, 'world')", {'s': "hello world"}, True),
    ("endsWith(s, 'world')", {'s': "hello world"}, True),
    ("indexOf(s, 'world')", {'s': "hello world"}, 6),
    ("length(s)", {'s': "hello world"}, 11),
    ("lower(s)", {'s': "HELLO WORLD"}, "hello world"),
    ("replace(s, 'world', 'everyone')", {'s': "hello world"}, "hello everyone"),
    ("split(s, ' ')", {'s': "hello world"}, ["hello", "world"]),
    ("startsWith(s, 'hello')", {'s': "hello world"}, True),
    ("upper(s)", {'s': "hello world"}, "HELLO WORLD"),

    # List Functions
    ("size(lst)", {'lst': [1, 2, 3]}, 3),

    # Type Conversion Functions
    ("int(a)", {'a': "10"}, 10),
    ("uint(a)", {'a': "10"}, 10),
    ("double(a)", {'a': "10.5"}, 10.5),
    ("string(a)", {'a': 10}, "10"),
    ("bool(a)", {'a': 1}, True),

    # Null Handling Functions
    ("existsOne(lst)", {'lst': [None, 1, None]}, True),

    # Date/Time Functions
    ("timestamp()", {}, str),  # Expecting a string output
    ("duration(a)", {'a': 10}, "10s"),
    ("time(2024, 8, 2, 12, 0, 0, 0)", {}, "2024-08-02T12:00:00.000000Z"),
    ("date(2024, 8, 2)", {}, "2024-08-02"),
    ("getFullYear(timestamp)", {'timestamp': datetime(2024, 8, 2)}, 2024),
    ("getMonth(timestamp)", {'timestamp': datetime(2024, 8, 2)}, 7),  # August is month 7 (0-indexed)
    ("getDate(timestamp)", {'timestamp': datetime(2024, 8, 2)}, 2),
    ("getHours(timestamp)", {'timestamp': datetime(2024, 8, 2, 12)}, 12),
    ("getMinutes(timestamp)", {'timestamp': datetime(2024, 8, 2, 12, 0)}, 0),
    ("getSeconds(timestamp)", {'timestamp': datetime(2024, 8, 2, 12, 0, 0)}, 0),
])
def test_builtin_functions(expression, context, expected):
    runtime = Runtime(expression)
    result = runtime.evaluate(context)

    if isinstance(expected, type):
        assert isinstance(result, expected)        
    else:
        assert result == expected
