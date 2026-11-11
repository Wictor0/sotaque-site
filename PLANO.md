# Plano de evolução — site da Sotaque

Escrito em 10/11/2026, corrigido em 11/11/2026 depois do S0.
Cada bloco abaixo é uma sessão nova de chat. Troca o modelo indicado, cola o
briefing do bloco e confere o resultado.

## Antes de tudo: onde fica o site

A raiz (`index.html` e `cases.html`) é só a tela de "em breve". **O site completo
está em `preview/index.html` e `preview/cases.html`.** Todos os blocos daqui pra
frente mexem nos arquivos de `preview/`.

As páginas de `preview/` não são autossuficientes: dependem de
`vendor/dc-runtime.js`, do React pela CDN e da pasta `assets/`. O `NOTAS.md`
explica como isso funciona.

No servidor local, os links limpos não funcionam: use `/preview/cases.html` em vez
de `/preview/cases`. No GitHub Pages funciona dos dois jeitos.

## Como usar

Sessão nova começa do zero: não sabe nada das conversas anteriores. Por isso cada
bloco tem um briefing pronto pra colar. Não funciona dizer só "continua".

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

Entre as versões do Fable, sempre a 5.2: é mais barata que a 5.1 e ganha dela em
todos os testes.

## Os blocos

| # | Bloco | Modelo | Status |
| --- | --- | --- | --- |
| S0 | Simplificar o projeto | Sonnet | feito (commit 105deac) |
| S1 | Transições entre seções | Opus | feito (commit 595b5b1) |
| S2 | Transição home para cases | Opus | a fazer |
| S3 | Personagens e stickers vivos | Opus | a fazer |
| S4 | Loader com peso | Fable 5.2 | a fazer |
| S5 | Parede de cobogós com luz | Fable 5.2 | só se o S4 convencer |

---

## S1 — Transições entre seções · Opus

O site tem um motor de scroll que já calcula a posição de cada seção e expõe isso
em variáveis de CSS (`--e`, `--p`, `--q`, `--o`, `--cv`). O que falta é usar melhor
o que já existe. Três pontos:

- O empilhamento de "O que fazemos" para "Cases" está raso: a seção que sai só
  encolhe um pouco e escurece.
- "Marcas que confiam", o cartão de contato e o rodapé entram sem animação
  nenhuma, destoando do resto.
- A entrada da seção escura por cima da clara merece mais profundidade.

**Briefing:**

> Lê o NOTAS.md em ~/Projects/sotaque-site. O site completo fica em
> preview/index.html, não na raiz. Quero refinar as transições entre as seções
> dessa página, usando o motor de scroll que já existe.
>
> Três coisas: o empilhamento de "O que fazemos" para "Cases" está raso demais, a
> seção escura entrando por cima da clara merece mais profundidade, e as seções
> "Marcas que confiam", contato e rodapé entram sem animação nenhuma, enquanto o
> resto do site tem.
>
> Faz as três, roda o site local e me avisa a porta e o caminho, que eu confiro e
> mando print. Não tira screenshot. No celular tem que continuar leve. Commit no
> final, sem push.

---

## S2 — Transição home para cases · Opus

Hoje a ida de `preview/index.html` para `preview/cases.html` é um corte seco entre
duas páginas. As duas compartilham o mesmo fundo escuro no topo, então dá pra
fazer parecer uma coisa só.

**Briefing:**

> Lê o NOTAS.md em ~/Projects/sotaque-site. O site completo fica em preview/. A ida
> de preview/index.html para preview/cases.html é um corte seco. Quero que o fundo
> escuro continue entre as duas páginas, como se fosse a mesma, tanto na ida quanto
> na volta.
>
> Vale pros links "Ver todos os cases", o do menu e o do rodapé. Se a pessoa chegar
> direto na página de cases pelo link, tem que funcionar igual. Lembra que no
> servidor local o caminho é /preview/cases.html, e no GitHub Pages é
> /preview/cases. Roda local e me avisa. Não tira screenshot. Commit no final, sem
> push.

---

## S3 — Personagens e stickers vivos · Opus

Os desenhos da Cecilia e do Wictor estão parados na seção "Quem somos". Os quatro
stickers dos bichos também. Dá pra dar vida sem sair do flat.

Um detalhe: os personagens hoje são PNG exportados do Figma. Alguns efeitos, como
os olhos seguirem o cursor, precisariam do SVG de volta, que está no histórico do
repositório.

**Briefing:**

> Lê o NOTAS.md em ~/Projects/sotaque-site. O site completo fica em
> preview/index.html. Quero dar vida aos desenhos da seção "Quem somos" e aos
> quatro stickers dos bichos, sem exagero e sem sair do estilo flat: piscar,
> respirar e o adesivo descolando um pouco no hover.
>
> Os personagens hoje são PNG (assets/cecilia.png e assets/wictor.png). Antes de
> começar, me diz se algum efeito que você quer fazer precisa do SVG de volta, que
> está no histórico do git. Roda local e me avisa. Não tira screenshot. Commit no
> final, sem push.

---

## S4 — Loader com peso · Fable 5.2

O bloco `#boot`, no começo das páginas de `preview/`, tem três cubos de cobogó
andando num quadrado de quatro espaços, sempre com um vazio, no sentido horário.
Hoje eles deslizam. A ideia é que tombem de verdade, com peso.

A mesma animação aparece na tela de "em breve" da raiz. Vale aplicar nas duas
depois que ficar bom.

É pequeno, isolado e de puro movimento. Serve pra testar se o Fable entrega algo
que o Opus não entregaria antes de gastar com o bloco grande.

**Briefing:**

> Lê o NOTAS.md em ~/Projects/sotaque-site. O bloco #boot no começo de
> preview/index.html e preview/cases.html é a tela de carregamento: três cubos de
> cobogó que andam num quadrado 2x2, sempre com um espaço vazio, no sentido
> horário, pela animação CSS bootMove. Hoje eles deslizam.
>
> Quero que tombem de verdade pro espaço vazio, com peso e inércia, girando sobre
> a aresta. Aplica nas duas páginas de preview e também na tela de "em breve" da
> raiz (index.html e cases.html), que usa a mesma animação. É a única coisa dessa
> sessão: não mexe em mais nada. Roda local e me avisa. Não tira screenshot. Commit
> no final, sem push.

---

## S5 — Parede de cobogós com luz · Fable 5.2

Cobogó existe pra filtrar luz, e o site ainda não mostra isso. A ideia é uma parede
com espessura real e uma luz atravessando os furos, projetando sombra conforme o
scroll.

É a peça de assinatura do site, e a mais cara de todas. Só vale depois do S4
mostrar que o investimento compensa.

Dois cuidados: a biblioteca de 3D soma peso e precisa carregar só quando a seção
aparece, com a versão atual de reserva em celular fraco. E os cobogós hoje são
imagem (`assets/cobogo-*.webp`); a cena precisaria deles em vetor.

**Briefing:**

> Lê o NOTAS.md em ~/Projects/sotaque-site. O site completo fica em preview/. Quero
> uma parede de cobogós em 3D numa seção só, com espessura real e luz atravessando
> os furos, projetando sombra conforme o scroll.
>
> Antes de escrever código, me manda o plano: qual seção, qual biblioteca, quanto
> pesa, como carrega só quando a seção aparece e qual é a reserva em celular fraco.
> Os cobogós hoje são imagem em assets/cobogo-*.webp; me diz se precisa deles em
> vetor.

---

## Tarefas soltas

Coisas pequenas que cabem no fim de qualquer bloco, ou numa sessão curta de Sonnet.

- **README.md desatualizado.** Ainda fala da pasta `design/` e trata o `index.html`
  da raiz como a página completa. Reescrever a partir do `NOTAS.md`.
- **Textos dos cases.** Os campos de desafio, solução e resultado continuam entre
  colchetes. Estão no doc "Cases da Sotaque — textos pra preencher". Não precisa de
  sessão de código: preenche o doc e manda.
- **E-mail e Instagram.** O site usa `contato@sotaqueagencia.com`, que não é o
  e-mail certo, e os links das redes não levam a lugar nenhum.

## Lançamento

Quando o site estiver pronto: copiar `preview/index.html` e `preview/cases.html`
por cima dos da raiz, trocar os links `/preview/...` por `/...`, tirar o `noindex`,
ajustar `og:url` e `<title>`, e apagar a pasta `preview/`. O `NOTAS.md` detalha.

## Fora do plano

**Reconstruir em Astro.** Foi sugerido pra melhorar indexação e velocidade. É
refazer do zero um site que funciona e está no ar, por um ganho que, num site de
agência com duas páginas, não paga o custo. Fica anotado caso o site cresça.

**Som dos sotaques.** Tocar a expressão falada quando clica na marca e troca de
estado, começando desligado. Depende de vocês gravarem os áudios.
