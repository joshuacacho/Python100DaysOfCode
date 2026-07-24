# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

while True:
    try:
        pages = int(input("Number of pages: "))
        print(pages)
        word_per_page = int(input("Number of words per page: ")) # removed == as when ran with returned 0
        print(word_per_page)
        total_words = pages * word_per_page
        print(total_words)
        break
    except ValueError as e:
        print(f"[ValueError]: Numeric value not entered, please try again. Details: {e}")
    except Exception as e:
        # print error type, such as ValueError and the exception which is causing the error type
        error_type = type(e).__name__
        print(f"[{error_type}]: {e}")