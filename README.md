# PetFuel — marketing site (petfuel.app)

The public landing page and privacy policy for **PetFuel**, an AI nutrition
tracker for pets. A single-folder static site — no build step.

- `index.html` — landing page (hero, problem, how-it-works, honest-data, waitlist)
- `privacy.html` — privacy policy (linked from the App Store listing)
- `CNAME` — pins the GitHub Pages site to **petfuel.app**

## Deploy

Pushing to `main` publishes via GitHub Pages. The `CNAME` file points the site
at petfuel.app; set the apex domain's DNS to GitHub Pages' four `A` records at
your registrar.

A Scarabyte product.
