def is_bad(problems):
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        x = problem.split(" ")
        if len(x) != 3:
            return "Error: Incorrect format."
        if x[1] != "+" and x[1] != "-":
            return "Error: Operator must be '+' or '-'."
        if len(x[0]) > 4 or len(x[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        try:
            int(x[0])
            int(x[2])
        except BaseException:
            return "Error: Numbers must only contain digits."
        return


def arithmetic_arranger(problems, show_result=False):
    s = is_bad(problems)
    if s is not None:
        return s
    result = list()
    operand1 = list()
    operand2 = list()
    operators = list()
    biggerLength = list()
    arranged_problems = ""
    for problem in problems:
        x = problem.split(" ")
        if x[1] == '+':
            result.append(int(x[0]) + int(x[2]))
        else:
            result.append(int(x[0]) - int(x[2]))
        operand1.append(x[0])
        operators.append(x[1])
        operand2.append(x[2])

    for i in range(0, len(operators)):
        if len(operand1[i]) > len(operand2[i]):
            biggerLength.append(len(operand1[i]))
        else:
            biggerLength.append(len(operand2[i]))
    c = 0
    for i in range(0, len(operators)):
        arranged_problems += "  "
        arranged_problems += str.rjust(operand1[i], biggerLength[i])
        if c != len(operators) - 1:
            c += 1
            arranged_problems += "    "
    arranged_problems += "\n"
    c = 0
    for i in range(0, len(operators)):
        arranged_problems += operators[i] + " "
        arranged_problems += str.rjust(operand2[i], biggerLength[i])
        if c <= len(operators):
            c += 1
            arranged_problems += "    "
    arranged_problems += "\n"
    j = 0
    c = 0
    for i in result:
        arranged_problems += "--"
        length = len(str(i))
        s = ""
        for k in range(0, biggerLength[j]):
            s += '-'
        arranged_problems += s
        if c <= len(operators):
            c += 1
            arranged_problems += "    "
        j += 1
    if show_result:
        arranged_problems += "\n"
        j = 0
        for i in result:
            #arranged_problems += "  "
            arranged_problems += str.rjust(str(i), biggerLength[j]+2) + "    "
            j += 1

    return arranged_problems


print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
