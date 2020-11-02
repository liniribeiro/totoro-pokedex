from sqlalchemy import Column, String

from pokedex.database.models.base import BaseModel


class PokemonModel(BaseModel):
    __tablename__ = 'pokemon'

    nome = Column(String)
    especie = Column(String)
    tipo = Column(String)

    def __repr__(self):
        return f'Pokemon {self.name}'

    def to_dict(self):
        return {
            'id': str(self.id),
            'nome': self.nome,
            'especie': self.especie,
            'tipo': self.tipo
        }




# #base de dados de pokemons
#
# pokemon1 = Pokemon(1, 'Meowth', 'Arranha Gato', 'Normal')
# pokemon2 = Pokemon(2, 'Charmander', 'Lagarto', 'Fogo')
# pokemon3 = Pokemon(3, 'Clefairy', 'Fada', 'Fada')
# pokemon4 = Pokemon(4, 'Machop', 'Superpoder', 'Lutador')
# pokemon5 = Pokemon(5, 'Rhyhorn', 'Espigão', 'Terrestre/pedra')
# pokemon6 = Pokemon(6, 'Cyndaquil', 'Rato de fogo', 'Fogo')
# pokemon7 = Pokemon(7, 'Shuckle', 'Mofo', 'Pedra')
# pokemon8 = Pokemon(8, 'Whismur', 'Sussuro', 'Normal')
# pokemon9 = Pokemon(9, 'Swablu', 'Pássaro de algodão', 'Voador')
# pokemon10 = Pokemon(10, 'Bidoof', 'Rato Gorducho', 'Normal')
#
# pokemon_list = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6, pokemon7, pokemon8, pokemon9, pokemon10]
