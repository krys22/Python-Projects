S = "0 - 22 1985--324"

def solution(S):
    final_string = ''
    counter = 1
    for i in range(0, len(S)):
        if S[i].isnumeric():
            if counter == 3:
                final_string += S[i]
                if i + 1 != len(S):
                    final_string += "-"
                counter = 0
            else:
                final_string += S[i]
            counter += 1
    
    last_two_characters = final_string[-2:]
    if "-" in last_two_characters:
        prefix_character = final_string[:-3]
        last_three = final_string[-3:].replace("-", "")
        return prefix_character + "-" + last_three
    else:
        return final_string

            

print(solution(S))