"""
So, In the previous level, the trick was visit the console to find in a huge text the correct letters
So I think it is the same trick, but this time, we seek a string of length 7 with the following format:
ABCdEFG -> One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
"""


def construct_chunk(line: str) -> str:
    """
    :param line: Get a line from the `get_line()` function
    :return: chunk: A string of length 7
    Constructs chunks of nine characters. For example, from the string 'AbvRkxZabCGRR', the function returns
    'AbvRkxZab', 'bvRkxZabC', 'vRkxZabCG' and so on
    This is a generator, yields chunks every time we request it
    """
    start_index = 0  # here starts from index 0
    increment_index = 9  # The limit to stop the slicing
    # The range of this loop is stops at the -7 position of the line
    for _ in range(len(line)-7):
        chunk = line[start_index:increment_index]  # slicing
        start_index += 1  # increment one position
        increment_index += 1 # moving upper limit
        yield chunk  # yielding the chunk


def body_guards(chunk_test: str):
    """
    This function determines if a substring has a small letter with three exactly bodyguards
    and also checks the first and last letters for lower letters
    """
    first_and_last_little = chunk_test[0].islower() and chunk_test[-1].islower()
    bigger_letters = chunk_test[1:4].isupper() and chunk_test[5:8].isupper()
    middle_small = chunk_test[4].islower()
    if first_and_last_little and middle_small and bigger_letters:
        # print(chunk_test)
        print(chunk_test[4], end='')  # this is the answer


# I put the text from the console of my browser in a file
text = open("/home/diego/Documents/python_challenge/Lv 3/level3_text.txt")

for line in text:
    for chunk in construct_chunk(line):  # here we have all yelding values
        body_guards(chunk)  # test the current chunk

# The url is linkedlist.php