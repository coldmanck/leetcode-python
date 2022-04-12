class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        temp_letter_logs = []
        temp_digit_logs = []
        for log in logs:
            if log.split(' ')[1][0] in ['0','1','2','3','4','5','6','7','8','9']:
                temp_digit_logs.append(log)
            else:
                temp_letter_logs.append(log)
        temp_letter_logs.sort(key=lambda x: x.split(' ')[0]) # sort on secondary key
        temp_letter_logs.sort(key=lambda x: x.split(' ')[1:]) # sort on primary key
        return temp_letter_logs + temp_digit_logs