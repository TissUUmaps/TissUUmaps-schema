# TissUUmaps-schema

Pydantic schema for TissUUmaps

## Requirements

This software requires [Python](https://www.python.org) 3.9 or later.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install tissuumaps-schema.

    pip install tissuumaps-schema

## Usage

To generate a JSON Schema of the specified version:

    tissuumaps-schema generate --version 1

To upgrade a JSON file to the specified schema version:

    tissuumaps-schema upgrade --to-version 2 myproject.tmap

To validate a JSON file against the specified schema version:

    tissuumaps-schema validate --expect-version 2 myproject.tmap

## Support

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
