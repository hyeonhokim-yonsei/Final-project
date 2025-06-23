
def series_convergence(a_n, max_n=10000, epsilon=1e-6):
    total = 0
    for n in range(1, max_n + 1):
        term = a_n(n)
        if abs(term) > 1e10:  # 항이 너무 크면 발산으로 간주
            return False, float('inf')
        total += term
        if abs(term) < epsilon and n > 100:  # 충분히 작아졌다고 판단
            return True, total
    return False, total  # 끝까지 충분히 작아지지 않으면 발산
