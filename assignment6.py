#!/usr/bin/env python3
"""
Create a Coaster class and build Coaster objects from rollercoasters.csv
No imports, no dictionaries used.
"""

class Coaster:
    def __init__(self,
                 park_id, theme, rollercoaster_type, custom_design,
                 excitement, excitement_rating, intensity, intensity_rating,
                 nausea, nausea_rating, max_speed, avg_speed,
                 ride_time, ride_length, max_pos_gs, max_neg_gs,
                 max_lateral_gs, total_air_time, drops,
                 highest_drop_height, inversions):
        # keep raw string attributes for text fields
        self.park_id = to_int(park_id)
        self.theme = theme
        self.rollercoaster_type = rollercoaster_type
        self.custom_design = to_int(custom_design)
        self.excitement = to_float(excitement)
        self.excitement_rating = excitement_rating
        self.intensity = to_float(intensity)
        self.intensity_rating = intensity_rating
        self.nausea = to_float(nausea)
        self.nausea_rating = nausea_rating
        self.max_speed = to_float(max_speed)
        self.avg_speed = to_float(avg_speed)
        self.ride_time = to_int(ride_time)
        self.ride_length = to_int(ride_length)
        self.max_pos_gs = to_float(max_pos_gs)
        self.max_neg_gs = to_float(max_neg_gs)
        self.max_lateral_gs = to_float(max_lateral_gs)
        self.total_air_time = to_float(total_air_time)
        self.drops = to_int(drops)
        self.highest_drop_height = to_int(highest_drop_height)
        self.inversions = to_int(inversions)

    def __repr__(self):
        return ("Coaster(rollercoaster_type={!r}, theme={!r}, park_id={!r}, "
                "excitement_rating={!r}, intensity={!r})").format(
                    self.rollercoaster_type, self.theme, self.park_id,
                    self.excitement_rating, self.intensity)

def to_float(s, default=None):
    try:
        return float(s)
    except Exception:
        return default

def to_int(s, default=None):
    try:
        return int(float(s))
    except Exception:
        return default

def read_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]

def build_coasters_from_csv(csv_path):
    """Return a list of Coaster objects created from the CSV rows."""
    lines = read_lines(csv_path)
    if not lines:
        return []

    header = lines[0].strip()
    headers = [h.strip() for h in header.split(',')]
    header_count = len(headers)

    coasters = []
    for line in lines[1:]:
        if not line.strip():
            continue
        # limit splits so later fields containing commas are preserved
        parts = [p.strip() for p in line.split(',', header_count - 1)]
        if len(parts) < header_count:
            # skip malformed rows
            continue
        # pass fields in CSV order to Coaster constructor
        c = Coaster(
            parts[0], parts[1], parts[2], parts[3],
            parts[4], parts[5], parts[6], parts[7],
            parts[8], parts[9], parts[10], parts[11],
            parts[12], parts[13], parts[14], parts[15],
            parts[16], parts[17], parts[18], parts[19],
            parts[20]
        )
        coasters.append(c)

    return coasters

if __name__ == '__main__':
    CSV_PATH = 'rollercoasters.csv'
    coasters = build_coasters_from_csv(CSV_PATH)
    print(f"Built {len(coasters)} Coaster objects.")
    # show first 8 as a quick sanity check
    for i in range(min(8, len(coasters))):
        print(coasters[i])