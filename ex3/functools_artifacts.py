from functools import reduce, lru_cache, partial
import operator
from functools import singledispatch


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in ops:
        raise ValueError(f"Unknown operation {operation}")

    func = ops[operation]

    if operation in ("max", "min"):
        return func(spells)
    else:
        return reduce(func, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, power=50, element="fire"),
        "ice_enchant": partial(base_enchantment, power=50, element="ice"),
        "lightning_enchant":
        partial(base_enchantment, power=50, element="lightning")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> callable:
    @singledispatch
    def cast(x):
        return f"Cannot cast spell on {x}"

    @cast.register
    def _(x: int):
        return f"Damage spell: {x} points"

    @cast.register
    def _(x: str):
        return f"Enchantment spell: {x}"

    @cast.register
    def _(x: list):
        return [cast(item) for item in x]

    return cast


if __name__ == "__main__":

    print("\nTesting spell reducer...")
    spells = [10, 20, 30, 40]  # matches expected output
    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))

    print("\nTesting memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))
