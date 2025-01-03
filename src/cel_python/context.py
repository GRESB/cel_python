import logging
from typing import Any, Dict

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Context:
    def __init__(self, variables: Dict[str, Any], types: Dict[str, str] = None):
        self.variables = variables
        self.types = types or {}
        logger.debug(f"Context initialized with variables: {self.variables} and types: {self.types}")

    def hasVariable(self, name: str) -> bool:
        has_var = name in self.variables
        logger.debug(f"Context.hasVariable('{name}') = {has_var}")
        return has_var

    def getVariable(self, name: str) -> Any:
        value = self.variables.get(name)
        logger.debug(f"Context.getVariable('{name}') = {value}")
        return value

    def setType(self, name: str, type_: str):
        self.types[name] = type_
        logger.debug(f"Context.setType('{name}', '{type_}')")

    def getType(self, name: str) -> str:
        type_ = self.types.get(name)
        logger.debug(f"Context.getType('{name}') = {type_}")
        return type_
