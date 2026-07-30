from abc import ABC, abstractmethod


class BaseSearchAdapter(ABC):

    @abstractmethod
    def search(self, query: str):
        """
        Returns raw search results.
        """
        pass