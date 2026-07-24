# age = int(input("How old are you?"))
# if age > 18:
# print("You can drive at age {age}.")


while True:
    try:
        age = int(input("How old are you? "))

        if age > 18:
            print(f"You can drive at age {age}.")
            break
    except ValueError as e:
        print(f"[ValueError]: Numeric value not entered, please try again. Details: {e}")

    # NOT NEEDED as Exactly. Indentation errors are compile-time errors,
        # meaning the Python interpreter catches them before the script even starts executing
    # except IndentationError as e:
    #     print(f"[IndentationError]: Indentation error near loop statement, please try again. Details: {e}")
    except Exception as e:
        # print error type, such as ValueError and the exception which is causing the error type
        error_type = type(e).__name__
        print(f"[{error_type}]: {e}")


