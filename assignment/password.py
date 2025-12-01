password = input("Enter your password: ")

def strength(pw):
    length = len(pw)
    has_upper = any(c.isupper() for c in pw)
    has_lower = any(c.islower() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    has_special = any(not c.isalnum() for c in pw)

    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    return score
strength_score = strength(password)
if strength_score <= 2:
    print("Password Strength: Weak")
    print("Consider using at least 8 characters with a mix of uppercase, lowercase, digits, and special characters.")
elif strength_score == 3 or strength_score == 4:
    print("Password Strength: Moderate")
    print("Consider adding more character types or increasing length for a stronger password.")
else:
    print("Password Strength: Strong")
    print("Your password is strong. Good job!")
