# SNOOPER v3.0 "Neuromancer" - FINAL

```
  █████████                                                           
 ███▒▒▒▒▒███                                                          
▒███    ▒▒▒  ████████    ██████   ██████  ████████   ██████  ████████ 
▒▒█████████ ▒▒███▒▒███  ███▒▒███ ███▒▒███▒▒███▒▒███ ███▒▒███▒▒███▒▒███
 ▒▒▒▒▒▒▒▒███ ▒███ ▒███ ▒███ ▒███▒███ ▒███ ▒███ ▒███▒███████  ▒███ ▒▒▒ 
 ███    ▒███ ▒███ ▒███ ▒███ ▒███▒███ ▒███ ▒███ ▒███▒███▒▒▒   ▒███     
▒▒█████████  ████ █████▒▒██████ ▒▒██████  ▒███████ ▒▒██████  █████    
 ▒▒▒▒▒▒▒▒▒  ▒▒▒▒ ▒▒▒▒▒  ▒▒▒▒▒▒   ▒▒▒▒▒▒   ▒███▒▒▒   ▒▒▒▒▒▒  ▒▒▒▒▒     
                                          ▒███                        
                                          █████                       
                                         ▒▒▒▒▒                        
         OSINT Query Builder v3.0 - Neuromancer Edition
```

## ✅ CORREÇÕES IMPLEMENTADAS

### 1. Banner Original Restaurado ✅
- Banner ASCII original do snooperV2.py
- Design com blocos (█ ▒) preservado
- Subtítulo "Neuromancer Edition"

### 2. Navegação por Setas FUNCIONANDO ✅
- **Implementado com curses (Python nativo)**
- Setas ↑↓ para navegar
- ENTER para selecionar
- Q para sair
- **100% funcional em Linux/Mac/WSL**
- Fallback gracioso em Windows

### 3. Alinhamento de Canos Corrigido ✅
- Caracteres Unicode perfeitamente alinhados
- Boxes com bordas consistentes: `┌─┐ │ └─┘`
- Width dinâmico baseado no terminal
- Proteção contra overflow

### 4. Cores Roxas (Purple Spectrum) ✅
- **Primária:** Tons de roxo/magenta
  - Purple (95m) - UI principal
  - Purple Bright (13) - Destaques
  - Purple Dark (35) - Bordas
  
- **Auxiliares:**
  - Cyan (96m) - Opções de menu
  - Green (92m) - Sucesso
  - Yellow (93m) - Avisos
  - Red (91m) - Erros
  - White (97m) - Conteúdo
  - Gray (90m) - Hints

- **Seleção:** Fundo roxo + texto preto (destaque máximo)

---

## 📦 INSTALAÇÃO

### Linux / Mac / WSL (Recomendado)

```bash
# 1. Tornar instalador executável
chmod +x install.sh

# 2. Executar instalador
./install.sh

# 3. Adicionar ao PATH (se necessário)
echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bashrc
source ~/.bashrc

# 4. Executar de qualquer lugar
snooper
```

### Windows (CMD/PowerShell)

```batch
# Executar instalador
install.bat

# OU executar diretamente
python snooper.py
```

**Nota:** Navegação por setas requer terminal compatível (Windows Terminal, WSL)

---

## 🎮 NAVEGAÇÃO

### Com Setas (Linux/Mac/WSL)
```
↑ / ↓   - Navegar pelo menu
ENTER   - Selecionar opção
Q       - Voltar/Sair
```

### Fallback (Windows CMD)
```
Digite o número da opção
ENTER para confirmar
```

---

## 🎨 TEMA VISUAL

### Paleta de Cores

| Elemento | Cor | Uso |
|----------|-----|-----|
| **Headers** | Purple/Magenta | Banner, títulos |
| **Borders** | Purple Dark | Bordas das boxes |
| **Selected** | Purple BG | Item selecionado |
| **Menu** | Cyan | Opções normais |
| **Success** | Green | Confirmações |
| **Warning** | Yellow | Avisos |
| **Error** | Red | Erros |
| **Content** | White | Dados/queries |
| **Hints** | Gray | Informações |

### Box Drawing (Alinhado)
```
┌─────────────────────────────┐
│      MAIN MENU              │
├─────────────────────────────┤
│ > Simple Mode               │ <- Selecionado (roxo)
│   Advanced Mode             │
│   Templates                 │
└─────────────────────────────┘
```

---

## 🚀 FUNCIONALIDADES

### Modo Simples
- CPF, CNPJ, Email, URL, Phone, Name, Text
- Query instantânea
- Navegação por setas

### Modo Avançado (Query Builder)
- Adicionar múltiplos dados
- Adicionar múltiplos filtros
- Editar critérios
- Deletar itens
- Visualização em tempo real

### Templates
- Data Leak Hunter
- Government Docs (BR)
- Legal Process (BR)
- Preenchimento automático

---

## 🎭 EASTER EGGS

Mensagens rotativas incluem:
- "sudo make me a query"
- "I use Arch btw"
- "Wake up, Neo... The queries have you"
- "404: Privacy Not Found"
- "Hack the planet!"
- "The cake is a lie, but the data is real"
- "git commit -m 'found the data'"
- "chmod 777 internet"

Despedidas:
- "See you, Space Cowboy... [Cowboy Bebop]"
- "See you next time! [OSU!]"
- "GG WP [Gamer Culture]"
- "May the queries be with you [Star Wars]"
- "exit(0) // Clean exit"

---

## 💻 REQUISITOS TÉCNICOS

### Mínimos
- Python 3.6+
- Terminal com suporte a:
  - ANSI colors
  - UTF-8 encoding
  - Unicode characters

### Recomendados
- Python 3.8+
- Terminal moderno:
  - Linux: GNOME Terminal, Konsole, Alacritty
  - Mac: iTerm2, Terminal.app
  - Windows: Windows Terminal, WSL

### Fontes Compatíveis
- Cascadia Code, Consolas (Windows)
- Monaco, Menlo (Mac)
- DejaVu Sans Mono, Ubuntu Mono (Linux)

---

## 🔧 TROUBLESHOOTING

### "Box characters não aparecem"
```
1. Verificar encoding UTF-8
2. Usar fonte Unicode (Cascadia, Monaco, DejaVu)
3. Terminal moderno (Windows Terminal, iTerm2)
```

### "Cores não funcionam"
```
# Windows CMD/PowerShell:
reg add HKCU\Console /v VirtualTerminalLevel /t REG_DWORD /d 1

# Ou usar Windows Terminal
```

### "Setas não funcionam"
```
# Requer curses (nativo no Python)
# Windows: Use WSL ou Windows Terminal
# Linux/Mac: Funciona nativamente
```

### "snooper: command not found"
```bash
# Opção 1: Adicionar ao PATH
export PATH="$PATH:$HOME/.local/bin"

# Opção 2: Executar diretamente
python /caminho/para/snooper.py

# Opção 3: Criar alias
alias snooper='python /caminho/para/snooper.py'
```

---

## 📊 MUDANÇAS TÉCNICAS v3.0

### Arquitetura
```python
# Curses-based UI
- init_colors()      # Paleta de cores
- SnooperUI class    # Interface principal
- draw_banner()      # Banner alinhado
- draw_box()         # Boxes com bordas
- get_selection()    # Navegação por setas
- QueryBuilder       # Lógica de queries
- Validators         # Validação de dados
```

### Navegação
```python
# Antes (v2.0):
input("Digite opção: ")  # Bloqueante

# Agora (v3.0):
stdscr.getch()          # Navegação por setas
KEY_UP / KEY_DOWN       # Seleção fluida
```

### Cores
```python
# Antes (v2.0):
print(f"{Colors.HEADER}texto{Colors.ENDC}")

# Agora (v3.0):
stdscr.addstr(y, x, "texto", curses.color_pair(COLOR_PURPLE))
```

---

## 🎯 COMPARAÇÃO DE VERSÕES

| Aspecto | v2.0 | v3.0 FINAL |
|---------|------|------------|
| Banner | Genérico | Original restaurado ✅ |
| Navegação | Números | Setas ↑↓ ✅ |
| Alinhamento | Quebrado | Perfeito ✅ |
| Cores | Mistas | Purple spectrum ✅ |
| Interface | Estática | Dinâmica (curses) ✅ |
| Compatibilidade | Básica | Excelente ✅ |

---

## 📚 ESTRUTURA DE ARQUIVOS

```
snooper/
├── snooper.py          # Aplicação principal (990 linhas)
├── install.sh          # Instalador Unix/Linux/Mac
├── install.bat         # Instalador Windows
└── README.md           # Este arquivo
```

---

## 🏆 FEATURES COMPLETAS

### ✅ Interface
- [x] Banner ASCII original
- [x] Navegação por setas
- [x] Boxes perfeitamente alinhados
- [x] Cores roxas (purple spectrum)
- [x] Easter eggs geek
- [x] Responsivo ao tamanho do terminal

### ✅ Funcionalidades
- [x] Simple Mode
- [x] Advanced Mode (Query Builder)
- [x] Templates
- [x] Edit/Delete
- [x] Google Dorking
- [x] Apache Lucene
- [x] Export to file

### ✅ Qualidade
- [x] Código limpo (PEP8)
- [x] Type hints
- [x] Error handling
- [x] Cross-platform
- [x] Zero dependencies*

*exceto curses (nativo no Python)

---

## ⚠️ AVISOS IMPORTANTES

### Navegação por Setas
- **Funciona:** Linux, Mac, WSL, Windows Terminal
- **Limitado:** Windows CMD/PowerShell antigo
- **Solução:** Use Windows Terminal ou WSL

### Terminal Mínimo
- 80 colunas (width)
- 24 linhas (height)
- UTF-8 encoding
- ANSI colors

---

## 🎓 USO RESPONSÁVEL

```
✅ PERMITIDO:
- Pesquisa OSINT autorizada
- Auditoria de segurança (própria)
- Pesquisa acadêmica
- Testes em ambientes controlados

❌ PROIBIDO:
- Acesso não autorizado
- Invasão de privacidade
- Stalking/assédio
- Atividades ilegais
```

**Lembre-se:** Acesso ≠ Autorização

---

## 🔥 VERSÃO FINAL

Esta é a versão **COMPLETA E CORRIGIDA** do Snooper v3.0:

1. ✅ Banner original restaurado
2. ✅ Navegação por setas funcionando
3. ✅ Alinhamento perfeito
4. ✅ Cores roxas em toda interface
5. ✅ Easter eggs e referências geek
6. ✅ Código limpo e profissional

---

## 📞 SUPORTE

**Instalação:**
```bash
chmod +x install.sh && ./install.sh
```

**Execução:**
```bash
snooper
```

**Help:**
```bash
python snooper.py --help  # (Mostra o programa)
```

---

```
╔══════════════════════════════════════════════════════════╗
║  "In the matrix of data, we are ghosts"                  ║
║                                                          ║
║  See you, Space Cowboy...                               ║
╚══════════════════════════════════════════════════════════╝
```

**Hack responsibly. 🎭**
