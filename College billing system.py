# Infix to Postfix Conversion

def infix_to_postfix(exp):
    stack = []
    postfix = ""

    for ch in exp:
        if ch.isalnum():
            postfix += ch

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()

        else:
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.append(ch)

        print("Stack:", stack)

    while stack:
        postfix += stack.pop()

    return postfix


# Evaluate Postfix Expression
def evaluate(postfix, values):
    stack = []

    for ch in postfix:
        if ch.isalnum():
            stack.append(values[ch])

        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a / b)

        print("Evaluation Stack:", stack)

    return stack.pop()


# Main Function
def main():
    exp = input("Enter Fee Formula (Infix): ")

    postfix = infix_to_postfix(exp)

    print("Postfix Expression:", postfix)

    values = {}

    values['T'] = float(input("Enter Tuition Fee: "))
    values['H'] = float(input("Enter Hostel Fee: "))
    values['E'] = float(input("Enter Exam Fee: "))
    values['S'] = float(input("Enter Scholarship: "))

    result = evaluate(postfix, values)

    print("Final Payable Fees:", result)


main()