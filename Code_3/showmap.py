# showmap.py - Launches a map in the browser using an address from the
# command line
# Usage: showmap 1 Chaucer, Hamilton, Victoria, Australia
import webbrowser, sys


if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    print("please provide an address.")
    exit(0)

# Open the web browser.
webbrowser.open('https://www.openstreetmap.org/search?query=' + address)

