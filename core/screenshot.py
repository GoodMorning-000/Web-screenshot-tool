import asyncio
from pathlib import Path

from loguru import logger

from core.retry import retry_decorator
from utils.scroll import auto_scroll
from utils.file_utils import sanitize_filename
from utils.url_utils import normalize_url


class Color:
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    GREEN = '\033[32m'
    RED = '\033[31m'
    RESET = '\033[0m'


@retry_decorator
async def capture(page, url):

    normalized_url = normalize_url(url)
    logger.info(f'{url} - {Color.YELLOW}开始访问{Color.RESET}')

    await page.goto(
        normalized_url,
        timeout=60000,
        wait_until='networkidle'
    )

    await auto_scroll(page)

    await asyncio.sleep(1)

    title = await page.title()

    title_text = title[:50] + '...' if len(title) > 50 else title
    logger.info(f'{url} - {Color.BLUE}页面标题: {title_text}{Color.RESET}')

    filename = sanitize_filename(
        url.replace('https://', '')
           .replace('http://', '')
    )

    output = Path('screenshots') / f'{filename}.png'

    await page.screenshot(
        path=str(output),
        full_page=True
    )

    logger.success(f'{url} - {Color.GREEN}截图完成{Color.RESET}')