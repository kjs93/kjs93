filelist=['e1.docx','e2.docx','e3.docx']
for file_name in filelist:
    filelist_item=file_name.split(".")
print(filelist_item[0])