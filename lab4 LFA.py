import random

def parse_regex(pattern):
    i = 0
    parsed = []
    while i < len(pattern):
        char = pattern[i]
        if char.isspace():
            i += 1
            continue
        if char == '(':
            end = pattern.find(')', i)
            options = pattern[i + 1:end].split('|')
            parsed.append(('group', options))
            i = end
        elif char == '^':
            if pattern[i + 1] == '+':
                parsed[-1] = ('repeat', parsed[-1], 1, 3)
                i += 1
            elif pattern[i + 1] == '*':
                parsed[-1] = ('repeat', parsed[-1], 0, 3)
                i += 1
            elif pattern[i + 1].isdigit():
                end = i + 2
                while end < len(pattern) and pattern[end].isdigit():
                    end += 1
                count = int(pattern[i + 1:end])
                parsed[-1] = ('repeat', parsed[-1], count, count)
                i = end - 1
        elif char == '?':
            parsed[-1] = ('repeat', parsed[-1], 0, 1)
        else:
            parsed.append(('char', char))
        i += 1
    return parsed

def generate_from_parsed(parsed):
    result = []
    for token in parsed:
        if token[0] == 'char':
            result.append(token[1])
        elif token[0] == 'group':
            result.append(random.choice(token[1]))
        elif token[0] == 'repeat':
            _, sub_token, min_count, max_count = token
            count = random.randint(min_count, max_count)
            for _ in range(count):
                result.append(generate_from_parsed([sub_token]))
    return ''.join(result)

def generate_from_regex(pattern, num_samples=10):
    parsed = parse_regex(pattern)
    return [generate_from_parsed(parsed) for _ in range(num_samples)]

def main():
    # Separated parts of the full regex
    part1 = "O(P|Q|R)^+2(3|4)"
    part2 = "A^*B(C|D|E)F(G|H|I)^2"
    part3 = "J^+K(L|M|N)^*O?(P|Q)^3"

    print("\n--- Part 1 (Prefix) ---")
    prefix_samples = generate_from_regex(part1, 10)
    print(prefix_samples)

    print("\n--- Part 2 (Middle) ---")
    middle_samples = generate_from_regex(part2, 10)
    print(middle_samples)

    print("\n--- Part 3 (Suffix) ---")
    suffix_samples = generate_from_regex(part3, 10)
    print(suffix_samples)

if __name__ == "__main__":
    main()
