# There is Block Scope in Python!

game_level = 3
enemies = ["Skeleton", "Zombies","Alien"]


def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]


if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)



# Challenge for Prime Number Checker
def is_prime(n):
    """Returns True if n is prime, False otherwise."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:  # Exclude all other even numbers
        return False

    # Check odd factors up to the square root of n
    # n ** 5 the square root of n or √n
        # int(n**0.5) + 1 (Stop): This calculates √n, rounds it down to a whole number,
            # and adds 1. In Python, range() stops right before the stop number,
            # so adding 1 ensures that √n itself is actually tested if it is a whole number
            # (like testing 3 when n=9)
    # The loop skips numbers by 2s. By starting at 3 and stepping by 2,
        # it only generates odd numbers (3, 5, 7, 9...).
        # This saves time by ignoring even numbers, which cannot evenly divide an odd number anyway.

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

# prime numbers
print(is_prime(2))
print(is_prime(3))
print(is_prime(5))
print(is_prime(7))
print(is_prime(11))
print(is_prime(13))
print(is_prime(17))
print(is_prime(19))
print(is_prime(23))
print(is_prime(29))
print(is_prime(31))
print(is_prime(37))
print(is_prime(41))
print(is_prime(43))
print(is_prime(47))
print(is_prime(53))
print(is_prime(59))
print(is_prime(61))
print(is_prime(67))
print(is_prime(71))
print(is_prime(73))
print(is_prime(79))
print(is_prime(83))
print(is_prime(89))
print(is_prime(97))

print("START OF NON PRIME NuMBERS")

# non prime numbers
print(is_prime(4))
print(is_prime(6))
print(is_prime(8))
print(is_prime(10))
print(is_prime(12))
print(is_prime(14))
print(is_prime(16))
print(is_prime(18))
print(is_prime(20))
print(is_prime(21))
print(is_prime(22))
print(is_prime(24))
print(is_prime(25))
print(is_prime(26))
print(is_prime(27))
print(is_prime(28))
print(is_prime(30))
print(is_prime(32))
print(is_prime(33))
print(is_prime(34))
print(is_prime(35))
print(is_prime(36))
print(is_prime(38))
print(is_prime(39))
print(is_prime(40))



