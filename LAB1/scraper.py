from bs4 import BeautifulSoup
import requests


URL = 'https://www.favikon.com/blog/the-20-most-famous-tiktok-influencers-in-the-world'

html_page = requests.get(URL).content
soup = BeautifulSoup(html_page, 'html.parser')

title = soup.title.text
title = title[:title.find('!')] + '.'

list = soup.find('div', attrs='tablecontent').find_all('li')

top20 = [item.text for item in list]

for item in top20:
    print(item)

links = [link['href'] if link else None for link in [paragraph.find('a') for paragraph in soup.find_all('p')]]

for link in links:
    if link and 'www.tiktok.com' in link:
        print(link)

links = soup.find_all('div', attrs=['w-embed w-script'])

for link in links:
    print(link.find('a')['href'])

# with open('soup.html', 'w') as file:
#     file.write(soup.prettify())

# paragraphs = soup.select('p')

# for paragraph in paragraphs:
#     print(paragraph)





with open('tiktok.md', 'w') as page:
    page.write(f'# {title}\n')
    for item in top20:
        page.write(f'- [{item}]({URL})\n')