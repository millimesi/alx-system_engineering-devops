#!/bin/bash
# specific conversion script for my html files to php

# Use shell globbing to create an array of HTML files
LIST=(*.html)

# Iterate over each HTML file in the array
for i in "${LIST[@]}"; do
    # Generate a new PHP filename by replacing the ".html" extension with ".php"
    NEWNAME="${i%.html}.php"

    # Copy the content of "beginfile" to the new PHP file
    cat beginfile > "$NEWNAME"

    # Manipulate the content of the HTML file and append it to the new PHP file
    cat "$i" | sed -e '1,25d' | tac | sed -e '1,21d' | tac >> "$NEWNAME"

    # Append the content of "endfile" to the new PHP file
    cat endfile >> "$NEWNAME"
done

