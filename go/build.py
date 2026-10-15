#!/usr/bin/env python3
"""Generate petfuel.app/go/<slug>/ redirect pages from go/links.json.

Each slug becomes a tiny page that forwards to the App Store with Apple's
campaign parameters (pt/ct) and, when set, a Custom Product Page id (ppid).
Installs then show up per campaign / per product page inside App Store
Connect > App Analytics, so a slug handed to one creator is traceable to them.
"""
import json, os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
cfg = json.load(open(os.path.join(HERE, "links.json")))
app_id, pt = cfg["app_id"], cfg.get("pt", "").strip()

def target(link):
    ppid = link.get("ppid", "").strip()
    params = []
    if pt:
        params += [f"pt={pt}", f"ct={link['ct']}", "mt=8"]
    if ppid:
        params.append(f"ppid={ppid}")
    base = f"https://apps.apple.com/app/apple-store/id{app_id}" if pt else f"https://apps.apple.com/app/id{app_id}"
    return base + ("?" + "&".join(params) if params else "")

PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>PetFuel on the App Store</title>
<meta http-equiv="refresh" content="0;url={url}">
<style>body{{font-family:-apple-system,system-ui,sans-serif;display:flex;min-height:100vh;align-items:center;justify-content:center;margin:0;background:#fff;color:#1a1a1a}}a{{color:#0E7C72}}</style>
</head><body><p>Taking you to PetFuel on the App Store… <a href="{url}">Tap here if nothing happens.</a></p>
<script>location.replace({url_js});</script></body></html>
"""

# Wipe generated folders (anything in go/ that is a directory) and rebuild.
for name in os.listdir(HERE):
    p = os.path.join(HERE, name)
    if os.path.isdir(p):
        shutil.rmtree(p)

for slug, link in cfg["links"].items():
    url = target(link)
    d = os.path.join(HERE, slug)
    os.makedirs(d)
    with open(os.path.join(d, "index.html"), "w") as f:
        f.write(PAGE.format(url=url, url_js=json.dumps(url)))
    print(f"/go/{slug:<12} -> {url}")

# Bare /go/ falls back to the plain store page.
with open(os.path.join(HERE, "index.html"), "w") as f:
    url = f"https://apps.apple.com/app/id{app_id}"
    f.write(PAGE.format(url=url, url_js=json.dumps(url)))
if not pt:
    print("\nNOTE: pt is empty in links.json, so links are NOT campaign-tracked yet.", file=sys.stderr)
