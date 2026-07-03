#!/usr/bin/env python3
"""Render poster-dealer.html as a 1080x1920 PNG image using Playwright."""

from playwright.sync_api import sync_playwright
import os

POSTER_URL = "http://localhost:8899/poster-dealer.html"
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "poster-dealer.png")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(
        viewport={"width": 1080, "height": 1920},
        device_scale_factor=2  # 2x for retina quality
    )
    page.goto(POSTER_URL, wait_until="networkidle")
    # Wait a bit for any animations to settle
    page.wait_for_timeout(2000)
    page.screenshot(path=OUTPUT, full_page=True)
    browser.close()
    print(f"✅ Poster saved to: {OUTPUT}")
    print(f"   Size: {os.path.getsize(OUTPUT) / 1024:.1f} KB")
