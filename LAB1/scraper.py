from bs4 import BeautifulSoup
import requests
from duckduckgo_search import DDGS

TEAM = 'G2 Esports'
TEAM_CODE = 'g2'
BASE_URL = 'https://lol.fandom.com'
URL = f'https://lol.fandom.com/wiki/{TEAM}'
PATH = './docs/_docs/lab1/'
GIT = 'https://querthdp.github.io/awww/labs/'


def front_matter(file, title, permalink, redirect = ''):
    file.write('---\n')
    file.write(f'title: {title}\n')
    file.write(f'permalink: {permalink}/\n')
    if redirect:
        file.write(f'redirect_from: {redirect}/\n')
    file.write('---\n')


if __name__ == '__main__':

    html_page = requests.get(URL).content
    soup = BeautifulSoup(html_page, 'html.parser')

    desc = next(DDGS().answers(TEAM))['text']

    table = soup.find('table', 'team-members').find_all('tr')

    with open(f'{PATH}{TEAM_CODE}.md', 'w') as team_file:
        front_matter(team_file, TEAM, f'labs/{TEAM_CODE}')
        image = next(DDGS().images(f'{TEAM} LEC logo'))['image']
        team_file.write(f"![{TEAM}]({image})\n")
        team_file.write(f'### Description\n')
        team_file.write(desc + '\n')
        team_file.write(f'### [Current roster]({GIT}{TEAM_CODE}_players)')

    with open(f'{PATH}{TEAM_CODE}_players.md', 'w') as roster_file:
        front_matter(roster_file, f'{TEAM} current roster', f'labs/{TEAM_CODE}_players')

        for player in table[1:6]:
            nickname = player.find('a').text
            name = player.find('td', 'team-members-irlname').text
            country = player.find('span', 'country-sprite')['title']
            role = player.find('span', 'role-sprite')['title']
            link = player.find('a')['href']
            image = next(DDGS().images(f'{TEAM_CODE.upper()} "{nickname}" gamepedia'))['image']

            roster_file.write(f"## {role}\n")
            roster_file.write(f"![{nickname}]({image})\n")
            roster_file.write(f"### [{nickname}]({GIT}{nickname.lower().replace(' ', '_')})\n")
            roster_file.write(f"{name}\n\n")
            roster_file.write(f"{country}\n")

            with open(f"{PATH}{nickname.lower().replace(' ', '_')}.md", 'w') as player_file:
                front_matter(player_file, nickname, f"labs/{nickname.lower().replace(' ', '_')}")