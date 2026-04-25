class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = [t[0] for t in trust]
        judge = n * (n + 1) / 2 - sum(set(people))
        trusted = [t[0] for t in trust if t[1] == judge]
        return int(judge) if len(set(trusted)) == n - 1 else -1 