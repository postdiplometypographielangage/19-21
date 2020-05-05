from datetime import datetime

fontURL = '../otf/roman.otf'

txt = FormattedString()
txt.font(fontURL)

# Glyphset
txt.fontSize(240)
txt.lineHeight(220)

txt.appendGlyph(*txt.listFontGlyphNames())

# Words
txt.fontSize(24)
txt.lineHeight(28)
txt += "\n" * 2

txt += "encaissasses seize cas cane ni nies naine cessasses cessas sens an aise assainissez zen scia sains cannisses sana sic sis seize cannisse assainissez encaissasses encaissiez encaissassiez encens essais aines encaissez encaissassiez casasses scies cas cas incises zinc an ans incisasse sens sise sis canna canisse saines aines cessa assainisses naissais inca encan cannes cassas anis ces encaisse nazies ac assassiniez science aisance sic sciences canne zinc naisses canines cas naine cas encaissiez se saisie assainissez cc encaissais sans incisassiez sain saisissez cessassiez se sic ceci anse ac aines ananas saisissiez nia encaissez aise zizanies saisies nain ci ai cannas nez saisi nias ananas naine ancien cc naissance"


# Spacing
txt += "\n" * 2

for glyphName in txt.listFontGlyphNames():
    txt.appendGlyph("n", "n", glyphName, "n", "n", "space")
    txt.appendGlyph("e", "e", glyphName, "e", "e", "space")



while txt:
    newPage("A4Landscape")
    txt = textBox(txt, (40, 40, width()-80, height()-100))
    
    # Add the date and name of the font
    psName = font(fontURL)
    font("Arial")
    fontSize(11)
    text(psName, (40, 40))
    date = datetime.today().strftime("%d/%m/%Y")
    font("Arial")
    fontSize(11)
    text(date,(width()-40,40), align="right")




 
