# spider_baike_demo
## 简单爬虫示例，爬取百度百科的数据

环境：Python 3.6.5

使用 bs4、urllib、re 模块

容易出现的问题：

- 1、urllib2 和 urllib3 在 Python3.x 后都被合并到 urllib 中

- 2、百度百科的词条关于 Python 的链接已经更改了，替换成新的即可

- 3、爬取的数据显示格式不正确，open(path, 'w', encoding='utf-8')

- 4、html 的标签是成对出现的，切勿粗心大意少写标签的结束。

- 5、使用正则匹配的时候，也需要进行修改：href=re.compile(r'/item/*')
