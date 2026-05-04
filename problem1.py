def get_value(ch):
    return ord(ch) - ord('a') + 1


def max_sum_substring(s):
    s = s + s
    n = len(s)

    used = set()
    left = 0
    curr_sum = 0
    ans = 0

    for right in range(n):
        while s[right] in used:
            used.remove(s[left])
            curr_sum -= get_value(s[left])
            left += 1

        used.add(s[right])
        curr_sum += get_value(s[right])

        if curr_sum > ans:
            ans = curr_sum

    return ans


s = "abca"
print(max_sum_substring(s))
