#!/usr/bin/env python3
"""Review-grade Markdown -> standalone HTML for worksheets.

NOT the production renderer (that's the bundler pipeline that makes worksheets/html/*.html).
This produces a clean, readable, Compound-styled standalone page so a worksheet .md can be
eyeballed visually. Self-contained (CSS inlined; web fonts via Google Fonts CDN).

Styling is codified in ONE place: worksheets/worksheet.css. This script inlines it into
each output so the HTML stays self-contained for printing/sharing. Edit the CSS there.

Convention: a table whose body cells are ALL blank is treated as a fillable grid — it gets
class="fill" (tall, writable rows) and, together with its section heading, is lifted onto
its own page (`.fill-page`). Put such a table as the LAST element of its section.

Usage:
  /usr/bin/python3 .claude/tools/render_worksheet.py worksheets/<slug>.md
    -> writes worksheets/review-html/<slug>.html
"""
import re, sys, html as _h
from pathlib import Path

def inline(s):
    s = _h.escape(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', s)
    s = re.sub(r'`(.+?)`', r'<code>\1</code>', s)
    return s

def render(md):
    lines = md.split("\n"); out=[]; i=0; n=len(lines)
    last_section_idx = [0]  # index in `out` of the most recent heading (section start)

    def flush_table(rows):
        if not rows: return
        # Parse cells per row, dropping the |---| separator row.
        parsed=[]
        for r,row in enumerate(rows):
            cells=[c.strip() for c in row.strip().strip("|").split("|")]
            if r==1 and all(set(c)<=set("-: ") for c in cells): continue
            parsed.append(cells)
        if not parsed: return
        header, data = parsed[0], parsed[1:]
        is_fill = bool(data) and all(c=="" for row in data for c in row)
        cls = ' class="fill"' if is_fill else ''
        tbl=[f"<table{cls}>"]
        if is_fill:
            # Fixed layout; weight the first column 2x (it holds the long descriptive field).
            ncol=len(header); total=ncol+1
            widths=[(2 if k==0 else 1)/total*100 for k in range(ncol)]
            tbl.append("<colgroup>"+"".join(f'<col style="width:{w:.4g}%">' for w in widths)+"</colgroup>")
        for r,cells in enumerate(parsed):  # parsed[0]=header; separator already dropped
            tag="th" if r==0 else "td"
            tbl.append("<tr>"+"".join(f"<{tag}>{inline(c)}</{tag}>" for c in cells)+"</tr>")
        tbl.append("</table>")
        if is_fill:
            # Lift section heading + intro + this table onto their own page.
            out.insert(last_section_idx[0], '<section class="fill-page">')
            out.extend(tbl)
            out.append("</section>")
        else:
            out.extend(tbl)

    while i<n:
        ln=lines[i]
        if re.match(r'^\s*\|.*\|\s*$', ln):
            rows=[]
            while i<n and re.match(r'^\s*\|.*\|\s*$', lines[i]): rows.append(lines[i]); i+=1
            flush_table(rows); continue
        m=re.match(r'^(#{1,4})\s+(.*)', ln)
        if m:
            lvl=len(m.group(1)); last_section_idx[0]=len(out)
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>"); i+=1; continue
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
    css=(p.parent/"worksheet.css").read_text(encoding="utf-8")
    doc=f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{_h.escape(title)} — Compound (review render)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600&family=Bricolage+Grotesque:wght@500;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>{css}</style></head><body>
<div class="banner">Review render (not production styling). Source of truth: {_h.escape(p.name)}</div>
{body}
</body></html>"""
    outdir=p.parent/"review-html"; outdir.mkdir(exist_ok=True)
    outp=outdir/(p.stem+".html"); outp.write_text(doc, encoding="utf-8")
    print(f"wrote {outp}")

if __name__=="__main__": main()
