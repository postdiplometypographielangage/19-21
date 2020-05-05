from datetime import datetime
import drawBot
import os

drawBot.newDrawing()

fontDir = '../otf'

for fontFileName in os.listdir(fontDir):
    if not fontFileName.endswith(".otf"):
        continue
        
    fontURL = os.path.join(fontDir, fontFileName)


    txt = drawBot.FormattedString()
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
        drawBot.newPage("A4Landscape")
        txt = drawBot.textBox(txt, (40, 40, drawBot.width()-80, drawBot.height()-100))
    
        # Add the date and name of the font
        psName = drawBot.font(fontURL)
        drawBot.font("Arial")
        drawBot.fontSize(11)
        drawBot.text(psName, (40, 40))
    
        date = datetime.today().strftime("%d/%m/%Y")
    
        drawBot.text(date,(drawBot.width()-40,40), align="right")

drawBot.saveImage("../specimen.pdf")

drawBot.endDrawing()

 
