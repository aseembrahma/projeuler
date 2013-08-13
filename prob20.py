def main():
    whole_list = range(1, 101)
    factor_list = []
    current_factor = 2
    while len(whole_list) != 0:
        while 1 in whole_list:
            whole_list.remove(1)
        current_factor_count = 0
        is_prime_factor = True
        for j in range(len(factor_list)):
            if current_factor % factor_list[j][0] == 0:
                is_prime_factor = False
                break
        if is_prime_factor:
            for i in range(len(whole_list)):
                while whole_list[i] % current_factor == 0:
                    whole_list[i] = whole_list[i] / current_factor
                    current_factor_count = current_factor_count + 1
            factor_list.append([current_factor, current_factor_count])
        current_factor = current_factor + 1
        
    print factor_list

if __name__ == "__main__":
    main()