print("󱉶 WEBSITE URL CHECKER 󱉶")
url = input('\nEnter a website URL: ')

if url.startswith("https://"):
    print("This website uses HTTPS  (secure)")
elif url.startswith("http://"):
    print("This website uses HTTP 󱙱 (insecure)")
else:
    print("The URL entered did not have an http(s) specification.")

