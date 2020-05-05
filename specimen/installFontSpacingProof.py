from datetime import datetime

fontURL = '../otf/roman.otf'

txt = FormattedString()
txt.font(fontURL)
# txt.font("Times")
txt.fallbackFont("Times-Italic")
txt.fontSize(60)




# font("Helvetica")
# txt += "Hello Amiens"

# help(txt)
# print(txt.listFontGlyphNames())

txt.appendGlyph(*txt.listFontGlyphNames())

txt += "\n" * 2

txt.fontSize(15)

for glyphName in txt.listFontGlyphNames():
    txt.appendGlyph("n", "n", glyphName, "n", "n", "space")
    txt.appendGlyph("e", "e", glyphName, "e", "e", "space")



while txt:
    newPage()
    txt = textBox(txt, (10, 10, width()-20, height()-20))


# Add the date and name of the fotn
psName = font(fontURL)
text(psName, (40, 40))
date = datetime.today().strftime("%d/%m/%Y")
font("Arial")
fontSize(11)
text(date,(width()-40,40), align="right")



