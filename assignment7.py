#!/usr/bin/env python3
"""
Sort rollercoasters by park_id and write to a new CSV file.
No imports or dictionaries used.
"""

def read_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]

def to_int(s, default=None):
    try:
        return int(float(s))
    except Exception:
        return default

def sort_by_park_id_and_write(input_csv, output_csv):
    """
    Read input_csv, sort data rows by numeric park_id (ascending),
    and write header + sorted rows to output_csv.
    Returns the number of data rows written.
    """
    lines = read_lines(input_csv)
    if not lines:
        # nothing to write
        with open(output_csv, 'w', encoding='utf-8') as out:
            out.write('')
        return 0

    header = lines[0].rstrip('\n')
    headers = [h.strip() for h in header.split(',')]
    header_count = len(headers)

    rows = []  # list of tuples (park_id_int, parts_list)
    for line in lines[1:]:
        if not line.strip():
            continue
        # limit splits so later fields containing commas are preserved
        parts = [p.strip() for p in line.split(',', header_count - 1)]
        if len(parts) < header_count:
            # skip malformed rows
            continue
        park_id = to_int(parts[0], default=0)
        rows.append((park_id, parts))

    # sort by park_id (stable)
    rows.sort(key=lambda x: x[0])

    with open(output_csv, 'w', encoding='utf-8') as out:
        out.write(header + '\n')
        for _, parts in rows:
            out.write(','.join(parts) + '\n')

    return len(rows)

if __name__ == '__main__':
    INPUT = 'rollercoasters.csv'
    OUTPUT = 'rollercoasters_sorted_by_park_id.csv'
    written = sort_by_park_id_and_write(INPUT, OUTPUT)
    print(f"Wrote {written} rows to {OUTPUT}")