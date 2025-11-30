# views.py

from django.shortcuts import render

# Question class (same as yours)
class Questions:
    def __init__(self, que, a, b, c, d, correct):
        self.que = que
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.correct = correct  # yeh 'a', 'b', 'c', 'd' mein se ek hoga

def testpaper(request):
    # Hardcoded questions (you can later move to database)
    questions = [
        Questions('प्रश्वसन (सांस अंदर लेने) के दौरान डायफ्राम में क्या परिवर्तन होता है?',
                  '(a) ऊपर की ओर उठता है', '(b) नीचे की ओर जाता है', '(c) संकुचित होता है', '(d) कोई परिवर्तन नहीं होता', 'b'),
        Questions('सांस अंदर लेते समय थोरैसिक कैविटी के वॉल्यूम का क्या होता है?',
                  '(a) वृद्धि', '(b) कम हो जाती है', '(c) वैसा ही रहता है', '(d) दोगुना हो जाता है', 'b'),
        Questions('साँस लेने (इंस्पिरेशन) के दौरान फेफड़ों में दबाव क्या होता है?',
                  '(a) बढ़ जाता है', '(b) घट जाता है', '(c) जैसा था वैसा ही रहता है', '(d) दोगुना हो जाता है', 'b'),
        Questions('साँस छोड़ने (एक्सपिरेशन) के दौरान कौन सा गैस बाहर निकलता है?',
                  '(a) ऑक्सीजन', '(b) नाइट्रोजन', '(c) कार्बन डाइऑक्साइड (CO₂)', '(d) हीलियम', 'c')
    ]

    # Agar form submit hua hai (POST request)
    if request.method == "POST":
        score = 0
        for i, q in enumerate(questions, 1):  # i = 1,2,3,4 (question number)
            selected_option = request.POST.get(f'option{i}')  # name="option1", "option2" etc.
            if selected_option == q.correct:
                score += 1

        total = len(questions)
        percentage = round((score / total) * 100, 1) if total > 0 else 0

        context = {
            'score': score,
            'total': total,
            'percentage': percentage
        }
        return render(request, 'result.html', context)

    # Pehli baar page load hone par (GET request)
    context = {'questions': questions}
    return render(request, 'question.html', context)
