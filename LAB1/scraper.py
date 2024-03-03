from bs4 import BeautifulSoup
import requests
from duckduckgo_search import DDGS

TEAM = 'G2 Esports'
TEAM_CODE = 'g2'
URL = f'https://lol.fandom.com/wiki/{TEAM}'


def front_matter(file, title, permalink, redirect = ''):
    file.write('---\n')
    file.write(f'title: {title}\n')
    file.write(f'permalink: {permalink}\n')
    if redirect:
        file.write(f'redirect_from: {redirect}\n')
    file.write('---\n')


if __name__ == '__main__':

    html_page = requests.get(URL).content
    soup = BeautifulSoup(html_page, 'html.parser')

    desc = next(DDGS().answers(TEAM))['text']

    with open(f'{TEAM_CODE}.md', 'w') as md_file:
        front_matter(md_file, TEAM, f'labs/{TEAM_CODE}/')
        md_file.write(f'# {TEAM}\n')
        md_file.write(desc + '\n')
        md_file.write(f'### [Current roster](https://querthdp.github.io/awww/labs/{TEAM_CODE}_players)')
