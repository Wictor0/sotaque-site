# Notas do projeto — site da Sotaque

Site da agência Sotaque, no ar em https://sotaqueagencia.com.br pelo GitHub Pages
(branch `main`, raiz do repositório). Não há build: o que está no repositório é o
que vai pro ar. Os arquivos HTML são editados direto.

O plano de evolução (blocos de sessão S0 a S5) está em `PLANO.md`.

> **Atenção:** o site real hoje está em `preview/`, não na raiz. Os
> `index.html` e `cases.html` da raiz são a tela de "em breve" (veja a seção
> "Raiz × preview"). Quando o plano falar em "editar o index.html" ou "o
> cases.html", é `preview/index.html` e `preview/cases.html`.

## Arquivos e pastas

| Caminho | Pra que serve |
| --- | --- |
| `index.html` | Tela de "em breve" mostrada em `/`. Autossuficiente: HTML, CSS e um JS pequeno que monta a parede de cobogós ao fundo. |
| `cases.html` | Cópia idêntica do `index.html` (mostra "em breve" também em `/cases`). |
| `preview/index.html` | **A home completa.** Marcação, CSS e a classe `Component` (JS) num arquivo só, ~150 KB. Acessível em `/preview/`. |
| `preview/cases.html` | **A página de cases completa**, mesma estrutura. Acessível em `/preview/cases`. |
| `vendor/dc-runtime.js` | Runtime que lê o bloco `<script type="text/x-dc">` das páginas de `preview/` e renderiza a marcação (`<sc-if>`, `{{estado}}`, `onMouseEnter="{{...}}"`) com React. Não editar. |
| `assets/` | Imagens e SVGs: letras da logo, wordmark, cobogós (`cobogo-*.webp`), pets/stickers, sócios (`cecilia`, `wictor`), fotos dos cases, logos de clientes. Os HTMLs referenciam por caminho absoluto (`/assets/...`). |
| `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `icon-512.png` | Ícones, com o monograma stq colorido. |
| `og-image.png` | Imagem 1200×630 de compartilhamento (WhatsApp, LinkedIn etc.). URL absoluta nas tags `og:image`. |
| `CNAME` | Domínio do GitHub Pages: `sotaqueagencia.com.br`. Não apagar. |
| `.nojekyll` | Impede o GitHub Pages de processar os arquivos com Jekyll. |
| `README.md` | Texto antigo, da época do protótipo. Está desatualizado (cita `design/` e `index.html` como página completa). Vale reescrever ou apagar. |
| `PLANO.md` | Plano de evolução do site, por bloco de sessão. |
| `NOTAS.md` | Este arquivo. |

A pasta `design/` foi removida. Ela guardava os templates com placeholders
(`%%B_S%%`, `%%STYLES%%`…) e um `build.py` que dependia de caminhos do ambiente
da Claude (`/home/claude/...`), que não existem aqui. Os arquivos de `preview/`
já são o resultado final desse processo e passam a ser a fonte. Os templates
continuam no histórico do git (commit anterior a esta limpeza) se alguém
precisar.

## Dependências externas

- React 18.3.1 e ReactDOM, via cdnjs, carregados no `<head>` das páginas de `preview/`.
- Google Fonts: Anton, Archivo e Gochi Hand (a tela de "em breve" usa só Archivo e Gochi Hand).
- Os contornos das letras dos 7 estilos alternativos da logo (Bagel Fat One,
  Shrikhand, Rubik Mono One, Bungee, Ultra, Abril Fatface, Climate Crisis) estão
  embutidos como paths dentro de `stylesData()` no JS. Não é carregada fonte nenhuma pra isso.

Ou seja: `preview/*` **não** é 100% autossuficiente. Precisa de `vendor/dc-runtime.js`,
do React na CDN e do `assets/`. Só a raiz (em breve) é independente.

## Seções do `preview/index.html`, na ordem

Todas dentro de um `<div>` raiz controlado pelo `Component`; antes delas há o
`<header>` fixo (logo + botão de menu) e o `<nav>` do menu em tela cheia.

1. `#topo` (`.hero`, `data-sc="out"`) — wordmark grande da Sotaque. Ao rolar, ela
   encolhe e viaja até a logo do cabeçalho (o "morph").
2. `#voz` (`.pin`, `data-sc="pin"`) — "Toda marca tem uma voz. A gente faz ela soar."
   Seção fixada (sticky) de ~1950px de altura; a rolagem anima a frase.
3. `.bands` — faixas "Expressões de todo canto", com os sotaques por estado.
4. `.mani` (`data-sc="in"`) — Manifesto, linha a linha.
5. `#fazemos` (`.svcSec .stk`) — "O que fazemos": cartões de serviços.
6. `#cases` (`.cases .stk .over`, tema escuro) — Cases em destaque, com link
   "Ver todos os cases" para `/preview/cases`.
7. `#quem` (`.about`, `data-sc="par"`) — "Quem somos": Cecilia, Wictor e os
   quatro stickers dos bichos.
8. `.logos` — "Marcas que confiam", logos de clientes.
9. `#contato` (`.cta`, `data-sc="par"`) — cartão de contato.
10. `<footer class="foot">` — rodapé, com `nav.flinks`.

Além das seções há o loader de cobogós (`#boot`), descrito abaixo.

A página `preview/cases.html` tem a mesma estrutura de arquivo: topo escuro com
cobogós, lista de cases (cada um com âncora: `#aika`, `#casal-corretor`,
`#instituto-colinas`…) e rodapé.

## Como a classe `Component` anima com o scroll

Tudo está no bloco `<script type="text/x-dc">` no fim do HTML. `class Component
extends DCLogic` guarda o estado (menu, estilo da logo, loader…) e roda
`scrollFx()` a cada frame de scroll. A função **não anima nada diretamente**:
ela mede onde cada seção está na tela e escreve o resultado como variável de CSS
no elemento. Quem anima é o CSS, com `calc()`, `translate`, `opacity`, `rotate`
usando essas variáveis. Pra mudar um movimento, quase sempre se mexe só no CSS.

Cada seção declara o modo no atributo `data-sc`; `vh` é a altura da janela e `r`
o `getBoundingClientRect()` da seção:

| Variável | Modo `data-sc` | Faixa | O que significa |
| --- | --- | --- | --- |
| `--e` | `in` | 0 a 1 | Progresso de **entrada**. 0 quando a seção ainda não apareceu, 1 quando já subiu 75% da altura da janela: `clamp((vh - top) / (vh * .75))`. Alimenta o texto que revela por linha (`.mani`), os cartões e os cases. Dentro, `--lp`, `--ce` derivam de `--e` e de um índice `--i` por item, pra escalonar. |
| `--p` | `pin` | 0 a 1 | Progresso dentro de uma seção **fixada** (sticky): `-top / (altura - vh)`. É 0 ao chegar e 1 ao terminar a rolagem da seção `#voz`. |
| `--q` | `par` | -1.2 a 1.2 | **Paralaxe**: distância do centro da seção ao centro da janela, em alturas de janela. 0 quando a seção está centrada, negativo acima, positivo abaixo. Usado em `.about`, `.cta` (e declarado em `.cases`). |
| `--o` | `out` | 0 a 1 | Progresso de **saída** do hero: `-top / (altura * .85)`. Também escreve `--m`, `--ws`, `--wx`, `--wy` e `--hl` (o morph da wordmark até o cabeçalho) e liga/desliga o estado `scrolled`. |
| `--cv` | `data-stack` | 0 a 1 | **Cobertura**: quanto a seção seguinte já subiu por cima desta, `(vh - topDoPróximo) / vh`. Em `.stk`, a seção que está sendo coberta encolhe (`scale(1 - cv*.07)`), desce 50px, perde até 45% de opacidade e ganha um véu escuro de até 50% (`.stk::after`). |
| `--stick` | `data-stack` | px | Offset do `position: sticky` das seções empilhadas, `min(0, vh - altura da seção)`. Faz seções mais altas que a janela rolarem até o fim antes de ficarem coladas. |
| `--ho` | raiz | 0 ou 1 | Visibilidade da logo do cabeçalho (some enquanto a wordmark do hero ainda está na tela). |
| `--pagebg` | raiz | cor | Cor de fundo da página conforme a seção sob 55% da janela (`data-pbg`). |

Outros detalhes úteis:

- `data-theme` (`hero`, `light`, `dark`) em cada seção diz ao cabeçalho de que cor
  ficar quando passa por baixo dela (estado `hdr`).
- Quando `window.innerHeight > 1900` o código assume que está no canvas de design
  da Claude (`isCanvas`) e fixa as variáveis no estado final. No navegador normal
  isso nunca dispara.
- `.stk` (sticky) + `z-index` crescente + `--cv` é o que cria o efeito de pilha de
  "O que fazemos" para "Cases".
- Há também um timer de 3s (`startTimer`/`onStep`) que troca o sotaque/estado
  mostrado nas faixas e na logo, e pausa com o menu aberto.

### Loader

Duas implementações diferentes:

- `#boot` no começo do `<body>` das duas páginas de `preview/`: três cubos de
  cobogó que andam num quadrado 2×2 (animação CSS `bootMove`, 2,16s). Some
  quando a logo (`.stq`) já renderizou e passou um tempo mínimo.
- O estado `loading`/`ld` dentro do `Component` (porcentagem e saudação) é um
  segundo loader, controlado pelo JS. O `#boot` cobre o início, esse cobre o resto.

## Raiz × preview

Enquanto o site novo é desenvolvido, `/` e `/cases` mostram uma tela de "em
breve" (cubos de cobogó animados, wordmark e a frase "Tamo afinando o sotaque do
site novo"). O site completo vive em `/preview/` e `/preview/cases`, com
`<meta name="robots" content="noindex">` pra não ser indexado.

Os links internos de `preview/` já apontam pra `/preview/...`
(ex.: `/preview/cases`, `/preview/#contato`), e os `href` do `Component`
também. As duas páginas removem `index.html` e `.html` da barra de endereço com
`history.replaceState`.

**Quando for lançar:** copiar `preview/index.html` e `preview/cases.html` por cima
de `index.html` e `cases.html` da raiz, trocar os links `/preview/...` por `/...`,
tirar o `noindex`, ajustar o `og:url`/`<title>` e apagar `preview/`.

## Rodar local

Os caminhos são absolutos (`/assets/...`, `/vendor/...`), então o servidor tem que
servir a raiz do projeto como `/`:

```bash
cd ~/Projects/sotaque-site
python3 -m http.server 8080
```

- Tela de "em breve": http://localhost:8080/ (o servidor simples não resolve
  `/cases`; use http://localhost:8080/cases.html)
- Home completa: http://localhost:8080/preview/
- Cases completo: http://localhost:8080/preview/cases.html

Abrir o HTML direto do Finder não funciona (caminhos absolutos e `fetch`). Sem
internet o React da CDN não carrega e `preview/` fica em branco.

Os links `/preview/cases` (sem `.html`) só resolvem no GitHub Pages, que aceita URL
limpa. No servidor local, essa navegação dá 404; ajuste manual na barra de endereço
ou use outro servidor com suporte a URL limpa (ex.: `npx serve`).

## Publicar

O GitHub Pages serve a branch `main` direto. Não há build nem CI.

```bash
git add -A
git commit -m "mensagem"
git push
```

Em um ou dois minutos a mudança está em sotaqueagencia.com.br. O `CNAME` precisa
continuar na raiz, senão o domínio é desvinculado.
