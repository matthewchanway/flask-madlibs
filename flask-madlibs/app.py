from flask import Flask, request, render_template
from stories import Story

testStory = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

app = Flask(__name__)


@app.route('/form/')
def show_form():
    lst = testStory.prompts
    return render_template("form.html",lst=lst)

@app.route('/story')
def show_story():
    place = request.args.get("place")
    noun = request.args.get("noun")
    verb = request.args.get("verb")
    adjective = request.args.get("adjective")
    plural_noun = request.args.get("plural_noun")
    if place is None:
        place = "na"
    if noun is None:
        noun = "na"
    if verb is None:
        verb = "na"
    if adjective is None:
        adjective = "na"
    if plural_noun is None:
        plural_noun = "na"
    ans = {
        "place": place,
        "noun" : noun,
        "verb" : verb,
        "adjective": adjective,
        "plural_noun": plural_noun
    }
    fin = testStory.generate(ans)
    return render_template("story.html",fin=fin)

