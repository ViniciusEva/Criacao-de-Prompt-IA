# 🏥 Atendente Virtual - Clínica Saúde Integrada

Este projeto utiliza Inteligência Artificial (Google Gemini) para automatizar o acolhimento de pacientes, focando na identificação e extração da modalidade de consulta desejada. O sistema é capaz de interpretar linguagem natural e converter a intenção do usuário em dados estruturados (JSON).

---

## 🎭 Persona e Comportamento
A IA atua como uma atendente virtual empática, profissional e organizada. Ela foi treinada para:
* Tratar o paciente de forma personalizada.
* Explicar claramente as opções de atendimento.
* Mapear gírias e expressões comuns para termos técnicos (**Presencial** ou **Online**).

## 🎯 Objetivo do Fluxo
Identificar se o paciente deseja realizar a consulta via **Telemedicina** ou **Presencial**, garantindo que o dado extraído seja processável por um sistema de agendamento.

---

## 🛠️ Tecnologias
* **Linguagem:** Python
* **IA:** Google Gemini API (`gemini-2.0-flash`)
* **SDK:** `google-genai`

## 🚀 Como Configurar

1. **Instale a dependência necessária:**
   ```bash
   pip install google-genai
   ```
2. **Obtenha sua Chave de API:**
   Acesse o `Google AI` Studio e gere seu token.
3. **Acesse o Google AI Studio e gere seu token:**
   * Certifique-se de que o arquivo teste.md contenha as instruções de prompt (Persona, Regras e Contexto).
   * Insira seu token na variável token dentro do código Python.
4. **Execute o programa**

## ⚖️ Regras de Extração (Lógica de Negócio)

Para garantir a consistência dos dados salvos no banco de dados, a IA segue uma lógica rigorosa de mapeamento de intenções:

| Se o usuário disser... | Mapeamento para `dado_extraido` |
| :--- | :--- |
| "Quero ir aí", "No consultório", "Vou até a clínica" | `["Presencial"]` |
| "Por vídeo", "Pelo celular", "Remoto", "Chamada" | `["Online"]` |
| "Tanto faz", "O que tiver vago", "Qualquer um" | `["Presencial", "Online"]` |

### 🛠️ Critérios de Validação

* **Formato de Saída:** O campo `dado_extraido` deve ser obrigatoriamente um **array de strings** (Ex: `["Online"]`).
* **Fluxo de Conversa:** O campo `avancar` será definido como `true` somente se a modalidade for identificada com clareza.
* **JSON Estrito:** A resposta é gerada sem blocos de código (markdown) ou textos explicativos, garantindo a compatibilidade direta com `json.loads()`.

## 📤 Formato de Saída (JSON Estrito)
```Json
{
  "avancar": boolean,
  "dado_extraido": "string[] | null",
  "resposta_ia": "string"
}
```

## 📝 Exemplo de Uso
**Input (:>):** "Eu prefiro fazer por vídeo, é mais fácil."
Resposta do Sistema:
```bash
Type: <class 'dict'> Resp: {'avancar': True, 'dado_extraido': ['Online'], 'resposta_ia': 'Com certeza, [Nome]! Já registrei que sua preferência é para o atendimento Online (vídeo). Vamos escolher o melhor horário?'}
```
