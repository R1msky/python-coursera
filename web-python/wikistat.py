from bs4 import BeautifulSoup
import unittest
import re


def parse(path_to_file):
    with open(path_to_file, 'r', encoding='UTF-8') as page:
        soup = BeautifulSoup(page, 'lxml')
        content = soup.find(id='bodyContent')
        imgs = content.find_all('img')
        imgs = len(list(filter(lambda width: int(width) >= 200,
                               [item['width'] for item in content.select('[width]')])))

        headers = content.find_all(re.compile('^h[1-6]'))
        headers = len(list(filter(lambda sym: sym in 'ETC',
                                  [header.text[0] for header in headers])))
        lists = content.find_all(['ol', 'ul'])
        lists = len(list(1 for tag in content.find_all(['ol', 'ul']) if not tag.find_parent(['ol', 'ul'])))

        tag = content.find('a')
        linkslen = 0
        links = content.find_all('a')
        for link in links:
            curlen = 1
            for tag in link.find_next_siblings():
                if tag.name != 'a':
                    break
                curlen += 1
            linkslen = max(curlen, linkslen)

    return [imgs, headers, linkslen, lists]


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
     unittest.main()
