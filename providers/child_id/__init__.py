from faker.providers import BaseProvider
from typing import Optional


class Provider(BaseProvider):
    def child_id(self, min: Optional[int] = 0, max: Optional[int] = 1000000) -> str:
        return self.random_int(min=min, max=max)
