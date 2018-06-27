import urllib3
from bs4 import BeautifulSoup
import os
import re

dest_folder = 'D:/workspace/doc/novatel'


def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print(path + ' 创建成功')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


def grabhtmlpage(_url, ecd='utf-8'):
    _http = urllib3.PoolManager()
    try:
        _result = _http.request('GET', _url)
        if _result.status != 200:
            return None
        texthtml = _result.data.decode(ecd)
    except UnicodeDecodeError as e:
        return None
    else:
        return texthtml


def html2bs(_html):
    try:
        bs = BeautifulSoup(_html, 'html.parser')
    except:
        return None
    else:
        return bs


def url2bs(_url, ecd='gbk'):
    html = grabhtmlpage(_url, ecd)
    if html == None:
        return None
    else:
        bs = html2bs(html)
        return bs


def grabbiqukan():
    # 2_2768 傲世九重天
    mainurl = 'http://www.biqukan.com/'
    nv_index = r'2_2768'

    _bs = url2bs(mainurl + nv_index, 'gbk')

    if _bs == None:
        print('return None')
        return None
    else:
        print(_bs.h2.string)
        mkdir(dest_folder)

        _dtstart = _bs.find('dt', text=re.compile('正文'))
        print(_dtstart.string)

        _capters = _dtstart.next_siblings

        with open(dest_folder + '/' + _bs.h2.string + '.txt', 'w', encoding='utf-8') as f:
            for _item in _capters:
                if _item.name != None:
                    _itembs = url2bs(mainurl + _item.contents[0]['href'])
                    if _itembs == None:
                        print('return None')
                        pass
                    else:
                        print(_itembs.h1.string)
                        f.write(_itembs.h1.string + '\r\n')
                        _content_div = _itembs.find('div', attrs={'id': 'content', 'class': 'showtxt'})
                        f.write(_content_div.get_text(strip=True) + '\r\n')


if __name__ == '__main__':
    grabbiqukan()
