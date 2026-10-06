# Network Inspector

Ferramenta desenvolvida em Python para estudar conceitos de redes, reconhecimento e fundamentos de Pentest.

O **Network Inspector** nasceu como um projeto de estudo para transformar conceitos de redes em código Python, explorando conexões TCP, identificação básica de serviços, HTTP e ICMP.

> Projeto educacional desenvolvido durante meus estudos de Python, Redes e Cybersecurity/Pentest.

---

## 🎯 Objetivo

O objetivo principal do projeto é aprender, na prática, como funcionam alguns dos mecanismos utilizados durante o reconhecimento de redes.

Em vez de apenas utilizar ferramentas prontas, o projeto busca implementar algumas funcionalidades utilizando bibliotecas nativas do Python, principalmente o módulo `socket`.

---

## ⚙️ Funcionalidades atuais

Atualmente o Network Inspector possui funcionalidades para:

* Verificar portas TCP;
* Identificar portas como:

  * `OPEN`
  * `CLOSED`
  * `TIME OUT`
* Medir o tempo aproximado de resposta de uma conexão;
* Realizar requisições HTTP;
* Identificar informações básicas do servidor HTTP através do header `Server`;
* Trabalhar com conexões TCP utilizando sockets;
* Realizar testes básicos utilizando ICMP;
* Exibir informações básicas sobre serviços encontrados.

---

## 🧠 Conceitos estudados

Durante o desenvolvimento do projeto foram estudados conceitos como:

* Python `socket`;
* TCP;
* UDP;
* TCP 3-Way Handshake;
* Portas e serviços;
* DNS;
* HTTP;
* Headers HTTP;
* ICMP;
* Timeout;
* `LISTENING`;
* Conexões TCP;
* Banner/Service Detection;
* Latência;
* Comunicação cliente/servidor.

---

## 🛠️ Tecnologias

* Python 3
* `socket`
* `os`
* `struct`
* `time`

O projeto utiliza principalmente bibliotecas padrão do Python.

---

## 🚀 Como executar

Clone o repositório:

```bash
git clone https://github.com/gbrn1/network-inspector.git
```

Entre no diretório:

```bash
cd network-inspector
```

Execute:

```bash
python network_inspector.py"
```

No Windows também pode ser utilizado:

```powershell
py .\network_inspector.py
```

---

## 🧪 Exemplo

O projeto pode ser utilizado para verificar algumas portas de um determinado host.

Exemplo de portas utilizadas durante os testes:

```text
21
22
23
25
53
80
110
139
443
445
3306
3389
8080
8000
```

Um resultado pode apresentar informações semelhantes a:

```text
Port 445: OPEN
Port 8080: CLOSED
Port 8000: OPEN
```

Quando um serviço HTTP é encontrado, o projeto também pode tentar identificar informações através da resposta HTTP.

Exemplo:

```text
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.13.5
```

---

## 🌐 Testes com HTTP

Uma das etapas do projeto foi implementar uma comunicação HTTP diretamente utilizando sockets.

O projeto envia uma requisição semelhante a:

```http
GET / HTTP/1.1
Host: localhost
Connection: close
```

Depois, a resposta é analisada para obter informações dos headers HTTP.

Isso permitiu estudar na prática a relação entre:

```text
Cliente
   ↓
TCP Connection
   ↓
HTTP Request
   ↓
HTTP Response
   ↓
Headers
   ↓
Server Information
```

---

## 📡 Testes com ICMP

O projeto também possui estudos relacionados ao protocolo ICMP.

Foi utilizado um socket raw para construir e enviar pacotes ICMP, permitindo compreender melhor o funcionamento de ferramentas como `ping`.

Conceitos estudados nessa etapa:

* ICMP Echo Request;
* ICMP Echo Reply;
* Type;
* Code;
* Checksum;
* Packet ID;
* Latência;
* `SOCK_RAW`;
* `IPPROTO_ICMP`.

Essa parte foi desenvolvida principalmente com objetivo educacional, para entender o que acontece por baixo de uma ferramenta de diagnóstico de rede.

---

## 🔐 Relação com Pentest

O Network Inspector faz parte da minha jornada de estudos em **Cybersecurity e Pentest**.

A ideia do projeto não é substituir ferramentas profissionais como Nmap, mas entender alguns dos conceitos que essas ferramentas utilizam.

Durante o desenvolvimento, o foco foi sair de:

```text
"Eu sei usar a ferramenta"
```

para:

```text
"Eu entendo o conceito por trás da ferramenta"
```

Esse projeto representa uma etapa do meu aprendizado em Python, redes e reconhecimento.

---

## 📚 Por que desenvolvi esta ferramenta?

Uma das minhas metas de estudo é evoluir em Python e, ao mesmo tempo, aprofundar meus conhecimentos em redes e Pentest.

Desenvolver ferramentas simples do zero ajuda a entender conceitos que podem passar despercebidos quando utilizamos somente ferramentas prontas.

O Network Inspector foi criado justamente com essa finalidade.

---

## ⚠️ Aviso

Este projeto foi desenvolvido para fins **educacionais e de estudo**.

Utilize a ferramenta somente em:

* seus próprios equipamentos;
* laboratórios;
* ambientes de CTF;
* sistemas onde você possui autorização explícita para realizar testes.

Não utilize a ferramenta contra sistemas de terceiros sem autorização.

---

## 🔮 Próximos passos

O projeto ainda está em desenvolvimento.

Algumas ideias para versões futuras:

* melhorar a identificação de serviços;
* melhorar o tratamento de erros;
* organizar melhor a saída;
* adicionar argumentos pela linha de comando;
* melhorar a identificação HTTP;
* adicionar mais protocolos;
* adicionar logging;
* melhorar a estrutura do código;
* criar uma versão `2.0`.

---

## 📌 Status

**Em desenvolvimento / Projeto de estudos**

Este projeto representa uma etapa prática da minha evolução em:

```text
Python
   ↓
Redes
   ↓
Linux
   ↓
Cybersecurity
   ↓
Pentest
```

---

## 👨‍💻 Autor

**gbrn1**

Projeto desenvolvido como parte dos meus estudos de Python, Redes e Cybersecurity.
