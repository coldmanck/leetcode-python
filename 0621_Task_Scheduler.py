from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter_tasks = Counter(tasks)
        max_count = counter_tasks.most_common(1)[0][1]
        n_max_tasks = sum(count == max_count for count in counter_tasks.values())
        return max(len(tasks), (max_count - 1) * (n + 1) + n_max_tasks)