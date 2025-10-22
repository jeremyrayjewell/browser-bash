# Browser Bash



A web-based terminal emulator with real network capabilities that runs entirely in your browser. Features authentic `curl` functionality via CORS proxies, making it perfect for testing APIs and web services without installing additional software.An in-browser bash terminal implementation using libv86 to run a complete Linux environment in your web browser.



## Features## Features



- **Real Network Access**: Uses CORS proxies to make genuine HTTP requests- Full Linux terminal experience in the browser

- **Authentic curl Implementation**: Real curl with proper options, error codes, and output formatting-  Modern terminal UI with macOS-style window controls  

- **Multiple CORS Proxy Fallbacks**: Automatically tries different proxies if one fails-  Real-time system monitoring

- **Terminal Commands**: Standard Unix-like commands (ls, cat, pwd, date, uname, etc.)-  Responsive design for desktop and mobile

- **Command History**: Use arrow keys to navigate through previous commands- 🔧 Complete bash shell with standard Unix tools

- **ANSI Color Support**: Full terminal color support for better readability

- **No Dependencies**: Single HTML file with embedded CSS and JavaScript## Setup

- **Cross-Platform**: Works in any modern web browser

### Prerequisites

## Live Demo

- Modern web browser with WebAssembly support

**GitHub Pages**: [https://jeremyrayjewell.github.io/browser-bash/terminal.html](https://jeremyrayjewell.github.io/browser-bash/terminal.html)- Python 3.x or Node.js (for local development server)

- Internet connection (for downloading system files)

##  Usage

### Quick Start

### Basic Commands

1. **Clone or download this repository**

```bash

# Get help2. **Download required files**:

help   

   Run the dependency download script:

# List files   ```bash

ls   node download-deps.js

   ```

# Show current directory   

pwd   Or manually download:

   - `libv86.js` from [libv86 releases](https://github.com/copy/v86/releases)

# Display file contents   - `v86.wasm` from the same release

cat readme.txt   - A Linux ISO image (see below for options)



# System information3. **Start a local server**:

uname -a   

   Using Python:

# Current date/time   ```bash

date   python -m http.server 8080

   ```

# Clear terminal   

clear   Or using Node.js:

```   ```bash

   npm install

### Network Commands   npm run start-node

   ```

```bash

# Make HTTP requests (real curl!)4. **Open your browser** and navigate to `http://localhost:8080`

curl https://httpbin.org/json

curl https://api.github.com/zen## Linux Images

curl -I https://example.com

This terminal needs a bootable Linux image. You have several options:

# Test API endpoints

curl https://jsonplaceholder.typicode.com/posts/1### Option 1: Buildroot (Recommended for minimal size)

- Lightweight Linux distribution perfect for terminal use

# Get headers only- Download from [buildroot.org](https://buildroot.org/)

curl -I https://httpbin.org/headers- Rename to `linux.iso`



# Verbose output### Option 2: Alpine Linux

curl -v https://api.github.com/user- Small, security-oriented Linux distribution

```- Download from [alpinelinux.org](https://alpinelinux.org/downloads/)

- Rename to `linux.iso`

### Special Features

### Option 3: Tiny Core Linux

```bash- Extremely minimal Linux distribution

# Show main menu- Download from [tinycorelinux.net](http://tinycorelinux.net/)

menu- Rename to `linux.iso`



# Test network connectivity## Project Structure

test https://httpbin.org/json

```

# Simulated pingbrowser-bash/

ping google.com├── index.html          # Main HTML file

├── styles.css          # Terminal styling

# Simulated wget├── app.js              # Main application logic

wget https://example.com├── package.json        # Project configuration

```├── download-deps.js    # Dependency download script

├── libv86.js          # libv86 library (downloaded)

## 🛠️ How It Works├── v86.wasm           # WebAssembly binary (downloaded)

└── linux.iso          # Linux image (user provided)

This terminal emulator uses several clever techniques to provide real network functionality:```



1. **CORS Proxy Chain**: Attempts multiple CORS proxy services in sequence:## Configuration

   - `api.allorigins.win` (primary)

   - `cors-anywhere.herokuapp.com` (fallback)You can modify the virtual machine configuration in `app.js`:

   - `thingproxy.freeboard.io` (secondary fallback)

- **Memory size**: Adjust `memory_size` for more RAM

2. **Content Security Policy**: Configured to allow connections to trusted CORS proxy domains- **Screen resolution**: Modify canvas dimensions

- **Boot options**: Change the ISO image or add disk images

3. **Authentic Error Handling**: Returns real curl exit codes:

   - `(6)` - Could not resolve host## Browser Compatibility

   - `(7)` - Failed to connect to server

   - `(22)` - HTTP error status- ✅ Chrome/Chromium 57+

   - `(35)` - SSL connect error- ✅ Firefox 52+  

- ✅ Safari 11+

4. **Real HTTP Responses**: Parses and displays actual HTTP responses with proper formatting- ✅ Edge 16+



##  Technical Details## Performance Tips



- **Single File Deployment**: Everything is contained in one HTML file- Use a lightweight Linux distribution

- **No Backend Required**: Runs entirely in the browser- Reduce memory allocation if running on lower-end devices

- **Modern JavaScript**: Uses async/await and ES6 features- Close other browser tabs for better performance

- **Responsive Design**: Works on desktop and mobile browsers

- **Terminal Emulation**: Authentic terminal look and feel with proper prompt## Troubleshooting



##  Hosting Options### Terminal won't load

- Ensure all required files are downloaded

This terminal works best on hosting platforms with permissive Content Security Policies:- Check browser console for error messages

- Verify local server is running properly

###  Recommended Platforms:

- **GitHub Pages** (Free, reliable, good CSP)### Slow performance

- **Netlify** (Free tier, excellent for static sites)- Try a smaller Linux image

- **Vercel** (Fast global CDN)- Reduce memory allocation in the configuration

- **Surge.sh** (Simple deployment)- Use a modern browser with good WebAssembly support



###  Not Recommended:### Keyboard not working

- **Neocities** (Restrictive CSP blocks CORS proxies)- Click inside the terminal area to focus

- Platforms with strict CSP that block external connections- Ensure the emulator has finished loading



##  Installation## Development



1. **Download**: Get the `terminal.html` file from this repositoryTo contribute or modify:

2. **Upload**: Host it on any web server or static hosting platform

3. **Access**: Open the URL in your browser1. Make changes to the source files

2. Test in multiple browsers

That's it! No build process, no dependencies, no configuration needed.3. Ensure the terminal remains responsive

4. Follow existing code style

##  Contributing

## License

Contributions are welcome! Here are some ideas:

MIT License - see LICENSE file for details

- Add more Unix commands

- Improve CORS proxy reliability## Acknowledgments

- Add syntax highlighting for code responses

- Implement file upload/download simulation- [libv86](https://github.com/copy/v86) - The amazing x86 emulator that makes this possible

- Add more terminal themes- Linux community - for creating the wonderful distributions we can run
- Improve mobile responsiveness

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🔗 Links

- **Repository**: https://github.com/jeremyrayjewell/browser-bash
- **Issues**: https://github.com/jeremyrayjewell/browser-bash/issues
- **Live Demo**: https://jeremyrayjewell.github.io/browser-bash/terminal.html

##  Important Notes

- CORS proxies may have rate limits or occasional downtime
- Some APIs may not work due to their own CORS policies
- This is a client-side terminal emulator, not a real shell environment
- Network requests are subject to browser security policies

---

**Built for developers who need quick API testing without leaving the browser**