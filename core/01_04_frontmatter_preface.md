# Prefácio {-}

Este é um texto de apoio à disciplina Matemática Discreta para os cursos de computação do Centro Universitário Luterano de Palmas. Sempre que possível serão apresentadas referências a conceitos da computação e como eles se relacionam com os conceitos matemáticos apresentados. A principal referência do conteúdo utilizado aqui é [@menezes2010matematica].

## Convenções {-}

Os trechos de código apresentados no livro seguem o seguinte padrão:

* **comandos**: devem ser executados no prompt; começam com o símbolo `$`
* **códigos-fontes**: trechos de códigos-fontes de arquivos

A seguir, um exemplo de comando:

```{style=nonumber .sh}
$ mkdir hello-world
```

O exemplo indica que o comando `mkdir`, com a opção `hello-world`, deve ser executado no prompt para criar uma pasta com o nome `hello-world`.

A seguir, um exemplo de código-fonte:

```python
class Pessoa:
    pass
```

O exemplo apresenta o código-fonte da classe `Pessoa`. Em algumas situações, trechos de código podem ser omitidos ou serem apresentados de forma incompleta, usando os símbolos `...` e `#`, como no exemplo a seguir:

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def salvar(self):
        # executa validação dos dados
        ...
        # salva 
        return ModelManager.save(self)
```

## Conhecimentos necessários e desejáveis  {-}

Este texto aborda conceitos matemáticos com aplicações em computação. Portanto, conhecimentos básicos dos cursos de computação são necessários, como noções de lógica, algoritmos e programação e estruturas de dados. Além disso, são desejáveis conhecimentos de bancos de dados e orientação a objetos e também podem ser recursos úteis: 

* Git [@githome]
* Visual Studio Code [@vscodehome]
* TypeScript [@typescripthome]
* Node.js [@nodejshome]
* npm [@npmjshome]
