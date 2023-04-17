# MIT License

# Copyright (c) 2023 13XLabs

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import time
import shutil
import undetected_chromedriver as uc

proxy_list = [
    '2.56.119.93:5074:rxwknsdc:0zqmat5csg14',
]

def create_proxy_auth_extension(proxy_host, proxy_port, proxy_username, proxy_password):
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
              singleProxy: {
                scheme: "http",
                host: "%(host)s",
                port: parseInt(%(port)s)
              },
              bypassList: [""]
            }
          };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%(user)s",
                password: "%(pass)s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """ % {
        "host": proxy_host,
        "port": proxy_port,
        "user": proxy_username,
        "pass": proxy_password,
    }

    chrome_proxy_auth_plugin_path = os.path.abspath("proxy_auth_plugin")

    if os.path.exists(chrome_proxy_auth_plugin_path):
        shutil.rmtree(chrome_proxy_auth_plugin_path)

    os.makedirs(chrome_proxy_auth_plugin_path, exist_ok=True)

    with open(os.path.join(chrome_proxy_auth_plugin_path, "manifest.json"), "w") as f:
        f.write(manifest_json.strip())

    with open(os.path.join(chrome_proxy_auth_plugin_path, "background.js"), "w") as f:
        f.write(background_js.strip())

    return chrome_proxy_auth_plugin_path

def chromeWithProxy():
    for proxy in proxy_list:
        # Split the proxy into its components
        ip, port, user, pwd = proxy.split(':')

        proxy_auth_plugin_path = create_proxy_auth_extension(
            ip, port, user, pwd
        )

        # Setting Chrome Options
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument(
            f'--load-extension={proxy_auth_plugin_path}')
        driver = uc.Chrome(use_subprocess=True,
                           version_main=112, options=chrome_options)

        # Set the size of the browser window
        driver.set_window_size(800, 600)

        driver.delete_all_cookies()  # Delete all cookies

        # Print the proxy being used
        print(f"Using proxy: {ip}:{port}")

        # What is my IP
        driver.get('https://www.whatismyip.com/')

        # Wait for 100 seconds
        time.sleep(100)

        # Close the browser
        driver.quit()

# Run the script
if __name__ == '__main__':
    chromeWithProxy()