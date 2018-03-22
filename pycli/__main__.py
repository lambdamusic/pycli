#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import click

from .classmodule import MyClass
from .funcmodule import my_function




CMD_LINE_EXAMPLES = """SOME EXAMPLES HERE:
$ pycli 
 => returns some nice text
"""




@click.command()
@click.argument('args', nargs=-1)
@click.option('--examples', is_flag=True, help='Show some examples')
@click.pass_context
def main_cli(ctx, args=None, examples=False):
    """Main CLI."""

    if examples:
        click.secho(CMD_LINE_EXAMPLES, fg="green")
        return

    if not args:
        # print dir(search_cli)
        click.echo(ctx.get_help())
        return
 
    for arg in args:
        print('passed argument :: {}'.format(arg))

    my_function('hello world')

    my_object = MyClass('Thomas')
    my_object.say_name()


if __name__ == '__main__':
    main_cli()