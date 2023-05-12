import urllib.request

url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzAyMTNfMTQ0%2FMDAxNjc2MjM0ODkwMDg0.aNGqR46R9-Edz8sZxa3QHm-brySer1ERxJIhz45Vke4g.dOQQ7iO7t2v7KL6JYg2ZIWeOi7XAIsALgBBm_SFNaKAg.PNG.hyunjae9132%2FScreen_Shot_2023-02-12_at_20.47.58.png&type=sc960_832"

savename = 'urldownload01.png'

result = urllib.request.urlretrieve(url, savename)

data = result.read()
print('#type(data) :', type(data))
print(savename + 'saved...')