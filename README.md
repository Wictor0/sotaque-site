# Sotaque — site

Landing page da Agência Sotaque. Esta versão é o **protótipo navegável** que saiu do canvas de design: já tem todas as animações, o morph da logo, as seções empilhadas e o layout responsivo (desktop, tablet e celular).

## Rodar localmente

A página precisa ser servida por HTTP (abrir o `index.html` direto do Finder não funciona):

```bash
cd sotaque-site
python3 -m http.server 8080
# abra http://localhost:8080
```

## Estrutura

```
index.html            página completa (marcação, estilos e lógica)
assets/               imagens: letras, pets, cobogós, sócios, fitas, megafone…
vendor/dc-runtime.js  runtime do protótipo (renderiza o <x-dc> da página)
design/               fonte usada para gerar o index.html
  Main.src.html       template com placeholders (%%B_S%%, %%STYLES%%…)
  brand.json          contornos da logo oficial e do monograma stq
  styles.json         contornos das letras nos 7 estilos alternativos
  build.py            script que injeta os contornos no template
```

React 18.3.1 é carregado do cdnjs.

## O que ainda falta

- Número do WhatsApp nos links `wa.me/55XXXXXXXXXXX`
- Imagens reais dos cases (hoje marcadas como `[imagem do case]`)
- Links de Instagram, Behance e LinkedIn
- Confirmar e-mail de contato (`contato@sotaqueagencia.com`)

## Próximo passo

Reconstruir como projeto de produção (sem o runtime do protótipo), usando este repositório como referência visual e de comportamento.

Fontes: Anton, Archivo e Gochi Hand (Google Fonts). Os estilos alternativos da logo usam contornos de Bagel Fat One, Shrikhand, Rubik Mono One, Bungee, Ultra, Abril Fatface e Climate Crisis (todas com licença livre no Google Fonts).
