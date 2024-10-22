import click

OUTPUT_FORMATS = ['basic','grouped']

#
# Each of the functions below is the entry point of a use case for the command line application.
# Call your code from each of these functions, but do not include all of your code in the functions
# in this file.
#

@click.command(no_args_is_help=True)
@click.option("--format", default='basic', type=click.Choice(OUTPUT_FORMATS), help=f"Output Format")
@click.argument("pattern_path", required=True, type=click.Path(exists=True))
@click.argument("log_path", required=True, type=click.Path(exists=True))
def main(format, pattern_path, log_path):
    """Main entry point of the console application."""

    #TODO add some of your code here
    # Remember to structure and package your code and tests appropriately.
    # Don't just add _all_ your code here.
    print(format)
    print(pattern_path)
    print(log_path)
    pass

if __name__ == '__main__':
    main()