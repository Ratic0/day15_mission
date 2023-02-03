def sort_insert(a, b):
	pokemons.append([a, b])
	sorted_pokemons = sorted(pokemons, key = lambda x: x[1])
	return sorted_pokemons

pokemons = [['피카츄', 10], ['파이리', 5], ['라이츄', 20]]

if __name__ == "__main__":

	while True:
		name = input("추가할 포켓몬--> : ")
		hp = int(input("포켓몬 체력--> : "))
		now_pokemons = sort_insert(name, hp)
		print(now_pokemons)
