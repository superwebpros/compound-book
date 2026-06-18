#!/usr/bin/env python3
"""Review-grade Markdown -> standalone HTML for worksheets.

NOT the production renderer (that's the bundler pipeline that makes worksheets/html/*.html).
This produces a clean, readable, Compound-styled standalone page so a worksheet .md can be
eyeballed visually. Self-contained (no deps); web fonts via Google Fonts CDN.

Usage:
  /usr/bin/python3 .claude/tools/render_worksheet.py worksheets/<slug>.md
    -> writes worksheets/review-html/<slug>.html
"""
import re, sys, html as _h
from pathlib import Path

CSS = """
:root{--paper:#FAFAF8;--ink:#0A0A0A;--red:#E11D2D;--muted:#6b6b66;--line:#e4e4df;--card:#fff;}
*{box-sizing:border-box}
body{background:var(--paper);color:var(--ink);font-family:'Archivo',system-ui,sans-serif;
  line-height:1.55;max-width:780px;margin:0 auto;padding:48px 28px 96px;font-size:17px}
h1{font-family:'Bricolage Grotesque','Archivo',sans-serif;font-size:2rem;line-height:1.15;margin:.2em 0 .1em}
h2{font-family:'Bricolage Grotesque','Archivo',sans-serif;font-size:1.3rem;margin:2.2em 0 .4em;
  padding-top:1.1em;border-top:1px solid var(--line)}
h3{font-size:1.05rem;margin:1.4em 0 .3em}
.kicker{font:600 .72rem/'1' 'JetBrains Mono',monospace;letter-spacing:.12em;text-transform:uppercase;
  color:var(--red);margin-bottom:14px}
.sub{color:var(--muted);font-size:1.05rem;margin-top:0}
ol,ul{padding-left:1.3em}li{margin:.3em 0}
strong{font-weight:600}
blockquote{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--red);
  border-radius:6px;padding:12px 16px;margin:1em 0;color:#333;font-size:.96rem}
table{border-collapse:collapse;width:100%;margin:1em 0;font-size:.9rem}
th,td{border:1px solid var(--line);padding:7px 10px;text-align:left;vertical-align:top}
th{background:#f1f1ec;font-weight:600}
hr{border:0;border-top:1px solid var(--line);margin:2em 0}
code{font-family:'JetBrains Mono',monospace;font-size:.85em;background:#f1f1ec;padding:1px 5px;border-radius:4px}
.banner{background:#fff6e9;border:1px solid #f0d9a8;border-radius:6px;padding:8px 12px;font-size:.8rem;color:#8a6d3b;margin-bottom:24px}
"""

def inline(s):
    s = _h.escape(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', s)
    s = re.sub(r'`(.+?)`', r'<code>\1</code>', s)
    return s

def render(md):
    lines = md.split("\n"); out=[]; i=0; n=len(lines)
    def flush_table(rows):
        if not rows: return
        out.append("<table>")
        for r,row in enumerate(rows):
            cells=[c.strip() for c in row.strip().strip("|").split("|")]
            if r==1 and all(set(c)<=set("-: ") for c in cells): continue
            tag="th" if r==0 else "td"
            out.append("<tr>"+"".join(f"<{tag}>{inline(c)}</{tag}>" for c in cells)+"</tr>")
        out.append("</table>")
    while i<n:
        ln=lines[i]
        if re.match(r'^\s*\|.*\|\s*$', ln):
            rows=[]
            while i<n and re.match(r'^\s*\|.*\|\s*$', lines[i]): rows.append(lines[i]); i+=1
            flush_table(rows); continue
        m=re.match(r'^(#{1,4})\s+(.*)', ln)
        if m:
            lvl=len(m.group(1)); out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>"); i+=1; continue
        if re.match(r'^\s*>\s?', ln):
            buf=[]
            while i<n and re.match(r'^\s*>\s?', lines[i]): buf.append(re.sub(r'^\s*>\s?','',lines[i])); i+=1
            out.append("<blockquote>"+inline(" ".join(buf))+"</blockquote>"); continue
        if re.match(r'^\s*\d+\.\s', ln):
            buf=[]
            while i<n and re.match(r'^\s*\d+\.\s', lines[i]): buf.append(re.sub(r'^\s*\d+\.\s','',lines[i])); i+=1
            out.append("<ol>"+"".join(f"<li>{inline(x)}</li>" for x in buf)+"</ol>"); continue
        if re.match(r'^\s*[-*]\s', ln):
            buf=[]
            while i<n and re.match(r'^\s*[-*]\s', lines[i]): buf.append(re.sub(r'^\s*[-*]\s','',lines[i])); i+=1
            out.append("<ul>"+"".join(f"<li>{inline(x)}</li>" for x in buf)+"</ul>"); continue
        if re.match(r'^\s*---+\s*$', ln): out.append("<hr>"); i+=1; continue
        if ln.strip()=="" : i+=1; continue
        buf=[ln]
        while i+1<n and lines[i+1].strip() and not re.match(r'^\s*(#{1,4}\s|>|\d+\.\s|[-*]\s|\||---+\s*$)', lines[i+1]):
            i+=1; buf.append(lines[i])
        out.append("<p>"+inline(" ".join(buf))+"</p>"); i+=1
    return "\n".join(out)

def main():
    p=Path(sys.argv[1]); md=p.read_text(encoding="utf-8")
    title=(re.search(r'^#\s+(.*)', md, re.M) or [None,p.stem])[1]
    body=render(md)
    doc=f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{_h.escape(title)} — Compound (review render)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600&family=Bricolage+Grotesque:wght@500;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="banner">Review render (not production styling). Source of truth: {_h.escape(p.name)}</div>
{body}
</body></html>"""
    outdir=p.parent/"review-html"; outdir.mkdir(exist_ok=True)
    outp=outdir/(p.stem+".html"); outp.write_text(doc, encoding="utf-8")
    print(f"wrote {outp}")

if __name__=="__main__": main()
