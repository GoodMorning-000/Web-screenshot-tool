import asyncio
from pathlib import Path

from loguru import logger

from core.retry import retry_decorator
from utils.scroll import auto_scroll
from utils.file_utils import sanitize_filename
from utils.url_utils import normalize_url


@retry_decorator
async def capture(page, url):

    normalized_url = normalize_url(url)
    logger.info(f'开始访问: {normalized_url}')

    await page.goto(
        normalized_url,
        timeout=60000,
        wait_until='networkidle'
    )

    await auto_scroll(page)

    await asyncio.sleep(1)

    title = await page.title()

    logger.info(f'页面标题: {title}')

    filename = sanitize_filename(
        url.replace('https://', '')
           .replace('http://', '')
    )

    output = Path('screenshots') / f'{filename}.png'

    await page.screenshot(
        path=str(output),
        full_page=True
    )

    logger.success(f'截图完成: {url}')