import asyncio

from loguru import logger

from core.browser import BrowserManager
from core.worker import process_url

from config.settings import settings

from utils.file_utils import ensure_dir


async def main():

    ensure_dir('screenshots')
    ensure_dir('logs')
    ensure_dir('data')

    logger.add(
        'logs/runtime.log',
        rotation='50 MB',
        retention='7 days'
    )

    with open('data/urls.txt', 'r', encoding='utf-8') as f:
        urls = [
            line.strip()
            for line in f
            if line.strip()
        ]

    browser_manager = BrowserManager()

    await browser_manager.start()

    semaphore = asyncio.Semaphore(
        settings.MAX_CONCURRENT
    )

    tasks = [
        process_url(browser_manager, url, semaphore)
        for url in urls
    ]

    await asyncio.gather(*tasks)

    await browser_manager.close()


if __name__ == '__main__':
    asyncio.run(main())