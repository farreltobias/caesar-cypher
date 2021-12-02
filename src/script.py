def encrypt(word, code):
  result = ""
  for letter in word:
    numericValue = ord(letter) + code
    if (numericValue > 122):
      numericValue = (numericValue - 122) + 96
    result += chr(numericValue)
  return result

def decrypt(word, code):
  result = ""
  for letter in word:
    numericValue = ord(letter) - code
    if (numericValue < 97):
      numericValue = 123 - (97 - numericValue)
    result += chr(numericValue)
  return result

def main():
  operation = input()
  word = input().lower()
  code = input()

  converted_operation = int(operation)
  converted_code = int(code)

  result = decrypt(word, converted_code) if converted_operation else encrypt(word, converted_code)

  print(result)

main()