# !/usr/bin/env python3
"""
Group rollercoasters into sets by avg_speed category and write to CSV.
No imports or dictionaries used.
"""
def read_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]
def to_float(s, default=None):
    try:
        return float(s)
    except Exception:
        return default
def categorize_avg_speed_and_write(input_csv, output_csv,
                                   low_threshold=10.0, high_threshold=15.0):
    """
    Read input_csv, classify each coaster by avg_speed into one of three sets:
      - 'Low'    : avg_speed < low_threshold
      - 'Medium' : low_threshold <= avg_speed <= high_threshold
      - 'High'   : avg_speed > high_threshold
    Writes a CSV with columns:
      category,park_id,theme,rollercoaster_type,avg_speed
    Returns a tuple with counts (low_count, medium_count, high_count).
    Uses only lists and sets (no dictionaries, no imports).
    """
    lines = read_lines(input_csv)
    if not lines:
        # write empty file
        with open(output_csv, 'w', encoding='utf-8') as out:
            out.write('')
        return (0, 0, 0)

    header = lines[0].strip()
    headers = [h.strip() for h in header.split(',')]
    header_count = len(headers)

    # find required indices
    try:
        idx_park = headers.index('park_id')
        idx_theme = headers.index('theme')
        idx_type = headers.index('rollercoaster_type')
        idx_avg_speed = headers.index('avg_speed')
    except ValueError:
        raise ValueError('Required header(s) missing')

    low_set = set()
    medium_set = set()
    high_set = set()

    # We'll store tuples (park_id, theme, type, avg_speed) in parallel lists for writing
    low_rows = []
    medium_rows = []
    high_rows = []

    for line in lines[1:]:
        if not line.strip():
            continue
        parts = [p.strip() for p in line.split(',', header_count - 1)]
        if len(parts) < header_count:
            continue
        avg = to_float(parts[idx_avg_speed], default=None)
        if avg is None:
            continue
        park = parts[idx_park]
        theme = parts[idx_theme]
        rtype = parts[idx_type]
        key = (park, theme, rtype, "{:.2f}".format(avg))
        if avg < low_threshold:
            if key not in low_set:
                low_set.add(key)
                low_rows.append(key)
        elif avg > high_threshold:
            if key not in high_set:
                high_set.add(key)
                high_rows.append(key)
        else:
            if key not in medium_set:
                medium_set.add(key)
                medium_rows.append(key)

    # write output CSV
    with open(output_csv, 'w', encoding='utf-8') as out:
        out.write('category,park_id,theme,rollercoaster_type,avg_speed\n')
        for park, theme, rtype, avg_s in low_rows:
            out.write(','.join(['Low', park, theme, rtype, avg_s]) + '\n')
        for park, theme, rtype, avg_s in medium_rows:
            out.write(','.join(['Medium', park, theme, rtype, avg_s]) + '\n')
        for park, theme, rtype, avg_s in high_rows:
            out.write(','.join(['High', park, theme, rtype, avg_s]) + '\n')

    return (len(low_rows), len(medium_rows), len(high_rows))

if __name__ == '__main__':
    IN = 'rollercoasters.csv'
    OUT = 'rollercoasters_by_avg_speed.csv'
    low_c, med_c, high_c = categorize_avg_speed_and_write(IN, OUT)
    print(f"Wrote {low_c + med_c + high_c} rows -> Low:{low_c} Medium:{med_c} High:{high_c}")
# filepath: /Users/kyal0513/Desktop/B210 assignment fun/assignment8.py
# !/usr/bin/env python3
"""
Group rollercoasters into sets by avg_speed category and write to CSV.
No imports or dictionaries used.
"""
def read_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]

def to_float(s, default=None):
    try:
        return float(s)
    except Exception:
        return default

def categorize_avg_speed_and_write(input_csv, output_csv,
                                   low_threshold=10.0, high_threshold=15.0):
    """
    Read input_csv, classify each coaster by avg_speed into one of three sets:
      - 'Low'    : avg_speed < low_threshold
      - 'Medium' : low_threshold <= avg_speed <= high_threshold
      - 'High'   : avg_speed > high_threshold
    Writes a CSV with columns:
      category,park_id,theme,rollercoaster_type,avg_speed
    Returns a tuple with counts (low_count, medium_count, high_count).
    Uses only lists and sets (no dictionaries, no imports).
    """
    lines = read_lines(input_csv)
    if not lines:
        # write empty file
        with open(output_csv, 'w', encoding='utf-8') as out:
            out.write('')
        return (0, 0, 0)

    header = lines[0].strip()
    headers = [h.strip() for h in header.split(',')]
    header_count = len(headers)

    # find required indices
    try:
        idx_park = headers.index('park_id')
        idx_theme = headers.index('theme')
        idx_type = headers.index('rollercoaster_type')
        idx_avg_speed = headers.index('avg_speed')
    except ValueError:
        raise ValueError('Required header(s) missing')

    low_set = set()
    medium_set = set()
    high_set = set()

    # We'll store tuples (park_id, theme, type, avg_speed) in parallel lists for writing
    low_rows = []
    medium_rows = []
    high_rows = []

    for line in lines[1:]:
        if not line.strip():
            continue
        parts = [p.strip() for p in line.split(',', header_count - 1)]
        if len(parts) < header_count:
            continue
        avg = to_float(parts[idx_avg_speed], default=None)
        if avg is None:
            continue
        park = parts[idx_park]
        theme = parts[idx_theme]
        rtype = parts[idx_type]
        key = (park, theme, rtype, "{:.2f}".format(avg))
        if avg < low_threshold:
            if key not in low_set:
                low_set.add(key)
                low_rows.append(key)
        elif avg > high_threshold:
            if key not in high_set:
                high_set.add(key)
                high_rows.append(key)
        else:
            if key not in medium_set:
                medium_set.add(key)
                medium_rows.append(key)

    # write output CSV
    with open(output_csv, 'w', encoding='utf-8') as out:
        out.write('category,park_id,theme,rollercoaster_type,avg_speed\n')
        for park, theme, rtype, avg_s in low_rows:
            out.write(','.join(['Low', park, theme, rtype, avg_s]) + '\n')
        for park, theme, rtype, avg_s in medium_rows:
            out.write(','.join(['Medium', park, theme, rtype, avg_s]) + '\n')
        for park, theme, rtype, avg_s in high_rows:
            out.write(','.join(['High', park, theme, rtype, avg_s]) + '\n')

    return (len(low_rows), len(medium_rows), len(high_rows))
if __name__ == '__main__':
    IN = 'rollercoasters.csv'
    OUT = 'rollercoasters_by_avg_speed.csv'
    low_c, med_c, high_c = categorize_avg_speed_and_write(IN, OUT)
    print(f"Wrote {low_c + med_c + high_c} rows -> Low:{low_c} Medium:{med_c} High:{high_c}")