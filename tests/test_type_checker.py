import pytest
from cel_python.runtime import Runtime

@pytest.mark.parametrize(
    "expression,context,expected_success,error_substrings",
    [
        # Successful type checks
        ("5", {}, True, []),
        ("3.14", {}, True, []),
        ('"hello"', {}, True, []),
        ("true", {}, True, []),
        ("false", {}, True, []),
        ("[1, 2, 3]", {}, True, []),
        ("5 + 3", {}, True, []),
        ("a + b", {"a": 2, "b": 4}, True, []),
        (
            "user.age >= 18",
            {"user": {"name": "Alice", "age": 20}},
            True,
            []
        ),
        (
            "user.age.really >= 18",
            {"user": {"name": "Alice", "age": {"really": 20}}},
            True,
            []
        ),
        ("!true", {}, True, []),

        # Failing type checks
        (
            "a + b",
            {"a": 2, "b": "4"},
            False,
            ["Operator '+' requires matching types", "'int' and 'string'"]
        ),
        (
            "5.5 + 3",
            {},
            False,
            ["'float' and 'int'"]
        ),
        (
            "5 + 'hello'",
            {},
            False,
            ["'int' and 'string'"]
        ),
        (
            "max('string', 1)",
            {},
            False,
            ["Argument 1 of function 'max' expects type 'int', but got 'string'"]
        ),
        (
            "!5",
            {},
            False,
            ["requires boolean operand"]
        ),
        (
            "true && 5",
            {},
            False,
            ["requires boolean operands"]
        ),
        (
            "2 == '2'",
            {},
            False,
            ["Mismatching types"]
        ),
        (
            "'23' == 23",
            {},
            False,
            ["Mismatching types"]
        ),
        (
            "'23' == true",
            {},
            False,
            ["Mismatching types"]
        ),
        (
            "'true' == true",
            {},
            False,
            ["Mismatching types"]
        ),
        (
            "1 == 1.2",
            {},
            False,
            ["Mismatching types"]
        ),
    ],
)
def test_type_check(expression, context, expected_success, error_substrings):
    result = Runtime.type_check(expression, context)
    assert result["success"] is expected_success

    if expected_success:
        assert "error" not in result
    else:
        assert "error" in result
        for substring in error_substrings:
            assert substring in result["error"]
