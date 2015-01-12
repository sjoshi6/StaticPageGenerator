PYTHON:

The application generates Static HTML pages by parsing the input file created using a new grammar.

Files:

cron.py --> Calls FileReader.py when input_folder contains a file

FileReader.py --> Consumes the input.txt file injected in the input_folder and produces a Static HTML page named index.html in the output_folder

Process::

1. Run cron.py from terminal

2. Insert the input.txt in input_folder

3. View the newly generated static HTML page in output_folder
