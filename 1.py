import pdfplumber

def resolve_dest(dest: object):
    # if isinstance(dest, (str, bytes)):
    #     dest = resolve1(doc.get_dest(dest))
    # elif isinstance(dest, PSLiteral):
    #     dest = resolve1(doc.get_dest(dest.name))
    # if isinstance(dest, dict):
    dest = dest["D"]
    # if isinstance(dest, PDFObjRef):
    #     dest = dest
    return dest

with pdfplumber.open(r"C:\Users\Deep\Desktop\Arrived\pdf_reader\The Recon Report August Part I.pdf") as pdf:
    x = pdf.doc.get_outlines()
    for y in x:
       (_, page_name, _, prob, _) = y
       if page_name == "Malware":
           dest = resolve_dest(prob.resolve())
           pageno = [dest[0].objid]
           print(page_name)
            

                
    