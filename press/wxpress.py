# -*- coding: utf-8 -*-
"""definicao da classe WxVpress para montar a apresentação

    Módulos importados:
        visual - contem a maioria dos recursos do VPython
        wx - contem todos os recursos para criacao e gestao de uma janela usando wxPython
"""

from visual import *

import wx


class WxVpress:

    def __init__(self):
        """inicializa os atributos necessarios para criacao da aplicação gráfica

            logica:
                define-se os principais atributos
                captura resoluçao de tela
                cria a interface grafica/janela
                cria o widget TextCtrl que é um campo texto
                cria os botoes
                seta o primeiro slide a ser carregado

            atributos principais:
                idslide = um contador, cujo valor representa um indice no atributo
                        slidep
                offset = valor de auxilio usado para posicionar widgets
                offsetw = recebe a largura extra correspondente a dimensao da janela
                offseth = recebe a altura extra correspondente a dimensao da janela
                    window = objeto VPython que faz um wrapper da classe wx.Frame
                        geralmente usada para definicao de classes customizadas
                        de janela
                prange = corresponde ao range do posicionamento da camera em relacao
                    aos objetos 3D criados na tela
                dsy = recebe um objeto display que cria a área(canvas) de renderizacao
                    3D a ser vinculado a janela
                code_editor = recebe um objeto wx.TextCtrl para load de arquivos .py
                win_panel = recebe o painel proveniente da criacao de um objeto window
                    que sera usado para vinculo de alguns widgets
                scr_mtrs = 'screen metrics' - recebe as dimensões do vídeo/tela
                    uma tupla (width,height)
                scr_center = 'screen center' - calcula conforme o scr_mtrs uma aproximacao
                    do centro da tela
        """

        self.idslide = -1
        self.offset = 20
        self.offsetw = window.dwidth
        self.offseth = window.dheight
        self.prange = 3.0
        self.dsy = None
        self.code_editor = None
        self.win_panel = None

        self.scr_mtrs = wx.GetDisplaySize()

        self.scr_center = (
            self.scr_mtrs[0]/2 - (self.offsetw + self.offset),
            self.scr_mtrs[1] - (self.offseth + self.offset)
        )

        self.set_slides()

        self.create_main_win()

        self.create_code_ed()

        self.create_btns()

        self.next_slide()

    def set_slides(self):
        """cria-se os atributos que vao auxiliar na coordenacao dos 'slides'

            logica:
                define uma lista que contem os arquivos .py que
                    contem códigos que correspondem a um 'slide'
                    da apresentação
                define a melhor range para posicionar a camera
                    de forma a garantir a melhor visualização do
                    conteudo 3d gerado por cada uma dos respectivos
                    arquivos .py

            atributos principais adicionados adicionados a classe WxVpress:

                slidesp = lista que contem paths de arquivos .py que
                    representam um slide gerado em 3D
                sliderange = lista de inteiros que sentam o range da
                    camera para melhor visualizacao do conteudo 3d gerado
                    em cada um dos arquivos .py

        """

        self.slidesp = [
            'press\\slides\\sld01.py',
            'press\\slides\\sld02.py',
            'press\\slides\\sld03.py',
            'press\\slides\\sld04.py',
            'press\\slides\\sld05.py',''
            'press\\exemplo\\bounce.py',
            'press\\exemplo\\bounce2.py',
            'press\\exemplo\\boxlighttest.py',
            'press\\exemplo\\doublependulum.py',
            'press\\exemplo\\faces_cone.py',
            'press\\exemplo\\gyro.py',
            'press\\exemplo\\gyro2.py',
            'press\\exemplo\\hanoi.py',
            'press\\slides\\sld06.py'
        ]

        self.sliderange = [3, 3, 3, 3, 3, 8, 8, 8, 3, 3, 2, 2, 15, 3]

    def create_main_win(self):
        """cria a interface gráfica e customiza seus atributos

            logica:
                cria a janela a partir de um objeto window
                cria um canvas 3D a partir do objeto display
                salva a cena 3D (caso tenha-se feito uma rotacao)
                    #TODO - salvar caso tenha-se feito um zoom
                define que a janela tera apenas o título e o botao de fechar
                seta o atributo win_panel para posterior uso para vinculo
                    widgets

            atributos principais:
                window_press = recebe um objeto window que cria a janela
                    recebendo os primeiros parametros para customizacao
                dsy = recebe um objeto display que define a area de desenho em 3D
                    vinculado a janela definida em window_press e atributos
                    definidos arbitrariamente anteriormente



        """

        self.window_press = window(
            width=self.scr_mtrs[0],
            height=self.scr_mtrs[1],
            title=u'Mutirão Python - Introdução ao VPython'
        )

        self.dsy = display(
            window=self.window_press,
            x=self.offset,
            y=self.offset,
            width=self.scr_center[0],
            height=self.scr_center[1],
            range=self.prange
        )

        self.save_scene()

        self.window_press.win.SetWindowStyle(wx.CAPTION | wx.CLOSE_BOX)

        self.win_panel = self.window_press.panel


    def create_code_ed(self):
        """cria um campo text - widget wx.TextCtrl

            logica:
                cria um widget TextCtrl e seta atributos basicos
                    e define que seja de multiplas linhas e scroll horizontal
                seta a fonte e os atributos desta a ser usada neste TextCtrl
        """

        coded = wx.TextCtrl(
            self.win_panel,
            -1,
            pos=(
                self.scr_center[0]+self.offsetw+self.offset,
                self.offset
            ),
            value='',
            size=(
                self.scr_center[0],
                self.scr_center[1]-self.offseth
            ),
            style=wx.TE_MULTILINE | wx.TE_PROCESS_ENTER | wx.HSCROLL
        )

        coded.SetFont(wx.Font(18, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Courier New'))

        self.code_editor = coded

    def create_btns(self):
        """cria-se 4 botoes para controle da aplicação.

            logica:
                carrega-se a imagem a ser usada em cada botao
                 define 4 botoes do tipo BitmapButton:
                    para avançar o slide
                    para retroceder o slide
                    para executar o código carregado no TextCtrl
                    para salvar o código carregado no TextCtrl no arquivo
                    originalmente lido
                define para cada botao, seu respectivo ToolTipo
                    dica para quando posiciona-se o mouse em cima do botao
                faz-se um bind de um método que representa a ação de cada botao

                atributos principais adicionados adicionados a classe WxVpress:

                    btnnext = objeto wx.BitmapButbon
                    btnprev = objeto wx.BitmapButbon
                    btnrun = objeto wx.BitmapButbon
                    btnsavef = objeto wx.BitmapButbon

        """

        imgtmp1 = wx.Image('img\\next32.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        imgtmp2 = wx.Image('img\\previous32.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        imgtmp3 = wx.Image('img\\run32.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        imgtmp5 = wx.Image('img\\save32.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()

        self.btnnext = wx.BitmapButton(
            self.win_panel,
            id=wx.ID_ANY,
            bitmap=imgtmp1,
            pos=(
                self.scr_center[0]+self.offsetw+self.offset+2*(imgtmp1.GetWidth()+5),
                self.scr_center[1]-10
            ),
            size = (
                imgtmp1.GetWidth()+5,
                imgtmp1.GetHeight()+5
            ),
        )

        self.btnprev = wx.BitmapButton(
            self.win_panel,
            id=wx.ID_ANY,
            bitmap=imgtmp2,
            pos=(
                self.scr_center[0]+self.offsetw+self.offset+imgtmp2.GetWidth()+5,
                self.scr_center[1]-10
            ),
            size = (
                imgtmp2.GetWidth()+5,
                imgtmp2.GetHeight()+5
            ),
        )

        self.btnrun = wx.BitmapButton(
            self.win_panel,
            id=wx.ID_ANY,
            bitmap=imgtmp3,
            pos=(
                self.scr_center[0]+self.offsetw+self.offset,
                self.scr_center[1]-10
            ),
            size = (
                imgtmp3.GetWidth()+5,
                imgtmp3.GetHeight()+5
            ),
        )

        self.btnsavef = wx.BitmapButton(
            self.win_panel,
            id=wx.ID_ANY,
            bitmap=imgtmp5,
            pos=(
                self.scr_center[0]+self.offsetw+self.offset+3*(imgtmp1.GetWidth()+5),
                self.scr_center[1]-10
            ),
            size = (
                imgtmp5.GetWidth()+5,
                imgtmp5.GetHeight()+5
            ),
        )

        self.btnnext.SetToolTip(wx.ToolTip(u'Próximo!'))
        self.btnprev.SetToolTip(wx.ToolTip(u'Anterior!'))
        self.btnrun.SetToolTip(wx.ToolTip(u'Run!'))
        self.btnsavef.SetToolTip(wx.ToolTip(u'Save File!'))

        self.btnrun.Bind(wx.EVT_BUTTON, self.vrun)
        self.btnnext.Bind(wx.EVT_BUTTON,self.next_slide)
        self.btnprev.Bind(wx.EVT_BUTTON,self.prior_slide)
        self.btnsavef.Bind(wx.EVT_BUTTON,self.save_pyfile)


    def prior_slide(self,event):
        """ metodo que carrega o 'slide' anterior no wx.TextCtrl

            parametros:
                event = todo metodo que é vinculado a um widget precisa
            ter um paramento para receber os eventos vinculados
            aquele widget

            logica:
                decrementa o atributo idslide
                testa se o atributo idslide passou do valor do
                    primeiro slide e caso verdadeiro, seta o
                    idslide como 0
                seta o conteudo do wx.TextCtrl com o texto do
                     módulo .py correspondente ao idslide
                    por meio do metodo load_pyfile que
                    le o arquivo e retorna seu conteudo

        """

        self.idslide -= 1

        if self.idslide < 0:
            self.idslide = 0

        self.code_editor.SetValue(
            self.load_pyfile(
                self.slidesp[self.idslide]
            )
        )

    def next_slide(self,event=None):
        """ metodo que carrega o proximo 'slide' no wx.TextCtrl

            parametros:
                event = todo metodo que é vinculado a um widget precisa
            ter um paramento para receber os eventos vinculados
            aquele widget
                        este metodo é chamado no __init__ e como nao foi
                        gerado via evento de um widget causa erro e por
                        isto teve seu valor padrão definido para None

            logica:
                incrementa o atributo idslide
                testa se o atributo idslide passou do valor do
                    último slide e caso verdadeiro, seta o
                    idslide com o indice correspondenteo ao
                    ultimo módulo py ou ultimo 'slide'
                seta o conteudo do wx.TextCtrl com o texto do
                     módulo .py correspondente ao idslide
                    por meio do metodo load_pyfile que
                    le o arquivo e retorna seu conteudo


        """

        self.idslide += 1

        if self.idslide > len(self.slidesp)-1:
            self.idslide = len(self.slidesp) - 1

        self.code_editor.SetValue(
            self.load_pyfile(
                self.slidesp[self.idslide]
            )
        )

    def vrun(self, event):
        """executa o módulo python carregado no momento no textCtrl.

            logica:
                faz a limpeza da cena
                restaura a posicao original da camera, caso tenha-se
                feito uma rotacao
                chama a funcao builtin execfile passando como argumento
                o modulo python carregado no momento

        """

        self.erase_scene()

        self.restore_scene()

        execfile(self.slidesp[self.idslide])

    def save_scene(self):
        """salvar a posicao inicial da camera na cena

            Cria um atributo do tipo dicionario para salvar:

                dist = determina a distancia que está-se da cena
                forw = o vetor inicial que aponta para onde a
                        camera esta 'olhando'
                vup = vetor que representa a coordenada espacial global 3d
                        correspondente ao eixo Y


        """

        self.scenesave = {
            'dist': mag(self.dsy.mouse.camera-self.dsy.center),
            'forw': vector(self.dsy.forward),
            'vup': vector(self.dsy.up)
        }

    def restore_scene(self):
        """restaura a cena 3d

            seta os atributos do objeto (dsy) display (canvas 3d)
                para seus valores originais

        """

        self.dsy.range = self.sliderange[self.idslide]

        self.dsy.up = self.scenesave['vup']
        self.dsy.forward = self.scenesave['forw']

    def erase_scene(self):
        """apaga os objetos existentes no espaço(canvas) 3d

            o objeto (dsy) display possui um atributo que
            armazena todos os objetos 3d gerados pelos comandos
            no módulo carregado em uma lista

            faz-se entao um loop percorrendo este atributo
            para setar o atributo visible de cada objeto 3d
            para False, pois desta forma dá-se inicio ao processo
            interno para sua exclusão em definitivo.
        """

        for each_3dobj in self.dsy.objects:
            each_3dobj.visible = False

    def load_pyfile(self, filecode):
        """metodo para leitura de arquivos

            parametro:
                filecode = path com arquivo

            logica:

                usa a funcao builtin 'open' para abrir o arquivo
                    em modo de leitura, passado pelo parametro filecode
                le-se todo o conteudo do arquivo
                fecha o handle para 'liberar' o arquivo para outras
                    operacoes
                retorna conteudo texto na encoding utf-8


        """

        nextfile = open(filecode,'r')

        content = nextfile.read()

        nextfile.close()

        return content.decode('utf-8')

    def save_pyfile(self, event):
        """metodo que salva o conteúdo do textCtrl em seu arquivo de origem

            parametros:
                event = todo metodo que é vinculado a um widget precisa
            ter um paramento para receber os eventos vinculados
            aquele widget

            logica:

                usa a funcao builtin 'open' para criar o arquivo
                    passado pelo parametro filecode
                recuperar o conteudo do textCtrl e transforma o
                    texto para enconding utf-8
                'escreve' o texto no seu arquivo de origem
                'fecha' o handle de manipulacao do arquivo

        """

        pfiletosave = open(self.slidesp[self.idslide], 'w')

        pfiletosave.write(self.code_editor.GetValue().encode('utf-8'))

        pfiletosave.close()
