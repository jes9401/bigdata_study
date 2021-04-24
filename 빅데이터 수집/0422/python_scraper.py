import re
import sqlite3
from urllib.request import urlopen
from html import unescape

def main():
    html = fetch('http://www.hanbit.co.kr/store/books/full_book_list.html')
    books = scrape(html)
    save('books.db', books)

def fetch(url):
    f = urlopen(url)
    encoding = f.info().get_content_charset(failobj="utf-8")
    html = f.read().decode(encoding)
    return html

def scrape(html):
    books = []
    # re.findall()을 사용해 도서 하나에 해당하는 HTML을 추출합니다.
    for partial_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
        # 도서의 URL을 추출합니다.
        url = re.search(r'<a href="(.*?)">', partial_html).group(1)
        url = 'http://www.hanbit.co.kr' + url
        title = re.sub(r'<.*?>', '', partial_html)
        title = unescape(title)
        books.append({'url': url, 'title': title})
    return books

def save(db_path, books):
    # 데이터베이스를 열고 연결을 확립합니다.
    conn = sqlite3.connect(db_path)
    # 커서를 추출합니다.
    c = conn.cursor()
    # execute() 메서드로 SQL을 실행합니다.
    # 스크립트를 여러 번 실행할 수 있으므로 기존의 books 테이블을 제거합니다.
    c.execute('DROP TABLE IF EXISTS books')
    # books 테이블을 생성합니다.
    c.execute('''
        CREATE TABLE books (
            title text,
            url text
        )
    ''')
    # executemany() 메서드를 사용하면 매개변수로 리스트를 지정할 수 있습니다.
    c.executemany('INSERT INTO books VALUES (:title, :url)', books)
    # 변경사항을 커밋(저장)합니다.
    conn.commit()
    # 연결을 종료합니다.
    conn.close()

# python 명령어로 실행한 경우 main() 함수를 호출합니다.
# 이는 모듈로써 다른 파일에서 읽어 들였을 때 main() 함수가 호출되지 않게 하는 것입니다.
# 파이썬 프로그램의 일반적인 작성 방식입니다.
if __name__ == '__main__':
    main()