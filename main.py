# -*- coding: utf-8 -*-
"""Rotina principal de execução - Entry Point

    press: presentation => apresentação

    A estrutura consiste de:
        pasta img = figuras para uso na interface ou usadas como ilustração nos slides
        pasta press = estrutura o código necessário para criar uma app similar a uma apresentação.
            subpasta exemplo = contem os codigos exemplos retirados da propria instalacao do VPython
            subpasta slides = arquivos .py com comandos VPython para montagem da apresentação.

        wxpress.py = módulo principal com a definicao:
            - do formato da janela
            - dos widgets que compoe a janela
            - da lógica para execucao dos arquivos contidos na subpasta slide e exemplo
"""


from press.wxpress import WxVpress

if __name__ == '__main__':

    presentation = WxVpress()
