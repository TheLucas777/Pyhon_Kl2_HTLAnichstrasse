while True:
    try:
        n = input("Bitte eine Ganzzahl (integer) eingeben: ")
        n = int(n)
        break
    except ValueError:
        print("Keine Integer! Bitte nochmals versuchen ...")
    except KeyboardInterrupt:
        print("NEIN NICHT BEENDEN")
print("Super! Das war's!")