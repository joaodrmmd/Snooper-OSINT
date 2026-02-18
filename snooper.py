#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SNOOPER - OSINT Query Builder Pro
Google Dorking & Apache Lucene formatter with arrow navigation
Version: 3.0 "Rainy"
"""

import re
import sys
import os
from typing import List, Dict, Optional
from datetime import datetime
import curses
from curses import wrapper


# ============================================================================
# COLORS - Purple spectrum theme
# ============================================================================
class Colors:
    """Terminal colors - Purple-focused palette"""
    # Purple spectrum (primary)
    PURPLE = '\033[95m'
    PURPLE_DARK = '\033[35m'
    PURPLE_LIGHT = '\033[1;35m'
    
    # Auxiliaries
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    
    # Formatting
    BOLD = '\033[1m'
    RESET = '\033[0m'


# ============================================================================
# CURSES COLOR PAIRS
# ============================================================================
def init_colors():
    """Initialize curses color pairs"""
    curses.start_color()
    curses.use_default_colors()
    
    # Purple spectrum (primary)
    curses.init_pair(1, curses.COLOR_MAGENTA, -1)  # Purple
    curses.init_pair(2, 13, -1)  # Bright purple
    curses.init_pair(3, 5, -1)   # Dark purple
    
    # Auxiliaries
    curses.init_pair(4, curses.COLOR_CYAN, -1)     # Cyan
    curses.init_pair(5, curses.COLOR_GREEN, -1)    # Green
    curses.init_pair(6, curses.COLOR_YELLOW, -1)   # Yellow
    curses.init_pair(7, curses.COLOR_RED, -1)      # Red
    curses.init_pair(8, curses.COLOR_WHITE, -1)    # White
    curses.init_pair(9, 8, -1)                     # Gray
    
    # Selected item (purple on white)
    curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_MAGENTA)


COLOR_PURPLE = 1
COLOR_PURPLE_BRIGHT = 2
COLOR_PURPLE_DARK = 3
COLOR_CYAN = 4
COLOR_GREEN = 5
COLOR_YELLOW = 6
COLOR_RED = 7
COLOR_WHITE = 8
COLOR_GRAY = 9
COLOR_SELECTED = 10


# ============================================================================
# ASCII ART & EASTER EGGS
# ============================================================================
BANNER = """  █████████                                                           
 ███▒▒▒▒▒███                                                          
▒███    ▒▒▒  ████████    ██████   ██████  ████████   ██████  ████████ 
▒▒█████████ ▒▒███▒▒███  ███▒▒███ ███▒▒███▒▒███▒▒███ ███▒▒███▒▒███▒▒███
 ▒▒▒▒▒▒▒▒███ ▒███ ▒███ ▒███ ▒███▒███ ▒███ ▒███ ▒███▒███████  ▒███ ▒▒▒ 
 ███    ▒███ ▒███ ▒███ ▒███ ▒███▒███ ▒███ ▒███ ▒███▒███▒▒▒   ▒███     
▒▒█████████  ████ █████▒▒██████ ▒▒██████  ▒███████ ▒▒██████  █████    
 ▒▒▒▒▒▒▒▒▒  ▒▒▒▒ ▒▒▒▒▒  ▒▒▒▒▒▒   ▒▒▒▒▒▒   ▒███▒▒▒   ▒▒▒▒▒▒  ▒▒▒▒▒     
                                          ▒███                        
                                          █████                       
                                         ▒▒▒▒▒                        """

SUBTITLE = "         OSINT Query Builder v3.0 - Rainy Edition"

EASTER_EGGS = [
    "sudo make me a query",
    "hur dur I uSe ArCh BtW hur dur",
    "There is no spoon, only data",
    "Wake up, Neo... The queries have you",
    "404: Privacy Not Found",
    "Hack the planet!",
    "The cake is a lie, but the data is real",
    "git commit -m 'found the data'",
    "chmod 777 internet",
    "query sequissíma filho",
    "SELECT * FROM secrets WHERE hidden=true",
]

GOODBYES = [
    "See you, Space Cowboy...",
    "See you next time!",
    "GG WP",
    "May the queries be with you",
    "So long, and thanks for all the data",
    "exit(0) // Clean exit",
    "Connection terminated.",
]


# ============================================================================
# QUERY BUILDER
# ============================================================================
class QueryBuilder:
    """Core query construction logic"""
    
    def __init__(self):
        self.criteria: List[Dict] = []
        self.filters: Dict[str, List[str]] = {}
    
    def add_data(self, data_type: str, value: str):
        """Add data criterion"""
        self.criteria.append({'type': data_type, 'value': value})
    
    def add_filter(self, filter_type: str, value: str):
        """Add filter criterion"""
        if filter_type not in self.filters:
            self.filters[filter_type] = []
        self.filters[filter_type].append(value)
    
    def remove_data(self, index: int) -> bool:
        """Remove data by index"""
        if 0 <= index < len(self.criteria):
            self.criteria.pop(index)
            return True
        return False
    
    def remove_filter_by_index(self, index: int) -> bool:
        """Remove filter by flat index"""
        flat_filters = []
        for ftype, values in self.filters.items():
            for val in values:
                flat_filters.append((ftype, val))
        
        if 0 <= index < len(flat_filters):
            ftype, val = flat_filters[index]
            self.filters[ftype].remove(val)
            if not self.filters[ftype]:
                del self.filters[ftype]
            return True
        return False
    
    def clear(self):
        """Clear all criteria"""
        self.criteria = []
        self.filters = {}
    
    def build_google_query(self) -> str:
        """Build Google Dorking query"""
        parts = []
        
        for criterion in self.criteria:
            dtype = criterion['type']
            value = criterion['value']
            
            if dtype in ['cpf', 'cnpj', 'phone']:
                clean = re.sub(r'\D', '', value)
                parts.append(f'"{clean}"')
            else:
                parts.append(f'"{value}"')
        
        query = ' AND '.join(parts) if parts else ''
        filter_parts = []
        
        if 'site' in self.filters:
            sites = self.filters['site']
            if len(sites) == 1:
                filter_parts.append(f'site:{sites[0]}')
            else:
                filter_parts.append(f"({' OR '.join([f'site:{s}' for s in sites])})")
        
        if 'filetype' in self.filters:
            ftypes = self.filters['filetype']
            if len(ftypes) == 1:
                filter_parts.append(f'filetype:{ftypes[0]}')
            else:
                filter_parts.append(f"({' OR '.join([f'filetype:{f}' for f in ftypes])})")
        
        for ftype in ['inurl', 'intitle', 'intext']:
            if ftype in self.filters:
                for val in self.filters[ftype]:
                    filter_parts.append(f'{ftype}:{val}')
        
        if 'after' in self.filters:
            filter_parts.append(f"after:{self.filters['after'][0]}")
        if 'before' in self.filters:
            filter_parts.append(f"before:{self.filters['before'][0]}")
        if 'exclude_site' in self.filters:
            for site in self.filters['exclude_site']:
                filter_parts.append(f'-site:{site}')
        if 'exclude_term' in self.filters:
            for term in self.filters['exclude_term']:
                filter_parts.append(f'-{term}')
        
        if filter_parts:
            query = f"{query} {' '.join(filter_parts)}" if query else ' '.join(filter_parts)
        
        return query
    
    def build_lucene_query(self) -> str:
        """Build Apache Lucene query"""
        parts = []
        
        for criterion in self.criteria:
            dtype = criterion['type']
            value = criterion['value']
            
            if dtype == 'cpf':
                clean = re.sub(r'\D', '', value)
                parts.append(f'cpf:"{clean}"')
            elif dtype == 'cnpj':
                clean = re.sub(r'\D', '', value)
                parts.append(f'cnpj:"{clean}"')
            elif dtype == 'email':
                parts.append(f'email:"{value}"')
            elif dtype == 'phone':
                clean = re.sub(r'\D', '', value)
                parts.append(f'telefone:"{clean}"')
            elif dtype == 'name':
                parts.append(f'nome:"{value}"')
            else:
                parts.append(f'"{value}"')
        
        query = ' AND '.join(parts) if parts else ''
        filter_parts = []
        
        if 'filetype' in self.filters:
            ftypes = self.filters['filetype']
            if len(ftypes) == 1:
                filter_parts.append(f'tipo_arquivo:{ftypes[0]}')
            else:
                filter_parts.append(f"tipo_arquivo:({' OR '.join(ftypes)})")
        
        if 'site' in self.filters:
            sites = self.filters['site']
            if len(sites) == 1:
                filter_parts.append(f'dominio:"{sites[0]}"')
            else:
                filter_parts.append(f"dominio:({' OR '.join([f'\"{s}\"' for s in sites])})")
        
        if 'after' in self.filters or 'before' in self.filters:
            after = self.filters.get('after', ['*'])[0].replace('-', '') if 'after' in self.filters else '*'
            before = self.filters.get('before', ['*'])[0].replace('-', '') if 'before' in self.filters else '*'
            filter_parts.append(f'data:[{after} TO {before}]')
        
        if filter_parts:
            query = f"{query} AND {' AND '.join(filter_parts)}" if query else ' AND '.join(filter_parts)
        
        return query


# ============================================================================
# VALIDATORS
# ============================================================================
class Validators:
    """Data validation"""
    
    @staticmethod
    def cpf(cpf: str) -> bool:
        clean = re.sub(r'\D', '', cpf)
        return len(clean) == 11 and clean != clean[0] * 11
    
    @staticmethod
    def cnpj(cnpj: str) -> bool:
        clean = re.sub(r'\D', '', cnpj)
        return len(clean) == 14 and clean != clean[0] * 14
    
    @staticmethod
    def email(email: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def url(url: str) -> bool:
        pattern = r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$'
        return bool(re.match(pattern, url))


# ============================================================================
# CURSES UI
# ============================================================================
class SnooperUI:
    """Curses-based UI with arrow navigation"""
    
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.qb = QueryBuilder()
        curses.curs_set(0)  # Hide cursor
        init_colors()
        
        import random
        self.easter_egg = random.choice(EASTER_EGGS)
    
    def draw_banner(self):
        """Draw banner"""
        lines = BANNER.split('\n')
        y = 0
        for line in lines:
            if y < curses.LINES - 1:
                try:
                    self.stdscr.addstr(y, 0, line[:curses.COLS-1], 
                                     curses.color_pair(COLOR_PURPLE) | curses.A_BOLD)
                except:
                    pass
                y += 1
        
        # Add subtitle
        if y < curses.LINES - 1:
            try:
                self.stdscr.addstr(y, 0, SUBTITLE[:curses.COLS-1], 
                                 curses.color_pair(COLOR_PURPLE_BRIGHT))
            except:
                pass
            y += 1
        
        return y + 1
    
    def draw_box(self, y, x, width, title=""):
        """Draw box with title - ALIGNED"""
        if y >= curses.LINES - 1:
            return y
        
        # Ensure width fits
        width = min(width, curses.COLS - x)
        
        # Top border
        try:
            self.stdscr.addstr(y, x, "┌" + "─" * (width - 2) + "┐", 
                             curses.color_pair(COLOR_PURPLE_DARK))
        except:
            pass
        
        # Title if provided
        if title:
            title_text = f" {title} "
            title_x = x + (width - len(title_text)) // 2
            if title_x + len(title_text) < x + width:
                try:
                    self.stdscr.addstr(y, title_x, title_text, 
                                     curses.color_pair(COLOR_PURPLE_BRIGHT) | curses.A_BOLD)
                except:
                    pass
        
        return y + 1
    
    def draw_box_bottom(self, y, x, width):
        """Draw bottom of box - ALIGNED"""
        if y >= curses.LINES - 1:
            return
        
        width = min(width, curses.COLS - x)
        
        try:
            self.stdscr.addstr(y, x, "└" + "─" * (width - 2) + "┘", 
                             curses.color_pair(COLOR_PURPLE_DARK))
        except:
            pass
    
    def draw_menu(self, y, options, selected, info=""):
        """Draw menu with arrow selection"""
        x = 2
        
        if info and y < curses.LINES - 1:
            try:
                self.stdscr.addstr(y, x, info[:curses.COLS-4], 
                                 curses.color_pair(COLOR_GRAY))
            except:
                pass
            y += 2
        
        for i, option in enumerate(options):
            if y >= curses.LINES - 3:
                break
            
            if i == selected:
                # Selected item - purple background
                try:
                    display = f"> {option}"
                    self.stdscr.addstr(y, x, display[:curses.COLS-4].ljust(curses.COLS-4), 
                                     curses.color_pair(COLOR_SELECTED) | curses.A_BOLD)
                except:
                    pass
            else:
                # Normal item
                try:
                    display = f"  {option}"
                    self.stdscr.addstr(y, x, display[:curses.COLS-4], 
                                     curses.color_pair(COLOR_CYAN))
                except:
                    pass
            y += 1
        
        if y < curses.LINES - 2:
            y += 1
            try:
                self.stdscr.addstr(y, x, "─" * (curses.COLS - 4), 
                                 curses.color_pair(COLOR_GRAY))
            except:
                pass
            y += 1
            
            try:
                self.stdscr.addstr(y, x, "Use: [↑↓] arrows | [ENTER] select | [Q] quit", 
                                 curses.color_pair(COLOR_YELLOW))
            except:
                pass
        
        return y + 2
    
    def get_selection(self, options, title="SELECT", info=""):
        """Get user selection with arrow keys"""
        selected = 0
        
        while True:
            self.stdscr.clear()
            y = self.draw_banner()
            y += 1
            
            box_width = min(curses.COLS - 1, 77)
            y = self.draw_box(y, 0, box_width, title)
            y = self.draw_menu(y, options, selected, info)
            self.draw_box_bottom(y, 0, box_width)
            
            self.stdscr.refresh()
            
            key = self.stdscr.getch()
            
            if key == curses.KEY_UP:
                selected = (selected - 1) % len(options)
            elif key == curses.KEY_DOWN:
                selected = (selected + 1) % len(options)
            elif key == ord('\n') or key == curses.KEY_ENTER or key == 10:
                return selected
            elif key == ord('q') or key == ord('Q'):
                return -1
    
    def get_input(self, prompt, validator=None):
        """Get text input from user"""
        curses.echo()
        curses.curs_set(1)
        
        self.stdscr.clear()
        y = self.draw_banner()
        y += 2
        
        try:
            self.stdscr.addstr(y, 2, prompt[:curses.COLS-4], 
                             curses.color_pair(COLOR_PURPLE) | curses.A_BOLD)
            y += 1
            self.stdscr.addstr(y, 2, "> ", curses.color_pair(COLOR_CYAN))
        except:
            pass
        
        self.stdscr.refresh()
        
        try:
            value = self.stdscr.getstr(y, 4, 60).decode('utf-8').strip()
        except:
            value = ""
        
        curses.noecho()
        curses.curs_set(0)
        
        if validator and value and not validator(value):
            self.show_message("Invalid format!", COLOR_RED)
            return None
        
        return value if value else None
    
    def show_message(self, message, color=COLOR_GREEN, wait=True):
        """Show a message"""
        self.stdscr.clear()
        y = curses.LINES // 2
        x = max(0, (curses.COLS - len(message)) // 2)
        
        try:
            self.stdscr.addstr(y, x, message[:curses.COLS-2], 
                             curses.color_pair(color) | curses.A_BOLD)
        except:
            pass
        
        if wait:
            y += 2
            prompt = "Press any key to continue..."
            x = max(0, (curses.COLS - len(prompt)) // 2)
            try:
                self.stdscr.addstr(y, x, prompt, curses.color_pair(COLOR_GRAY))
            except:
                pass
        
        self.stdscr.refresh()
        
        if wait:
            self.stdscr.getch()
    
    def confirm(self, message):
        """Ask for confirmation"""
        options = ["Yes", "No"]
        idx = self.get_selection(options, "CONFIRM", message)
        return idx == 0
    
    def show_queries(self):
        """Display generated queries"""
        google = self.qb.build_google_query()
        lucene = self.qb.build_lucene_query()
        
        if not google and not lucene:
            self.show_message("No criteria added yet!", COLOR_YELLOW)
            return
        
        self.stdscr.clear()
        y = self.draw_banner()
        y += 2
        
        box_width = min(curses.COLS - 1, 77)
        
        # Google query
        if google:
            y = self.draw_box(y, 0, box_width, "GOOGLE DORKING")
            
            # Word wrap
            words = google.split()
            line = ""
            for word in words:
                if len(line + word) < box_width - 4:
                    line += word + " "
                else:
                    if y < curses.LINES - 3:
                        try:
                            self.stdscr.addstr(y, 2, line[:box_width-4], 
                                             curses.color_pair(COLOR_WHITE))
                        except:
                            pass
                        y += 1
                    line = word + " "
            if line and y < curses.LINES - 3:
                try:
                    self.stdscr.addstr(y, 2, line[:box_width-4], 
                                     curses.color_pair(COLOR_WHITE))
                except:
                    pass
                y += 1
            
            self.draw_box_bottom(y, 0, box_width)
            y += 2
        
        # Lucene query
        if lucene and y < curses.LINES - 5:
            y = self.draw_box(y, 0, box_width, "APACHE LUCENE")
            
            words = lucene.split()
            line = ""
            for word in words:
                if len(line + word) < box_width - 4:
                    line += word + " "
                else:
                    if y < curses.LINES - 3:
                        try:
                            self.stdscr.addstr(y, 2, line[:box_width-4], 
                                             curses.color_pair(COLOR_WHITE))
                        except:
                            pass
                        y += 1
                    line = word + " "
            if line and y < curses.LINES - 3:
                try:
                    self.stdscr.addstr(y, 2, line[:box_width-4], 
                                     curses.color_pair(COLOR_WHITE))
                except:
                    pass
                y += 1
            
            self.draw_box_bottom(y, 0, box_width)
            y += 2
        
        # Save option
        if y < curses.LINES - 2:
            y += 1
            try:
                self.stdscr.addstr(y, 2, "Press [S] to save, any other key to continue...", 
                                 curses.color_pair(COLOR_YELLOW))
            except:
                pass
        
        self.stdscr.refresh()
        key = self.stdscr.getch()
        
        if key == ord('s') or key == ord('S'):
            filename = f"query_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"SNOOPER - Generated Query\n")
                f.write(f"{'='*75}\n\n")
                f.write(f"GOOGLE DORKING:\n{google}\n\n")
                f.write(f"APACHE LUCENE:\n{lucene}\n")
            self.show_message(f"Saved: {filename}", COLOR_GREEN)
    
    def run_simple_mode(self):
        """Simple mode"""
        data_types = [
            ("CPF - Brazilian ID", 'cpf', Validators.cpf),
            ("CNPJ - Company ID", 'cnpj', Validators.cnpj),
            ("Email Address", 'email', Validators.email),
            ("URL / Domain", 'url', Validators.url),
            ("Phone Number", 'phone', None),
            ("Person Name", 'name', None),
            ("Free Text", 'text', None),
            ("« Back to Main Menu", None, None),
        ]
        
        while True:
            options = [dt[0] for dt in data_types]
            idx = self.get_selection(options, "SIMPLE MODE", self.easter_egg)
            
            if idx == -1 or idx == len(data_types) - 1:
                return
            
            label, dtype, validator = data_types[idx]
            value = self.get_input(f"Enter {label.split('-')[0].strip()}", validator)
            
            if value:
                self.qb.clear()
                self.qb.add_data(dtype, value)
                self.show_queries()
                self.qb.clear()
    
    def run_advanced_mode(self):
        """Advanced mode - query builder"""
        while True:
            options = [
                "Add Data (CPF, Email, etc)",
                "Add Filter (site, filetype, etc)",
                "Edit Data",
                "Delete Item",
                "Generate Query",
                "Clear All",
                "« Back to Main Menu"
            ]
            
            # Show current state
            info = "Current: "
            if self.qb.criteria:
                info += f"{len(self.qb.criteria)} data"
            if self.qb.filters:
                total = sum(len(v) for v in self.qb.filters.values())
                info += f", {total} filters" if self.qb.criteria else f"{total} filters"
            if not self.qb.criteria and not self.qb.filters:
                info = "No criteria yet"
            
            idx = self.get_selection(options, "QUERY BUILDER", info)
            
            if idx == -1 or idx == 6:
                if self.qb.criteria or self.qb.filters:
                    if self.confirm("Discard current query?"):
                        self.qb.clear()
                        return
                else:
                    return
            elif idx == 0:
                self.add_data()
            elif idx == 1:
                self.add_filter()
            elif idx == 2:
                self.edit_data()
            elif idx == 3:
                self.delete_item()
            elif idx == 4:
                self.show_queries()
            elif idx == 5:
                if self.confirm("Clear all criteria?"):
                    self.qb.clear()
    
    def add_data(self):
        """Add data to query"""
        data_types = [
            ("CPF", 'cpf', Validators.cpf),
            ("CNPJ", 'cnpj', Validators.cnpj),
            ("Email", 'email', Validators.email),
            ("URL", 'url', Validators.url),
            ("Phone", 'phone', None),
            ("Name", 'name', None),
            ("Free Text", 'text', None),
        ]
        
        options = [f"{dt[0]} - {dt[1].upper()}" for dt in data_types] + ["« Cancel"]
        idx = self.get_selection(options, "ADD DATA")
        
        if idx >= 0 and idx < len(data_types):
            label, dtype, validator = data_types[idx]
            value = self.get_input(f"Enter {label}", validator)
            if value:
                self.qb.add_data(dtype, value)
                self.show_message(f"Added {label}!", COLOR_GREEN)
    
    def add_filter(self):
        """Add filter to query"""
        filters = [
            ("Site/Domain (e.g., gov.br)", 'site'),
            ("File Type (e.g., pdf)", 'filetype'),
            ("Term in URL", 'inurl'),
            ("Term in Title", 'intitle'),
            ("Term in Text", 'intext'),
            ("Date After (YYYY-MM-DD)", 'after'),
            ("Date Before (YYYY-MM-DD)", 'before'),
            ("Exclude Site", 'exclude_site'),
            ("Exclude Term", 'exclude_term'),
        ]
        
        options = [f[0] for f in filters] + ["« Cancel"]
        idx = self.get_selection(options, "ADD FILTER")
        
        if idx >= 0 and idx < len(filters):
            label, ftype = filters[idx]
            value = self.get_input(label)
            if value:
                self.qb.add_filter(ftype, value)
                self.show_message(f"Filter added!", COLOR_GREEN)
    
    def edit_data(self):
        """Edit existing data"""
        if not self.qb.criteria:
            self.show_message("No data to edit", COLOR_YELLOW)
            return
        
        options = [f"{c['type'].upper()}: {c['value']}" for c in self.qb.criteria] + ["« Cancel"]
        idx = self.get_selection(options, "EDIT DATA")
        
        if idx >= 0 and idx < len(self.qb.criteria):
            old = self.qb.criteria[idx]
            new_val = self.get_input(f"New value for {old['type'].upper()}")
            if new_val:
                self.qb.criteria[idx]['value'] = new_val
                self.show_message("Updated!", COLOR_GREEN)
    
    def delete_item(self):
        """Delete data or filter"""
        if not self.qb.criteria and not self.qb.filters:
            self.show_message("Nothing to delete", COLOR_YELLOW)
            return
        
        options = ["Delete Data", "Delete Filter", "« Cancel"]
        idx = self.get_selection(options, "DELETE")
        
        if idx == 0 and self.qb.criteria:
            items = [f"{c['type'].upper()}: {c['value']}" for c in self.qb.criteria] + ["« Cancel"]
            sel = self.get_selection(items, "DELETE DATA")
            if sel >= 0 and sel < len(self.qb.criteria):
                self.qb.remove_data(sel)
                self.show_message("Deleted!", COLOR_GREEN)
        
        elif idx == 1 and self.qb.filters:
            items = []
            for ftype, values in self.qb.filters.items():
                for val in values:
                    items.append(f"{ftype}: {val}")
            items.append("« Cancel")
            
            sel = self.get_selection(items, "DELETE FILTER")
            if sel >= 0 and sel < len(items) - 1:
                self.qb.remove_filter_by_index(sel)
                self.show_message("Deleted!", COLOR_GREEN)
    
    def run_templates(self):
        """Template mode"""
        templates = {
            'leak': {
                'name': 'Data Leak Hunter',
                'google': '{data} (leak OR breach OR dump) (filetype:txt OR filetype:sql)',
                'lucene': '{data} AND tipo:(vazamento OR breach) AND formato:(txt OR sql)'
            },
            'gov': {
                'name': 'Government Docs (BR)',
                'google': 'site:gov.br {data} filetype:pdf',
                'lucene': 'dominio:gov.br AND {data} AND formato:pdf'
            },
            'lawsuit': {
                'name': 'Legal Process (BR)',
                'google': 'site:jus.br {data} processo filetype:pdf',
                'lucene': 'dominio:jus.br AND {data} AND tipo:processo'
            },
        }
        
        options = [t['name'] for t in templates.values()] + ["« Back"]
        idx = self.get_selection(options, "TEMPLATES")
        
        if idx >= 0 and idx < len(templates):
            template = list(templates.values())[idx]
            
            # Get variables
            vars_needed = set(re.findall(r'\{(\w+)\}', template['google']))
            values = {}
            
            for var in vars_needed:
                val = self.get_input(f"Enter {var.title()}")
                if val:
                    values[var] = val
                else:
                    return
            
            # Replace vars
            google_q = template['google']
            lucene_q = template['lucene']
            
            for var, val in values.items():
                google_q = google_q.replace(f'{{{var}}}', val)
                lucene_q = lucene_q.replace(f'{{{var}}}', val)
            
            # Show
            self.stdscr.clear()
            y = self.draw_banner()
            y += 2
            
            box_width = min(curses.COLS - 1, 77)
            
            y = self.draw_box(y, 0, box_width, "GOOGLE")
            try:
                self.stdscr.addstr(y, 2, google_q[:box_width-4], curses.color_pair(COLOR_WHITE))
            except:
                pass
            y += 1
            self.draw_box_bottom(y, 0, box_width)
            y += 2
            
            y = self.draw_box(y, 0, box_width, "LUCENE")
            try:
                self.stdscr.addstr(y, 2, lucene_q[:box_width-4], curses.color_pair(COLOR_WHITE))
            except:
                pass
            y += 1
            self.draw_box_bottom(y, 0, box_width)
            
            self.stdscr.refresh()
            self.stdscr.getch()
    
    def show_about(self):
        """Show about screen"""
        self.stdscr.clear()
        y = self.draw_banner()
        y += 2
        
        about = [
            "SNOOPER v3.0 'Rainy'",
            "",
            "Google Dorking & Apache Lucene Query Builder",
            "",
            "Created by: Aviation Guy",
            "Inspired by: My uncle Sherlock",
            "",
            "Remember: With great power comes great responsibility!",
            "Ethics: Use only for authorized OSINT research",
        ]
        
        for line in about:
            if y < curses.LINES - 2:
                try:
                    self.stdscr.addstr(y, 2, line, curses.color_pair(COLOR_CYAN))
                except:
                    pass
                y += 1
        
        if y < curses.LINES - 2:
            y += 2
            try:
                self.stdscr.addstr(y, 2, "Press any key...", curses.color_pair(COLOR_GRAY))
            except:
                pass
        
        self.stdscr.refresh()
        self.stdscr.getch()
    
    def run(self):
        """Main loop"""
        while True:
            options = [
                "Simple Mode - Quick Queries",
                "Advanced Mode - Query Builder [Recommended]",
                "Templates - Pre-built Queries",
                "About - Info & Credits",
                "Exit - Disconnect"
            ]
            
            idx = self.get_selection(options, "MAIN MENU", self.easter_egg)
            
            if idx == -1 or idx == 4:
                import random
                goodbye = random.choice(GOODBYES)
                self.show_message(goodbye, COLOR_PURPLE, wait=False)
                curses.napms(2000)
                break
            elif idx == 0:
                self.run_simple_mode()
            elif idx == 1:
                self.run_advanced_mode()
            elif idx == 2:
                self.run_templates()
            elif idx == 3:
                self.show_about()


# ============================================================================
# MAIN
# ============================================================================
def main(stdscr):
    """Main entry point for curses"""
    try:
        app = SnooperUI(stdscr)
        app.run()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    try:
        wrapper(main)
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Interrupted{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}Error: {e}{Colors.RESET}")
