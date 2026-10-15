# PetFuel — marketing site (petfuel.app)

The public landing page and privacy policy for **PetFuel**, an AI nutrition
tracker for pets. A single-folder static site — no build step.

- `index.html` — landing page (hero, problem, how-it-works, FAQ, App Store download)
- `privacy.html` — privacy policy (linked from the App Store listing)
- `CNAME` — pins the GitHub Pages site to **petfuel.app**

## Deploy

Pushing to `main` publishes via GitHub Pages. The `CNAME` file points the site
at petfuel.app; set the apex domain's DNS to GitHub Pages' four `A` records at
your registrar.

A Scarabyte product.

## Creator / campaign links (`go/`)

`petfuel.app/go/<slug>` forwards to the App Store with Apple campaign
parameters, so installs are traceable per creator or brief in App Store
Connect → App Analytics. `go/links.json` is the source of truth; after editing
it run `python3 go/build.py` and push `main`. Set `pt` (the provider token from
App Analytics → Acquisition → Campaigns → Generate Campaign Link) once, and a
Custom Product Page id in `ppid` per slug when that page exists.
