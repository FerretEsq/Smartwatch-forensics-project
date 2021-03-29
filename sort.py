#Meme machine



def main():
    import fnmatch, datetime, os
    path = os.getcwd()
    for item in os.scandir(path):
        if os.path.isdir(item):
            if item.name == ".git":
                pass
            else:
                print("__")
                print("  |"+item.name)# +" is a directory")
                #print("Traversing "+path+"/"+item.name+":")
                for item in os.scandir(path+"/"+item.name):
                    print("  |--"+item.name)
                    if os.path.isdir(item):
                        print("  |__"+"\n     |"+item.name) # is a directory")
                        for thing in os.scandir(item):
                            print("     |--"+thing.name)
                    


if __name__ == "__main__":
    main()