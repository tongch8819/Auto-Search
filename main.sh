if [ $# -ne 2 ]; then
    echo "$0 [keyword_zh] [keyword_en]"
    exit 1
fi
kw_zh=$1
kw_en=$2
echo "Search Keyword[zh]" $kw_zh
echo "Search Keyword[en]" $kw_en

# videos
youtube="https://www.youtube.com/results?search_query=$kw_en"
bilibili="https://search.bilibili.com/all?keyword=$kw_zh&from_source=webtop_search&spm_id_from=333.1007"

# general
google="https://www.google.com.hk/search?q=$kw_en"
bing_en="https://www.bing.com/search?q=$kw_en"
bing_zh="https://www.bing.com/search?q=$kw_zh"
baidu="https://www.baidu.com/s?wd=$kw_zh"
zhihu="https://www.zhihu.com/search?type=content&q=$kw_zh"

# ebook
libgen="https://libgen.is/search.php?req=$kw_en&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def"



for url in $youtube, $bilibili; do
    echo $url
    open -a safari $url
done