# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [unreleased] - YYYY-MM-DD

- Adjust test matrix to use Wagtail 5.2 [@nickmoreton](https://github.com/nickmoreton)
- Drop wagtail 5.0 from the test matrix [@nickmoreton](https://github.com/nickmoreton)
- Update tox.ini envlist to consider that Django 3.2 does not support Python 3.11 [@katdom13](https://github.com/katdom13)
- Update minimum Wagtail version to 4.1 in setup.py [@katdom13](https://github.com/katdom13)
- Add USE_TZ to avoid removal warnings from Django [@katdom13](https://github.com/katdom13)
- Adapt tox-gh-actions [@katdom13](https://github.com/katdom13)
- Run updatemodulepaths [@katdom13](https://github.com/katdom13)
- Update gitignore [@katdom13](https://github.com/katdom13)
- Add GitHub Actions [@engineervix](https://github.com/engineervix)
- Add staticfiles/ to .gitignore [@engineervix](https://github.com/engineervix)
- Add test suite [@engineervix](https://github.com/engineervix)
- Update setup.py to include testing deps [@engineervix](https://github.com/engineervix)
- Add testing dependencies [@engineervix](https://github.com/engineervix)
- Add tox configuration [@engineervix](https://github.com/engineervix)

## [1.0.0] - 2023-12-19

**New maintainers!** This release is identical to 0.2.1, but is the first release to follow semantic versioning, and is the first release by the new maintainers.

## [0.2.1] - 2020-02-04

- Support Django 3 [@tomdyson](https://github.com/tomdyson)

## [0.2.0] - 2020-01-07

- Upgrade to latest tota11y ([#9](https://github.com/wagtail-nest/wagtail-accessibility/issues/9)) [@seb-b](https://github.com/seb-b)
- Fixes [#3](https://github.com/wagtail-nest/wagtail-accessibility/issues/3) Added override kwarg to use tota11y outside of preview mode ([#5](https://github.com/wagtail-nest/wagtail-accessibility/pull/5)) [@seb-b](https://github.com/seb-b)
- Fixes [#4](https://github.com/wagtail-nest/wagtail-accessibility/issues/4) use getattr to check for is_preview ([#5](https://github.com/wagtail-nest/wagtail-accessibility/pull/5)) [@seb-b](https://github.com/seb-b)

## [0.1.1] - 2016-09-20

- Add jinja2 tag ([#1](https://github.com/wagtail-nest/wagtail-accessibility/issues/1)) [@LiamBrenner](https://github.com/LiamBrenner)
- Work with static files correctly, fixes ([#2](https://github.com/wagtail-nest/wagtail-accessibility/issues/2)) [@LiamBrenner](https://github.com/LiamBrenner)

## [0.1.0] - 2016-02-22

First release - [@LiamBrenner](https://github.com/LiamBrenner)
