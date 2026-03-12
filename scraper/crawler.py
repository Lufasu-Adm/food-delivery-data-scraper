import time
import random
import logging
from playwright.sync_api import sync_playwright

def fetch_page_html(url: str) -> str:
    """Mengambil konten HTML menggunakan murni Microsoft Edge (msedge) mode Stealth."""
    with sync_playwright() as p:
        logging.info("Opening Microsoft Edge in Stealth headless mode...")
        
        # Menggunakan channel="msedge"
        browser = p.chromium.launch(
            channel="msedge",
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )

        # User agent juga disesuaikan menjadi Edge (Edg/123.0.0.0)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
            viewport={'width': 1920, 'height': 1080},
            device_scale_factor=1
        )
        
        context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        page = context.new_page()

        try:
            logging.info(f"Navigating to: {url}")
            page.goto(url, wait_until="networkidle", timeout=60000)

            logging.info("Simulating human scroll...")
            for _ in range(4):
                page.mouse.wheel(0, random.randint(600, 900))
                time.sleep(random.uniform(1.5, 3.5))

            extra_wait = random.uniform(2, 4)
            logging.info(f"Waiting for {extra_wait:.2f} seconds to ensure dynamic content loads...")
            time.sleep(extra_wait)

            html_content = page.content()
            logging.info("HTML content successfully captured using Edge.")
            return html_content

        except Exception as e:
            logging.error(f"Error during crawling: {e}")
            try:
                page.screenshot(path="logs/error_screenshot.png")
            except:
                pass
            return ""
        
        finally:
            browser.close()