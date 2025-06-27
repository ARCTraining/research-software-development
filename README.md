# Research Software Development (in Python) Course

SWD3: Research Software Development documentation and course notes.

Shortened link to this material: bit.ly/swd3-python

[![DOI](https://zenodo.org/badge/1008390809.svg)](https://zenodo.org/badge/latestdoi/1008390809)

## Building instructions

*Note that this repository is also configured to build via a GitHub action. HTML pages are not tracked via version control*.

You can use pip to install the package `heading_container` to run the scripts in this project. These scripts pull in the content from presentations and format them as an article. The environment with this package must be active before using Quarto to render the material.

Install the most recent development version (may not be stable):

```bash
pip install heading_container@git+https://github.com/ARCTraining/research-software-development
```

Or install a specific version (version 0.1.0 in this example; please check the releases page):

```bash
pip install https://github.com/ARCTraining/research-software-development/archive/refs/tags/v0.1.0.tar.gz

# or

pip install heading_container@git+https://github.com/ARCTraining/research-software-development@v0.1.0
```

## Author

Below is a list of contributors (in chronological order of addition) with associated Contributor Role Taxonomy (CRediT) roles. Please see the [CRediT website](https://credit.niso.org/) for definitions of roles.

- [Maeve Murphy Quinlan](https://orcid.org/0000-0003-2958-1008): conceptualization, writing (original draft), writing (review and editing), data curation, methodology.
  - Creation of website, Python workflows, GitHub actions.
  - Redesign of course.

## Citation instructions

Plain text citation:

Murphy Quinlan, Maeve. 2025. “Research Software Development in Python.” June 24, 2025. https://arctraining.github.io/research-software-development/.

BibTex citaton:

```
@online{murphy_quinlan2025,
  author = {Murphy Quinlan, Maeve},
  title = {Research {Software} {Development} in {Python}},
  date = {2025-06-24},
  url = {https://arctraining.github.io/research-software-development/},
  langid = {en}
}
```

## License

This material is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License](https://creativecommons.org/licenses/by-nc-sa/4.0/), and is copyrighted by the University of Leeds.
