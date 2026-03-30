def is_palindrome(word):
    # Inverta a string usando reversed() e join().
     reversed_str = ''.join(reversed(word))
     return word == reversed_str


def test_is_palindrome():
    # Defina a string de entrada
    input_str = "ANA"
    
    result = is_palindrome(input_str)

    assert result == True
    
    print("Teste aprovado! '" + input_str + "' é um palíndromo.")