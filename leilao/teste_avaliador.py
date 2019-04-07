from unittest import TestCase

from leilao.dominio import Avaliador, Leilao, Lance, Usuario


class TestAvaliador(TestCase):

    def test_quando_leilao_ordem_crescente_avalia_maior_menor_lance(self):
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')

        lance_do_yuri = Lance(yuri, 100.0)
        lance_do_gui = Lance(gui, 150.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_do_yuri)
        leilao.lances.append(lance_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

        def test_quando_leilao_ordem_decrescente_avalia_maior_menor_lance(self):
            gui = Usuario('Gui')
            yuri = Usuario('Yuri')

            lance_do_gui = Lance(gui, 150.0)
            lance_do_yuri = Lance(yuri, 100.0)

            leilao = Leilao('Celular')

            leilao.lances.append(lance_do_yuri)
            leilao.lances.append(lance_do_gui)

            avaliador = Avaliador()
            avaliador.avalia(leilao)

            menor_valor_esperado = 100.0
            maior_valor_esperado = 150.0

            self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
            self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

        def test_quando_leilao_somente_um_lance_avalia_maior_menor_lance_com_valores_iguais(self):
            gui = Usuario('Gui')
            lance_do_gui = Lance(gui, 150.0)

            leilao = Leilao('Celular')

            leilao.lances.append(lance_do_gui)

            avaliador = Avaliador()
            avaliador.avalia(leilao)

            menor_valor_esperado = 150.0
            maior_valor_esperado = 150.0

            self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
            self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

        def test_quando_leilao_mais_de_dois_lances_avalia_maior_menor_lance(self):
            gui = Usuario('Gui')
            yuri = Usuario('Yuri')
            vini = Usuario('Vini')

            lance_do_gui = Lance(gui, 150.0)
            lance_do_yuri = Lance(yuri, 100.0)
            lance_do_vini = Lance(vini, 200.00)

            leilao = Leilao('Celular')

            leilao.lances.append(lance_do_yuri)
            leilao.lances.append(lance_do_gui)
            leilao.lances.append(lance_do_vini)

            avaliador = Avaliador()
            avaliador.avalia(leilao)

            menor_valor_esperado = 100.0
            maior_valor_esperado = 200.0

            self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
            self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

