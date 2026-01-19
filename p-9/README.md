# Secret Auction CLI

This Python application facilitates a "secret auction" by leveraging the OpenAI API to dynamically generate auction items and managing a multi-user bidding process via the command line.

## Technical Overview

The application integrates LLM-generated content with a standard dictionary-based bidding logic.

## Logic Flow

- Item Generation: The app sends a system prompt to the LLM requesting a JSON object containing an item, description, and starting_bid.

- Input Validation: A while loop ensures that any user-entered bid meets or exceeds the starting_bid retrieved from the JSON payload.

- Data Storage: Bidders and their respective bids are stored in a local dictionary (bidders).

- Winner Determination: The get_winner() function utilizes the max() function with a lambda key to identify the dictionary key (name) associated with the highest value (bid).
