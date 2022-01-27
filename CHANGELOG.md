# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!--next-version-placeholder-->

## v0.5.0 (2022-01-27)
### Feature
* Rework the post release process ([`546de45`](https://github.com/nigelm/gh_release/commit/546de4562b2b4b85cb1ec3b249925e1cc3bed4f9))

## v0.4.2 (2022-01-26)
### Fix
* Move the post release inline so sees the updated code ([`a361512`](https://github.com/nigelm/gh_release/commit/a361512106792c5fff12ab095163c3db4569003e))

## v0.4.1 (2022-01-26)
### Fix
* Correct post release process in CI ([`adef879`](https://github.com/nigelm/gh_release/commit/adef879b58414e0a76b9f9d6024b059053896936))

## v0.4.0 (2022-01-26)
### Feature
* Full lifecycle github actions ([`eed6957`](https://github.com/nigelm/gh_release/commit/eed6957eecde5e70d2eaf30c7c460214a03e2a7f))

### Fix
* Filter on deploy ci ([`d54663b`](https://github.com/nigelm/gh_release/commit/d54663b98d257dcc84c87a3f3b783f9a74931dca))
* Deployment secrets ([`9bfaa07`](https://github.com/nigelm/gh_release/commit/9bfaa077ea6dc5b6c6b68920817827219a0859a5))
* Correct ci tests ([`3f87b67`](https://github.com/nigelm/gh_release/commit/3f87b6784b5432d9ebe2ab68b4ed46a06b9b10cb))
* Correct tests version checking ([`44d2e95`](https://github.com/nigelm/gh_release/commit/44d2e9525e6e71ef2eaf313d1fa2df83fa4f1757))

### Documentation
* Added a set of fake filler documentation ([`f473306`](https://github.com/nigelm/gh_release/commit/f4733065aba6ad2c12de833d47795ad56adb4ea9))

## v0.3.0 (2022-01-24)
### Feature
* Try to move setup phase into its own workflow ([`3cfe119`](https://github.com/nigelm/gh_release/commit/3cfe1190a7e020d54ec994a1af15627724394f92))

### Fix
* Rework setup code into a separate action ([`13b2e3a`](https://github.com/nigelm/gh_release/commit/13b2e3ac83c1cda0432442eec1a977fc0ac48cc4))

## v0.2.4 (2022-01-24)
### Fix
* Attempt to dual cache with simplification ([`dfa16c9`](https://github.com/nigelm/gh_release/commit/dfa16c9432a1bfde21ea68b5ba24ed9c09a04810))

## v0.2.3 (2022-01-24)
### Fix
* It appears only one active cache works... ([`c0b26d2`](https://github.com/nigelm/gh_release/commit/c0b26d29790fcf2d27c601f2959f443dc16a65a7))

## v0.2.2 (2022-01-24)
### Fix
* Perturb cache key ([`ec27a96`](https://github.com/nigelm/gh_release/commit/ec27a9603f5a5734e86766006dc837d1b38d0dbd))

## v0.2.1 (2022-01-24)
### Fix
* Put cache back ([`498d0c5`](https://github.com/nigelm/gh_release/commit/498d0c5486f1341baff1596bb14fd85d792d98f5))
* Find out where poetry puts things ([`1dc02ac`](https://github.com/nigelm/gh_release/commit/1dc02ac01bf7d11b342b8416a67a7d88a02ac272))
* Correct some venv issues ([`668b894`](https://github.com/nigelm/gh_release/commit/668b894dd3a701f86f2b5714d253048f16d78a09))
* Move venv to make it cache correctly ([`054b592`](https://github.com/nigelm/gh_release/commit/054b592711919fe32bfd21bbd3499b7fcf99643e))

## v0.2.0 (2022-01-24)
### Feature
* Github upload of release package ([`ae314e6`](https://github.com/nigelm/gh_release/commit/ae314e671896a4cc4e770dc986c301800698e3a5))

### Fix
* Turn check_build_status off ([`42552c0`](https://github.com/nigelm/gh_release/commit/42552c0d439792563542c140e0f61284685157af))
* Modify build parameters ([`f60ca7d`](https://github.com/nigelm/gh_release/commit/f60ca7de1fc99e85d045fcda4e952f988151ce4e))
* Try changing poetry path ([`e74567d`](https://github.com/nigelm/gh_release/commit/e74567dcf0e2a2267b122c283eff544f6909069d))
* Another attempt... ([`8810337`](https://github.com/nigelm/gh_release/commit/88103379986524daa154aeb0b4198ab232d3aa91))
* Another attempt to handle build within python-smantic-release ([`89aa02a`](https://github.com/nigelm/gh_release/commit/89aa02a9ff42346e80e28c3145f430e0ed83bbfd))

## v0.1.2 (2022-01-23)
### Fix
* Fix github token name ([`837fc2f`](https://github.com/nigelm/gh_release/commit/837fc2fc114d52ea667050bae0ca6a52836dd278))
* Move virtenvs into project for caching ([`fe1d8e5`](https://github.com/nigelm/gh_release/commit/fe1d8e5910d617c4839ad0ace50944f53a9bacb9))

## v0.1.1 (2022-01-23)
### Fix
* Hash the action naming ([`199115c`](https://github.com/nigelm/gh_release/commit/199115cf82f8f1bff58985c7be64f3abb30131f7))

## v0.1.0 (2022-01-23)
### Feature
* Rework for internal releaser ([`91a0e64`](https://github.com/nigelm/gh_release/commit/91a0e6459d723a6bfccd72540c545dbc47680eb5))
* Rework to use our python-semantic-release ([`709d449`](https://github.com/nigelm/gh_release/commit/709d4491e903f1cff0b2bad1ccf9c4375f101897))

## v0.1.0 (2022-01-23)
### Feature
* Rework for internal releaser ([`91a0e64`](https://github.com/nigelm/gh_release/commit/91a0e6459d723a6bfccd72540c545dbc47680eb5))
* Rework to use our python-semantic-release ([`709d449`](https://github.com/nigelm/gh_release/commit/709d4491e903f1cff0b2bad1ccf9c4375f101897))

## v0.0.4 (2022-01-23)
### Fix
* Force dist to exist for semantic release ([`5b165c7`](https://github.com/nigelm/gh_release/commit/5b165c7b0f9f37821506b909ae870d2cdb5f2911))

## v0.0.3 (2022-01-23)
### Fix
* Do not upload release to repository ([`c5fc0dc`](https://github.com/nigelm/gh_release/commit/c5fc0dc2a0e94e8356d8d4a8276a54e5db25e993))

## v0.0.2 (2022-01-23)



----
