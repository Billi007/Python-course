# Check if a password is "Weak", "Medium", or "Strong", Criteria: <6 chars(Weak), 6-10(Medium), >10(Strong)

password = "tanu!@768fghf"
password_len = len(password)

if password_len <6:
    strength = "Weak"
elif password_len <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Strength of your password is:", strength)