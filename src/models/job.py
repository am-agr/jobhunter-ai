from dataclasses import dataclass, field
from typing import List


@dataclass
class Job:
    company: str
    role: str
    location: str
    url: str
    source: str

    posted_date: str = ""
    employment_type: str = ""
    experience: str = ""

    description: str = ""

    skills: List[str] = field(default_factory=list)

    match_score: int = 0

    status: str = "NEW"