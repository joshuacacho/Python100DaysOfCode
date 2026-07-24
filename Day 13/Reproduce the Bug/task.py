from random import randint

# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_images[dice_num])


# 1. What is the above code doing?
    # the above code is picking a random integer from the range 1 to 6 and attempting to print it out
# 2. When is the build in method randint meant to do?
    # the randint method takes in the lower range value (1) and also includes the upper range value (6)
# 3. What are your assumptions about the value of the bug?
    # the bug is that when 6 is chosen it is OUTSIDE the range of the dice images length of 5
        # dice_images[6]
# 4. What is the fix?
    # the fix is to ensure the randint lower and upper range values
        # NEVER goes beyond the length of the dice images list

# Fix # 1
    # since dice are always 1 to 6 we can make the randint lower and upper range values 0,5
dice_images_fix1 = ["1", "2", "3", "4", "5", "6"]
dice_num_fix1 = randint(0, 5)
print(dice_images_fix1[dice_num_fix1])


# Fix # 2
    # fix # 1 above DOES NOT ensure that if a new dice was added one day with a number 7 we would have to
        # UPDATE the CODE again
    # permanent fix is just to always do length of list - 1 (to account for NOT getting index out of range exception
dice_images_fix2 = ["1", "2", "3", "4", "5", "6"]
dice_num_fix2 = randint(0, len(dice_images_fix2) - 1)
print(dice_images_fix2[dice_num_fix2])