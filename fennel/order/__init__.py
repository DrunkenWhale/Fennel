import click
from fennel.order.history import show
from fennel.order.add import add
from fennel.order.finish import finish


@click.group()
def cli():
    pass


cli.add_command(show)
cli.add_command(finish)
cli.add_command(add)
