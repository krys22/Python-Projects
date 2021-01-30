A = ["pim", "pom"]
B = ["9999999999", "777888999"]
P = "88999"

def solution (A, B, P):
    smallest_contact_name = []
    print(len(B))
    for i in range(0, len(B)):
        string_item = B[i]
        if P in string_item:
            smallest_contact_name.append(A[i])
    if len(smallest_contact_name) == 0:
        return "NO CONTACT"
    elif len(smallest_contact_name) == 1:
        return smallest_contact_name[0]
    else:
        return min(smallest_contact_name, key = len)

print(solution(A,B,P))