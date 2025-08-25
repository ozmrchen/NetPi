import requests, json

pokemon_id = 25  # Pikachu
resp = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
data = resp.json()
print(f"🔍 API INTELLIGENCE: {data['name'].title()} (#{data['id']})")
print(
    f"⚡ Type: {data['types'][0]['type']['name']} | Weight: {data['weight'] / 10}kg | Abilities: {len(data['abilities'])}"
)
print(
    f"🔒 API Security: HTTPS ✅ | Rate Limit: {resp.headers.get('X-RateLimit-Remaining', 'Unknown')}"
)
