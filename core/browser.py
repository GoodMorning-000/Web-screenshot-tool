from playwright.async_api import async_playwright
from config.settings import settings
import os


class BrowserManager:

    def __init__(self):
        self.playwright = None
        self.browser = None

    def _get_browser_path(self):
        chrome_paths = [
            r'C:\Program Files\Google\Chrome\Application\chrome.exe',
            r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
        ]
        for path in chrome_paths:
            if os.path.exists(path):
                return ('chromium', path)
        
        edge_paths = [
            r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
            r'C:\Program Files\Microsoft\Edge\Application\msedge.exe',
        ]
        for path in edge_paths:
            if os.path.exists(path):
                return ('chromium', path)
        
        return (None, None)

    async def start(self):
        self.playwright = await async_playwright().start()

        browser_type, browser_path = self._get_browser_path()
        
        launch_kwargs = {
            'headless': settings.HEADLESS,
            'args': [
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--no-sandbox',
            ]
        }
        
        if browser_path:
            launch_kwargs['executable_path'] = browser_path

        self.browser = await self.playwright.chromium.launch(**launch_kwargs)

    async def new_page(self):
        context = await self.browser.new_context(
            viewport={
                'width': settings.WINDOW_WIDTH,
                'height': settings.WINDOW_HEIGHT,
            },
            user_agent=(
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 '
                '(KHTML, like Gecko) '
                'Chrome/123.0.0.0 Safari/537.36'
            ),
            locale='zh-CN',
            timezone_id='Asia/Shanghai'
        )

        await context.add_init_script(
            path='config/browser.js'
        )

        page = await context.new_page()

        return page

    async def close(self):
        await self.browser.close()
        await self.playwright.stop()