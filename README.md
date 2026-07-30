# Student Management — Python College Project

Simple CLI application to manage students (add, list, find, delete, export CSV).

Usage:

Initialize and show help:

```
python main.py --help
```

Add a student:

```
python main.py add --name "Alice" --age 20 --grade 85
```

List students:

```
python main.py list
```

Find by name:

```
python main.py find --name "Ali"
```

Delete by id:

```
python main.py delete --id 1
```

Export to CSV:

```
python main.py export --path students.csv
```

Dependencies:

- Optional: `tabulate` for nicer tables (`pip install tabulate`).
