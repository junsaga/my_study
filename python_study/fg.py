def get_page_cnt(isbn):
    # Yes24 도서 검색 페이지 URL
    url ="http://www.yes24.com/Product/Search?domain=Book&query={}"
    # URL에 ISBN을 넣어 HTML을 가져옵니다
    r = request.get(url.frmat)