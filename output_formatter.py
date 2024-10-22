def generate_output(matches, output_format):
    """
    Outputs the matches in the specified format (basic or grouped).
    """

    if output_format == 'basic':
        output_basic(matches)
    elif output_format == 'grouped':
        output_grouped(matches)
    else:
        print(f"Unknown output format: {output_format}")

def output_basic(matches):
    """
    Outputs the matches in the 'basic' format:
    <UserID>,<Pattern Description>
    """
    for match in matches:
        print(f"{match['user_id']},{match['message']}")

def output_grouped(matches):
    """
    Outputs the matches in the 'grouped' format:
    <UserID>:
        <Pattern 1>
        <Pattern 2>
    """
    grouped_matches = {}

    # Group matches by user_id
    for match in matches:
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
        print()
