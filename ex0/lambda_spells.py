def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda m: m['power'])['power']
    min_power = min(mages, key=lambda m: m['power'])['power']
    avg_power = round(sum(map(lambda m: m['power'], mages)) / len(mages), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"}
    ]

    spells = ["fireball", "heal", "shield"]

    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)

    print(f"{sorted_artifacts[0]['name']} "
          f"({sorted_artifacts[0]['power']} power) "
          f"comes before {sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power']} power)\n")

    print("Testing spell transformer...")
    transformed_spells = spell_transformer(spells)

    print(" ".join(transformed_spells))
