class Solution:
    def validIPAddress(self, IP: str) -> str:
        IP = IP.split('.')
        ip_type_v4 = True # ipv4
        if len(IP) != 1 and len(IP) != 4:
            return 'Neither'
        if len(IP) == 1:
            IP = IP[0].split(':')
            ip_type_v4 = False # ipv6
            if len(IP) != 8:
                return 'Neither'

        if ip_type_v4:
            return 'IPv4' if all([len(i) != 0 and i.isnumeric() and ((i[0] == '0' and len(i) == 1) or (i[0] != '0' and 0 < int(i) < 256)) for i in IP]) else 'Neither'
        else:
            return 'IPv6' if all([1 <= len(i) <= 4 and ((i[0] == '0' and all([ord(j) == ord('0') for j in i])) or all([0 <= ord(j) - ord('0') <= 9 or 0 <= ord(j) - ord('a') <= 5 for j in i.lower()]) and 0 <= int(i.lower(), 16) < 16**4) for i in IP]) else 'Neither'
