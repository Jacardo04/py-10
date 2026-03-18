def mage_counter() -> callable:
    count = 0

    def counter():
        nonlocal count  # allows ust to change the outer count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    total = initial_power

    def accumulate(amount: int):
        nonlocal total
        total += amount
        return total

    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"

    return enchant


def memory_vault() -> dict[str, callable]:
    storage = {}

    def store(key: str, value):
        storage[key] = value

    def recall(key: str):
        return storage.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


if __name__ == "__main__":

    print("\nTesting mage counter...")
    counter = mage_counter()
    for i in range(1, 4):
        print(f"Call {i}: {counter()}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")

    print(flaming("Sword"))
    print(frozen("Shield"))

    accumulator = spell_accumulator(10)
    print(accumulator(5))  # 15
    print(accumulator(10))  # 25
    print()

    vault = memory_vault()
    vault["store"]("spell", "fireball")
    print(vault["recall"]("spell"))        # fireball
    print(vault["recall"]("unknown"))      # Memory not found
