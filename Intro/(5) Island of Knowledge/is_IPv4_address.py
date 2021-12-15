# An IP address is a numerical label assigned to each device (e.g., computer, printer) 
# participating in a computer network that uses the Internet Protocol for communication. 
# There are two versions of the Internet protocol, and thus two versions of addresses. 
# One of them is the IPv4 address. Given a string, find out if it satisfies the IPv4 
# address naming rules.

# four 8-bit integers without leading zeroes, separated by dots
def solution(input: str):
    try:
        x = input.split('.')
        return (len(x) == 4) and all(0 <= int(num) < 256 for num in x) \
                             and all(num == num.lstrip('0') if int(num) != 0 else num == "0" for num in x)
    except:
        return False

# passed all tests