file = input("File name: ")

match file.lower().strip().split(".")[-1]:
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "gif":
        print("image/gif")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")