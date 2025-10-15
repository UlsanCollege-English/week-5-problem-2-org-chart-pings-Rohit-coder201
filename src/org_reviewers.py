def count_senior(root, min_level):
    """
    Return how many people in the org tree have level >= min_level.
    Node format: {"name": str, "level": int, "reports": [nodes]}
    """
    if root is None:
        return 0

    # Some nodes may not have 'reports' key
    reports = root.get("reports", [])

    count = 1 if root.get("level", 0) >= min_level else 0

    for r in reports:
        count += count_senior(r, min_level)

    return count
