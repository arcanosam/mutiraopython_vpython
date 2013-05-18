mutiraopython_vpython
================================

Aplicação usada para apresentação do Mutirão Python - Introdução ao VPython
* URL da apresentação: [Meu canal no Youtube](https://www.youtube.com/user/arcanosam).*

<dl>
  <dt>Pasta Exemplos</dt>
  <dd>Não detenho a autoria sobre nenhum dos códigos desta pasta</dd>
  <dd>Foram selecionados apenas para visualização nesta aplicação, podendo conter uma outra modificação necessária.</dd>
  <dd>Suas versões originais e identificação dos respectivos autores podem ser conferidos na pasta examples da instalação do VPython.</dd>
  <dd>Todos os direitos reservados</dd>
</dl>


18/05/2013
    Funcionalidades:
        - Interface gráfica full-screen contém:
            - 1 canvas 3d
                - o atributo range do objeto display é 3
                    pois foi o melhor para visualizacao
                    dos textos 3D
                    obs: o funcionamento normal é a cena ser montada auto-centralizada e
                        auto-escalada, e prejudicava a visualização dos textos

            - 1 widget para simples edição de código
                com scrolls verticais e horizontais
            - 4 botões:
                - 'Run' - Executar códigos
                - 'Voltar' - Retorna ao módulo python anterior
                - 'Próximo' - Avança para o próximo módulo python
                - 'Salvar' - Salvar o código no seu arquivo de origem
            - A saída do programa dá-se apenas por alt-f4 ou ao clicar
                no botão de fechar no canto direito superior da tela

    #TODOS

        prioridade Alta:
            - Prevenir que o usuário clique mais de uma vez seguidamente no botão
                'Salvar' pois poder causar de interromper o processo de 'salvar'
                iniciado originalmente e nao gravar o conteudo do textCtrl,
                passando o módulo python a permanecer em branco

        prioridade Baixa:
            - Resetar camera a sua posição de origem quando houver sido
            dado um zoom
            - Incluir um widget do tipo combo que poderia listar bandeiras para
            que o usuário selecione a sua língua de origem.
            - Eliminar a ilusão de ótica do alinhamento dos objetos 3d nos slides
                - a ilusão se dá pela posição da camera e a posição global
                    dos objetos no espaço 3d global