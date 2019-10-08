class Section1:

    # Provide an implementation for the count_even method. This method receives a non-negative int n and returns
    # the number of digits in n that are even (zero is an even number) - Use recursion - no loops.
    #
    # Example1: count_even(285) -> 2
    # Example2: count_even (565891) -> 2
    # Example3: count_even (2468) -> 4
    # Example4: count_even (1357) -> 0
    # Example5: count_even (130570) -> 2

    @staticmethod
    def count_even(n):  # To make a recursive call, do this: Section1.count_even( ... )
        if n < 10:
            # if n is even
            if n % 2 == 0:
                return 1

            # if n is odd
            return 0

        last_digit = n % 10
        rest_of_digits = n // 10

        if last_digit % 2 == 0:
            return 1 + Section1.count_even(rest_of_digits)

        return Section1.count_even(rest_of_digits)


def main():
    test_result = Section1.count_even(130570)

    print("test_result = ", test_result)


if __name__ == "__main__":
    main()
