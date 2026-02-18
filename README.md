# SNOOPER v3.0 "Rainy" 

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
         OSINT Query Builder v3.0 - Rainy Edition
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


## 📚 ESTRUTURA DE ARQUIVOS

```
snooper/
├── snooper.py          # Aplicação principal (990 linhas)
├── install.sh          # Instalador Unix/Linux/Mac
├── install.bat         # Instalador Windows
└── README.md           # Este arquivo
```

---


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
