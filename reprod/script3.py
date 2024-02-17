from focused_rings import NAME_TO_ID

import rsuanalyzer as ra


def main():
    rings = [
        # (name, theta, description)
        ("syn-T-1", 0, "three membered ring in Pd6L4 (L=1)"),
        ("1,3-alt-S", 0, "four membered ring in Pd6L4 (L=1)"),
        ("syn-T-1", 34, "three membered ring in Pd9L6 (L=2)"),
        ("syn-S-2", 30, "four membered ring in Pd9L6 (L=2)"),
        ("syn-S-1", 38, "four membered ring in Pd12L8 (L=2)"),
    ]

    for name, theta, description in rings:
        ring_id = NAME_TO_ID[name]
        rsu = ra.calc_rsu(ring_id, theta, delta_=87)
        print(f"{name} at {theta} deg: {rsu:.3f} ({description})")


if __name__ == "__main__":
    main()
