# Chrome Proxy Manager

This `README.MD` file provides an overview of the Chrome Proxy Manager, a Python script that automates the process of setting up and using multiple proxies with Google Chrome via the `undetected_chromedriver` package.

## Features
- Automated proxy authentication setup for Google Chrome
- Utilizes a list of proxies with their corresponding IP, port, username, and password
- Clears cookies before browsing
- Displays the currently used proxy
- Visits "https://www.whatismyip.com/" to verify the proxy is working
- Closes the browser after a predefined time

## Requirements
- Python 3.x
- undetected_chromedriver

To install the required package, run:

```python
pip install undetected_chromedriver
```

## Usage

1. Prepare a list of proxies in the `proxy_list` variable with the format: `IP:PORT:USERNAME:PASSWORD`. Example:

```python
proxy_list = [
    '2.56.119.93:5074:rxwknsdc:0zqmat5csg14',
]
```

2. Set the desired browsing window size by modifying the `driver.set_window_size()` function. Example:

```python
driver.set_window_size(800, 600)
```

3. Set the desired browsing time by modifying the `time.sleep()` function. Example:

```python
time.sleep(100)
```

4. Run the script:

```python
python chrome_proxy_manager.py
```

## MIT License
Copyright (c) 2023 13XLabs

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 