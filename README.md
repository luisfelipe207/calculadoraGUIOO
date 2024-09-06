# calculadoraGUIOO

Este repositório contém o código fonte de uma calculadora simples com interface gráfica usando Tkinter.

## Como Executar o Programa

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/calculadora-gui.git
    cd calculadora-gui
    ```

2. Navegue até o diretório `src`:
    ```bash
    cd src
    ```

3. Execute o programa:
    ```bash
    python calculadora_gui.py
    ```

## Principais Decisões de Design

- **Estrutura do Código**: O código está organizado em um único arquivo Python `calculadora_gui.py` dentro da pasta `src` para simplicidade.
- **Interface Gráfica**: Utiliza o Tkinter para criar uma interface gráfica intuitiva para uma calculadora básica.
- **Botões e Funcionalidade**: Cada botão é criado com a função `create_button`, e o comportamento é gerenciado pela função `on_button_click`.
- **Tratamento de Erros**: A expressão é avaliada com `eval`, e qualquer erro de cálculo resulta em "Erro" na tela da calculadora.

Sinta-se à vontade para contribuir ou modificar conforme necessário.
