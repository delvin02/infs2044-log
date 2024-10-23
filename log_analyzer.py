import click
from log_parser import LogParser
from output_formatter import OutputGenerator
from user_statistics import UserStatistics
from patterns import PatternMatcher
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
    try:
        # Step 1: Parse the log file
        log_parser = LogParser(log_path)
        log_entries = log_parser.parse()
        if not log_entries:
            click.echo("No valid log entries found.")
            return

        # Step 2: Compute user statistics
        user_stats_computer = UserStatistics(log_entries)
        user_stats = user_stats_computer.compute()
        print(user_stats)
        # Step 3: Load patterns
        pattern_matcher = PatternMatcher(pattern_path)
        patterns = pattern_matcher.load_patterns()
        if not patterns:
            click.echo("No patterns loaded")
            return 
        
        # Step 4: Match patterns
        matches = pattern_matcher.match(user_stats)

        # Step 5: Generate output
        output_generator = OutputGenerator(matches, format)
        output_generator.generate()

    except ValueError as e:
        click.echo(str(e))
    

if __name__ == '__main__':
    main()