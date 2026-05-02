import threading
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED

class Solution:

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = startUrl.split('/')[2]
        base = f'http://{hostname}'
        stack = [startUrl]
        visited = {startUrl}
        lock = threading.Lock()

        def worker(url):
            child_urls = htmlParser.getUrls(url)
            with lock:
                for child_url in child_urls:
                    if not child_url.startswith(base): continue
                    if child_url in visited: continue
                    stack.append(child_url)
                    visited.add(child_url)

        with ThreadPoolExecutor(max_workers=8) as executor:
            pending_futures = set()
            while stack:
                url = stack.pop()
                future = executor.submit(worker, url)
                pending_futures.add(future)
                while not stack and pending_futures:
                    _, pending_futures = wait(
                        pending_futures,
                        return_when=FIRST_COMPLETED
                    )
        return list(visited)
 
