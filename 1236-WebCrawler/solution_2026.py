class Solution:

    def helper(self, startUrl: str, baseUrl: str, urlSet: set[str], visited: set[str], parser: 'HtmlParser') -> None:
        if startUrl in visited:
            return
        visited.add(startUrl)
        if not startUrl.startswith(baseUrl):
            return
        urlSet.add(startUrl)
        for url in parser.getUrls(startUrl):
            self.helper(url, baseUrl, urlSet, visited, parser)

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        urls, visited = set(), set()
        host_name = startUrl.strip().split('/')[2]
        base_url = f'http://{host_name}'
        self.helper(startUrl, base_url, urls, visited, htmlParser)
        return list(urls)
 
