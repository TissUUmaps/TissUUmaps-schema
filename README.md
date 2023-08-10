# TissUUmaps-schema

[![pypi](https://img.shields.io/pypi/v/tissuumaps-schema?label=pypi)](https://pypi.org/project/tissuumaps-schema/)
[![python](https://img.shields.io/pypi/pyversions/tissuumaps-schema?label=python)](https://www.python.org)
[![test-and-deploy](https://img.shields.io/github/actions/workflow/status/TissUUmaps/tissuumaps-schema/test-and-deploy.yml?label=test-and-deploy)](https://github.com/TissUUmaps/tissuumaps-schema/actions/workflows/test-and-deploy.yml)
[![coverage](https://img.shields.io/codecov/c/gh/TissUUmaps/tissuumaps-schema?label=coverage)](https://app.codecov.io/gh/TissUUmaps/tissuumaps-schema)
[![issues](https://img.shields.io/github/issues/TissUUmaps/tissuumaps-schema?label=issues)](https://github.com/TissUUmaps/tissuumaps-schema/issues)
[![pull requests](https://img.shields.io/github/issues-pr/TissUUmaps/tissuumaps-schema?label=pull%20requests)](https://github.com/TissUUmaps/tissuumaps-schema/pulls)
[![license](https://img.shields.io/github/license/TissUUmaps/tissuumaps-schema?label=license)](https://github.com/TissUUmaps/tissuumaps-schema/blob/main/LICENSE)

Pydantic schema for TissUUmaps

## Requirements

[Python](https://www.python.org) 3.9 or later

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install tissuumaps-schema:

    pip install tissuumaps-schema

## Usage

To list all available `$VERSION` values:

    tissuumaps-schema versions

To list all available `$MODEL` values for the specified `$VERSION`:

    tissuumaps-schema models --version $VERSION

To generate a JSON Schema for the specified `$VERSION` and `$MODEL`:

    tissuumaps-schema generate --version $VERSION $MODEL

To upgrade an existing instance of `$MODEL` to the specified `$VERSION`:

    tissuumaps-schema upgrade --to-version $VERSION $MODEL myinstance.json

To validate an existing instance of `$MODEL` against the specified `$VERSION`:

    tissuumaps-schema validate --expect-version $VERSION $MODEL myinstance.json

## Support

For each `$VERSION` and `$MODEL`, a JSON Schema is hosted on:

    https://tissuumaps.github.io/TissUUmaps-schema/$VERSION/$MODEL.json

The JSON Schema of each `$VERSION` and `$MODEL` is documented on:

    https://tissuumaps.github.io/TissUUmaps-schema/$VERSION/$MODEL_doc.html

If you find a bug, please [raise an issue](https://github.com/TissUUmaps/TissUUmaps-schema/issues/new).

## Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Changelog

[Changelog](https://github.com/TissUUmaps/TissUUmaps-schema/blob/main/CHANGELOG.md)

## Authors

[SciLifeLab BioImage Informatics Facility (BIIF)](https://biifsweden.github.io)

## License

[MIT](https://github.com/TissUUmaps/TissUUmaps-schema/blob/main/LICENSE)
