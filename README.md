# LED Frame Rate Checker para Fotogrametria

## Descrição
Esta aplicação foi desenvolvida para facilitar a verificação da adequação da taxa de frames de vídeos utilizados em análises fotogramétricas. O script utiliza um Raspberry Pi Pico para alternar o estado de dois LEDs em intervalos regulares e registra o tempo de cada alternância em um arquivo CSV. Este arquivo pode ser usado para verificar a consistência e precisão da taxa de frames de uma câmera de vídeo, comparando os registros de tempo com os frames capturados.

## Características
- **Alternância Automática de LEDs**: Os LEDs são alternados automaticamente com precisão temporal, utilizando um timer programável.
- **Registro de Tempo**: Cada alternação dos LEDs é registrada com o horário preciso em milissegundos.
- **Saída de Dados em CSV**: Os tempos são gravados em um arquivo CSV para análise subsequente.
- **Feedback de Sucesso de Escrita**: O script verifica e informa se os dados foram gravados com sucesso no arquivo CSV.

## Pré-requisitos
- Raspberry Pi Pico
- MicroPython instalado no Raspberry Pi Pico
- LEDs e resistores apropriados
- Conexão com um computador para transferência de arquivos CSV

## Instalação
Carregue o script para o Raspberry Pi Pico utilizando a IDE Thonny ou uma ferramenta similar de sua preferência.

## Uso
1. Conecte os LEDs aos pinos 14 e 17 do seu Raspberry Pi Pico.
2. Carregue o script para o Pico.
3. Execute o script. Os LEDs começarão a alternar automaticamente.
4. Grave um vídeo dos LEDs alternando.
5. Após o teste automático, o script alternará os LEDs manualmente por cinco vezes.
6. Recupere o arquivo `tempos.csv` do Raspberry Pi Pico.
7. Compare os tempos do arquivo CSV com os frames do vídeo para verificar a taxa de frames e a consistência.

### Exemplo de Uso
Imagine que você precisa verificar se uma câmera grava a 30 frames por segundo com precisão. Você configuraria o script para alternar os LEDs a cada 33 milissegundos e gravaria os LEDs em ação com a câmera. Depois, utilizando um software de edição de vídeo, você pode sobrepor os tempos registrados no arquivo CSV com os frames capturados para assegurar que cada frame corresponde a uma alternância de LED.
