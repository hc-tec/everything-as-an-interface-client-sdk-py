from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, Iterator, List, Mapping, MutableMapping, Optional, Tuple


# Copy from src/core/task_params.py
@dataclass
class TaskParams:
    """Task configuration container with extensibility.

    Common options are exposed as typed attributes, while any additional
    plugin-specific options are stored in ``extra``. The object behaves like
    a read-only mapping that merges common fields and ``extra``.
    """

    # Common, strongly-typed fields
    headless: Optional[bool] = None
    cookie_ids: List[str] = field(default_factory=list)
    viewport: Optional[Dict[str, int]] = None
    user_agent: Optional[str] = None
    extra_http_headers: Optional[Dict[str, str]] = None
    close_page_when_task_finished: bool = False

    # Don't need [extra] field in client_sdk

# Copy from src/services/base_service.py
@dataclass
class ServiceParams:
    """Common configuration for services.

    Attributes:
        response_timeout_sec: Max seconds to wait for a response event.
        delay_ms: Delay between pages/batches/polls (when applicable).
        queue_maxsize: Optional queue size hint for internal buffers.
        max_pages: Optional page limit for paginated collectors.
        scroll_pause_ms: Pause after each scroll, in milliseconds.
        max_idle_rounds: Stop after this many consecutive idle rounds (for DOM collectors or custom loops).
        max_items: Optional item limit (applies where relevant).
        scroll_mode: Optional strategy indicator: "default" | "selector" | "pager".
        scroll_selector: Used when scroll_mode == "selector".
        pager_selector: Used when scroll_mode == "pager".
    """

    response_timeout_sec: float = 5.0
    delay_ms: int = 500
    queue_maxsize: Optional[int] = None
    scroll_pause_ms: int = 800
    max_idle_rounds: int = 2
    max_items: Optional[int] = 10000
    max_seconds: int = 600
    auto_scroll: bool = True
    scroll_mode: Optional[str] = None
    scroll_selector: Optional[str] = None
    max_pages: Optional[int] = None
    pager_selector: Optional[str] = None
    need_raw_data: bool = False