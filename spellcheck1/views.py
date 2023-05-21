import enchant

from django.shortcuts import render

def spellcheck(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        words = text.split()
        corrected_words = []
        for word in words:
            if not enchant.Dict("en_US").check(word):
                suggestions = enchant.Dict("en_US").suggest(word)
                if suggestions:
                    corrected_words.append(', '.join(suggestions))
                else:
                    corrected_words.append(word)
            else:
                corrected_words.append(word)
        corrected_text = ' '.join(corrected_words)
        return render(request, 'spellcheck.html', {'text': text, 'corrected_text': corrected_text})
    else:
        return render(request, 'spellcheck.html')