# Handoff — Arala (2026-08-21)

Read `CLAUDE.md` first (project map, build, workflow, conventions). This file is the current-state snapshot.

## State
- Dev branch `claude/betweenle-site-preview-wwj7e2` @ `bf34894`. **Origin is the source of truth** (the container reset the working tree several times this session).
- Live Artifact preview: https://claude.ai/code/artifact/42cc01b9-5aed-4688-901b-d41a10863a70
- `main` @ `49122a0` — advanced by a **separate** AdSense-prep PR (#2, branch `claude/adsense-hazirlik`), NOT this session. See Known issues.

## Completed this session
- **Stats:** daily result on top + general stats below + wide "Paylaş" button. Stats button always shows the DAILY result even while browsing an archive day. Added PUAN DAĞILIMI (0–5) bars with gold stars (achieved band green).
- **Archive:** solved/half-finished days reopen in their saved state; "Devam ediyor" label for in-progress days; days finished before state-saving get answer+score reconstructed from the result code. Numbers start at #1 (1 Aug 2026).
- **Typing:** tiles are peach `#ffb38a` (removed on request, then RESTORED on request → peach is current); single faint dot on the next slot; on submit they sweep left→right to `--tile` blue, then slide to the boundary.
- **Alphabet hint:** writable = prominent (belirgin), non-writable = faded (soluk). (A light/dark variant was tried and reverted.)
- **Layout/UI:** alphabet centered with equal board↔keyboard gaps; keyboard keys enlarged (taller, rounded); modal titles centered with X at top-right; help title "Nasıl Oynanır" (no "?"); how-to example tiles match the game (blue bounds, green answer, angular).
- **Logo:** "ARALA" A/R/L/A blue (`--tile`), middle A green (`--ok`); logo icon + wordmark enlarged/proportioned.
- **Word pool replaced:** `cevaplar.txt` (2788 answers) + `kelimehavuzu.txt` (5585 pool); WORDS=5586. `loadWords` fetches these (was `kelimehavuzu.txt`+`kabul.txt`).
- Added `CLAUDE.md`, `build_preview.py`, `.gitignore`. Merged dev→main twice earlier (before the AdSense PR landed).

## Key decisions
- Peach typing fill is the intended current behavior (user confirmed restore).
- Alphabet uses prominent/faded, not keyboard-green.
- Secrets from `cevaplar.txt`, guesses from `kelimehavuzu.txt`; the union guarantees every answer is guessable.
- Panel button order (Arşiv · İstatistikler · Nasıl Oynanır · Ayarlar) was verified already correct — no change made.

## Files
`index.html` (whole game) · `cevaplar.txt`/`kelimehavuzu.txt` (word data — don't read) · `build_preview.py` · `CLAUDE.md` · `logo.png`.

## Unfinished / next steps
- Nothing user-requested is pending. If the live preview looks stale, rebuild + republish: `python3 build_preview.py <scratch>/aradle-onizleme.html`, publish that file to the same Artifact URL. (The last publish hit a cross-session conflict.)

## Known issues
- **Merging dev→main needs care.** main includes the AdSense-prep PR (#2) and is missing this session's last 4 dev commits (centered headers, logo enlarge, peach restore, CLAUDE.md). Do NOT blindly `git merge -X theirs` when merging dev→main — review the diff first so the AdSense-branch changes aren't discarded; reconcile deliberately.
- **Environment resets:** the container repeatedly reverted the working tree to an old commit (`ec00fe7`) and wiped the scratchpad (build/test files, screenshots) mid-session. Recover with `git fetch && git reset --hard origin/<branch>` before working.
- One answer ("akbil") is in `cevaplar.txt` but not `kelimehavuzu.txt`; the union makes it guessable (hence WORDS=5586). Remove from answers or add to the pool for a clean subset.
- Playwright's physical keyboard drops Turkish characters — type via on-screen key clicks `.key[data-k="…"]`.
