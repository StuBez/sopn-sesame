# Extracting candidate data from Statement of Persons Nominated (SOPN)

Automatically extract candidate data from SOPNs using computers.

See [Machine learning to help elections](https://democracyclub.org.uk/blog/2018/03/12/machine-learning-help-elections/) for details of what we're trying to achieve.

So far this library only determines the individual cells that form the table with the candidate information. The idea is that this will form the basis of extracting the individual candidate information from the PDF.

## Set up
### You will need
- Python (tested with Python 3.6)
- [Poppler](https://poppler.freedesktop.org)

### Getting Python ready
```bash
$ virtualenv .
$ source bin/activate
$ pip install -r requirements.txt
```

## Generating the files so they can be processed
```bash
# You will need to have installed Poppler already

# Create an XML file with all the text from the PDF. This file contains elements with the coordinates and size of each text block.
# pdf-file.pdf is the SOPN for the election. xml-file.xml is the file that will be created with the text from the PDF.
$ pdftohtml -c -hidden -xml pdf-file.pdf xml-file.xml

# Generate a PNG image from the PDF so we can work out where the candidate table cells are.
# prefix is some static text that will be prepended to the filename for each PDF page.
# E.g. prefix will create files like prefix-1.png, prefix-2.png
$ pdftoppm -png pdf-file.pdf prefix
```

## Calculating where the tables cells are
```bash
$ python table-coords.py png-file.png
```

This will generate a file with the 'processed' suffix that has overlays for the detected cells. Each detected cell will also have the height, width, and x, and y coordinates so they can be compared against the values in the generated XML file.