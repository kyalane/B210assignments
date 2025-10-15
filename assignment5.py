#!/usr/bin/env python3
"""
Compute average intensity for coasters with excitement_rating 'High', grouped by theme.
No imports allowed.

Function:
  avg_high_excitement_intensity_by_theme(csv_path)
    - Returns dict { theme: average_intensity }
    - Skips rows with missing or non-numeric intensity
    - Uses exact match 'High' for excitement_rating
"""

def read_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]

def parse_header(header_line):
    return [h.strip() for h in header_line.split(',')]

def to_float(s, default=None):
    try:
        return float(s)
    except Exception:
        return default

def avg_high_excitement_intensity_by_theme(csv_path):
    """Return a dictionary mapping theme -> average intensity for 'High' excitement entries."""
    lines = read_lines(csv_path)
    if not lines:
        return {}

    headers = parse_header(lines[0])
    # required columns
    try:
        idx_theme = headers.index('theme')
        idx_excitement_rating = headers.index('excitement_rating')
        idx_intensity = headers.index('intensity')
    except ValueError as e:
        raise ValueError('Missing required header: ' + str(e))

    header_count = len(headers)
    sums = {}  # theme -> sum of intensities
    counts = {}  # theme -> count

    for line in lines[1:]:
        if not line.strip():
            continue
        parts = [p.strip() for p in line.split(',', header_count - 1)]
        if len(parts) <= max(idx_theme, idx_excitement_rating, idx_intensity):
            continue
        theme = parts[idx_theme]
        excitement = parts[idx_excitement_rating]
        intensity_val = to_float(parts[idx_intensity], default=None)
        if (excitement == 'High') and (intensity_val is not None):
            sums[theme] = sums.get(theme, 0.0) + intensity_val
            counts[theme] = counts.get(theme, 0) + 1

    averages = {}
    for theme in sums:
        averages[theme] = sums[theme] / counts[theme]

    return averages


if __name__ == '__main__':
    CSV_PATH = 'rollercoasters.csv'
    avgs = avg_high_excitement_intensity_by_theme(CSV_PATH)
    if not avgs:
        print('No results')
    else:
        print('Average intensity for coasters with excitement_rating == "High", by theme:')
        # print sorted by theme name
        for theme in sorted(avgs.keys()):
            print(f"- {theme}: {avgs[theme]:.2f}")
