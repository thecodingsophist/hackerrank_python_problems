# Find the largest unique substring within a larger string

def find_uniq_substr(input_str: str) -> str:
    left = 0
    right = 0
    longest_sub = 0
    max_r = 0
    max_l = 0
    text_len = len(input_str)
    indexes = {}
    while right <= text_len:
        if input_str[right] in indexes:
            left = max(left, indexes[input_str[right]])

        curr_sub = right - left + 1

        if curr_sub > longest_sub:
            longest_sub = curr_sub
            max_r = right
            max_l = left

        right += 1
        indexes[input_str[right]] = right + 1

    return input_str[left:right]
