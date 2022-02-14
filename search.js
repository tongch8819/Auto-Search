function search() {
    st = document.getElementById("st").value;
    kw = document.getElementById("kw").value;

    google=   "https://www.google.com.hk/search?q=";
    bing=     "https://www.bing.com/search?q=";
    baidu=    "https://www.baidu.com/s?wd=";

    youtube=  "https://www.youtube.com/results?search_query="
    bilibili=  "https://search.bilibili.com/all?keyword="

    libgen=   `https://libgen.is/search.php?req=${kw}&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def`
    zlibrary = `https://sg1lib.org/s/${kw}?`

    webster = `https://www.merriam-webster.com/dictionary/${kw}`
    youdao = `https://youdao.com/result?word=${kw}&lang=en`

    if( st == 'general' ){
        window.open(baidu + kw);
        window.open(bing + kw);
        window.open(google + kw);
    } else if ( st == 'video' ) {
        window.open(youtube + kw);
        window.open(bilibili + kw);
    } else if ( st == 'ebook' ) {
        window.open(libgen);
        window.open(zlibrary);
    } else if ( st == 'enw' ) {
        window.open(webster);
        window.open(youdao);
    } else {
        window.alert("Not Support");
    }

}