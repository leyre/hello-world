# multiple base cases recursive example; palendromes.
# non-numeric example
def is_palendrome(s):
    """
    input: any string
    return: boolean True if string is palendrome, else False
    """
    def to_chars(s):
        """
        input: any string
        return: string as lowercase letters only, no spaces or special chars.
        """
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstovwxyz':
                ans += c
        return ans

    def is_pal(s):
        """
        input: any string as lowercase letters only, no spaces or special chars.
        return: boolean True if string is palendrome, else False
        """
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s)) # don't forget final return in nested functions!

print("Is Eve a palendrome?", is_palendrome('eve'))

print("Is 'Able was I, ere I saw Elba' a palendrome?", is_palendrome('Able was I, ere I saw Elba'))

'''
Results
Is Eve a palendrome? True
Is 'Able was I, ere I saw Elba' a palendrome? True
...
'''
