from pydantic import BaseModel


class Settings(BaseModel):
    HEADLESS: bool = True

    WINDOW_WIDTH: int = 1920
    WINDOW_HEIGHT: int = 1080

    PAGE_TIMEOUT: int = 60000

    MAX_CONCURRENT: int = 5

    MAX_RETRY: int = 3

    MAX_SCROLL_STEP: int = 10

    SCREENSHOT_QUALITY: int = 90

    MAX_PAGE_HEIGHT: int = 15000


settings = Settings()