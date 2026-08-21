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

Both currently list the same 19 repositories; the site adds the Store link and the screenshots on
top of that.

## The Microsoft Store link

**Astro Photo Viewer** (store id `9PMDZP16TGBG`) is `tianwen-fits` packaged as MSIX -- see
`packaging/windows/msix/README.md` in `SharpAstro/tianwen` for how that package is built and why it
ships through the Store at all.

It is deliberately **not** a section of its own. A standalone "Install" band read as a page about one
product suddenly talking about a different one, with the suite's capabilities resuming underneath it.
So the viewer is the seventh use case (`#viewer`, "Look at what came back") -- last, because looking
at the frames is what happens after the night -- and the hero names it beside the browser demo, so
both applications are visible before any scrolling. Nothing about it needs styles of its own: it uses
`.usecase`, `.cta-row` and `.detail` like every neighbour.

It is a plain `<a>` in a `.cta-row`, **not** Microsoft's `<ms-store-badge>` web component, which was
tried and removed. The component pulls a module, a badge SVG and a hidden iframe from
`get.microsoft.com`; that would be the only third-party request the published page makes, when the
fonts are self-hosted for precisely that reason. It also renders *nothing* when the module is blocked,
being a custom element -- so it needs a fallback link anyway, and the fallback alone is the whole
feature. Two of its own quirks are worth recording in case it ever comes back:

- Its `theme` attribute names the **artwork, not the page**: `theme="dark"` is the dark-on-pale badge,
  which belongs on a *light* background. `theme="auto"` follows the OS preference only, so it would
  disagree with this site's theme toggle and has to be set by hand, inverted.
- `animation` cannot be changed after the element upgrades: it appends a stylesheet per change and
  never removes the previous one, so the hover transform survives being switched off. Honouring
  `prefers-reduced-motion` means setting the attribute before its module runs.

The Store link deliberately carries no `hl`/`gl` query, so the Store localises for whoever opens it, and no
version number, which would go stale on every submission.

## Screenshots

Captured from a DEBUG build of `tianwen-gui` driven against its simulated devices, so the whole run
is reproducible and no real hardware or personal data appears. Stored as WebP (the same set as PNG
was 3.9 MB against 0.68 MB).

`assets/img/viewer.webp` is the one exception to all of that: it is `tianwen-fits` on a real OIII/HOO
stack of the Sagittarius triplet, and it is **the same screenshot the Store listing carries**, so the
two shopfronts show the same thing. Downscaled from the 2880x1848 capture to 1800px wide at quality
86, which is the width every other application shot here uses.

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
