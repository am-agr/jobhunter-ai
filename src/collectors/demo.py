from src.collectors.base import BaseCollector
from src.models.job import Job


class DemoCollector(BaseCollector):

    def collect(self):

        return [

            Job(
                company="Deloitte",
                role="Strategy Consultant",
                location="Gurgaon",
                source="Demo",
                url="https://example.com"
            ),

            Job(
                company="American Express",
                role="Business Strategy Analyst",
                location="Gurgaon",
                source="Demo",
                url="https://example.com"
            )

        ]