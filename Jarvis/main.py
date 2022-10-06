import speech_recognition


def voice_recognition() -> None:
    # Microfone
    mic = speech_recognition.Recognizer()
    # Ouvindo o mic
    while True:
        with speech_recognition.Microphone() as source:
            # mic.adjust_for_ambient_noise(source)
            audio = mic.listen(source)
        try:
            # armazena o texto na variavel phrase
            phrase = mic.recognize_google(audio, language='pt-BR')
            # se tiver phrase imprime ela
            if phrase != None:
                yield "Voce disse: " + phrase
                break
        # Caso nao reconheca o audio
        except speech_recognition.RequestError:
            # Imprime que nao entendeu
            yield "Assistente: Nao foi possivel entender"
            break
        except speech_recognition.UnknownValueError:
            # Imprime que nao entendeu
            yield "Assistente: Nao foi possivel entender"
            break