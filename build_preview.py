#!/usr/bin/env python3
"""Build the self-contained Artifact preview from index.html + word lists.

Usage: python3 build_preview.py [out.html]   (default: ./aradle-onizleme.html)

Embeds cevaplar.txt (answers -> window.EMBEDDED_WORDS) and kelimehavuzu.txt
(pool -> window.EMBEDDED_ACCEPT) at the <!--EMBED--> marker, and drops the
<html>/<head>/<body> wrapper the Artifact host supplies. Publish the output
file as the Artifact. Don't commit the output.
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "aradle-onizleme.html")


def words(name):
    text = open(os.path.join(ROOT, name), encoding="utf-8").read()
    return [w.strip() for w in text.split() if len(w.strip()) == 5]


answers, pool = words("cevaplar.txt"), words("kelimehavuzu.txt")
assert not any('"' in w or "\\" in w for w in answers + pool), "unexpected char in word"
embed = ('<script>window.EMBEDDED_WORDS="' + " ".join(answers)
         + '";window.EMBEDDED_ACCEPT="' + " ".join(pool) + '";</script>')

src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
start = src.index("<!--AR-HEAD-START-->") + len("<!--AR-HEAD-START-->")
body = src[start:src.index("<!--AR-BODY-END-->")]
for token in ("</head>", "<body>", "<!--AR-BODY-START-->"):
    body = body.replace(token, "")
assert "<!--EMBED-->" in body, "EMBED marker missing"
body = body.replace("<!--EMBED-->", embed).strip() + "\n"

open(OUT, "w", encoding="utf-8").write(body)
print(f"built {OUT}: {len(body)} bytes | answers {len(answers)} | pool {len(pool)}"
      f" | WORDS {len(set(answers) | set(pool))}")
