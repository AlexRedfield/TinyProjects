import urllib.request
import urllib.parse
import urllib.robotparser


def download(url, headers=None, proxy=None, num_retries=1):
    print('Downloading:', url)
    headers = headers or {}
    request = urllib.request.Request(url, headers=headers)
    opener = urllib.request.build_opener()
    if proxy:  # 添加代理
        proxy_params = {urllib.request.urlparse(url).scheme: proxy}
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))

    try:
        # 不加代理的版本：html = urllib.request.urlopen(request).read().decode('utf-8')
        html = opener.open(request).read().decode('utf-8')

    except urllib.request.URLError as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, headers, num_retries - 1)
    return html
