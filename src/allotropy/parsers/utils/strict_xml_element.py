from __future__ import annotations

from xml.etree import ElementTree

# xml fromstring is vulnerable so defusedxml version is used instead
from defusedxml.ElementTree import fromstring

from allotropy.parsers.utils.values import assert_not_none, try_float


class StrictXmlElement:
    @classmethod
    def create_from_bytes(cls, data: bytes) -> StrictXmlElement:
        return StrictXmlElement(fromstring(data))

    def __init__(self, element: ElementTree.Element):
        self.element = element

    def find_or_none(self, name: str) -> StrictXmlElement | None:
        element = self.element.find(name)
        return StrictXmlElement(element) if element is not None else None

    def find(self, name: str) -> StrictXmlElement:
        return assert_not_none(
            self.find_or_none(name),
            msg=f"Unable to find '{name}' in xml file contents",
        )

    def recursive_find_or_none(self, names: list[str]) -> StrictXmlElement | None:
        if len(names) == 0:
            return self
        name, *sub_names = names
        if element := self.find_or_none(name):
            return element.recursive_find_or_none(sub_names)
        return None

    def recursive_find(self, names: list[str]) -> StrictXmlElement:
        if len(names) == 0:
            return self
        name, *sub_names = names
        return self.find(name).recursive_find(sub_names)

    def findall(self, name: str) -> list[StrictXmlElement]:
        return [StrictXmlElement(element) for element in self.element.findall(name)]

    def get_attr(self, name: str) -> str:
        return str(
            assert_not_none(
                self.element.get(name),
                msg=f"Unable to find '{name}' in xml file contents",
            )
        )

    def get_text(self) -> str:
        return str(self.element.text)

    def get_float(self, name: str) -> float:
        return try_float(self.get_text(), name)