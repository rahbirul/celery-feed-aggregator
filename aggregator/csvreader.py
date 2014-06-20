import csv
import codecs
import cStringIO


class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")


class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self


def get_csv_rows(csv_filepath):
    fp = open(csv_filepath, 'r')
    data = UnicodeReader(fp)
    try:
        # Read the column names from the first line of the file
        fields = data.next()

        for row in data:
            item = {}
            for (name, value) in zip(fields, row):
                item[name] = value.strip()
            yield item

    except csv.Error, e:
        logger.exception("Error in file %s at line %d: %s" % (csv_src, data.line_num, e))

    fp.close()