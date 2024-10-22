import click
from log_parser import parse_log_file
from output_formatter import generate_output
from user_statistics import compute_user_statistics
from patterns import match_patterns, load_patterns
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
    
    # Step 1: Parse the log file
    log_entries = parse_log_file(log_path)
    if not log_entries:
        click.echo("No valid log entries found.")
        return

    # Step 2: Compute user statistics
    user_stats = compute_user_statistics(log_entries)

    # Step 3: Load patterns
    patterns = load_patterns(pattern_path)
    if not patterns:
        click.echo("No patterns loaded")
        return 
    
    # Step 4: Match patterns
    matches = match_patterns(user_stats, patterns)

    # Step 5: Generate output
    generate_output(matches, format)
    

if __name__ == '__main__':
    main()