# Controle por Gestos para Paint e Ajuste de Volume

Este projeto utiliza visão computacional e reconhecimento de gestos de mão para controlar duas funcionalidades principais em uma máquina Windows:

**Abrir e Fechar o Paint:** Usando o gesto de um dedo, o programa abre o Microsoft Paint. Com o gesto de quatro dedos, ele fecha o Paint.
**Ajustar o Volume:** Usando o número de dedos levantados na mão direita, o sistema ajusta o volume do sistema, de 0% a 100%.

### O projeto faz uso das seguintes bibliotecas Python:

**OpenCV:** Para captura de vídeo e processamento de imagens.
**PyCaw:** Para controlar o áudio do sistema.
**cvzone:** Para o rastreamento das mãos e reconhecimento de gestos.
**psutil:** Para verificar se o Paint está rodando.

### Requisitos

**Python 3.x**

**OpenCV**

**PyCaw**

**cvzone**

**psutil**

**comtypes**

### Para instalar as bibliotecas necessárias, execute:

    pip install opencv-python pycaw cvzone psutil comtypes
  
## Funcionalidades

1. Gesto para Abrir o Paint
   
Quando o usuário levanta um dedo (por exemplo, o dedo indicador), o programa abre o Microsoft Paint, caso ele não esteja já aberto.

3. Gesto para Fechar o Paint
   
Quando o usuário levanta quatro dedos (por exemplo, todos os dedos exceto o polegar), o programa fecha o Microsoft Paint, caso ele esteja aberto.

4. Gesto para Controlar o Volume
   
Usando a mão direita:

- 0 dedos levantados: Volume no mínimo (0%).
  
- 1 dedo levantado: Volume em 20%.
  
- 2 dedos levantados: Volume em 40%.
 
- 3 dedos levantados: Volume em 60%.
  
- 4 dedos levantados: Volume em 80%.
  
- 5 dedos levantados: Volume em 100%.
  






