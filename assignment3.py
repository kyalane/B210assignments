#!/usr/bin/env python3
"""
Count distinct rollercoaster types from rollercoasters.csv without using any imports.

Outputs the number of distinct types and a sorted list of the types.
"""

CSV_PATH = 'rollercoasters.csv'

def read_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]

def parse_header_index(header_line, column_name):
    headers = [h.strip() for h in header_line.split(',')]
    try:
        return headers.index(column_name), len(headers)
    except ValueError:
        return None, len(headers)

def main():
    lines = read_lines(CSV_PATH)
    if not lines:
        print('No data in', CSV_PATH)
        return

    # find index of rollercoaster_type
    idx, header_count = parse_header_index(lines[0], 'rollercoaster_type')
    if idx is None:
        print("Header 'rollercoaster_type' not found in CSV header")
        return

    types_set = set()
    # we'll limit splits to header_count-1 so fields after the target column (or any commas later)
    # don't cause the rollercoaster_type field to be split incorrectly.
    for line in lines[1:]:
        if not line.strip():
            continue
        # limit number of splits so we get exactly header_count fields at most
        parts = [p.strip() for p in line.split(',', header_count - 1)]
        if len(parts) <= idx:
            # malformed line — skip
            continue
        value = parts[idx].strip()
        if value:
            types_set.add(value)

    types_list = sorted(types_set)
    print('Number of distinct rollercoaster types:', len(types_list))
    print('Types:')
    for t in types_list:
        print('-', t)

if __name__ == '__main__':
    main()
