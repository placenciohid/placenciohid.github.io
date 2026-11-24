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

## Credits

Design: [Forty by HTML5 UP](https://html5up.net/forty), Jekyll port by [Andrew Banchich](https://github.com/andrewbanchich/forty-jekyll-theme). Retain attribution and the original license files. No new license is asserted for third-party content.
