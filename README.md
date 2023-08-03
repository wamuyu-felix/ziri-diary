# Simple Diary CLI

This command-line interface (CLI) provides a simple diary application that allows you to manage diary entries. You can add, update, read, list, and remove diary entries.

## Requirements

- Python 3.x
- The `argparse` module.

## Functionality

The diary CLI has the following actions:

### Add

Add a new diary or add a new entry to an existing diary.

```
python ziri add <date> <text>
```

- `<date>`: Date in the format `yyyy-mm-dd`.
- `<text>`: Text you want to add to the diary.

### Update

Update an entire diary for a specific date.

```
python ziri update <date> <text>
```

- `<date>`: Date in the format `yyyy-mm-dd`.
- `<text>`: Text you want to add to the diary.

### Clear

Clear the contents of a diary for a specific date.

```
python ziri clear <date>
```

- `<date>`: Date in the format `yyyy-mm-dd`.

### Remove

Delete a diary for a specific date.

```
python ziri remove <date>
```

- `<date>`: Date in the format `yyyy-mm-dd`.

### Read

Read the contents of a diary for a specific date.

```
python ziri read <date>
```

- `<date>`: Date in the format `yyyy-mm-dd`.

### List

List all your diary entries.

```
python ziri list
```

## Usage

To use the diary CLI, run the `ziri` script followed by the action and appropriate arguments. For example:

```
python ziri add 2023-08-03 "Wrote a README for diary project."
python ziri read 2023-08-03
```

## Note

This is a simple diary CLI for personal use. Feel free to modify and extend it to suit your needs.

---

Please make sure to replace `ziri` with the actual filename of your script. You can copy this README content to a new file named `README.md` and place it in the same directory as your script to provide documentation for your diary application.
