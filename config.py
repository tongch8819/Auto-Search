# videos
youtube=  "https://www.youtube.com/results?search_query={}"
bilibili= "https://search.bilibili.com/all?={}&from_source=webtop_search&spm_id_from=333.1007"
# general
google=   "https://www.google.com.hk/search?q={}"
bing=     "https://www.bing.com/search?q={}"
baidu=    "https://www.baidu.com/s?wd={}"
# zhihu=    "https://www.zhihu.com/search?type=content&q={}"
zhihu = None
# ebook
libgen=   "https://libgen.is/search.php?req={}&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def"
jiumo =  None 
zlibrary = "https://sg1lib.org/s/{}?"

alias_to_name = {
    'safa' : 'safari',
    'chro' : 'Google Chrome'
}

URLS = dict(
video = [
    youtube, bilibili
],
general = [
    google, bing, zhihu, baidu
],
ebook = [
    libgen, jiumo, zlibrary 
],
zh = [
    baidu, zhihu, 
],
)

def make_urls(kw, tp):
    tplts = URLS.get(tp)
    res = []
    for tplt in tplts:
        if tplt is None:
            continue
        res.append(
            tplt.format(kw)
        )
    return res
