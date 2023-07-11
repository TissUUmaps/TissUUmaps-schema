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

To list all available `{SCHEMA_VERSION}` values:

    tissuumaps-schema versions

To generate a JSON Schema for the specified `{SCHEMA_VERSION}`:

    tissuumaps-schema generate --version {SCHEMA_VERSION}

To upgrade an existing JSON file to the specified `{SCHEMA_VERSION}`:

    tissuumaps-schema upgrade --to-version {SCHEMA_VERSION} myproject.tmap

To validate an existing JSON file against the specified `{SCHEMA_VERSION}`:

    tissuumaps-schema validate --expect-version {SCHEMA_VERSION} myproject.tmap

## Support

For each `{SCHEMA_VERSION}`, a JSON Schema is hosted on:

    https://tissuumaps.github.io/TissUUmaps-schema/{SCHEMA_VERSION}/schema.json

The JSON Schema of each `{SCHEMA_VERSION}` is documented on:

    https://tissuumaps.github.io/TissUUmaps-schema/{SCHEMA_VERSION}/schema_doc.html

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
