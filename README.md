<p align="middle"><img src='https://i.imgur.com/HfAUyKJ.png' /></p>  

# SSScripter
SSScripter is a advanced scanner to test whether a website is vulnerable to Same-Site Scripting.

### Features:

- [x] Gathers subdomains via bruteforce as well as a public APIs.
- [x] Multiple modules employed in identifying vulnerabilities.
- [x] Less chances of false positives.
- [x] Has huge subdomain paths (3 different files containing 1000, 2000, 10000).
- [x] Support for custom subdomains path.

<img src="https://i.imgur.com/Qd4mSqm.png" />

#### Requirements:

- tld
- requests
- bs4

#### Usage:

➲ Clone the script and launch it.
```
git clone https://github.com/the-Infected-Drake/SSScripter.git
cd SSScripter
```
➲ Install the dependencies.
```
pip install -r requirements
```
➲ Launch the script.
```
python ssscripter.py
```
➲ Enter the website target.
```
examplesite.com
```
➲ Let the scanner load up.

➲ Keep track of PoCs which may appear (if bug exists).

➲ Report to owners if any bugs found... ; )

#### Version:

- v1.1.0

#### To Do's:
- Associate multithreading for the better.

> Thank you...

✎ @_tID (Team CodeSploit)
