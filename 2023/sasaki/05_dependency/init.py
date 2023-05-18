rf = open("source.txt")
wf = open("source_formatted.txt", "w")

# format source file
for l in rf:
    l = l.rstrip()
    if l == "":
        continue

    text_buffer = ""
    for i in range(0, len(l)):
        s = l[i]
        text_buffer += s
        if s == "。" or i == (len(l) - 1):
            text_buffer += "\n"

    wf.writelines([text_buffer])
