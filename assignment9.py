#!/usr/bin/env python3
"""
Calculate max, median, mean, and mode for max_pos_gs and max_neg_gs.
Write results as tuples to a new CSV file.
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

def find_max(values):
    """Return max value from a list of floats."""
    if not values:
        return None
    max_val = values[0]
    for v in values[1:]:
        if v > max_val:
            max_val = v
    return max_val

def find_mean(values):
    """Return mean (average) of a list of floats."""
    if not values:
        return None
    total = 0.0
    for v in values:
        total += v
    return total / len(values)

def find_median(values):
    """Return median of a list of floats."""
    if not values:
        return None
    # sort values using bubble sort
    sorted_vals = list(values)
    for i in range(len(sorted_vals)):
        for j in range(len(sorted_vals) - 1 - i):
            if sorted_vals[j] > sorted_vals[j + 1]:
                sorted_vals[j], sorted_vals[j + 1] = sorted_vals[j + 1], sorted_vals[j]
    n = len(sorted_vals)
    if n % 2 == 1:
        return sorted_vals[n // 2]
    else:
        return (sorted_vals[n // 2 - 1] + sorted_vals[n // 2]) / 2.0

def find_mode(values):
    """Return mode (most frequent value) of a list of floats."""
    if not values:
        return None
    max_count = 0
    mode_val = values[0]
    for v in values:
        count = 0
        for v2 in values:
            if v == v2:
                count += 1
        if count > max_count:
            max_count = count
            mode_val = v
    return mode_val

def calculate_gs_stats_and_write(input_csv, output_csv):
    """
    Read input_csv, extract max_pos_gs and max_neg_gs columns.
    Calculate max, median, mean, and mode for each.
    Write results as tuples to output_csv.
    Returns a tuple ((max_pos_max, max_pos_median, max_pos_mean, max_pos_mode),
                     (max_neg_max, max_neg_median, max_neg_mean, max_neg_mode))
    """
    lines = read_lines(input_csv)
    if not lines:
        with open(output_csv, 'w', encoding='utf-8') as out:
            out.write('')
        return (None, None)

    header = lines[0].strip()
    headers = [h.strip() for h in header.split(',')]
    header_count = len(headers)

    # find required indices
    try:
        idx_max_pos_gs = headers.index('max_pos_gs')
        idx_max_neg_gs = headers.index('max_neg_gs')
    except ValueError:
        raise ValueError('Required header(s) missing')

    max_pos_values = []
    max_neg_values = []

    for line in lines[1:]:
        if not line.strip():
            continue
        parts = [p.strip() for p in line.split(',', header_count - 1)]
        if len(parts) < header_count:
            continue
        pos_val = to_float(parts[idx_max_pos_gs], default=None)
        neg_val = to_float(parts[idx_max_neg_gs], default=None)
        if pos_val is not None:
            max_pos_values.append(pos_val)
        if neg_val is not None:
            max_neg_values.append(neg_val)

    # calculate stats
    pos_max = find_max(max_pos_values)
    pos_median = find_median(max_pos_values)
    pos_mean = find_mean(max_pos_values)
    pos_mode = find_mode(max_pos_values)

    neg_max = find_max(max_neg_values)
    neg_median = find_median(max_neg_values)
    neg_mean = find_mean(max_neg_values)
    neg_mode = find_mode(max_neg_values)

    # write to CSV
    with open(output_csv, 'w', encoding='utf-8') as out:
        out.write('metric,max_pos_gs,max_neg_gs\n')
        out.write('max,{:.2f},{:.2f}\n'.format(pos_max, neg_max))
        out.write('median,{:.2f},{:.2f}\n'.format(pos_median, neg_median))
        out.write('mean,{:.2f},{:.2f}\n'.format(pos_mean, neg_mean))
        out.write('mode,{:.2f},{:.2f}\n'.format(pos_mode, neg_mode))

    pos_tuple = (pos_max, pos_median, pos_mean, pos_mode)
    neg_tuple = (neg_max, neg_median, neg_mean, neg_mode)
    return (pos_tuple, neg_tuple)


if __name__ == '__main__':
    IN = 'rollercoasters.csv'
    OUT = 'gs_statistics.csv'
    pos_stats, neg_stats = calculate_gs_stats_and_write(IN, OUT)
    print(f"max_pos_gs stats: {pos_stats}")
    print(f"max_neg_gs stats: {neg_stats}")
    print(f"Wrote statistics to {OUT}")