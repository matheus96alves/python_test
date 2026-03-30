
def is_palindrome(Ana):
    # Inverta a string usando reversed() e join().
     reversed_str = ''.join(reversed(Ana))
     return Ana == reversed_str


def test_is_palindrome():
    # Defina a string de entrada
    input_str = "Ana"
    
    # Execute a verificação do palíndromo
    result = is_palindrome(input_str)
    
    # Verifique se o resultado é True (verdadeiro) para um palíndromo
    assert result == True
    
    print("Teste aprovado! '" + input_str + "' é um palíndromo.")