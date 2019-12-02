class TracingSection:

    name = 'Alex Avila'
    utep_id = "80631370"
    class_secret = "Class secret goes here"

    @staticmethod
    def get_problem_1_answer():

        sort_result = [0, 1, 4, 2, 5, 3]  # <- Replace the contents of the array with your answer

        return sort_result

    @staticmethod
    def get_problem_2_answer():

        visited_array = [0, 1, 4, 2, 5, 3]  # <- Replace the contents of the array with your answer
        return visited_array

    @staticmethod
    def get_problem_3_answer():

        visited_array = [0, 4, 5, 3, 2, 1]  # <- Replace the contents of the array with your answer
        return visited_array

    @staticmethod
    def get_problem_4_answer():

        dist = [1, 0, 3, 9, 5]
        path = [1, -1, 0, 4, 2]

        return dist, path

    @staticmethod
    def get_problem_5_answer():

        solution = [
            # '' 'S' 'T' 'A' 'C' 'K'
            [0, 1, 2, 3, 4, 5],  # ''
            [1, 0, 1, 2, 3, 4],  # 'S'
            [2, 1, 1, 2, 3, 4],  # 'M'
            [3, 2, 2, 1, 2, 3],  # 'A'
            [4, 3, 3, 2, 2, 3],  # 'R'
            [5, 4, 3, 3, 3, 3]   # 'T'

        ]

        return solution

    @staticmethod
    def i_earned_extra_credit():
        return True
