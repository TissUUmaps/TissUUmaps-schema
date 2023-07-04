import json
from typing import Optional, TextIO

import click

from .formats import VERSION_FORMAT_TYPES, CurrentFormat, guess_format_version


@click.group(name="tissuumaps-schema")
def cli() -> None:
    pass


@cli.command(name="generate", help="Generate a JSON Schema of the specified version.")
@click.option(
    "--version",
    "version",
    type=click.Choice(list(VERSION_FORMAT_TYPES.keys())),
    default=CurrentFormat.version,
    show_default=True,
    help="Version of the generated schema.",
)
@click.option(
    "--indent",
    "indent",
    type=click.IntRange(min=0),
    default=2,
    show_default=True,
    help="JSON indentation level.",
    metavar="INTEGER",
)
def generate(version: str, indent: int) -> None:
    format_type = VERSION_FORMAT_TYPES[version]
    schema_json_data = format_type.project_type.model_json_schema(by_alias=True)
    schema_json = json.dumps(schema_json_data, indent=indent or None)
    click.echo(message=schema_json)


@cli.command(
    name="upgrade", help="Upgrade a JSON file to the specified schema version."
)
@click.argument("project_file", type=click.File())
@click.option(
    "--from-version",
    "from_version",
    type=click.Choice(list(VERSION_FORMAT_TYPES.keys())),
    help="Schema version to upgrade from.",
)
@click.option(
    "--to-version",
    "to_version",
    type=click.Choice(list(VERSION_FORMAT_TYPES.keys())),
    default=CurrentFormat.version,
    show_default=True,
    help="Schema version to upgrade to.",
)
@click.option(
    "--strict/--no-strict",
    "strict",
    default=None,
    show_default=True,
    help="Whether to parse strictly or not.",
)
@click.option(
    "--indent",
    "indent",
    type=click.IntRange(min=0),
    default=2,
    show_default=True,
    help="JSON indentation level.",
    metavar="INTEGER",
)
def upgrade(
    project_file: TextIO,
    from_version: Optional[str],
    to_version: str,
    strict: Optional[bool],
    indent: int,
) -> None:
    project_json_data = json.load(project_file)
    if from_version is None:
        from_version = guess_format_version(project_json_data)
    from_format_type = VERSION_FORMAT_TYPES[from_version]
    to_format_type = VERSION_FORMAT_TYPES[to_version]
    project = from_format_type().parse(project_json_data, strict=strict)
    upgraded_project = to_format_type().upgrade(project)
    upgraded_project_json = upgraded_project.model_dump_json(
        indent=indent, by_alias=True
    )
    click.echo(upgraded_project_json)


@cli.command(
    name="validate", help="Validate a JSON file against the specified schema version."
)
@click.argument("project_file", type=click.File())
@click.option(
    "--expect-version",
    "expected_version",
    type=click.Choice(list(VERSION_FORMAT_TYPES.keys())),
    default=CurrentFormat.version,
    show_default=True,
    help="Schema version to validate against.",
)
@click.option(
    "--strict/--no-strict",
    "strict",
    default=None,
    show_default=True,
    help="Whether to parse strictly or not.",
)
@click.option(
    "--indent",
    "indent",
    type=click.IntRange(min=0),
    default=2,
    show_default=True,
    help="JSON indentation level.",
    metavar="INTEGER",
)
def validate(
    project_file: TextIO,
    expected_version: Optional[str],
    strict: Optional[bool],
    quiet: bool,
    indent: int,
) -> None:
    project_json_data = json.load(project_file)
    if expected_version is None:
        expected_version = guess_format_version(project_json_data)
    format_type = VERSION_FORMAT_TYPES[expected_version]
    format_type().parse(project_json_data, strict=strict)
