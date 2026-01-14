def find_anagrams(s, p):
    if len(p) > len(s):
        return []

    result = []

    freq_p = [0] * 26
    freq_window = [0] * 26

    for ch in p:
        freq_p[ord(ch) - ord('a')] += 1

    window_size = len(p)

    for i in range(window_size):
        freq_window[ord(s[i]) - ord('a')] += 1

    if freq_window == freq_p:
        result.append(0)

    for i in range(window_size, len(s)):
        freq_window[ord(s[i]) - ord('a')] += 1
        freq_window[ord(s[i - window_size]) - ord('a')] -= 1

        if freq_window == freq_p:
            result.append(i - window_size + 1)

    return result

def main():
    s = "cbaebabacd"
    p = "abc"

    ans = find_anagrams(s, p)
    print(ans)

if __name__ == "__main__":
    main()
