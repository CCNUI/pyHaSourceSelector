import concurrent.futures
import os
import time

import requests
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# --- Configuration ---
# Read timeout from environment variable, default to 5 seconds if not set
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 5))

# --- Source List ---
# A dictionary mapping descriptive names to the URLs to be tested.
# You can easily add, remove, or modify sources here.
SOURCES = {
    "高速站点(nju.edu.cn)": "https://ghcr.nju.edu.cn",
    "高速站点(hassbus)": "https://ghcr.hassbus.cn",
    "高速站点(fashgh)": "https://ghcr.fashgh.com",
    "高速站点(fastgh)": "https://fastgh.me",
    "高速站点(linkos)": "https://ghcr.linkos.top",
    "高速站点(haospeed)": "https://ghcr.haospeed.com",
    "高速站点(tonbcr)": "https://ghcr.tonb.icu",
    "原始站点(ghcr.io)": "https://ghcr.io",
}


def test_latency(url: str) -> float:
    """
    Tests the latency of a single URL by making a lightweight HEAD request.

    Args:
        url: The URL to test.

    Returns:
        The latency in milliseconds, or float('inf') if an error occurs.
    """
    try:
        start_time = time.perf_counter()
        response = requests.head(url, timeout=REQUEST_TIMEOUT)
        end_time = time.perf_counter()

        # Check for a successful status code (2xx or 3xx)
        if 200 <= response.status_code < 400:
            return (end_time - start_time) * 1000
        else:
            return float('inf')
    except requests.exceptions.RequestException:
        return float('inf')


def find_best_source():
    """
    Concurrently tests all sources and prints a ranked list of results.
    """
    print(f"🚀 Testing all sources with a {REQUEST_TIMEOUT}-second timeout...")

    results = {}

    # Use a ThreadPool to test all URLs concurrently for speed
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(SOURCES)) as executor:
        future_to_name = {executor.submit(test_latency, url): name for name, url in SOURCES.items()}

        for future in concurrent.futures.as_completed(future_to_name):
            name = future_to_name[future]
            try:
                latency = future.result()
                results[name] = latency
            except Exception:
                results[name] = float('inf')

    # Sort results by latency (the second item in the tuple)
    sorted_results = sorted(results.items(), key=lambda item: item[1])

    # --- Print Results ---
    print("\n--- ✅ Test Results (fastest to slowest) ---")
    print(f"{'Source Name':<25} {'Latency (ms)':<10}")
    print("-" * 37)

    best_source_name = None

    for name, latency in sorted_results:
        if latency != float('inf'):
            if best_source_name is None:
                best_source_name = name
                # ANSI escape code for green color for the best result
                print(f"\033[92m{name:<25} {latency:<10.2f}\033[0m")
            else:
                print(f"{name:<25} {latency:<10.2f}")
        else:
            # ANSI escape code for red color for failed tests
            print(f"\033[91m{name:<25} {'FAILED':<10}\033[0m")

    print("-" * 37)

    # --- Print Recommendation ---
    if best_source_name:
        best_url = SOURCES[best_source_name]
        print(f"\n✨ Recommended Source: \033[92m{best_source_name}\033[0m")
        print(f"   URL: {best_url}")
    else:
        print("\n❌ All sources failed the test. Please check your network connection and try again.")


if __name__ == "__main__":
    find_best_source()