import base64
import codecs
import html
import urllib.parse
action = True
action_encdec = True
action_ny = True
print("Welcome to CODEC")
while action_encdec:
    choice = input("Encoding or decoding (enc/dec)? : ")
    if choice.lower() != "enc" and choice.lower() != "dec":
        print("You have a typing mistake, try it again")

    elif choice.lower() == "dec":
        def decoder():
            if decode_type == "base64":
                decoded_text = base64.b64decode(text.decode('utf-8'))
                print("Decoded text is: " + str(decoded_text))
            elif decode_type == "base32":
                decoded_text = base64.b32decode(text.decode('utf-8'))
                print("Decoded text is: " + str(decoded_text))
            elif decode_type == "html":
                decoded_text = html.unescape(text)
                print("Decoded text is: " + str(decoded_text))
            elif decode_type == "rot13":
                decoded_text = codecs.decode(text, 'rot13')
                print("Decoded text is: " + str(decoded_text))
            elif decode_type == "url":
                decoded_text = urllib.parse.unquote(text)
                print("Decoded text is: " + str(decoded_text))
            elif decode_type == "utf-8":
                decoded_text = text.decode('utf-8')
                print("Decoded text is: " + str(decoded_text))
            else:
                print("Sorry, we don't have such a type yet")
        while action:
            text = input("Type your clear text: ")
            decode_type = input(
                "Type your decode method (such as 'base64', 'base32', 'html', 'url', 'rot13'. 'utf-8' etc): ")
            decoder()
            while action_ny:
                query = input("Do you want do it again (y/n)? : ")
                if query.lower() == "y":
                    pass
                    break
                elif query.lower() == "n":
                    print("Okay, thank you ")
                    action = False
                    action_encdec = False
                    action_ny = False
                else:
                    print("Only y and n")

    elif choice.lower() == "enc":
        def encoder():
            if encode_type == "base64":
                encoded_text = base64.b64encode(text.encode('utf-8'))
                print("Chipper text is: " + str(encoded_text))
            elif encode_type == "html":
                encoded_text = html.escape(text)
                print("Chipper text is: " + str(encoded_text))
            elif encode_type == 'rot13':
                encoded_text = codecs.encode(text, 'rot_13')
                print("Chipper text is: " + str(encoded_text))
            elif encode_type == 'url':
                encoded_text = urllib.parse.quote(text)
                print("Chipper text is: " + str(encoded_text))
            elif encode_type == 'utf-8':
                encoded_text = text.encode(encoding='utf-8')
                print("Chipper text is: " + str(encoded_text))
            elif encode_type == 'base32':
                encoded_text = base64.b32encode(text.encode('utf-8'))
                print("Chipper text is: " + str(encoded_text))
            else:
                print("Sorry, we don't have such a type yet")
        while action:
            text = input("Type your clear text: ")
            encode_type = input("Type your encode method (such as 'base64', 'base32',"
                                " 'html', 'url', 'rot13'. 'utf-8' etc): ")
            encoder()
            while action_ny:
                query = input("Do you want do it again (y/n)? : ")
                if query.lower() == "y":
                    pass
                    break
                elif query.lower() == "n":
                    print("Okay, thank you ")
                    action = False
                    action_encdec = False
                    action_ny = False
                else:
                    print("Only y and n")
