def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        tmp = skill
        for i in skill_tree:
            if i in tmp:
                if i==tmp[0]:
                    tmp= tmp[1:]
                else:
                    break
        else:
            answer += 1

    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print solution(skill, skill_trees)