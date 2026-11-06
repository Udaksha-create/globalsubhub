# GlobalSubHub starter

A static, mobile-friendly starter site with a working client-side SRT timing adjustment tool. No backend, paid API, or tracking required.

## Deploy on Cloudflare Pages
1. Unzip the archive.
2. Open Cloudflare Dashboard > Workers & Pages > Create > Pages > Upload assets.
3. Upload the extracted folder (containing `index.html`).
4. Visit the generated `*.pages.dev` URL.

You can also commit `index.html` to a GitHub repository and connect that repository to Cloudflare Pages. For a static site, no build command is necessary; the output directory is the repository root.

## Included
- Responsive home page
- Five-language selector (UI preference only; no translations yet)
- Working SRT offset tool entirely in browser
- Clearly labeled placeholders for licensed movie metadata, authorized subtitle catalog, and future local Whisper tool

## Next phases
- Verify TMDB licensing for commercial use before enabling metadata ingestion.
- Implement a curated licensed subtitle catalog.
- Build local Windows Whisper transcription and review workflow.
- Add multilingual UI translations and release matching.

Only process media you have the right to use and only publish subtitles you have permission to redistribute.
