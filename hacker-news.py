import requests
import bs4

r = requests.get("https://thehackernews.com/")
soup = bs4.BeautifulSoup(r.text, 'lxml')


title = []

for x in soup.select('.home-title'):

	title.append(x.text)


article = []

for x in soup.select('.home-desc'):

	article.append(x.text)


image_title = []

for x in soup.select('.home-img-src'):

	image_title.append(x['alt'])


image_link = []

for x in soup.select('.home-img-src'):

	image_link.append(x['data_src'])


# Download all the image in the page

for x in range(len(image_link)):

	link = requests.get(image_link[x])

	f = open(image_title[x] + '.jpg','wb')

	f.write(link.content)

	f.close()


article_link = []

for x in soup.select('.story-link'):

	article_link.append(x['href'])









