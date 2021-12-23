from translate import Translator

lang_iso = {"Hindi":"hi","English":"en",'Japanese':'ja','Spanish':'es'}
def translate_sentence(from_language,to_language,sentence):
    from_lang_iso = lang_iso[from_language]
    to_lang_iso = lang_iso[to_language]
    
    translator = Translator(to_lang=to_lang_iso,from_lang=from_lang_iso)
    translation = translator.translate(sentence)
    return translation

if __name__ == "__main__":
    print(translate_sentence(to_language="Hindi",from_language="English",sentence="Hello"))