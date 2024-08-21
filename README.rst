=========
cel-in-py
=========

**This project is not ready for production yet.**

.. image:: https://img.shields.io/pypi/v/cel_in_py.svg
        :target: https://pypi.python.org/pypi/cel_in_py

.. image:: https://img.shields.io/travis/yottanami/cel_in_py.svg
        :target: https://travis-ci.com/yottanami/cel_in_py

.. image:: https://readthedocs.org/projects/cel-in-py/badge/?version=latest
        :target: https://cel-in-py.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status



Parser and evaluator for CEL in Python using ANTLR4

This library provides parser and evaluator for Common Expression Language (CEL) expressions in Python projects. CEL is a language developed by Google that allows for safe and fast evaluation of expressions in a wide variety of applications, such as policy engines, rule engines, and more.


* Documentation: https://cel-in-py.readthedocs.io.


Features
--------

- Parse and evaluate CEL expressions directly within TypeScript projects.
- Support for common arithmetic operations, logical operations, and comparisons.
- Extensible design for adding custom functions and variables.
- Error handling during parsing with custom error listeners.
- Context-based evaluation to support dynamic expression evaluation.


Installation
------------

You can install cel-in-py via pip:


.. code-block:: python

   pip install cel_in_py



Usage
-----

Evaluate expression
^^^^^^^^^^^^^^^^^^^

To use the CEL parser and evaluator, you can instantiate the Runtime class with a CEL expression, and then evaluate it with a given context.

.. code-block:: python

    from cel_in_py import Runtime
 
    # Define a CEL expression
    expression = "a + b * 10"
 
    # Create a Runtime instance with the expression
    runtime = Runtime(expression)

    # Define a context with variables
    context = {
      "a": 5,
      "b": 3
    }

    # Evaluate the expression with the context
    result = runtime.evaluate(context)
    print(f"Result: {result}")  # Output: Result: 35



Parsing Valiation

^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from cel_in_py import Runtime

    # Define a CEL expression
    expression = "a + b * 10"

    # Create a Runtime instance with the expression
    runtime = Runtime(expression)

    # Define a context with variables
    context = {
        "a": 5,
        "b": 3
    }

    # Evaluate the expression with the context
    result = runtime.evaluate(context)

    print(f"Result: {result}")  # Output: Result: 35


Advanced Usage
^^^^^^^^^^^^^^

The VisitorInterp class allows for extending the functionality by adding custom functions or modifying the evaluation logic.

.. code-block:: python

    from cel_in_py.visitor_interp import VisitorInterp

    # Define a custom function
    def custom_function(x):
        return x * x

    # Extend the visitor with the custom function
    class CustomVisitor(VisitorInterp):
        def __init__(self, context):
            super().__init__(context)
            self.function_registry["custom_function"] = custom_function

    # Use the custom visitor in the runtime
    expression = "custom_function(5)"
    runtime = Runtime(expression)
    visitor = CustomVisitor({})
    result = visitor.visit(runtime.ast)

    print(f"Result: {result}")  # Output: Result: 25
