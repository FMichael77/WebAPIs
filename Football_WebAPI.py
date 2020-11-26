import requests
# football-data.org fornece dados e estatísticas de futebol 
# (resultados ao vivo, jogos, tabelas, times, escalações / subs, etc.).

url = "http://api.football-data.org/v2/competitions/PL/matches/?matchday=22"

headers = {
    'X-Auth-Token': '8a4353e0b8144778a8110b74427469c4'
}

response = requests.get(url, headers=headers).json()

print(response)