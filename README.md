# Darío Placencio — portfolio website

**Live:** https://placenciohid.github.io/  
**Code showcase:** https://github.com/placenciohid/Resume

Professional experience in operational excellence, data science, and automation, plus selected technical projects. This is a GitHub Pages site using Jekyll and the Forty theme; the original article URLs are preserved.

## Develop

Use Ruby 3.1 and Bundler. Run `bundle install`, then `bundle exec jekyll serve --baseurl ""`. To validate the production output, run `bundle exec jekyll build --baseurl ""` followed by `python scripts/check_site.py` (Python 3.10+).

## Update content

- Homepage selections: `_data/featured.yml`.
- Experience: `_includes/bio.md` (shared by About and Resume).
- Professional summaries: `work/`; runnable project introductions: `projects/`.
- Original articles: `_posts/`. Retain filenames and dates to preserve URLs.
- Contact and social links: `_config.yml`. Site is hosted at the root, so `baseurl` is empty.

`jekyll.yml` builds pull requests and pushes, checks internal links, and publishes only pushes to `master`. No deployment credentials are needed for pull-request builds. Merge the companion showcase changes before publishing updated code links. Roll back through a normal revert commit if needed.

Professional summaries exclude employer datasets, code, and internal screenshots. Technical examples and limitations are documented in the code repository.

## Professional presentation and figures

The homepage leads with professional case studies, followed by technical implementations and publications. Full technical walkthroughs remain in accessible, expandable sections on the professional case-study pages. Every project retains a direct link to its evidence in the Resume repository.

The production-error graphic represents the author-supplied 21% improvement as an index: prior baseline 100, forecast model 79. It does not invent a raw production series. The document-search graphic shows collection scale and four adopting teams, not user counts or financial value. The backtest chart inside the technical walkthrough is explicitly synthetic and is calculated from the saved companion results. SVG source is editable under `assets/images/topics/`.

## Credits

Design: [Forty by HTML5 UP](https://html5up.net/forty), Jekyll port by [Andrew Banchich](https://github.com/andrewbanchich/forty-jekyll-theme). Retain attribution and the original license files. No new license is asserted for third-party content.
