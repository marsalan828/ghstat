from pydantic import BaseModel
from dataclasses import dataclass

class Repo(BaseModel):
    name: str
    stargazers_count: int
    language: str | None = None
    html_url: str

@dataclass(frozen=True)
class RetryPolicy:
    max_attempts: int = 5
    base_delay: float = 0.5
    max_delay: float = 30.0
