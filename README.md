# Sistema de Agendamento de Emails

Este é um sistema de agendamento de envio de emails em Python usando o Flask e o APScheduler. Ele permite adicionar emails, agendar o envio e enviar automaticamente os emails na data programada.

## Como usar

1. **Configuração do Gmail**:
   - Abra o arquivo `app.py` e substitua as informações de configuração do Gmail:
     - `MAIL_USERNAME`: seu endereço de email do Gmail.
     - `MAIL_PASSWORD`: sua senha do Gmail.
   - Certifique-se de que a autenticação de apps menos seguros esteja ativada na sua conta do Gmail.

2. **Adicione Emails**:
   - Envie uma solicitação POST para `/add-emails` com os emails que deseja agendar (separados por vírgula).
   - O sistema registrará a data e hora em que os emails foram adicionados.

3. **Agende o Envio**:
   - O sistema agendará automaticamente o envio dos emails para 7 dias após a data de recebimento.
   - Você pode ajustar o período de agendamento conforme necessário.

4. **Envio Automático**:
   - O sistema enviará os emails automaticamente na data programada.

## Executando o Aplicativo

1. Instale as dependências:
```
pip install flask flask-mail apscheduler

```

2. Execute o aplicativo:
```
python app.py

```

Não deixe de ler o arquivo LICENSE!😉
