# https://leetcode.com/problems/defanging-an-ip-address/


def defangIPaddr(address: str) -> str:
    return "[.]".join(address.split("."))


address1 = "1.1.1.1"
address2 = "255.100.50.0"

print(defangIPaddr(address1))
print(defangIPaddr(address2))
