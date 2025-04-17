import time
import os
from icrawler.builtin import BingImageCrawler

# List of search keywords to broaden dataset variety
keywords = [
    "Dalek Doctor Who",
    "Classic Dalek",
    "Dalek toy",
    "Dalek prop",
    "Gold Dalek",
    # "Dalek model kit",
    "Dalek figurine"
    # "Dalek cosplay"
]

# Base folder to store images
base_dir = "dataset"

# Loop through each keyword
for idx, keyword in enumerate(keywords):
    # Convert keyword to a safe folder name
    safe_name = keyword.lower().replace(" ", "_")

    # Directory to store this keyword's images
    save_path = os.path.join(base_dir, safe_name)

    # Make sure the directory exists
    os.makedirs(save_path, exist_ok=True)

    print(f"\n🔍 Searching Bing for: {keyword}")
    print(f"📁 Saving to: {save_path}")

    # Create a BingImageCrawler instance
    crawler = BingImageCrawler(
        storage={'root_dir': save_path},
        downloader_threads=1  # safer and less likely to be flagged
    )

    # Start crawling
    crawler.crawl(
        keyword=keyword,
        max_num=200,
        min_size=(200, 200),
        file_idx_offset=0
    )

    print(f"✅ Finished downloading for '{keyword}'")

    # Optional delay between requests (to be respectful to Bing)
    time.sleep(20)  # 10 second pause between keywords
