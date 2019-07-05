class Logic:
    @staticmethod
    def build_fibonacci_sequence(n):
        if n < 0:
            raise ValueError("Sequence count should be positive")
        if n == 0:
            return []
        if n == 1:
            return [0]
        res = [0, 1]
        if n == 2:
            return res

        while len(res) < n:
            res.append(res[-1] + res[-2])
        return res
