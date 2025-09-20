# Py Source Selector

A simple, fast, and configurable Python script to test the latency of multiple mirror sources and intelligently select the fastest one for your current network environment.

## Features

-   **Concurrent Testing**: Uses multithreading to test all sources simultaneously for quick results.
-   **Accurate Latency Measurement**: Measures the response time of a lightweight `HEAD` request to determine latency.
-   **Clear & Colorful Output**: Displays a ranked list of sources from fastest to slowest, with color-coded results for success and failure.
-   **Easy to Customize**: Add, remove, or edit sources by simply modifying the `SOURCES` dictionary in the script.
-   **Configurable Timeout**: Adjust the request timeout via a `.env` file without changing the code.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

You need to have Python 3.6+ installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/py-source-selector.git](https://github.com/your-username/py-source-selector.git)
    cd py-source-selector
    ```
    *(Replace `your-username` with your actual GitHub username)*

2.  **Create a virtual environment (recommended):**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure your environment (optional):**
    The default request timeout is 5 seconds. If you want to change it, first rename the example environment file:
    ```bash
    # For macOS/Linux
    mv .env.example .env

    # For Windows
    rename .env.example .env
    ```
    Then, edit the new `.env` file to change the `REQUEST_TIMEOUT` value.

## Usage

To run the script and find the best source, simply execute the `main.py` file from your terminal:

```bash
python main.py
```

### Example Output

The script will print a ranked list of the sources and recommend the best one.

```
🚀 Testing all sources with a 5-second timeout...

--- ✅ Test Results (fastest to slowest) ---
Source Name               Latency (ms)
-------------------------------------
[92m高速站点(nju.edu.cn)        45.12     [0m
高速站点(haospeed)            88.67     
原始站点(ghcr.io)             150.23    
[91m高速站点(tonbcr)              FAILED    [0m
[91m高速站点(hassbus)             FAILED    [0m
-------------------------------------

✨ Recommended Source: [92m高速站点(nju.edu.cn)[0m
   URL: [https://ghcr.nju.edu.cn](https://ghcr.nju.edu.cn)
```

## How to Customize Sources

You can easily test your own list of URLs. Open the `main.py` file and modify the `SOURCES` dictionary at the top:

```python
# main.py

# ... (imports and config) ...

# --- Source List ---
# Add, remove, or change any source here.
SOURCES = {
    "Google DNS": "[https://8.8.8.8](https://8.8.8.8)",
    "Cloudflare DNS": "[https://1.1.1.1](https://1.1.1.1)",
    "My Private Mirror": "[https://mirror.example.com](https://mirror.example.com)",
}

# ... (rest of the script) ...
```

## License

This project is licensed under the MIT License.