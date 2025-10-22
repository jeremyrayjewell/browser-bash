#!/usr/bin/env python3

import http.server
import socketserver
import urllib.parse
import os
from pathlib import Path

# ANSI color codes
class Colors:
    reset = '\033[0m'
    bright = '\033[1m'
    dim = '\033[2m'
    
    # Foreground colors
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'
    
    # Bright foreground colors
    bright_black = '\033[90m'
    bright_red = '\033[91m'
    bright_green = '\033[92m'
    bright_yellow = '\033[93m'
    bright_blue = '\033[94m'
    bright_magenta = '\033[95m'
    bright_cyan = '\033[96m'
    bright_white = '\033[97m'

# ASCII Art with colors
logo = f"""{Colors.bright_cyan}
    ⱯᘓᘓʁEᘓⱯꓕʁOИ  ℝ𝔼ℂ𝕆ℝ𝔻𝕊
    ═══════════════════════
    
    {Colors.bright_red}▄▄▄{Colors.bright_yellow}▄▄▄{Colors.bright_green}▄▄▄{Colors.bright_blue}▄▄▄{Colors.bright_magenta}▄▄▄{Colors.bright_cyan}▄▄▄{Colors.reset}
    {Colors.bright_red}█▀█{Colors.bright_yellow}█▀█{Colors.bright_green}█▀█{Colors.bright_blue}█▀█{Colors.bright_magenta}█▀█{Colors.bright_cyan}█▀█{Colors.reset}
    {Colors.bright_red}█ █{Colors.bright_yellow}█ █{Colors.bright_green}█ █{Colors.bright_blue}█ █{Colors.bright_magenta}█ █{Colors.bright_cyan}█ █{Colors.reset}
    {Colors.bright_red}▀▀▀{Colors.bright_yellow}▀▀▀{Colors.bright_green}▀▀▀{Colors.bright_blue}▀▀▀{Colors.bright_magenta}▀▀▀{Colors.bright_cyan}▀▀▀{Colors.reset}
    
    {Colors.dim}Terminal Interface v2.0{Colors.reset}
"""

pages = {
    '/': f"""{logo}
{Colors.bright_cyan}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.reset}
{Colors.bright_cyan}║{Colors.reset}  {Colors.bright_white}Welcome to the COLORFUL terminal version of Aggregatron Records!{Colors.reset}            {Colors.bright_cyan}║{Colors.reset}
{Colors.bright_cyan}║{Colors.reset}                                                                              {Colors.bright_cyan}║{Colors.reset}
{Colors.bright_cyan}║{Colors.reset}  {Colors.bright_yellow}📋 MAIN MENU - Choose an option:{Colors.reset}                                            {Colors.bright_cyan}║{Colors.reset}
{Colors.bright_cyan}║{Colors.reset}                                                                              {Colors.bright_cyan}║{Colors.reset}
{Colors.bright_cyan}║{Colors.reset}  {Colors.bright_green}[1]{Colors.reset} {Colors.white}JRJ Enterprises{Colors.reset}      {Colors.dim}(curl localhost:8000/1){Colors.reset}                  {Colors.bright_cyan}║{Colors.reset}
{Colors.bright_cyan}║{Colors.reset}  {Colors.bright_green}[2]{Colors.reset} {Colors.white}Lucre-Naut{Colors.reset}           {Colors.dim}(curl localhost:8000/2){Colors.reset}                  {Colors.bright_cyan}║{Colors.reset}
{Colors.bright_cyan}║{Colors.reset}  {Colors.bright_green}[3]{Colors.reset} {Colors.white}Aggrega-Soft Tools{Colors.reset}   {Colors.dim}(curl localhost:8000/3){Colors.reset}                  {Colors.bright_cyan}║{Colors.reset}
{Colors.bright_cyan}║{Colors.reset}  {Colors.bright_green}[4]{Colors.reset} {Colors.white}YouTube Channel{Colors.reset}      {Colors.dim}(curl localhost:8000/4){Colors.reset}                  {Colors.bright_cyan}║{Colors.reset}
{Colors.bright_cyan}║{Colors.reset}  {Colors.bright_green}[5]{Colors.reset} {Colors.white}All Links{Colors.reset}            {Colors.dim}(curl localhost:8000/5){Colors.reset}                  {Colors.bright_cyan}║{Colors.reset}
{Colors.bright_cyan}║{Colors.reset}  {Colors.bright_green}[0]{Colors.reset} {Colors.white}Help / Info{Colors.reset}          {Colors.dim}(curl localhost:8000/0){Colors.reset}                  {Colors.bright_cyan}║{Colors.reset}
{Colors.bright_cyan}║{Colors.reset}                                                                              {Colors.bright_cyan}║{Colors.reset}
{Colors.bright_cyan}║{Colors.reset}  {Colors.bright_yellow}💡 USAGE:{Colors.reset} {Colors.cyan}curl localhost:8000/[NUMBER]{Colors.reset} {Colors.white}or{Colors.reset} {Colors.cyan}curl localhost:8000/[NAME]{Colors.reset}      {Colors.bright_cyan}║{Colors.reset}
{Colors.bright_cyan}║{Colors.reset}  {Colors.dim}Example: curl localhost:8000/1  OR  curl localhost:8000/jrj{Colors.reset}                  {Colors.bright_cyan}║{Colors.reset}
{Colors.bright_cyan}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.reset}
""",

    '/jrj': f"""{Colors.bright_red}
     ██╗██████╗      ██╗
     ██║██╔══██╗     ██║
     ██║██████╔╝     ██║
██   ██║██╔══██╗██   ██║
╚█████╔╝██║  ██║╚█████╔╝
 ╚════╝ ╚═╝  ╚═╝ ╚════╝ 
{Colors.reset}
{Colors.bright_yellow}🎵 JRJ ENTERPRISES{Colors.reset} {Colors.bright_green}- Experimental Electronics & Ambient{Colors.reset}

{Colors.cyan}Experimental electronics and ambient music{Colors.reset}

{Colors.bright_magenta}🎧 STREAMING PLATFORMS:{Colors.reset}
{Colors.bright_green}Spotify:{Colors.reset} {Colors.yellow}https://open.spotify.com/artist/2pHmIqZZ8f7UPt9UDgkinC{Colors.reset}
{Colors.bright_green}Bandcamp:{Colors.reset} {Colors.yellow}https://jrjenterprises.bandcamp.com/{Colors.reset}

{Colors.dim}← Back: curl localhost:8000/{Colors.reset}
""",

    '/lucre': f"""{Colors.bright_blue}
██╗     ██╗   ██╗ ██████╗██████╗ ███████╗
██║     ██║   ██║██╔════╝██╔══██╗██╔════╝
██║     ██║   ██║██║     ██████╔╝█████╗  
██║     ██║   ██║██║     ██╔══██╗██╔══╝  
███████╗╚██████╔╝╚██████╗██║  ██║███████╗
╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝
           ███╗   ██╗ █████╗ ██╗   ██╗████████╗
           ████╗  ██║██╔══██╗██║   ██║╚══██╔══╝
           ██╔██╗ ██║███████║██║   ██║   ██║   
           ██║╚██╗██║██╔══██║██║   ██║   ██║   
           ██║ ╚████║██║  ██║╚██████╔╝   ██║   
           ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   
{Colors.reset}

{Colors.bright_yellow}🎵 LUCRE-NAUT{Colors.reset} {Colors.bright_green}- Breaks, IDM & Left-field Club{Colors.reset}

{Colors.cyan}Breaks, IDM, and left-field club music{Colors.reset}

{Colors.bright_magenta}🎧 STREAMING PLATFORMS:{Colors.reset}
{Colors.bright_green}Spotify:{Colors.reset} {Colors.yellow}https://open.spotify.com/artist/1xljb8IWF5AZRfoUEsBFEL{Colors.reset}
{Colors.bright_green}Bandcamp:{Colors.reset} {Colors.yellow}https://lucre-naut.bandcamp.com/{Colors.reset}

{Colors.dim}← Back: curl localhost:8000/{Colors.reset}
""",

    '/software': f"""{Colors.bright_magenta}
 █████╗  ██████╗  ██████╗ ██████╗ ███████╗ ██████╗  █████╗ 
██╔══██╗██╔════╝ ██╔════╝ ██╔══██╗██╔════╝██╔════╝ ██╔══██╗
███████║██║  ███╗██║  ███╗██████╔╝█████╗  ██║  ███╗███████║
██╔══██║██║   ██║██║   ██║██╔══██╗██╔══╝  ██║   ██║██╔══██║
██║  ██║╚██████╔╝╚██████╔╝██║  ██║███████╗╚██████╔╝██║  ██║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝
                    ███████╗ ██████╗ ███████╗████████╗
                    ██╔════╝██╔═══██╗██╔════╝╚══██╔══╝
                    ███████╗██║   ██║█████╗     ██║   
                    ╚════██║██║   ██║██╔══╝     ██║   
                    ███████║╚██████╔╝██║        ██║   
                    ╚══════╝ ╚═════╝ ╚═╝        ╚═╝   
{Colors.reset}

{Colors.bright_yellow}💻 AGGREGA-SOFT™{Colors.reset} {Colors.bright_green}Musical Solutions{Colors.reset}

{Colors.bright_cyan}🔧 Piecework Splitter:{Colors.reset} {Colors.yellow}https://bright-capybara-8e9e2c.netlify.app/{Colors.reset}
{Colors.green}• Split audio into pieces for remixing{Colors.reset}

{Colors.bright_cyan}🎛️  Aggregatrex5000:{Colors.reset} {Colors.yellow}https://aggregatron.netlify.app/{Colors.reset}
{Colors.green}• Advanced audio aggregation tool{Colors.reset}

{Colors.dim}← Back: curl localhost:8000/  |  Main Menu: curl localhost:8000/0{Colors.reset}
""",

    '/4': f"""{Colors.bright_red}
██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝
 ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝█████╗  
  ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝  
   ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████╗
   ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝
{Colors.reset}

{Colors.bright_yellow}📺 AGGREGATRON YOUTUBE CHANNEL{Colors.reset}

{Colors.bright_white}Subscribe for experimental music videos and live visuals!{Colors.reset}

{Colors.bright_red}🔗 Channel Link:{Colors.reset}
{Colors.yellow}https://www.youtube.com/@aggregatron{Colors.reset}

{Colors.bright_green}📊 Content:{Colors.reset}
{Colors.green}• Live music performances with Three.js visuals{Colors.reset}
{Colors.green}• Experimental electronic music videos{Colors.reset}
{Colors.green}• Behind-the-scenes production content{Colors.reset}

{Colors.dim}← Back: curl localhost:8000/  |  Main Menu: curl localhost:8000/0{Colors.reset}
""",

    '/5': f"""{Colors.bright_white}
╔══════════════════════════════════════════════════════════════════════════════╗
║                              ALL LINKS                                      ║
╠══════════════════════════════════════════════════════════════════════════════╣
{Colors.reset}

{Colors.bright_yellow}🎵 JRJ ENTERPRISES{Colors.reset} {Colors.dim}(Experimental Electronics & Ambient){Colors.reset}
{Colors.bright_green}├─ Spotify:{Colors.reset}  {Colors.yellow}https://open.spotify.com/artist/2pHmIqZZ8f7UPt9UDgkinC{Colors.reset}
{Colors.bright_green}└─ Bandcamp:{Colors.reset} {Colors.yellow}https://jrjenterprises.bandcamp.com/{Colors.reset}

{Colors.bright_blue}🎵 LUCRE-NAUT{Colors.reset} {Colors.dim}(Breaks, IDM & Left-field Club){Colors.reset}
{Colors.bright_green}├─ Spotify:{Colors.reset}  {Colors.yellow}https://open.spotify.com/artist/1xljb8IWF5AZRfoUEsBFEL{Colors.reset}
{Colors.bright_green}└─ Bandcamp:{Colors.reset} {Colors.yellow}https://lucre-naut.bandcamp.com/{Colors.reset}

{Colors.bright_magenta}💻 AGGREGA-SOFT™{Colors.reset} {Colors.dim}(Musical Solutions){Colors.reset}
{Colors.bright_green}├─ Piecework Splitter:{Colors.reset} {Colors.yellow}https://bright-capybara-8e9e2c.netlify.app/{Colors.reset}
{Colors.bright_green}└─ Aggregatrex5000:{Colors.reset}   {Colors.yellow}https://aggregatron.netlify.app/{Colors.reset}

{Colors.bright_red}📺 VIDEO{Colors.reset}
{Colors.bright_green}└─ YouTube:{Colors.reset} {Colors.yellow}https://www.youtube.com/@aggregatron{Colors.reset}

{Colors.dim}← Back: curl localhost:8000/  |  Main Menu: curl localhost:8000/0{Colors.reset}
""",

    '/0': f"""{Colors.bright_cyan}
╔══════════════════════════════════════════════════════════════════════════════╗
║                          HELP & INFORMATION                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
{Colors.reset}

{Colors.bright_yellow}📋 NAVIGATION OPTIONS:{Colors.reset}

{Colors.bright_white}By Number:{Colors.reset}
{Colors.bright_green}curl localhost:8000/1{Colors.reset}  {Colors.white}→ JRJ Enterprises{Colors.reset}
{Colors.bright_green}curl localhost:8000/2{Colors.reset}  {Colors.white}→ Lucre-Naut{Colors.reset}
{Colors.bright_green}curl localhost:8000/3{Colors.reset}  {Colors.white}→ Aggrega-Soft Tools{Colors.reset}
{Colors.bright_green}curl localhost:8000/4{Colors.reset}  {Colors.white}→ YouTube Channel{Colors.reset}
{Colors.bright_green}curl localhost:8000/5{Colors.reset}  {Colors.white}→ All Links{Colors.reset}
{Colors.bright_green}curl localhost:8000/0{Colors.reset}  {Colors.white}→ This help page{Colors.reset}

{Colors.bright_white}By Name:{Colors.reset}
{Colors.bright_green}curl localhost:8000/jrj{Colors.reset}      {Colors.white}→ JRJ Enterprises{Colors.reset}
{Colors.bright_green}curl localhost:8000/lucre{Colors.reset}    {Colors.white}→ Lucre-Naut{Colors.reset}
{Colors.bright_green}curl localhost:8000/software{Colors.reset} {Colors.white}→ Aggrega-Soft Tools{Colors.reset}

{Colors.bright_yellow}🎨 FEATURES:{Colors.reset}
{Colors.green}• Full ANSI color support{Colors.reset}
{Colors.green}• ASCII art logos{Colors.reset}
{Colors.green}• Numbered menu navigation{Colors.reset}
{Colors.green}• Works from any terminal with curl{Colors.reset}
{Colors.green}• Integrated web terminal interface{Colors.reset}

{Colors.bright_yellow}💡 TIP:{Colors.reset} {Colors.cyan}Aggregatron Records = JRJ Enterprises = Lucre-Naut{Colors.reset}

{Colors.dim}← Back: curl localhost:8000/{Colors.reset}
"""
}

# HTML template for the web terminal interface
web_terminal_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aggregatron Terminal</title>
    <style>
        body {
            margin: 0;
            padding: 20px;
            background: #1e1e1e;
            color: #ffffff;
            font-family: 'Courier New', monospace;
            line-height: 1.4;
        }

        .terminal-container {
            max-width: 1200px;
            margin: 0 auto;
            background: #1e1e1e;
            border: 2px solid #333;
            border-radius: 8px;
            overflow: hidden;
        }

        .terminal-header {
            background: #2d2d2d;
            padding: 10px 15px;
            display: flex;
            align-items: center;
            gap: 10px;
            border-bottom: 1px solid #333;
        }

        .terminal-button {
            width: 12px;
            height: 12px;
            border-radius: 50%;
        }

        .close { background: #ff5f56; }
        .minimize { background: #ffbd2e; }
        .maximize { background: #27ca3f; }

        .terminal-title {
            color: #ccc;
            font-size: 14px;
            margin-left: 10px;
        }

        .terminal-content {
            padding: 20px;
            min-height: 600px;
            background: #1e1e1e;
        }

        .output {
            white-space: pre-wrap;
            font-family: 'Courier New', monospace;
            margin-bottom: 15px;
        }

        .input-line {
            display: flex;
            align-items: center;
            margin-top: 10px;
        }

        .prompt {
            color: #00ff00;
            margin-right: 8px;
        }

        input[type="text"] {
            background: transparent;
            border: none;
            color: #ffffff;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            outline: none;
            flex: 1;
        }

        .loading {
            color: #ffbd2e;
        }

        /* ANSI Color Support */
        .ansi-black { color: #000000; }
        .ansi-red { color: #cd0000; }
        .ansi-green { color: #00cd00; }
        .ansi-yellow { color: #cdcd00; }
        .ansi-blue { color: #0000ee; }
        .ansi-magenta { color: #cd00cd; }
        .ansi-cyan { color: #00cdcd; }
        .ansi-white { color: #e5e5e5; }
        .ansi-bright-black { color: #7f7f7f; }
        .ansi-bright-red { color: #ff0000; }
        .ansi-bright-green { color: #00ff00; }
        .ansi-bright-yellow { color: #ffff00; }
        .ansi-bright-blue { color: #5c5cff; }
        .ansi-bright-magenta { color: #ff00ff; }
        .ansi-bright-cyan { color: #00ffff; }
        .ansi-bright-white { color: #ffffff; }

        .navigation-hint {
            color: #888;
            font-size: 12px;
            margin-top: 20px;
            padding: 10px;
            border: 1px solid #333;
            border-radius: 4px;
            background: #2a2a2a;
        }
    </style>
</head>
<body>
    <div class="terminal-container">
        <div class="terminal-header">
            <div class="terminal-button close"></div>
            <div class="terminal-button minimize"></div>
            <div class="terminal-button maximize"></div>
            <div class="terminal-title">Aggregatron Terminal - localhost:8000</div>
        </div>
        <div class="terminal-content">
            <div class="output" id="output"></div>
            <div class="input-line">
                <span class="prompt">$ </span>
                <input type="text" id="commandInput" placeholder="Try: curl /1 or curl /jrj" autocomplete="off">
            </div>
            <div class="navigation-hint">
                <strong>Quick Navigation:</strong><br>
                • curl /1 → JRJ Enterprises<br>
                • curl /2 → Lucre-Naut<br>
                • curl /3 → Aggrega-Soft Tools<br>
                • curl /4 → YouTube<br>
                • curl /5 → All Links<br>
                • curl /0 → Help<br>
                <br>
                <strong>External Access:</strong> curl localhost:8000/[route]
            </div>
        </div>
    </div>

    <script>
        const output = document.getElementById('output');
        const commandInput = document.getElementById('commandInput');
        
        // ANSI escape sequence parser
        function parseAnsi(text) {
            const ansiMap = {
                '\\033[0m': '</span>',  // Reset
                '\\033[1m': '<span style="font-weight: bold;">',  // Bright
                '\\033[2m': '<span style="opacity: 0.6;">',  // Dim
                '\\033[30m': '<span class="ansi-black">',
                '\\033[31m': '<span class="ansi-red">',
                '\\033[32m': '<span class="ansi-green">',
                '\\033[33m': '<span class="ansi-yellow">',
                '\\033[34m': '<span class="ansi-blue">',
                '\\033[35m': '<span class="ansi-magenta">',
                '\\033[36m': '<span class="ansi-cyan">',
                '\\033[37m': '<span class="ansi-white">',
                '\\033[90m': '<span class="ansi-bright-black">',
                '\\033[91m': '<span class="ansi-bright-red">',
                '\\033[92m': '<span class="ansi-bright-green">',
                '\\033[93m': '<span class="ansi-bright-yellow">',
                '\\033[94m': '<span class="ansi-bright-blue">',
                '\\033[95m': '<span class="ansi-bright-magenta">',
                '\\033[96m': '<span class="ansi-bright-cyan">',
                '\\033[97m': '<span class="ansi-bright-white">'
            };
            
            let result = text;
            for (const [ansi, html] of Object.entries(ansiMap)) {
                result = result.replace(new RegExp(ansi, 'g'), html);
            }
            return result;
        }

        const commands = {
            curl: async function(args) {
                if (args.length === 0) {
                    return "Usage: curl [path]\\nExample: curl /1 or curl /jrj";
                }
                
                const path = args[0];
                const loadingMsg = `<span class="loading">Fetching ${path}...</span>`;
                appendOutput(loadingMsg);
                
                try {
                    const response = await fetch(path);
                    const text = await response.text();
                    // Remove loading message
                    output.innerHTML = output.innerHTML.replace(loadingMsg, '');
                    return text;
                } catch (error) {
                    output.innerHTML = output.innerHTML.replace(loadingMsg, '');
                    return `Error: ${error.message}`;
                }
            },
            
            help: function() {
                return `Available commands:
• curl [path] - Fetch terminal content
• clear - Clear the terminal
• help - Show this help

Quick paths:
• /1 or /jrj - JRJ Enterprises
• /2 or /lucre - Lucre-Naut  
• /3 or /software - Aggrega-Soft Tools
• /4 - YouTube Channel
• /5 - All Links
• /0 - Help & Info`;
            },
            
            clear: function() {
                output.innerHTML = '';
                return '';
            }
        };

        function appendOutput(text) {
            if (text) {
                const div = document.createElement('div');
                div.innerHTML = parseAnsi(text);
                output.appendChild(div);
            }
        }

        function processCommand(input) {
            const parts = input.trim().split(' ');
            const command = parts[0].toLowerCase();
            const args = parts.slice(1);

            appendOutput(`<span class="prompt">$ </span>${input}`);

            if (commands[command]) {
                const result = commands[command](args);
                if (result instanceof Promise) {
                    result.then(appendOutput);
                } else {
                    appendOutput(result);
                }
            } else {
                appendOutput(`Command not found: ${command}\\nType 'help' for available commands.`);
            }
        }

        commandInput.addEventListener('keydown', function(e) {
            if (e.key === 'Enter') {
                const command = this.value;
                this.value = '';
                processCommand(command);
            }
        });

        // Initialize with welcome message
        appendOutput(`Welcome to Aggregatron Terminal!
Type 'curl /' to see the main menu, or try 'curl /1' for JRJ Enterprises.
Type 'help' for available commands.
`);

        // Focus on input
        commandInput.focus();
    </script>
</body>
</html>"""

class UnifiedTerminalHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        
        # Serve the web terminal interface at root
        if path == '/' or path == '' or path.startswith('/?'):
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(web_terminal_html.encode('utf-8'))
            return
        
        # Handle numbered routes
        number_routes = {
            '/1': '/jrj',
            '/2': '/lucre', 
            '/3': '/software'
        }
        
        if path in number_routes:
            path = number_routes[path]
        
        # Get terminal content
        content = pages.get(path, pages['/'])
        
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

def run_server(port=8000):
    with socketserver.TCPServer(("", port), UnifiedTerminalHandler) as httpd:
        print(f"""{Colors.bright_cyan}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  🚀 AGGREGATRON UNIFIED TERMINAL SERVER                     ║
║                                                              ║
║  🌐 Web Terminal: http://localhost:{port}                        ║
║  📱 External curl: curl localhost:{port}/[route]                 ║
║                                                              ║
║  ✅ Same-origin - No CORS issues!                           ║
║  🎨 Full ANSI color support                                  ║
║  🔢 Numbered navigation (1-5, 0)                            ║
║                                                              ║
║  Press Ctrl+C to stop the server                            ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{Colors.reset}""")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n{Colors.bright_yellow}🛑 Server stopped.{Colors.reset}")

if __name__ == "__main__":
    run_server()