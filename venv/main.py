from PokemonFileIO import *
import PokeClass

def main():
    IO.start()
    for i in POKEDEX:
        print(i.name, "\t \t", i.gender, "\t \t", i.ability)

if __name__ == "__main__":
    main()



