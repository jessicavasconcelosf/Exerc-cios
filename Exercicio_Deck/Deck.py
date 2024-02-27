import requests


def retirar_cartas(deck_id, quantidade):
    resposta = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={quantidade}')
    cartas = [card['code'] for card in resposta.json()['cards']]
    print("Cartas retiradas:", cartas)
    return len(cartas)


resposta = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=3')
deck_id = resposta.json()['deck_id']
print("Deck ID:", deck_id)


requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/')


cartas_remanecentes = 3 * 52  

cartas_remanecentes -= retirar_cartas(deck_id, 3)
print("Cartas remanecentes no baralho:", cartas_remanecentes)


requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/')

cartas_remanecentes -= retirar_cartas(deck_id, 3)
print("Cartas remanecentes no baralho:", cartas_remanecentes)


requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/')


cartas_remanecentes -= retirar_cartas(deck_id, 3)
print("Cartas remanecentes no baralho:", cartas_remanecentes)
