def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda *args, **kwargs: (
        spell1(*args, **kwargs),
        spell2(*args, **kwargs))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda *args, **kwargs: base_spell(*args, **kwargs) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    return lambda *args, **kwargs: (
        spell(*args, **kwargs)
        if condition(*args, **kwargs)
        else "Spell fizzled"
    )


def spell_sequence(spells: list[callable]) -> callable:
    return lambda *args, **kwargs: [spell(*args, **kwargs) for spell in spells]


if __name__ == "__main__":

    print("\nTesting spell combiner...")

    def fireball(target):
        return f"Fireball hits {target}"

    def heal(target):
        return f"Heals {target}"

    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")

    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")

    def base_spell(x):
        return x

    amplified = power_amplifier(base_spell, 3)

    original = base_spell(10)
    boosted = amplified(10)

    print(f"Original: {original}, Amplified: {boosted}")
