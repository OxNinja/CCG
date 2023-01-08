salt = $SALT
password = [ord(x) for x in "$FLAG"]

def check(passwd):
    if len(passwd) < 1:
        return False
    ok = True
    to_check = [ord(x) + salt for x in passwd]
    for i in range(len(to_check)):
        if to_check[i] != password[i]:
            ok = False

    return ok

if __name__ == "__main__":
    if check(input("Give me the password: ")):
        print("Congratulations, you can validate the challenge with the given password!")
    else:
        print("Try again")