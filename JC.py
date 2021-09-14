import httpx
from lxml import etree
import execjs


class JingCamera(object):

    def __init__(self):
        self.__url = "https://www.jinjing365.com/index.asp"
        self.__dataName = "LabelsData"

    def do_get(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
        return httpx.get(url=self.__url, headers=headers).text

    def parse(self, data):
        selector = etree.HTML(data)
        content = selector.xpath('//script/text()')
        script = list(filter(lambda x: (self.__dataName in x), content))[0]
        docjs = execjs.compile(script)
        res = docjs.eval(self.__dataName)
        return res

    def run(self):
        content = self.do_get()
        return self.parse(content)


if __name__ == '__main__':
    jc = JingCamera()
    result = jc.run()
    print(result)
