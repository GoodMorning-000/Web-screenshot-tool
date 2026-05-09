import asyncio


async def auto_scroll(page, max_step=10):
    current = 0

    for _ in range(max_step):
        current += 1000

        await page.evaluate(
            f'window.scrollTo(0, {current})'
        )

        await asyncio.sleep(0.5)