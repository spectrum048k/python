from datetime import datetime, timezone

def listChunker(lst, csize:int):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), csize):
        yield lst[i:i + csize]

def report(msg:str):
    _time = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    print(f"{_time}: {msg}")

def weirdCase(targetString:str):  # sourcery skip: assign-if-exp
    returnWord:str = ""
    for i,letter in enumerate(targetString):
        i += 1
        if (i % 2 == 0):
            returnWord += letter.lower()
        else:
            returnWord += letter.upper()
    return 

# read: 7fgfsuogkeqpl25c3fv7gwxr36r2av3rjvlequgdnncx32br2jdq
# write: 7vavqrcrtkg4vwbnl3nnudr5ftl3n3mgrbc5dqieyeo3zrshfnla

