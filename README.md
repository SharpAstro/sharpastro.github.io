# sharpastro.github.io

The SharpAstro organisation site, served at <https://sharpastro.github.io/>.

A hand-authored static page: one `index.html`, one stylesheet, self-hosted fonts and a handful of
screenshots. No build step and no framework, so a change is an edit and a push.

## Why this repository exists at all

GitHub serves an organisation's root site **only** from a repository named exactly
`<org>.github.io`. Enabling Pages on the org's `.github` repository publishes it at
`https://sharpastro.github.io/.github/`, which is the same class of URL as a project site and does
not answer the root. Hence this repo.

It coexists with the project sites rather than competing with them: this repo owns `/`, and
`SharpAstro/tianwen` continues to own `/tianwen/` (the live in-browser planner and sky atlas). The
only way they could collide is if this repo ever grew a `tianwen/` directory.

## Content

The library catalogue is seeded from `profile/README.md` in the `SharpAstro/.github` repository,
which is what renders on the organisation's GitHub profile. The two are **maintained separately** by
deliberate choice, so this page can say things the profile README should not. When a library is
added or renamed, update both.

Two repositories currently on the site are missing from that profile README: `WebGl.Renderer` and
`LAN.Lib`.

## Screenshots

Captured from a DEBUG build of `tianwen-gui` driven against its simulated devices, so the whole run
is reproducible and no real hardware or personal data appears. Stored as WebP (the same set as PNG
was 3.9 MB against 0.68 MB).

`assets/img/og-cover.jpg` is deliberately a JPEG and a different crop: social scrapers are the one
consumer whose WebP support is still uneven, and they want a 1200x630 card.

## After replacing any screenshot

    python tools/stamp-image-dims.py

Every `<img>` is `loading="lazy"`, and a lazy image with no declared size is a zero-height box until
it loads -- which silently collapsed a figure to its 1px border. The script stamps each tag with its
file's real dimensions so the browser reserves the right box up front. Hand-written numbers go stale
without anyone noticing, which is exactly what had already happened.

## Local preview

    python -m http.server 5177

Then open <http://127.0.0.1:5177/>. Serve it over HTTP rather than opening the file directly: under
`file://` the browser blocks the self-hosted fonts as a cross-origin request and the page renders in
fallback faces.
