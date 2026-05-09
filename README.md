# Modern Web Screenshot Platform

A modern web screenshot system built with Playwright, featuring high stability, concurrency, anti-detection capabilities, and automatic retry mechanisms.

## Features

- ✅ **High Stability**: Built on Playwright for reliable browser automation
- ✅ **High Concurrency**: AsyncIO-based concurrent screenshot processing
- ✅ **Anti-Detection**: Browser fingerprint spoofing to bypass bot detection
- ✅ **Auto Retry**: Automatic retry on failure using tenacity
- ✅ **Auto Logging**: Comprehensive logging with loguru
- ✅ **Auto Lazy Loading**: Automatic scrolling to trigger lazy-loaded content
- ✅ **Full Page Screenshot**: Native support for capturing entire web pages
- ✅ **Cross-Browser Support**: Works with Chrome, Edge, and Chromium

## Requirements

- Python 3.11+
- Playwright
- Playwright-stealth
- loguru
- tenacity
- pydantic

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Install browser (if not using system Chrome/Edge)
playwright install chromium
```

## Usage

1. Add URLs to `data/urls.txt` (one URL per line)

2. Run the screenshot tool:

```bash
python main.py
```

3. Screenshots will be saved in the `screenshots/` directory

## Configuration

Edit `config/settings.py` to customize:

- `HEADLESS`: Run browser in headless mode (default: True)
- `WINDOW_WIDTH`: Browser window width (default: 1920)
- `WINDOW_HEIGHT`: Browser window height (default: 1080)
- `PAGE_TIMEOUT`: Page load timeout in milliseconds (default: 60000)
- `MAX_CONCURRENT`: Maximum concurrent screenshots (default: 5)
- `MAX_RETRY`: Maximum retry attempts (default: 3)
- `MAX_SCROLL_STEP`: Maximum scroll steps for lazy loading (default: 10)

## Project Structure

```
modern_screenshot_project/
├── config/              # Configuration files
│   ├── settings.py      # Application settings
│   └── browser.js       # Browser fingerprint spoofing
├── core/                # Core modules
│   ├── browser.py       # Browser manager
│   ├── screenshot.py    # Screenshot logic
│   ├── worker.py        # Concurrent task worker
│   └── retry.py         # Retry decorator
├── utils/               # Utility functions
│   ├── file_utils.py    # File operations
│   ├── scroll.py        # Auto-scroll for lazy loading
│   └── url_utils.py     # URL validation and normalization
├── data/                # Data files
│   └── urls.txt         # URLs to screenshot
├── screenshots/         # Screenshot output directory
├── logs/                # Log files
├── main.py              # Main entry point
└── requirements.txt     # Python dependencies
```

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.