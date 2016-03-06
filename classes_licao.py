class Song(object):
    def __init__(self, letras):
        self.letras = letras

    def sing_me_a_song(self):
        for line in self.letras:
            print(line)

    def quem_e_o_cantor(self):
        for line in self.letras:
            for letra in line:
                if letra in "aeiou":
                    print("*")
                else:
                    print(letra)


feliz_aniversario = Song(["Parabens para voce",
                        "nessa data querida",
                         "muitas felicidades",
                         "muitos anos de vida"])

framengo = Song(["Quando surge o Framengo imponente",
                "no gramado onde a luta o aguarda",
                "sabe bem que vai ser rebaixado",
                "por que esse clube nao vale nada"])

feliz_aniversario.sing_me_a_song()
print
framengo.sing_me_a_song()
print
wilco = ["California stars", "Amor meu grande amor", "jesus etc", "blablabla"]
lulu = ["Mais uma de amor", "Qualquer porra", "Mais uma musica", "Poodle atolado na merda"]
wilco = Song(wilco)
lulu = Song(lulu)
wilco.sing_me_a_song()
print
lulu.sing_me_a_song()
lulu.quem_e_o_cantor()
framengo.quem_e_o_cantor()