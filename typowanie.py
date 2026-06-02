from typing import Optional
from collections.abc import Sequence

def get_user(user_id: int) -> Optional[dict]:
    pass

def process_items(items: Sequence[str]) -> list[str]:
    return [item.upper() for item in items]

