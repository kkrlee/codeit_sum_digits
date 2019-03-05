def sum_digits(n):
    if n < 10:
        return n
    else:
        str_n = str(n)
        return int(str_n[0]) + sum_digits(int(str_n[1:]))

print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))
