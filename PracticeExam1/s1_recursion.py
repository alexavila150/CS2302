class Section1:

    # Given a non-negative int n, return the number
    # of digits in n that are less than or equal
    # to 5 - Use recursion - no loops.

    # Example1: count(285) -> 2
    # Example2: count(565891) -> 3

    @staticmethod
    def count(n: int) -> int:
        if n <= 5:
            return 1

        if n < 10:
            return 0

        last_digit = n % 10
        rest_of_digits = n // 10
        if last_digit <= 5:
            return 1 + Section1.count(rest_of_digits)

        return Section1.count(rest_of_digits)

def main():
    test_result = Section1.count(1273)

    print("test_result = ", test_result)


if __name__ == "__main__":
    main()
