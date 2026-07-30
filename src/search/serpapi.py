import os
import requests

from src.search.base import BaseSearchAdapter
from src.models.search_result import SearchResult


class SerpApiSearch(BaseSearchAdapter):

    BASE_URL = "https://serpapi.com/search.json"

    def search(self, query: str):

        api_key = os.getenv("SERPAPI_API_KEY")

        if not api_key:
            raise ValueError("SERPAPI_API_KEY not found.")

        params = {
            "engine": "google",
            "q": query,
            "api_key": api_key,
            "num": 10
        }

        response = requests.get(self.BASE_URL, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()

        results = []

        for item in data.get("organic_results", []):

            results.append(
                SearchResult(
                    title=item.get("title", ""),
                    url=item.get("link", ""),
                    source="SerpAPI"
                )
            )

        return results