# Mapa para a validação do prompt_v2

Lista de trabalho da sessão de validação (reconstrução cega). Gerado em 2026-11-13 a partir dos arquivos em disco.
Caminhos relativos a `ENTREGA01/task02_entradas/regras_explicadas/`. Prompt: `prompt_v2.md`, sha256 `d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73` em todos.

**Atenção para a sessão cega:** ao lado de cada `entrada_{id}.md` está o `regra_{id}.gobr` original (gabarito). Ler só o `entrada_{id}.md`.

Faixa: a do catálogo do `config.py` quando existe. Para modelos que o catálogo deixa fora das três faixas, a faixa é derivada do preço de saída por milhão de tokens: até US$ 2,50 mais barato, até US$ 5,00 intermediário, acima melhor. Marcada como "derivada do preço".

| Modelo | Fornecedor | Faixa | regra_020 | regra_228 | regra_032 | Temperatura usada |
|---|---|---|---|---|---|---|
| `gpt-6-luna` | openai | mais barato | `20261113-180708_gpt-6-luna_v2/regra_020/entrada_020.md` | `20261113-180708_gpt-6-luna_v2/regra_228/entrada_228.md` | `20261113-180708_gpt-6-luna_v2/regra_032/entrada_032.md` | 1 (imposta pelo modelo; recusa outro valor) |
| `gpt-6.1-terra` | openai | intermediário | `20261113-180708_gpt-6.1-terra_v2/regra_020/entrada_020.md` | `20261113-180708_gpt-6.1-terra_v2/regra_228/entrada_228.md` | `20261113-180708_gpt-6.1-terra_v2/regra_032/entrada_032.md` | 1 (imposta pelo modelo; recusa outro valor) |
| `gpt-6-astra` | openai | melhor | `20261113-183339_gpt-6-astra_v2/regra_020/entrada_020.md` | `20261113-183339_gpt-6-astra_v2/regra_228/entrada_228.md` | `20261113-183339_gpt-6-astra_v2/regra_032/entrada_032.md` | 1 (imposta pelo modelo; recusa outro valor) |
| `gpt-4.1-mini-2025-04-14` | openai | mais barato (derivada do preço) | `20261113-180708_gpt-4.1-mini-2025-04-14_v2/regra_020/entrada_020.md` | `20261113-180708_gpt-4.1-mini-2025-04-14_v2/regra_228/entrada_228.md` | `20261113-180708_gpt-4.1-mini-2025-04-14_v2/regra_032/entrada_032.md` | 1 (padrão; o script não envia temperatura à OpenAI, mas o modelo aceitaria 0.0 a 2.0) |
| `gpt-4o-mini-2024-07-18` | openai | mais barato (derivada do preço) | `20261113-180708_gpt-4o-mini-2024-07-18_v2/regra_020/entrada_020.md` | `20261113-180708_gpt-4o-mini-2024-07-18_v2/regra_228/entrada_228.md` | `20261113-180708_gpt-4o-mini-2024-07-18_v2/regra_032/entrada_032.md` | 1 (padrão; o script não envia temperatura à OpenAI, mas o modelo aceitaria 0.0 a 2.0) |
| `gpt-5-mini-2025-08-07` | openai | mais barato (derivada do preço) | `20261113-180708_gpt-5-mini-2025-08-07_v2/regra_020/entrada_020.md` | `20261113-180708_gpt-5-mini-2025-08-07_v2/regra_228/entrada_228.md` | `20261113-180708_gpt-5-mini-2025-08-07_v2/regra_032/entrada_032.md` | 1 (imposta pelo modelo; recusa outro valor) |
| `gpt-5.4-mini-2026-03-17` | openai | intermediário (derivada do preço) | `20261113-180708_gpt-5.4-mini-2026-03-17_v2/regra_020/entrada_020.md` | `20261113-180708_gpt-5.4-mini-2026-03-17_v2/regra_228/entrada_228.md` | `20261113-180708_gpt-5.4-mini-2026-03-17_v2/regra_032/entrada_032.md` | 1 (padrão; o script não envia temperatura à OpenAI, mas o modelo aceitaria 0.0 a 2.0) |
| `gemini-3.1-flash-lite` | gemini | mais barato | `20261113-183339_gemini-3.1-flash-lite_v2/regra_020/entrada_020.md` | `20261113-183339_gemini-3.1-flash-lite_v2/regra_228/entrada_228.md` | `20261113-183339_gemini-3.1-flash-lite_v2/regra_032/entrada_032.md` | 0.3 (escolhida no config; o modelo aceita 0.0 a 2.0) |
| `gemini-3.5-flash-lite` | gemini | mais barato (derivada do preço) | `20261113-180708_gemini-3.5-flash-lite_v2/regra_020/entrada_020.md` | `20261113-180708_gemini-3.5-flash-lite_v2/regra_228/entrada_228.md` | `20261113-180708_gemini-3.5-flash-lite_v2/regra_032/entrada_032.md` | 0.3 (escolhida no config; o modelo aceita 0.0 a 2.0) |
| `gemini-3.6-flash` | gemini | intermediário | `20261113-180708_gemini-3.6-flash_v2/regra_020/entrada_020.md` | `20261113-180708_gemini-3.6-flash_v2/regra_228/entrada_228.md` | `20261113-180708_gemini-3.6-flash_v2/regra_032/entrada_032.md` | 0.3 (escolhida no config; o modelo aceita 0.0 a 2.0) |
| `gemini-3.8-flash` | gemini | intermediário (derivada do preço) | `20261113-183339_gemini-3.8-flash_v2/regra_020/entrada_020.md` | `20261113-183339_gemini-3.8-flash_v2/regra_228/entrada_228.md` | `20261113-183339_gemini-3.8-flash_v2/regra_032/entrada_032.md` | 0.3 (escolhida no config; o modelo aceita 0.0 a 2.0) |
| `gemini-4-carbon` | gemini | melhor | `20261113-183339_gemini-4-carbon_v2/regra_020/entrada_020.md` | `20261113-183339_gemini-4-carbon_v2/regra_228/entrada_228.md` | `20261113-183339_gemini-4-carbon_v2/regra_032/entrada_032.md` | 0.3 (escolhida no config; o modelo aceita 0.0 a 2.0) |

**Integridade:** 12 modelos na validação, 12 responderam nas três regras, 36 descrições para validar (12 × 3).

## Descartados

- `gpt-4.1-mini`, `gpt-4o-mini`, `gpt-5-mini`, `gpt-5.4-mini`: apelidos sem data; podem mudar de instantâneo, e a D9 exige proveniência recriável. Valem os gêmeos datados. As descrições geradas ficam em `20261113-180708_{apelido}_v2/`, fora da validação.
- `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-2.5-pro`: a geração devolve `404 NOT_FOUND`, "This model ... is no longer available to new users". Nenhuma descrição gerada.
- `gemini-2.5-flash-image`: modelo de imagem usado para texto; se devolver imagem, o custo calculado fica subestimado, e ele não representa a família 2.5. As descrições geradas ficam em `20261113-180708_gemini-2.5-flash-image_v2/`, fora da validação.
- `gpt-4o-mini-transcribe`, `gpt-4o-mini-tts` e seus 4 instantâneos datados: não são modelos de chat (`404`, "This is not a chat model"); nunca chamados pelo script.
- `gemini-3.1-pro-preview`: ausente da listagem da conta; a chamada de teste devolve `404 NOT_FOUND`.
- `gpt-6.1-sol`: modelo de chat disponível, mas a faixa "melhor" da OpenAI já tem representante testado (`gpt-6-astra`). Não chamado.
