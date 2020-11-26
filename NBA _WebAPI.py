import requests
# API gratuita para acessar dados relacionados à NBA.

game_id = '1'
url = "https://free-nba.p.rapidapi.com/games/{game_id}"
url = url.format(game_id=game_id)

headers = {
    'x-rapidapi-key': "bd4f7d1459msh6fd24d906d341b8p1500f2jsn62a019aad86f",
    'x-rapidapi-host': "free-nba.p.rapidapi.com"
}

response = requests.get(url, headers=headers).json()

print(" Data do jogo: %s \n"
      " Time da casa: %s Pontos: %i\n"
      " Time visitante: %s Pontos: %i" %
      (response['date'], response['home_team']['full_name'], response['home_team_score'],
       response['visitor_team']['full_name'], response['visitor_team_score']))
