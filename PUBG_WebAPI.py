import requests
# O PUBG Game Data Service torna mais fácil para os usuários terem acesso aberto aos dados do jogo, 
# que os desenvolvedores podem usar para criar ferramentas e serviços incríveis.

url = "https://api.pubg.com/shards/$platform/players/account.50e9bf6d4d2a4e7081f21b3ac607977b/seasons/division.bro.official.console-09"

headers = {
    'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzY2Q4"
                     "N2Q0MC0xMTk0LTAxMzktNjg1Yy0wMjUxZDFmMTIwMzkiLCJpc3MiOiJnYW1l"
                     "bG9ja2VyIiwiaWF0IjoxNjA2MzQwMjA0LCJwdWIiOiJibHVlaG9sZSIsInRp"
                     "dGxlIjoicHViZyIsImFwcCI6IndoZXJlLWlzLWl0LXRvIn0.0rdfF4IzNk-DV"
                     "jBVp7J-9-0xU6hzkfehZi678p2sOPQ",
    'Accept': "application/vnd.api+json"
}

response = requests.get(url, headers=headers).json()

print(response)
