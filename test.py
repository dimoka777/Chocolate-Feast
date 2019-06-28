def chocolateFeast(n, c, m):

    result = n // c

    def wrapp(wrappers):
        if wrappers < m:
            return 0
        elif wrappers >= m:
            res_wrap = wrappers // m
            return res_wrap + wrapp((wrappers % m) + res_wrap)
    total_wrapps = wrapp(result)
    result += total_wrapps
    return result


print(chocolateFeast(6,2,2))
