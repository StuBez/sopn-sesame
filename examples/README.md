# Example

```bash
$ pdftohtml -c -hidden -xml 7809.pdf 7809.xml
$ pdftoppm -png 7809.pdf 7809
$ python ../table-coords.py 7809-1.png
```

## The files
- `7809.pdf`: The original PDF SOPN.
- `7809.xml`: The generated XML file with the PDF text and metadata.
- `7809-1.png`: The first (and only) page from the PDF, rendered as a PNG.
- `7809-1-processed.png`: The rendered PNG with debugging overlay, showing the detected candidate cells with the x, y, height, and width.