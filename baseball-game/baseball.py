# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

class Solution(object):
    def calPoints(self, operations: list[str]):
        scores = list()
        for operation in operations:
            try:
                number = float(operation)
                if number.is_integer():
                    number = int(operation)
                scores.append(number)
            except ValueError:
                if operation == '+':
                    scores.append(scores[-1] + scores[-2])
                elif operation == 'D':
                    scores.append(scores[-1] * 2)
                elif operation == 'C':
                    scores.pop()
                else:
                    continue
            print(scores)
        return sum(scores)

                
                
sol = Solution()
print(sol.calPoints(["1","C"]))