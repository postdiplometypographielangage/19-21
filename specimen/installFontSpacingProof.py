
txt = FormattedString()
txt.font('/otf/roman.otf')
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


