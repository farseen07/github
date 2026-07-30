import argparse
from db import init_db, add_student, list_students, find_student, delete_student, export_csv
from student import Student

try:
    from tabulate import tabulate
except Exception:
    tabulate = None


def print_rows(rows):
    if not rows:
        print('No students found.')
        return
    headers = ['ID', 'Name', 'Age', 'Grade']
    if tabulate:
        print(tabulate(rows, headers=headers, tablefmt='github'))
    else:
        print(', '.join(headers))
        for r in rows:
            print(f"{r[0]}, {r[1]}, {r[2]}, {r[3]}")


def main():
    init_db()

    parser = argparse.ArgumentParser(description='Simple Student Management CLI')
    sub = parser.add_subparsers(dest='cmd')

    p_add = sub.add_parser('add', help='Add a new student')
    p_add.add_argument('--name', required=True)
    p_add.add_argument('--age', type=int, required=True)
    p_add.add_argument('--grade', type=float, required=True)

    p_list = sub.add_parser('list', help='List all students')

    p_find = sub.add_parser('find', help='Find students by name')
    p_find.add_argument('--name', required=True)

    p_del = sub.add_parser('delete', help='Delete a student by id')
    p_del.add_argument('--id', type=int, required=True)

    p_export = sub.add_parser('export', help='Export students to CSV')
    p_export.add_argument('--path', default='students.csv')

    args = parser.parse_args()

    if args.cmd == 'add':
        add_student(args.name, args.age, args.grade)
        print('Student added.')
    elif args.cmd == 'list':
        rows = list_students()
        print_rows(rows)
    elif args.cmd == 'find':
        rows = find_student(args.name)
        print_rows(rows)
    elif args.cmd == 'delete':
        delete_student(args.id)
        print('Student deleted (if existed).')
    elif args.cmd == 'export':
        export_csv(args.path)
        print(f'Exported to {args.path}')
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
