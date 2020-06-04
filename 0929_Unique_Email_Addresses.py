class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # seen = set()
        # count = 0
        # for email in emails:
        #     addr = ''.join(email.split('@')[0].split('+')[0].split('.')) + '@' + email.split('@')[1]
        #     if addr not in seen:
        #         seen.add(addr)
        #         count += 1
        # return count
        
        emails = [''.join(email.split('@')[0].split('+')[0].split('.')) + '@' + email.split('@')[1] for email in emails]
        return len(set(emails))