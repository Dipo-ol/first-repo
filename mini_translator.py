
def translator(language):
    translations = {
        'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
        'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
        'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
    }

    def translate_word(word):
        if word.lower().strip() in translations[language]:
            return translations[language][word.lower().strip()]
        else:
            return 'no translation'
    return translate_word


esp_translate = translator('spanish')
fran_translate = translator('french')
ita_translate = translator('italian')
print(esp_translate('hello'))
print(fran_translate('goodbye'))
print(ita_translate('thank you'))
