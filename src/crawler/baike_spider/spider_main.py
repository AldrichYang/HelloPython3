# coding:utf-8
from src.baike_spider import html_downloader, url_manager, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownlaoder()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                # 获取新的url
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                # 下载新的网页内容
                html_cont = self.downloader.download(new_url)
                # 解析网页
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 添加新的待解析url
                self.urls.add_new_urls(new_urls)
                # 保存网页内容
                self.outputer.collect_data(new_data)
                if count == 10:
                    break
                count = count + 1
            except:
                print("craw failed")

        self.outputer.output_html()


if __name__ == "__main__":
    root_url_ = "http://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url_)
