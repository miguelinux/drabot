# SPDX-FileCopyrightText: 2024-present Miguel Bernal Marin <miguel.bernal.marin@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from drabot.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="drabot")
def drabot():
    click.echo("Hello world!")
