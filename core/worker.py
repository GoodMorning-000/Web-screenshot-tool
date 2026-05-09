import asyncio

from loguru import logger

from core.screenshot import capture


async def process_url(browser_manager, url, semaphore):

    async with semaphore:

        page = await browser_manager.new_page()

        try:
            await capture(page, url)

        except Exception as e:
            logger.error(f'{url} 失败: {e}')

            with open(
                'data/failed_urls.txt',
                'a',
                encoding='utf-8'
            ) as f:
                f.write(url + '\n')

        finally:
            await page.close()