# 🛠️ BOT DE MINERAÇÃO 
Este **bot automatiza a mineração de minério de cobre** na área **Lady's Sake**. 
---
## 🔄 Compatibilidade

Embora o bot seja configurado para **minério de cobre**, você pode adaptá-lo para **outros itens** no jogo:

1. Posicione a câmera de forma semelhante à referência.
2. Ajuste as coordenadas dos cliques conforme a localização do novo item.
3. Teste e refine os intervalos e delays, se necessário.

---

## 🖥️ Resolução da Tela

- ✅ **Resolução recomendada:** `1366x768`

> ⚠️ Caso sua resolução **não seja** 1366x768:
> - Você precisará **ajustar manualmente as coordenadas (X, Y)** usadas pelo mouse.
> - Veja em "Configuração do Código" quais partes precisam ser alteradas para funcionar corretamente.

---

## 📸 Configuração da Câmera

> 🔍 **Referência visual obrigatória:**  
📷 [Visualizar referência de câmera](https://snipboard.io/MDrkic.jpg)

- Garanta que sua câmera esteja exatamente como na imagem acima antes de iniciar o bot.

---

## 🖥️ Tecnologias Utilizadas

- pyautogui – para automação de cliques e movimentos do mouse.

- tqdm – para barra de progresso visual durante as fases de mineração.

```shell
pip install pyautogui tqdm
```

## ⚙️ Configuração do Código

1. Ative a opção *"Easy Camera"* nas configurações do jogo.
2. Vá até o mapa **Lady’s Lake** e posicione o nome de seu jogador sobre o centro do minerio (como mostra o print acima).
3. Afaste a câmera até ao máximo para garantir o mesmo enquadramento.
4. Para descobrir as coordenadas da tela, execute o seguinte código:

```python
import pyautogui
import time

time.sleep(3)
print(pyautogui.position())  # Durante os 3 segundos, mova o mouse até o ponto desejado.
```

> 🧭 As coordenadas X e Y exibidas no terminal devem ser copiadas e coladas nas funções do bot, conforme abaixo.

---

### ✍️ Como preencher os pontos no código

Após identificar as coordenadas:

- **`mouse_position(x=, y=)`**  
  👉 Coloque aqui a posição onde está o **próximo minério** (onde o mouse irá se posicionar).

- **`item(x=, y=, fase='1ª Fase')`**  
  👉 Coloque aqui as coordenadas do **minério que será minerado**, que está colado após `mouse_position`.

- **`troca_ferramenta(x=, y=)`**  
  👉 Coloque aqui a posição onde estará a **nova ferramenta no inventário** (use preferencialmente o **3º slot**).

---

> ⚠️ **Dica importante:**  
Se você tiver **várias ferramentas no inventário**, alterne entre elas nas fases.  
**Evite usar sempre a mesma picareta** para aumentar a durabilidade total durante a mineração automatizada.



## 📂 Futuro do projeto (Visão Computacional)

Planejamos uma evolução do projeto com Visão Computacional, incluindo:

- **OpenCV** – Para capturar e interpretar o conteúdo da tela do jogo.

- **YOLO** – Para identificar minérios automaticamente em tempo real.

Essas tecnologias permitirão ao bot reconhecer objetos na tela, identificar minérios sozinho e mover ao tempo real




## 🤝 Aviso Legal

**Este bot foi criado exclusivamente para fins educacionais e acadêmicos.**


Ele não deve ser utilizado para:

> Prejudicar a experiência de outros jogadores.

> Obter vantagens desleais.

> Impactar servidores ou violar termos de uso do jogo.

⚠️ Use com responsabilidade e ética.


## 📄 Relatório de Uso de Inteligência Artificial

Este projeto utilizou A.I. como apoio técnico em alguns pontos.  
Para saber mais sobre o que foi feito com A.I., veja o relatório completo abaixo:

👉 [Ver Relatório (PDF)](documentacao/Relatorio_AI_projeto_bot.pdf)


⚠️⚠️⚠️ Código e bot em construção...