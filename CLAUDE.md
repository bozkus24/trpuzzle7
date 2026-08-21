# Arala — guide for Claude

Turkish daily word puzzle (Betweenle-style): find the hidden 5-letter word, narrowed alphabetically between an upper and a lower bound. The whole game is one self-contained `index.html` (vanilla JS/CSS, no framework, no build step). It is previewed/shipped as a claude.ai Artifact.

## Files — edit here, don't scan the repo
- `index.html` — the ENTIRE game (HTML+CSS+JS). Almost every edit goes here. Section markers: `<!--AR-HEAD-START-->`, `<!--AR-BODY-START-->`, `<!--EMBED-->`, `<!--AR-BODY-END-->`.
- `cevaplar.txt` — answers/secrets (~2788 five-letter words). Plain word list — **don't read it**.
- `kelimehavuzu.txt` — full accepted-guess pool (~5585 words). Plain word list — **don't read it**.
- `build_preview.py` — builds the Artifact preview. `logo.png`, `README.md` — asset/docs.

## Word model
`WORDS = cevaplar ∪ kelimehavuzu` (sorted, ~5586); `ANSWERS = cevaplar`. The secret comes from ANSWERS, positioned in WORDS. Served build `fetch`es `cevaplar.txt` (answers) + `kelimehavuzu.txt` (pool). The Artifact embeds the same data at `<!--EMBED-->` as `window.EMBEDDED_WORDS` (answers) + `window.EMBEDDED_ACCEPT` (pool).

## Run / preview / test
- Real use (the game fetches the txt files): `python3 -m http.server 8123 --directory .` then open `/index.html?debug=1`. Opening `index.html` via `file://` fails (fetch is blocked).
- Artifact preview: `python3 build_preview.py <scratch>/aradle-onizleme.html` → a self-contained file (words embedded, works via `file://`). Publish THAT file as the Artifact (favicon ↕️; re-publishing the same path keeps the URL). Don't commit the generated file.
- Headless test/screenshot: `playwright-core` + chromium at `/opt/pw-browsers/chromium`, launch args `['--no-sandbox']`.
- Debug API (`?debug=1`): `window.__aradle` → `.state()` (N, answers, secret, secretIdx, lo, hi, done, mode, words, inAnswers…), `.guess(w)` (instant, skips animation), `.archive(day)`, `.daily()`, `.openArchive()`. Type by clicking `.key[data-k="<lowercase-letter|ENTER|BACK>"]` (physical keys drop Turkish characters).

## Git workflow — IMPORTANT
- Dev branch: `claude/betweenle-site-preview-wwj7e2`. Commit + push after every change; **origin is the source of truth**.
- This environment often resets the working tree to an old commit mid-session. If `git log` looks stale (missing recent work), recover before doing anything: `git fetch origin <branch> && git reset --hard origin/<branch>`.
- Merge to main only when asked: `git checkout -B main origin/main && git merge --no-ff -X theirs origin/<branch>`, verify `git diff origin/<branch>` is empty, push `main`, then check out the dev branch again.

## Conventions
- Turkish casing: CSS `text-transform:uppercase` needs `lang="tr"` on the element (the artifact wrapper has no `<html lang>`); in JS use Turkish-locale casing; compare in tests with `toLocaleLowerCase('tr')`.
- Theming = three-state tokens: `:root` (light) · `@media (prefers-color-scheme:dark){:root:not([data-theme="light"])}` · `:root[data-theme="dark"]`.
- Colors: `--tile` blue = guessed bounds, `--ok` green = answer, `#ffb38a` peach = tiles while typing (sweeps to `--tile` on submit).
- localStorage keys start with `aradle_`. Puzzle number: `EPOCH=2026-01-01`, launch 1 Aug 2026 = #1, `puzzleNo(day)=day-LAUNCH+1`.
