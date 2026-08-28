from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class DNA:
    """Copy Anything 的统一中间结构。"""

    type: str
    source: str
    summary: str = ""
    structure: dict[str, Any] = field(default_factory=dict)
    patterns: list[str] = field(default_factory=list)
    rebuild_plan: list[str] = field(default_factory=list)
    verification: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
