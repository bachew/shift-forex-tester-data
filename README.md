# Shift Forex Tester data

```
$ pip install shift-forex-tester-data
$ shiftdata --help
Usage: shiftdata [OPTIONS] INPUT_FILE OUTPUT_FILE

  Shift Forex Tester data time so that daily candle closes with price at daily closing time.

  INPUT_FILE is Forex Tester exported data with defaut settings, OUTPUT_FILE
  has the same format and can be imported back into Forex Tester with default
  settings.

  Example:

    shiftdata -c 18:00 XAUUSD.csv XAUUSD2.csv
    shiftdata -c 17:00 EURUSD.csv EURUSD2.csv

  In XAUUSD2.csv, 18:00 will be shifted to 00:00 so that after importing into
  Forex Tester, daily candle closing price becomes that of 17:59:59 but the
  closing time becomes 23:59:59. Similarly for EURUSD2.csv but with different
  closing time.

Options:
  --version                Show the version and exit.
  -c, --close TIME         Daily closing time  [required]
  -z, --timezone TIMEZONE  Closing time timezone  [default: America/New_York]
  --include-weekends       Do not remove Saturday and Sunday data
  -h, --help               Show this message and exit.
```

To install:

```console
$ pip install shift-forex-tester-data
```


## Development

Development command:

```console
$ bin/dev --help
```

To enter virtual environment, spawn a subshell:

```console
$ bin/dev run bash
$ dev --help  # no need to type "bin/" in the subshell
```

To lint code:

```console
$ dev lint
```

To run unit test:

```console
$ bin/dev run pytest
```

To build library and upload to PyPI:

```console
$ dev build
$ dev upload
```
