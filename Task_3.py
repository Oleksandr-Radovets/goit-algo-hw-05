import timeit

# Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = [0] * m
    j = 0

    # Будуємо масив LPS
    for i in range(1, m):
        while j > 0 and pattern[j] != pattern[i]:
            j = lps[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        lps[i] = j

    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            return True  # Знайдено
    return False  # Не знайдено

# Алгоритм Рабіна-Карпа
def rabin_karp_search(text, pattern, base=256, prime=101):
    n, m = len(text), len(pattern)
    hash_text, hash_pattern = 0, 0
    h = 1

    for _ in range(m - 1):
        h = (h * base) % prime

    for i in range(m):
        hash_pattern = (hash_pattern * base + ord(pattern[i])) % prime
        hash_text = (hash_text * base + ord(text[i])) % prime

    for i in range(n - m + 1):
        if hash_pattern == hash_text:
            if text[i:i + m] == pattern:
                return True  # Знайдено
        if i < n - m:
            hash_text = (hash_text - ord(text[i]) * h) * base + ord(text[i + m])
            hash_text %= prime
            if hash_text < 0:
                hash_text += prime
    return False  # Не знайдено

# Алгоритм Боєра-Мура
def boyer_moore_search(text, pattern):
    n, m = len(text), len(pattern)
    bad_char = {}

    # Побудова таблиці поганих символів
    for i in range(m):
        bad_char[pattern[i]] = i

    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return True  # Знайдено
        s += max(1, j - bad_char.get(text[s + j], -1))
    return False  # Не знайдено

def main():
    # Завантаження текстів
    with open("text_1.txt", encoding="utf-8") as f1, open("text_2.txt", encoding="utf-8") as f2:
        text1 = f1.read()
        text2 = f2.read()

    # Тести
    existing_substring = "алгоритм"
    nonexistent_substring = "нейронні мережі"

    # Замір часу
    algorithms = {
        "KMP": lambda txt, pat: kmp_search(txt, pat),
        "Rabin-Karp": lambda txt, pat: rabin_karp_search(txt, pat),
        "Boyer-Moore": lambda txt, pat: boyer_moore_search(txt, pat)
    }

    results = {}
    for algo_name, algo_func in algorithms.items():
        results[algo_name] = {
            "existing_text1": timeit.timeit(lambda: algo_func(text1, existing_substring), number=1),
            "nonexistent_text1": timeit.timeit(lambda: algo_func(text1, nonexistent_substring), number=1),
            "existing_text2": timeit.timeit(lambda: algo_func(text2, existing_substring), number=1),
            "nonexistent_text2": timeit.timeit(lambda: algo_func(text2, nonexistent_substring), number=1),
        }

    # Виведення результатів
    for algo_name, times in results.items():
        print(f"{algo_name}:")
        for case, time in times.items():
            print(f"  {case}: {time:.6f} секунд")

if __name__ == "__main__":
    main()
