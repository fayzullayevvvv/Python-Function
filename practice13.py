def is_palindrome(text: str) -> bool:
    result = ''
    for i in text:
        if i.isalpha():
            result += i.lower()
    
    return result[::-1] == result

print(is_palindrome('hello'))