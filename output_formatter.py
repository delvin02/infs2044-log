class OutputGenerator:
    """Class to handle output formatting and generation."""
    
    def __init__(self, matches, output_format):
        self.matches = matches
        self.output_format = output_format

    
    def generate(self):
        """
        Outputs the matches in the specified format (basic or grouped).
        """

        if self.output_format == 'basic':
           self.__output_basic()
        elif self.output_format == 'grouped':
            self.__output_grouped()
        else:
            print(f"Unknown output format: {self.output_format}")

    def __output_basic(self):
        """
        Outputs the matches in the 'basic' format:
        <UserID>,<Pattern Description>
        """
        for match in self.matches:
            print(f"{match['user_id']},{match['message']}")

    def __output_grouped(self):
        """
        Outputs the matches in the 'grouped' format:
        <UserID>:
            <Pattern 1>
            <Pattern 2>
        """
        grouped_matches = {}

        # Group matches by user_id
        for match in self.matches:
            user_id = match['user_id']
            message = match['message']
            if user_id not in grouped_matches:
                grouped_matches[user_id] = []
            grouped_matches[user_id].append(message)

        # Print the matches in grouped format
        for user_id, messages in grouped_matches.items():
            print(f"{user_id}:")
            for message in messages:
                print(f"    {message}")
