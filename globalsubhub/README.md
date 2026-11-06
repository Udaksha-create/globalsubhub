# GlobalSubHub starter

Static Cloudflare Pages movie discovery catalog with a scheduled GitHub Actions updater.

## Before enabling TMDB updates
Obtain permission for your intended commercial, advertising-supported TMDB usage, including metadata and any images. The workflow deliberately does not run until repository variable `TMDB_COMMERCIAL_RIGHTS_CONFIRMED` is set to `true` after authorization. Store `TMDB_API_KEY` in GitHub Actions repository Secrets, never in public files.

## Setup
1. Create a GitHub repository and upload these files, preserving `.github/workflows/discover.yml`.
2. In GitHub Settings → Secrets and variables → Actions, add secret `TMDB_API_KEY`.
3. Once you have appropriate rights, add repository variable `TMDB_COMMERCIAL_RIGHTS_CONFIRMED` = `true`.
4. Go to Actions → Daily movie discovery → Run workflow to test.
5. In Cloudflare Workers & Pages, create a Pages project connected to your GitHub repository. Use no build command, and output directory `/` (repository root). GitHub commits will trigger redeployment.
6. A scheduled run occurs daily at 01:15 UTC (10:15 JST), subject to GitHub scheduling delays.

## Important limitations
TMDB discover's `primary_release_date` is not a complete country-by-country theatrical release calendar. Release status here is based on the primary release date, not each local territory. The script retrieves up to 10 pages daily, which may miss some worldwide titles. For production, add regional release-date detail queries, pagination and quota handling, licensing checks, and a database as needed.

## Subtitles
No copyrighted subtitle files are bundled. Only publish files with redistribution permission and documented licenses. Before launch, add operator contact information, a functional takedown process, privacy policy, and proper notices.
