# Plano de evolução — site da Sotaque

Escrito em 10/11/2026. Cada bloco abaixo é uma sessão nova de chat.
Troca o modelo indicado, cola o briefing do bloco e confere o resultado.

## Como usar

Sessão nova começa do zero: não sabe nada das conversas anteriores.
Por isso cada bloco tem um briefing pronto pra colar. Não funciona dizer
só "continua".

Três coisas que economizam crédito em qualquer bloco:

- Faz o bloco inteiro numa sentada só. Voltar no dia seguinte custa bem mais caro.
- Pede o escopo fechado do briefing. Ampliar no meio obriga a reler tudo.
- Termina o briefing com "não tira screenshot, eu confiro". Olhar imagem é caro,
  e você confere mais rápido.

## Qual modelo pra quê

| Modelo | Quando usar |
| --- | --- |
| Sonnet | Tarefa mecânica e bem definida: mover arquivo, ajuste de CSS já decidido, commit |
| Opus | Mudança com julgamento visual em código que já existe: timing, curva, o que fica bom |
| Fable 5.2 | Problema grande e mal definido, ou movimento complexo. O mais caro, só onde se paga |

Entre as versões do Fable, sempre a 5.2: é mais barata que a 5.1 e ganha dela
em todos os testes.

## Os blocos

| # | Bloco | Modelo | Status |
| --- | --- | --- | --- |
| S0 | Simplificar o projeto | Sonnet | a fazer |
| S1 | Transições entre seções | Opus | a fazer |
| S2 | Transição home para cases | Opus | a fazer |
| S3 | Personagens e stickers vivos | Opus | a fazer |
| S4 | Loader com peso | Fable 5.2 | a fazer |
| S5 | Parede de cobogós com luz | Fable 5.2 | só se o S4 convencer |

O S0 vem antes de todos. Sem ele, as sessões seguintes não conseguem
reconstruir o site.

---

## S0 — Simplificar o projeto · Sonnet

Hoje o `index.html` e o `cases.html` são gerados por uma fábrica de scripts que
só existia no ambiente da Claude, não no seu Mac. Uma sessão nova não consegue
reconstruir o site a partir do `design/Main.src.html`. Como o site agora vive no
GitHub Pages, e não mais no canvas da Claude, a saída é abandonar essa fábrica:
o `index.html` e o `cases.html` passam a ser o arquivo original mesmo. Os dois
são autossuficientes, com o CSS e o JavaScript dentro.

**Briefing:**

> O site fica em ~/Projects/sotaque-site e está no ar em sotaqueagencia.com.br
> pelo GitHub Pages. Hoje o index.html e o cases.html são gerados por uma fábrica
> de scripts que não existe mais, então ninguém consegue reconstruí-los a partir
> da pasta design. Quero que o index.html e o cases.html virem o arquivo original,
> editados direto.
>
> Faz o seguinte: apaga a pasta design, e cria no lugar um NOTAS.md explicando a
> estrutura do projeto. O NOTAS.md precisa cobrir: quais arquivos existem e pra
> que serve cada um, as seções do index.html na ordem, como o JavaScript da classe
> Component controla as animações pelas variáveis de CSS do scroll (--e, --p, --q,
> --o, --cv), o que é a pasta preview e por que a raiz mostra uma tela de "em
> breve", e como rodar o site local e publicar.
>
> Não mexe no visual nem no comportamento do site. Confere que index.html,
> cases.html e as duas páginas dentro de preview continuam abrindo igual. Commit
> no final, sem push.

---

## S1 — Transições entre seções · Opus

O site tem um motor de scroll que já calcula a posição de cada seção e expõe isso
em variáveis de CSS. O que falta é usar melhor o que já existe. Três pontos:

- O empilhamento de "O que fazemos" para "Cases" está raso: a seção que sai só
  encolhe um pouco e escurece.
- "Marcas que confiam", o cartão de contato e o rodapé entram sem animação
  nenhuma, destoando do resto.
- A entrada da seção escura por cima da clara merece mais profundidade.

**Briefing:**

> Lê o NOTAS.md em ~/Projects/sotaque-site. Quero refinar as transições entre as
> seções do index.html, usando o motor de scroll que já existe.
>
> Três coisas: o empilhamento de "O que fazemos" para "Cases" está raso demais, a
> seção escura entrando por cima da clara merece mais profundidade, e as seções
> "Marcas que confiam", contato e rodapé entram sem animação nenhuma, enquanto o
> resto do site tem.
>
> Faz as três, roda o site local e me avisa a porta, que eu confiro e mando print.
> Não tira screenshot. No celular tem que continuar leve.

---

## S2 — Transição home para cases · Opus

Hoje a ida da home para `/cases` é um corte seco entre duas páginas. As duas
compartilham o mesmo fundo escuro no topo, então dá pra fazer parecer uma coisa
só.

**Briefing:**

> Lê o NOTAS.md em ~/Projects/sotaque-site. A ida da home para /cases é um corte
> seco. Quero que o fundo escuro continue entre as duas páginas, como se fosse a
> mesma, tanto na ida quanto na volta.
>
> Vale pros links "Ver todos os cases", o do menu e o do rodapé. Se a pessoa
> chegar direto em /cases pelo link, tem que funcionar igual. Roda local e me
> avisa. Não tira screenshot.

---

## S3 — Personagens e stickers vivos · Opus

Os desenhos da Cecilia e do Wictor estão parados na seção "Quem somos". Os quatro
stickers dos bichos também. Dá pra dar vida sem sair do flat.

Um detalhe: os personagens hoje são PNG exportados do Figma. Alguns efeitos, como
os olhos seguirem o cursor, precisariam do SVG de volta, que está no histórico do
repositório.

**Briefing:**

> Lê o NOTAS.md em ~/Projects/sotaque-site. Quero dar vida aos desenhos da seção
> "Quem somos" e aos quatro stickers dos bichos, sem exagero e sem sair do estilo
> flat: piscar, respirar e o adesivo descolando um pouco no hover.
>
> Os personagens hoje são PNG. Antes de começar, me diz se algum efeito que você
> quer fazer precisa do SVG de volta, que está no histórico do git. Roda local e
> me avisa. Não tira screenshot.

---

## S4 — Loader com peso · Fable 5.2

A tela de carregamento tem três cubos de cobogó andando num quadrado de quatro
espaços, sempre com um vazio. Hoje eles deslizam. A ideia é que tombem de
verdade, com peso.

É pequeno, isolado e de puro movimento. Serve pra testar se o Fable entrega algo
que o Opus não entregaria antes de gastar com o bloco grande.

**Briefing:**

> Lê o NOTAS.md em ~/Projects/sotaque-site. A tela de carregamento tem três cubos
> de cobogó que andam num quadrado 2x2, sempre com um espaço vazio, no sentido
> horário. Hoje eles deslizam.
>
> Quero que tombem de verdade pro espaço vazio, com peso e inércia, girando sobre
> a aresta. É a única coisa dessa sessão: não mexe em mais nada do site. Roda
> local e me avisa. Não tira screenshot.

---

## S5 — Parede de cobogós com luz · Fable 5.2

Cobogó existe pra filtrar luz, e o site ainda não mostra isso. A ideia é uma
parede com espessura real e uma luz atravessando os furos, projetando sombra
conforme o scroll.

É a peça de assinatura do site, e a mais cara de todas. Só vale depois do S4
mostrar que o investimento compensa.

Dois cuidados: a biblioteca de 3D soma peso e precisa carregar só quando a seção
aparece, com a versão atual de reserva em celular fraco. E os cobogós hoje são
imagem; a cena precisaria deles em vetor.

**Briefing:**

> Lê o NOTAS.md em ~/Projects/sotaque-site. Quero uma parede de cobogós em 3D numa
> seção só do site, com espessura real e luz atravessando os furos, projetando
> sombra conforme o scroll.
>
> Antes de escrever código, me manda o plano: qual seção, qual biblioteca, quanto
> pesa, como carrega só quando a seção aparece e qual é a reserva em celular
> fraco. Os cobogós hoje são imagem em assets; me diz se precisa deles em vetor.

---

## Fora do plano

**Reconstruir em Astro.** Foi sugerido pra melhorar indexação e velocidade. É
refazer do zero um site que funciona e está no ar, por um ganho que, num site de
agência com duas páginas, não paga o custo. Fica anotado caso o site cresça.

**Som dos sotaques.** Tocar a expressão falada quando clica na marca e troca de
estado, começando desligado. Depende de vocês gravarem os áudios.

**Textos dos cases.** Os campos de desafio, solução e resultado continuam entre
colchetes no site. Estão no doc "Cases da Sotaque — textos pra preencher". Não
precisa de sessão de código: preenche o doc e manda.

**Tirar o "em breve".** Quando o site estiver pronto, a raiz volta a ser o site
completo e a pasta preview some.
