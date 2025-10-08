#!/usr/bin/env python3
"""
Provide functions to query rollercoasters.csv without importing any modules.

Function:
  coasters_medium_excitement_high_intensity(csv_path)
    - Reads csv_path (comma-separated, header on first line)
    - Returns a list of rollercoaster_type strings where
        excitement_rating == 'Medium' AND numeric intensity > 5.40

No modules or external libraries are used.
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

def coasters_medium_excitement_high_intensity(csv_path):
    """Return list of rollercoaster_type names with excitement_rating 'Medium' and intensity > 5.40."""
    lines = read_lines(csv_path)
    if not lines:
        return []

    headers = parse_header(lines[0])
    # get indices
    try:
        idx_type = headers.index('rollercoaster_type')
    except ValueError:
        raise ValueError("Missing header 'rollercoaster_type'")
    try:
        idx_excitement_rating = headers.index('excitement_rating')
    except ValueError:
        raise ValueError("Missing header 'excitement_rating'")
    try:
        idx_intensity = headers.index('intensity')
    except ValueError:
        raise ValueError("Missing header 'intensity'")

    result = []
    # limit splits to header_count-1 so fields after do not cause extra splits
    header_count = len(headers)
    for line in lines[1:]:
        if not line.strip():
            continue
        parts = [p.strip() for p in line.split(',', header_count - 1)]
        if len(parts) <= max(idx_type, idx_excitement_rating, idx_intensity):
            # malformed; skip
            continue
        coaster_type = parts[idx_type].strip()
        excitement_rating = parts[idx_excitement_rating].strip()
        intensity_val = to_float(parts[idx_intensity].strip(), default=None)
        if (excitement_rating == 'Medium') and (intensity_val is not None) and (intensity_val > 5.40):
            result.append(coaster_type)

    return result


if __name__ == '__main__':
    CSV_PATH = 'rollercoasters.csv'
    matches = coasters_medium_excitement_high_intensity(CSV_PATH)
    print('Found', len(matches), 'rollercoasters matching criteria:')
    for m in matches:
        print('-', m)
