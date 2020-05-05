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


font(fontURL, 24)
textBox("encaissasses seize cas cane ni nies naine cessasses cessas sens an aise assainissez zen scia sains cannisses sana sic sis seize cannisse assainissez encaissasses encaissiez encaissassiez encens essais aines encaissez encaissassiez casasses scies cas cas incises zinc an ans incisasse sens sise sis canna canisse saines aines cessa assainisses naissais inca encan cannes cassas anis ces encaisse nazies ac assassiniez science aisance sic sciences canne zinc naisses canines cas naine cas encaissiez se saisie assainissez cc encaissais sans incisassiez sain saisissez cessassiez se sic ceci anse ac aines ananas saisissiez nia encaissez aise zizanies saisies nain ci ai cannas nez saisi nias ananas naine ancien cc naissance sain encans zen incisa scie encaissassiez cc sana assainissez nain canisses nazie ai ", (40, height()-500, width()-80, 200), align="left")
  
# Add the date and name of the font
psName = font(fontURL)
font("Arial")
fontSize(11)
text(psName, (40, 40))
date = datetime.today().strftime("%d/%m/%Y")
font("Arial")
fontSize(11)
text(date,(width()-40,40), align="right")


