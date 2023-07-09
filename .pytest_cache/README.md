# pytest cache directory #

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.

@autor: Clarice Ferreira

- Explicação sobre os diretórios
  - pages: 
    - Neste diretório estão todas as páginas do sistema que estão sendo chamadas para teste.
    - Cada página do sistema (login, home, cadastro) é representado por um arquivo nesta pasta, ou seja, sempre que o teste é redirecionado para outra pagina é criado um novo arquivo para continuar validando os dados da pagina atual.
  
  - tests:
    - Neste diretório estão todos os arquivos de testes que acessam as extendem as classes criadas em cada páginas.
    - Para cada caso de teste é criado um novo arquivo.


- Explicação sobre os arquivos 
    - conftest.py 
      - Este arquivo contém as configurações básicas para acessar a aplicação a ser testada.
    - pages/base_page.py
      - Este arquivo contém métodos genéricos que podem ser usados em qualquer momento do teste, por isso, todas as classes (de cada página) herdam desta página, assim podem usar os métodos definidos nela.
    - pages/login_page.py (a exemplo de todos as demais páginas)
      - Este arquivo representa a página de login, dentro dele temos o método __init__ que é o construtor da classe, dentro deste métodos são declarados todos os locators que serão válidados, ou seja, cada campo, botão, texto entre outros que estão contidos nesta página
      - O self é utilizado para usar os atributos fora do escopo do método
      - Contém também neste arquivo o método fazer_login (a exemplo de todos os demais desta página):
        - Este método, como o nome sugere, representa a ação de realizar login, e dentro dele, utilizando o self, é possível fazer uma chamada aos metodos da base_page, como também, se fosse o caso, seria possível realizar ações próprias deste método como por exemplo no método verificar_texto_mensagem_erro_login, também deste arquivo, que usa o comando assert para comparar texto, além de usar os métodos da classe que herda, neste caso base_page.
    - tests/test_login_valido.py (a exemplo de todos os demais arquivos de teste)
      - Este arquivo irá validar se passando um usuário e senha válido, o login é realizado com sucesso.
      - Neste arquivo é passada toda massa de dados necessária para fazer os testes e validações que são executadas nos métodos das classes extendidas por este arquivo de teste.
      - Ao extender a classe LoginPage do arquivo login_page.py é possível fazer uma chamada ao métodos definidos neste arquivo e enviar requeridos.
      - Este arquivo contém cada passo que será realizado pelo usuário para realizar o teste, e cada passo é representado por um método que é chamado na ordem em que deve ser executado.
    - Da mesma forma da explicação acima funciona os demais arquivos de cada pasta mencionada
  