def print_factors(number, *factors):
    for f in factors:
        try:
            if f < 0:
                raise ValueError('Invalid factor')
            if number % f == 0:
                print('Valid factor for {}: {}'.format(number, f))
        except ZeroDivisionError:
            pass
        except ValueError as ve:
            print(ve)
    # try:
    #     for f in factors:
    #         if f < 0:
    #             raise ValueError('Invalid factor')
    #         if number % f == 0:
    #             print('Valid factor for {}: {}'.format(number, f))
    # except ZeroDivisionError:
    #     pass
    # except ValueError as ve:
    #     print(ve)


if __name__ == '__main__':
    print_factors(100, 3, 5, 8, 0, -10, 4, 6)
