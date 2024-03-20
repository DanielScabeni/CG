<h1 align="center">
  <img src="https://raw.githubusercontent.com/DanielScabeni/CG/master/title.svg" alt="title" />
</h1>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<table>
  <tr>
    <td width="50%">
      <a href="https://github.com/DanielScabeni/CG">
        <img src="https://github-readme-stats.vercel.app/api/pin/?username=DanielScabeni&repo=CG&theme=chartreuse-dark" alt="Readme Card">
      </a>
    </td>
    <td width="50%">
  </a>
    <p style="color: white;">Repositorio da matéria de Computação e Projeto Gráfico de 2024 do curso de Sistemas de Informações da Universidade MaterDei (UNIMATER), ministrada pelo professor Dr. Rafael Barbosa.</p>
    </td>
  </tr>
</table>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

# O que é o Bate Bate

- O Bate-Bate é um jogo simples em Python que demonstra o movimento de um texto na tela. O texto se move aleatoriamente e muda de cor quando colide com as bordas da tela.

## Estrutura do Projeto:

### O projeto é dividido em três arquivos:

- main.py: Contém a classe main que inicia o jogo.
- Game.py: Contém a classe Game que controla a tela, o fps e a atualização do jogo.
- MecMovimento.py: Contém a classe MovendoTexto que controla o movimento, a cor e a posição do texto.

<img src="https://github.com/DanielScabeni/CG/Classes.png">

### Classe Main

- Inicializa rodando o jogo pela classe Game

### Classe Game

- A classe Game é a responsável por gerenciar o funcionamento geral do jogo. Ela controla a inicialização do Pygame, a criação da janela do jogo, o loop principal e a atualização do texto móvel.

#### Atributos:

- largura: Define a largura da janela do jogo em 800 pixels.
- altura: Define a altura da janela do jogo em 600 pixels.
- tela: Superfície do Pygame que representa a janela do jogo. Definida com as variaveis de largura e altura.
- clock: O objeto Clock do Pygame é usado para controlar a taxa de atualização (fps) do jogo (limitando a 60 quadros por segundo).
- MovendoTexto: Objeto da classe MovendoTexto que controla o texto que se move na tela.

#### Metodos: 

  ##### __init__(self): 
  - Construtor da classe Game. É chamado automaticamente quando um objeto da classe é criado.
- Define a largura, altura, titulo da janela, cria a superficie da tela utilizando esses valores.
- Cria um objeto para controlar a taxa de atualização e um para controlar o texto que se move na tela.

  ##### run(self):
  - Loop principal do jogo, É responsável por manter o jogo rodando até que o usuário feche a janela.
- Responsável por atualizar a tela e a posição do texto, preenche a tela com a cor preta e limitar o fps para 60.



<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

| [![GitHub Stats](https://github-readme-stats.vercel.app/api?username=DanielScabeni&show_icons=true&card_width=300&theme=chartreuse-dark)](https://github.com/DanielScabeni) | [![GitHub Stats](https://github-readme-stats.vercel.app/api?username=DanielScabeni&show_icons=true&card_width=130&theme=dark#gh-dark-mode-only)](https://github.com/DanielScabeni) |
| --- | --- |

| [![Card 1](https://github-readme-stats.vercel.app/api/top-langs/?username=DanielScabeni&layout=donut-vertical&theme=chartreuse-dark)](https://github.com/DanielScabeni) | [![Card 2](https://github-readme-stats.vercel.app/api/top-langs/?username=DanielScabeni&langs_count=8&theme=chartreuse-dark)](https://github.com/DanielScabeni) | [![Card 3](https://github-readme-stats.vercel.app/api/top-langs/?username=DanielScabeni&layout=pie&theme=chartreuse-dark)](https://github.com/DanielScabeni) |
| --- | --- | --- |
