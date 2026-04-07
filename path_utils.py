def format_path(ticket, path):
    return {
        "ticket": ticket,
        "paths": [
            {"path": p, "cost": c}
            for p, c in path
        ]
    }