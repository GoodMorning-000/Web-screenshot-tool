import asyncio

from loguru import logger

from core.screenshot import capture, Color


async def process_url(browser_manager, url, semaphore):

    async with semaphore:

        page = await browser_manager.new_page()

        try:
            await capture(page, url)

        except Exception as e:
            error_msg = str(e).split('\n')[0][:80] if '\n' in str(e) else str(e)[:80]
            logger.error(f'{url} - {Color.RED}失败{Color.RESET}: {error_msg}')

            with open(
                'data/failed_urls.txt',
                'a',
                encoding='utf-8'
            ) as f:
                f.write(f'{url}\n')

        finally:
            await page.close()